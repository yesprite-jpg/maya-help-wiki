#!/usr/bin/env python3
"""Add missing help pages to this pack: suggest (default, offline) or apply (network).

SUGGEST MODE IS THE DEFAULT. It reads references/missing_pages.json only and prints
what could be added; it makes no network request and writes no file. Nothing in this
file imports urllib.request at module level -- fetching lives inside fetch_bytes(),
which --apply reaches only after the batch size and host whitelist checks pass.

Index, manifest, hashing, path sanitising and atomic writes are imported from
scripts/sync_wiki_docs.py so this tool cannot drift from the pack's own口径.

Pre-write backups go OUTSIDE the pack (default: ../.maya-help-wiki-backup/<timestamp>/,
override with --backup-dir) and at most 3 are kept; inside the pack only
references/.extension/CHANGELOG.local.md and the newest report-*.json stay.
Exit codes: 0 ok (also for --suggest), 2 applied-then-aborted (rolled back) or unreadable
input file, 3 refused by a safety rule (no request, no write).

Stdlib only. Additive: existing pages, existing manifest entries and existing assets
are never modified or removed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import random
import re
import shutil
import sys
import time
import unicodedata
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from urllib.parse import urljoin, urlsplit

SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import sync_wiki_docs as swd  # noqa: E402  (reused: render_index / sha256 / safe_relative / ...)

PACK_ROOT = SCRIPTS_DIR.parent
REFERENCES = PACK_ROOT / "references"
DOCS_ROOT = REFERENCES / "docs"
MANIFEST_PATH = REFERENCES / "wiki-manifest.json"
INDEX_PATH = REFERENCES / "INDEX.md"
MISSING_PATH = REFERENCES / "missing_pages.json"
EXT_ROOT = REFERENCES / ".extension"
# Backups live OUTSIDE the pack: a manifest+INDEX+missing snapshot is ~7 MB each and the
# pack is what people copy, publish and share.
BACKUP_ROOT = PACK_ROOT.parent / ".maya-help-wiki-backup"
MAX_BACKUP_KEPT = 3
REFUSED_RC = 3
CHANGELOG_PATH = EXT_ROOT / "CHANGELOG.local.md"

ALLOWED_HOSTS = {"help.autodesk.com"}
MAX_APPLY_PAGES = 30
WORD_LIMIT = 300
MAX_ATTEMPTS = 3
USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
              "Chrome/124.0 Safari/537.36")

VOID = {"img", "br", "hr", "meta", "link", "input", "area", "base", "col", "source", "wbr"}
SKIP = {"script", "style"}
BLOCKISH = {"p", "div", "dl", "ol", "ul", "h1", "h2", "h3", "h4", "li", "table", "pre"}

# Ruling D39 (2026-10-12): a page at references/docs/<d1>/.../<dn>/<file>.md sits n+0 dirs under
# docs/, so its image link must climb (len of its relative path parts) levels to reach
# references/.extension/assets/. The old fixed "../" was only right for one depth and left every
# deeper page's images broken. This is the single place the depth口径 lives.
ASSET_LINK_RE = re.compile(r"(\]\()((?:\.\./)+)(\.extension/assets/)")


def asset_link_prefix(local_path: str) -> str:
    return "../" * len(PurePosixPath(local_path).parts)


def asset_link(target_rel: str, local_path: str) -> str:
    return asset_link_prefix(local_path) + ".extension/assets/" + target_rel


class Refuse(Exception):
    """A guarded input or safety rule blocked the run; nothing was written."""


# ---------------------------------------------------------------- selection


def load_missing() -> list[dict]:
    data = json.loads(MISSING_PATH.read_text(encoding="utf-8"))
    rows = data.get("pages")
    if not isinstance(rows, list) or not rows:
        raise Refuse(f"{MISSING_PATH.name} has no pages array")
    return rows


def select(rows: list[dict], keywords: str | None, paths_file: Path | None,
           url_file: Path | None) -> list[dict]:
    chosen = [r for r in rows if all(isinstance(r.get(k), str) for k in ("t", "p", "u", "b"))]
    if keywords:
        terms = [t.casefold() for t in keywords.split() if t.strip()]
        if not terms:
            raise Refuse("--keywords has no usable term")
        chosen = [r for r in chosen
                  if any(t in r["t"].casefold() or t in r["p"].casefold() for t in terms)]
    elif paths_file:
        wanted = [ln.strip() for ln in paths_file.read_text(encoding="utf-8").splitlines() if ln.strip()]
        by_path = {r["p"]: r for r in chosen}
        missing = [w for w in wanted if w not in by_path]
        if missing:
            raise Refuse(f"{len(missing)} path(s) not in missing list, e.g. {missing[:3]}")
        chosen = [by_path[w] for w in wanted]
    elif url_file:
        wanted = {ln.strip() for ln in url_file.read_text(encoding="utf-8").splitlines() if ln.strip()}
        chosen = [r for r in chosen if r["u"] in wanted]
        if len(chosen) != len(wanted):
            raise Refuse(f"{len(wanted) - len(chosen)} URL(s) not in missing list")
    return sorted(chosen, key=lambda r: r["p"])


# ---------------------------------------------------------------- parsing


class Node:
    __slots__ = ("tag", "attrs", "children")

    def __init__(self, tag, attrs=None):
        self.tag = tag
        self.attrs = attrs or {}
        self.children: list = []


class DOM(HTMLParser):
    """Entities are decoded while parsing (convert_charrefs), the pack's正文口径."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node("root")
        self.stack = [self.root]

    def _push(self, tag, attrs):
        node = Node(tag, attrs)
        self.stack[-1].children.append(node)
        return node

    def handle_starttag(self, tag, attrs):
        node = self._push(tag, dict(attrs))
        if tag not in VOID:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self._push(tag, dict(attrs))

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        if self.stack[-1].tag in SKIP:
            return
        self.stack[-1].children.append(data)


def elements(node):
    yield node
    for child in node.children:
        if isinstance(child, Node):
            yield from elements(child)


def classes(node) -> list[str]:
    return (node.attrs.get("class") or "").split()


def find_div(node, wanted: str):
    for el in elements(node):
        if el.tag == "div" and wanted in classes(el):
            return el
    return None


def texts(node) -> str:
    if isinstance(node, str):
        return node
    return "".join(texts(c) for c in node.children)


def normalize_space(raw: str) -> str:
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", raw)).strip()


def word_count(node) -> int:
    return len(re.sub(r"\s+", "", normalize_space(texts(node))))


def encode_link(path: str) -> str:
    for ch, esc in (("%", "%25"), (" ", "%20"), ("(", "%28"), (")", "%29")):
        path = path.replace(ch, esc)
    return path


def resolve(url: str, href: str) -> str:
    href = (href or "").strip()
    if not href or href.startswith("#"):
        return url + href
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", href):
        return href
    return urljoin(url, href)


def relpath_target(src_local: str, dst_local: str) -> str:
    src, dst = src_local.split("/"), dst_local.split("/")
    i = 0
    while i < len(src) - 1 and i < len(dst) - 1 and src[i] == dst[i]:
        i += 1
    return "../" * (len(src) - 1 - i) + "/".join(dst[i:])


class Body:
    """The captured page body: div.body subtree, else the <body> element (landing pages)."""

    def __init__(self, html: str, url: str):
        dom = DOM()
        dom.feed(html)
        self.node = find_div(dom.root, "body")
        self.fallback = self.node is None
        if self.fallback:
            self.node = next((el for el in elements(dom.root) if el.tag == "body"), None)
        if self.node is None:
            raise Refuse(f"no div.body and no body element: {url}")
        self.images = [el for el in elements(self.node)
                       if el.tag == "img" and "/images/" in resolve(url, el.attrs.get("src", ""))]
        self.words = word_count(self.node)
        self.load_bearing = self.words < WORD_LIMIT and bool(self.images)
        self.reason = ("正文 %d 字 <%d 且带图" % (self.words, WORD_LIMIT)) if self.load_bearing \
            else ("正文 %d 字 ≥%d，非承重" % (self.words, WORD_LIMIT))


class Renderer:
    """Markdown in the same shape as the pack's captured pages (ADR 0001 image hooks)."""

    def __init__(self, url: str, title: str, local_path: str, body: Body,
                 url_to_local: dict[str, str], asset_urls: dict[str, str]):
        self.url, self.title, self.local_path = url, title, local_path
        self.body, self.url_to_local, self.asset_urls = body, url_to_local, asset_urls
        self.hooks: list[dict] = []
        self.parent: dict[int, list] = {}

    def map_parents(self, node, chain):
        here = chain + [node]
        for child in node.children:
            if isinstance(child, Node):
                self.parent[id(child)] = here
                self.map_parents(child, here)

    def inline(self, node) -> str:
        if isinstance(node, str):
            return node
        if node.tag == "img":
            return self.image_markdown(node)
        if node.tag == "a":
            raw_href = node.attrs.get("href", "")
            if raw_href.startswith("#") or not raw_href.strip():
                return normalize_space("".join(self.inline(c) for c in node.children))
            href = resolve(self.url, raw_href)
            base_url = href.split("#")[0].split("?")[0]
            frag = href[len(base_url):]
            loc = None if "?" in href else self.url_to_local.get(base_url)
            link = encode_link(relpath_target(self.local_path, loc) + frag) if loc else href
            label = normalize_space("".join(self.inline(c) for c in node.children)) \
                or base_url.rsplit("/", 1)[-1]
            return "[%s](%s)" % (label, link)
        if node.tag == "br":
            return " "
        inner = "".join(self.inline(c) for c in node.children)
        if node.tag in ("b", "strong"):
            return "**%s**" % inner if inner.strip() else inner
        if node.tag in ("code", "tt"):
            return "`%s`" % inner.strip() if inner.strip() else inner
        if node.tag in ("i", "em"):
            return "*%s*" % inner if inner.strip() else inner
        return inner

    def inline_of(self, node) -> str:
        return normalize_space("".join(self.inline(c) for c in node.children))

    def plain_of(self, node) -> str:
        if isinstance(node, str):
            return node
        if node.tag == "img":
            return ""
        return "".join(self.plain_of(c) for c in node.children)

    def context_for(self, img) -> str:
        for anc in reversed(self.parent.get(id(img), [])):
            if anc.tag in ("li", "dd", "dt", "p", "td"):
                txt = re.sub(r"[#|`>\s]+", " ", normalize_space(self.plain_of(anc))).strip(" .;；")
                if len(txt) >= 4:
                    return txt[:60] + "…" if len(txt) > 60 else txt
        return "（图旁无可取正文，Maya 手册 img 无 alt）"

    def image_markdown(self, img) -> str:
        abs_url = resolve(self.url, img.attrs.get("src", ""))
        staged = self.asset_urls.get(abs_url)
        target, downloaded = abs_url, False
        if staged:
            target, downloaded = staged, True
        comment = '<!-- baize:img-hook downloaded=%s reason="%s" -->' % (
            "true" if downloaded else "false", self.body.reason)
        self.hooks.append({"url": abs_url, "downloaded": downloaded,
                           "context": self.context_for(img)})
        return "![图：%s](%s) %s" % (self.context_for(img), target, comment)

    def block(self, node, out: list[str], depth: int = 0, marker: str = "") -> None:
        if isinstance(node, str):
            txt = normalize_space(node)
            if txt:
                out.append("  " * depth + txt + "\n")
            return
        if node.tag in SKIP:
            return
        if node.tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            out.append("\n%s%s %s\n" % ("  " * depth, "#" * int(node.tag[1]), self.inline_of(node)))
            return
        if node.tag == "p":
            txt = self.inline_of(node)
            if txt:
                out.append("  " * depth + marker + txt + "\n")
            return
        if node.tag == "pre":
            raw = texts(node).replace("\r\n", "\n")
            body = "\n".join(ln.rstrip() for ln in raw.split("\n")).strip("\n")
            if body:
                joined = " ".join(classes(node) + [node.attrs.get("class") or ""]).lower()
                lang = "python" if "python" in joined else "mel" if "mel" in joined else "text"
                out.append("\n" + "  " * depth + "```%s\n%s\n```\n" % (lang, body))
            return
        if node.tag == "table":
            self.render_table(node, out, depth)
            return
        if node.tag in ("ol", "ul"):
            index = 0
            for child in node.children:
                if isinstance(child, Node) and child.tag == "li":
                    index += 1
                    self.block(child, out, depth, "%d. " % index if node.tag == "ol" else "- ")
                elif isinstance(child, Node):
                    self.block(child, out, depth)
                elif normalize_space(child):
                    out.append("  " * depth + normalize_space(child) + "\n")
            return
        if node.tag in ("li", "dd"):
            self.mixed(node, out, depth, marker)
            return
        if node.tag == "dl":
            self.render_dl(node, out, depth)
            return
        if node.tag == "dt":
            txt = self.inline_of(node)
            if txt:
                out.append("\n" + "  " * depth + txt + "\n")
            return
        if node.tag == "caption":
            txt = self.inline_of(node)
            if txt:
                out.append("\n" + "  " * depth + "**表：%s**\n" % txt)
            return
        if node.tag == "div" and "note" in classes(node):
            title, rest = "", []
            for child in node.children:
                if isinstance(child, Node) and child.tag == "span" and "notetitle" in classes(child):
                    title = normalize_space(self.inline_of(child)).rstrip("：:")
                else:
                    rest.append(child)
            out.append("\n" + "  " * depth + "**%s**\n" % (title or "注"))
            for child in rest:
                self.block(child, out, depth)
            return
        self.mixed(node, out, depth)

    def mixed(self, node, out: list[str], depth: int, marker: str = "") -> None:
        parts: list = []

        def flush() -> None:
            if not parts:
                return
            txt = normalize_space("".join(self.inline(x) for x in parts))
            del parts[:]
            if txt:
                out.append("  " * depth + marker + txt + "\n")

        for child in node.children:
            if isinstance(child, Node) and child.tag in BLOCKISH:
                flush()
                self.block(child, out, depth + 1 if marker else depth)
            else:
                parts.append(child)
        flush()

    def topmost(self, tr) -> Node | None:
        for anc in reversed(self.parent.get(id(tr), [])):
            if anc.tag == "table":
                return anc
        return None

    def cell_of(self, cell) -> str:
        return self.inline_of(cell).replace("|", "\\|").replace("\n", " ")

    def render_table(self, table, out: list[str], depth: int) -> None:
        rows = []
        for tr in [el for el in elements(table) if el.tag == "tr"]:
            if self.topmost(tr) is not table:
                continue
            cells = [self.cell_of(td) for td in tr.children
                     if isinstance(td, Node) and td.tag in ("td", "th")]
            if cells:
                rows.append(cells)
        if not rows:
            return
        width = max(len(r) for r in rows)
        pad = 2 if width == 1 else width
        out.append("")
        out.append("  " * depth + "| " + " | ".join(rows[0] + [""] * (pad - len(rows[0]))) + " |")
        out.append("  " * depth + "|" + "---|" * pad)
        for row in rows[1:]:
            out.append("  " * depth + "| " + " | ".join(row + [""] * (pad - len(row))) + " |")
        out.append("")

    def render_dl(self, dl, out: list[str], depth: int) -> None:
        kids = [c for c in dl.children if isinstance(c, Node) and c.tag in ("dt", "dd")]
        hashes = "#" * 4
        i = 0
        while i < len(kids):
            if kids[i].tag == "dt":
                name = self.inline_of(kids[i])
                if name:
                    out.append("\n" + "  " * depth + hashes + " " + name + "\n")
                i += 1
                while i < len(kids) and kids[i].tag == "dd":
                    self.block(kids[i], out, depth)
                    i += 1
            else:
                self.block(kids[i], out, depth)
                i += 1

    def render(self) -> str:
        self.map_parents(self.body.node, [])
        out: list[str] = ["# " + self.title + "\n"]
        for child in self.body.node.children:
            self.block(child, out)
        text = re.sub(r"\n{3,}", "\n\n", "\n".join(out))
        return "\n".join(ln.rstrip() for ln in text.split("\n")).strip("\n") + "\n"


def summary_of(md: str) -> str:
    body = [ln.strip() for ln in md.split("\n")
            if ln.strip() and not ln.lstrip().startswith(("#", "!", ">", "|", "```"))]
    txt = " ".join(body)
    txt = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", txt)
    txt = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", txt)
    txt = re.sub(r"[`*]", "", normalize_space(txt))
    return (txt[:110] + "…") if len(txt) > 110 else txt


def keywords_of(title: str, local_path: str) -> list[str]:
    kw = {PurePosixPath(local_path).parent.name}
    kw.update(PurePosixPath(local_path).parts[1:-1])
    for part in re.split(r"[，。、（）()\s/：:？?！!]+", title):
        if 2 <= len(part.strip()) <= 20:
            kw.add(part.strip())
    return sorted(item for item in kw if item)[:8]


# ---------------------------------------------------------------- fetching


def check_hosts(rows: list[dict]) -> None:
    bad = sorted({r["u"] for r in rows if urlsplit(r["u"]).netloc.casefold() not in ALLOWED_HOSTS})
    if bad:
        raise Refuse("host not in whitelist %s: %s" % (sorted(ALLOWED_HOSTS), bad[:5]))


def check_batch_size(rows: list[dict]) -> None:
    if len(rows) > MAX_APPLY_PAGES:
        raise Refuse("batch of %d pages exceeds the %d-page limit; split it into smaller runs"
                     % (len(rows), MAX_APPLY_PAGES))


def fetch_bytes(url: str) -> tuple[bytes, dict]:
    import urllib.request  # deferred: --suggest never reaches this line

    last = None
    for attempt in range(MAX_ATTEMPTS):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=40) as resp:
                head = {k.lower(): v for k, v in resp.headers.items()}
                return resp.read(), {"status": getattr(resp, "status", None), "head": head}
        except Exception as exc:  # noqa: BLE001
            last = "%r" % (exc,)[:200]
            time.sleep(round(random.uniform(1.0, 1.5), 2))
    raise RuntimeError("fetch failed after %d attempts: %s (%s)" % (MAX_ATTEMPTS, url, last))


# ---------------------------------------------------------------- writing


def timestamp() -> str:
    return time.strftime("%Y%m%d-%H%M%S")


def sha16_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def backup(stamp: str, files: list[Path]) -> Path:
    dest = BACKUP_ROOT / stamp
    dest.mkdir(parents=True, exist_ok=False)
    for src in files:
        shutil.copy2(src, dest / src.name)
    return dest


STAMP_RE = re.compile(r"^\d{8}-\d{6}$")


def prune_old_backups(keep: int = MAX_BACKUP_KEPT) -> list[dict]:
    """Keep the newest `keep` timestamp dirs we created; older ones are listed (with per-file
    sha16) before being removed. Only dirs named exactly like our own <timestamp> are touched."""
    if not BACKUP_ROOT.is_dir():
        return []
    stamps = sorted(p.name for p in BACKUP_ROOT.iterdir()
                    if p.is_dir() and STAMP_RE.match(p.name))
    pruned: list[dict] = []
    for name in stamps[: max(len(stamps) - keep, 0)]:
        directory = BACKUP_ROOT / name
        entries = [{"file": item.name, "bytes": os.path.getsize(item),
                    "sha256_16": sha16_of(item)}
                   for item in sorted(directory.iterdir()) if item.is_file()]
        for item in directory.iterdir():
            if item.is_file():
                item.unlink()
        if not any(directory.iterdir()):
            os.rmdir(directory)
            pruned.append({"stamp": name, "bytes": sum(e["bytes"] for e in entries), "files": entries})
        else:
            pruned.append({"stamp": name, "bytes": sum(e["bytes"] for e in entries),
                           "files": entries, "kept": "dir not empty, left in place"})
    return pruned


def prune_empty_dirs(paths: list[Path]) -> list[str]:
    """Drop directories this run created and left empty; never touches a dir holding files."""
    gone: list[str] = []
    candidates: set[Path] = set()
    for path in paths:
        cursor = path.parent
        while cursor != DOCS_ROOT and DOCS_ROOT in cursor.parents:
            candidates.add(cursor)
            cursor = cursor.parent
    for directory in sorted(candidates, key=lambda q: len(q.parts), reverse=True):
        if directory.is_dir() and not any(directory.iterdir()):
            os.rmdir(directory)
            gone.append(directory.relative_to(DOCS_ROOT).as_posix())
    return gone


def rollback_from(stamp: str, written_docs: list[Path], written_assets: list[Path]) -> list[str]:
    dest = BACKUP_ROOT / stamp
    actions: list[str] = []
    for name in ("wiki-manifest.json", "INDEX.md", "missing_pages.json"):
        src = dest / name
        if src.is_file():
            shutil.copy2(src, REFERENCES / name)
            actions.append("restored " + name)
    for path in written_docs + written_assets:
        if path.is_file():
            path.unlink()
            actions.append("removed own file " + path.relative_to(REFERENCES).as_posix())
    for rel in prune_empty_dirs(written_docs):
        actions.append("removed own empty dir " + rel)
    return actions


def append_changelog(lines: list[str]) -> None:
    EXT_ROOT.mkdir(parents=True, exist_ok=True)
    header = ""
    if not CHANGELOG_PATH.is_file():
        header = ("# Local extension changelog\n\n"
                  "One line per page added by scripts/add_pages.py. Newest appended last.\n")
    with CHANGELOG_PATH.open("a", encoding="utf-8", newline="\n") as handle:
        if header:
            handle.write(header)
        handle.write("".join(ln + "\n" for ln in lines))


def suggest(rows: list[dict], manifest: dict) -> int:
    documents = manifest.get("documents", {})
    sizes = []
    for local_path in sorted(documents)[:400]:
        path = DOCS_ROOT / PurePosixPath(local_path).as_posix()
        if path.is_file():
            sizes.append(path.stat().st_size)
    avg = sum(sizes) // len(sizes) if sizes else 0
    print("MODE: --suggest (offline, read-only, no request was sent)")
    print("source=%s entries_in_list=%d" % (MISSING_PATH.as_posix(), len(rows)))
    for row in rows:
        print("- %s | %s | %s" % (row["p"], row["t"], row["u"]))
    print("selected pages: %d" % len(rows))
    print("estimated bytes: ~%d (estimate: mean of %d sampled captured docs = %d B each)"
          % (avg * len(rows), len(sizes), avg))
    print("NOTE: no request sent, no file written")
    return 0


def capture_one(row: dict, local_path: str, source_url: str, url_to_local: dict[str, str],
                written_assets: list[Path]) -> tuple[bytes, Body, dict]:
    """Fetch + convert one page. Returns md bytes; images go to .extension/assets only."""
    raw, info = fetch_bytes(source_url)
    body = Body(raw.decode("utf-8", errors="replace"), source_url)
    asset_urls: dict[str, str] = {}
    if body.load_bearing:
        for img in body.images:
            abs_url = resolve(source_url, img.attrs.get("src", ""))
            if urlsplit(abs_url).netloc.casefold() not in ALLOWED_HOSTS:
                continue
            rel = "%s/%s" % (row["b"], PurePosixPath(urlsplit(abs_url).path).name)
            dest = EXT_ROOT / "assets" / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            data, _ = fetch_bytes(abs_url)
            dest.write_bytes(data)
            written_assets.append(dest)
            asset_urls[abs_url] = asset_link(rel, local_path)
    renderer = Renderer(source_url, row["t"], local_path, body, url_to_local, asset_urls)
    md = swd.normalize_markdown(renderer.render())
    if not md.startswith("# "):
        raise Refuse("rendered page has no H1: " + local_path)
    return md.encode("utf-8"), body, info


def shrink_excluded(excluded, added_urls: set[str], added_count: int):
    """coverage.excluded is either a count or a roster of hook entries; shrink both ways."""
    if isinstance(excluded, list):
        return [item for item in excluded
                if not (isinstance(item, dict) and item.get("url") in added_urls)]
    if isinstance(excluded, int):
        return max(excluded - added_count, 0)
    return excluded


def apply_pages(rows: list[dict], manifest: dict, batch: str) -> int:
    check_batch_size(rows)
    check_hosts(rows)
    documents = manifest.get("documents")
    if not isinstance(documents, dict):
        raise Refuse("manifest.documents must be an object")
    url_to_local = {entry["source_url"]: path for path, entry in documents.items()
                    if isinstance(entry, dict) and isinstance(entry.get("source_url"), str)}

    stamp = timestamp()
    backup_dir = backup(stamp, [MANIFEST_PATH, INDEX_PATH, MISSING_PATH])
    pruned_backups = prune_old_backups()
    written_docs: list[Path] = []
    written_assets: list[Path] = []
    changelog: list[str] = []
    report: dict = {"batch": batch, "stamp": stamp, "backup": backup_dir.as_posix(),
                    "backups_pruned": pruned_backups,
                    "requested": len(rows), "added": [], "skipped": [], "failed": []}
    try:
        for row in rows:
            local_path = swd.safe_relative(row["p"], markdown=True)
            source_url = swd.validate_url(row["u"], "missing_pages.u")
            target = DOCS_ROOT / PurePosixPath(local_path).as_posix()
            if target.exists() or local_path in documents:
                report["skipped"].append({"local_path": local_path, "reason": "already in pack"})
                continue
            try:
                data, body, info = capture_one(row, local_path, source_url, url_to_local,
                                               written_assets)
            except Exception as exc:  # noqa: BLE001
                report["failed"].append({"local_path": local_path, "source_url": source_url,
                                         "error": str(exc)[:300]})
                continue
            swd.atomic_write(target, data)
            written_docs.append(target)
            documents[local_path] = {
                "title": row["t"],
                "source_url": source_url,
                "source_path": urlsplit(source_url).path,
                "local_path": local_path,
                "summary": summary_of(data.decode("utf-8")),
                "keywords": keywords_of(row["t"], local_path),
                "content_hash": swd.sha256(data),
                "updated_at": swd.utc_now(),
            }
            url_to_local[source_url] = local_path
            sha16 = hashlib.sha256(data).hexdigest()[:16]
            changelog.append("| %s | %s | `%s` | %s | %d | `%s` |" % (
                time.strftime("%Y-%m-%d %H:%M:%S"), batch, local_path,
                "<" + source_url + ">", os.path.getsize(target), sha16))
            report["added"].append({"local_path": local_path, "source_url": source_url,
                                    "bytes": os.path.getsize(target),
                                    "sha256_16": sha16, "words": body.words,
                                    "load_bearing": body.load_bearing,
                                    "http_status": info["status"]})
            time.sleep(round(random.uniform(1.0, 1.5), 2))
        if not changelog:
            raise Refuse("nothing added (%d skipped, %d failed); leaving pack untouched"
                         % (len(report["skipped"]), len(report["failed"])))
        coverage = dict(manifest.get("coverage", {}))
        added = len(report["added"])
        failed_list = report["failed"]
        added_urls = {item["source_url"] for item in report["added"]}
        coverage["captured"] = int(coverage.get("captured", 0)) + added
        coverage["discovered"] = coverage["captured"] + len(failed_list)
        coverage["failed"] = failed_list
        coverage["excluded"] = shrink_excluded(coverage.get("excluded"), added_urls, added)
        coverage["complete"] = not failed_list and coverage["discovered"] == coverage["captured"]
        manifest["coverage"] = coverage
        manifest["last_sync_at"] = swd.utc_now()
        index_bytes = swd.render_index(manifest["wiki"]["title"], manifest["wiki"]["source_root"], documents)
        missing_data = json.loads(MISSING_PATH.read_text(encoding="utf-8"))
        added_paths = {item["local_path"] for item in report["added"]}
        missing_data["pages"] = [r for r in missing_data["pages"] if r["p"] not in added_paths]
        missing_data["_meta"]["entries"] = len(missing_data["pages"])
        missing_data["_meta"]["generated_at"] = time.strftime("%Y-%m-%d %H:%M:%S")
        missing_bytes = (json.dumps(missing_data, ensure_ascii=False,
                                    separators=(",", ":")) + "\n").encode("utf-8")
        swd.atomic_write(INDEX_PATH, index_bytes)
        swd.atomic_write(MANIFEST_PATH, (json.dumps(manifest, ensure_ascii=False, indent=2,
                                                   sort_keys=True) + "\n").encode("utf-8"))
        swd.atomic_write(MISSING_PATH, missing_bytes)
        append_changelog(changelog)
        report["documents_total"] = len(documents)
        report["assets_written"] = [p.relative_to(EXT_ROOT).as_posix() for p in written_assets]
    except Exception as exc:  # noqa: BLE001
        actions = rollback_from(stamp, written_docs, written_assets)
        report["aborted"] = str(exc)[:400]
        report["rollback"] = actions
        print("FAILED: %s" % str(exc)[:400], file=sys.stderr)
        print("rolled back: %s" % ("; ".join(actions) or "nothing to undo"))
        write_report(batch, report)
        info = {"batch": batch, "stamp": stamp, "backup": backup_dir.as_posix(),
                "ok": False, "aborted": True, "added": 0, "skipped": len(report["skipped"]),
                "failed": len(report["failed"]), "reason": str(exc)[:200]}
        return 2, info
    write_report(batch, report)
    print("APPLIED batch=%s added=%d skipped=%d failed=%d documents=%d"
          % (batch, len(report["added"]), len(report["skipped"]), len(report["failed"]),
             report["documents_total"]))
    print("backup=%s stamp=%s" % (backup_dir.as_posix(), stamp))
    print("run scripts/selfcheck.py before you trust this batch")
    info = {"batch": batch, "stamp": stamp, "backup": backup_dir.as_posix(),
            "ok": True, "added": len(report["added"]), "skipped": len(report["skipped"]),
            "failed": len(report["failed"]), "documents_total": report["documents_total"],
            "added_bytes": sum(int(x.get("bytes", 0)) for x in report["added"])}
    return 0, info


def write_report(batch: str, report: dict) -> None:
    EXT_ROOT.mkdir(parents=True, exist_ok=True)
    path = EXT_ROOT / ("report-%s.json" % report["stamp"])
    older = sorted(p for p in EXT_ROOT.glob("report-*.json") if p != path)
    if older:
        report["older_reports_removed"] = [
            {"file": p.name, "bytes": os.path.getsize(p), "sha256_16": sha16_of(p)} for p in older]
    path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8", newline="\n")
    if json.loads(path.read_text(encoding="utf-8")).get("stamp") != report["stamp"]:
        raise Refuse("report did not round-trip: " + path.as_posix())
    for p in older:
        p.unlink()
    if BACKUP_ROOT.is_dir() and (BACKUP_ROOT / report["stamp"]).is_dir():
        shutil.copy2(path, BACKUP_ROOT / report["stamp"] / path.name)


def rollback(stamp: str) -> int:
    dest = BACKUP_ROOT / stamp
    if not dest.is_dir():
        raise Refuse("no backup directory " + dest.as_posix())
    report: dict = {}
    report_file = EXT_ROOT / ("report-%s.json" % stamp)
    if not report_file.is_file() and (dest / ("report-%s.json" % stamp)).is_file():
        report_file = dest / ("report-%s.json" % stamp)
    if report_file.is_file():
        report = json.loads(report_file.read_text(encoding="utf-8"))
    docs = [DOCS_ROOT / item["local_path"] for item in report.get("added", [])]
    assets = [EXT_ROOT / item for item in report.get("assets_written", [])]
    actions = rollback_from(stamp, docs, assets)
    batch = report.get("batch", "")
    if batch and CHANGELOG_PATH.is_file():
        kept = [ln for ln in CHANGELOG_PATH.read_text(encoding="utf-8").splitlines()
                if ln.strip() and "| %s |" % batch not in ln]
        CHANGELOG_PATH.write_text("\n".join(kept) + ("\n" if kept else ""),
                                 encoding="utf-8", newline="\n")
        actions.append("pruned CHANGELOG lines of batch " + batch)
    print("ROLLBACK stamp=%s" % stamp)
    for line in actions:
        print("- " + line)
    return 0


def _patch_newest_report(infos: list[dict], stopped: bool) -> None:
    """Fold the whole-run summary into the newest in-pack report (only one report stays in-pack
    by design), so per-slice stamps/added/bytes survive even though the earlier reports get pruned."""
    if not infos:
        return
    reports = sorted(EXT_ROOT.glob("report-*.json"))
    if not reports:
        return
    newest = reports[-1]
    try:
        data = json.loads(newest.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001  an unreadable report must not crash the run summary
        return
    data["multi_slice"] = {
        "batches": [{k: v for k, v in it.items() if k in
                     ("batch", "stamp", "added", "skipped", "failed", "added_bytes",
                      "documents_total", "ok")} for it in infos],
        "total_batches": len(infos),
        "total_added": sum(it.get("added", 0) for it in infos),
        "total_failed": sum(it.get("failed", 0) for it in infos),
        "stopped": stopped,
        "not_run_after_stop": (len(infos) and stopped),
    }
    text = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    newest.write_text(text, encoding="utf-8", newline="\n")
    if json.loads(newest.read_text(encoding="utf-8")).get("stamp") != data.get("stamp"):
        raise Refuse("multi-slice summary did not round-trip: " + newest.as_posix())


def run_in_slices(rows: list[dict], batch: str, max_per_batch: int | None) -> int:
    """Apply a whole selected list, auto-sharded into serial slices of <= MAX_APPLY_PAGES each.
    Full-list safety review happens before the first request; any slice that returns non-zero
    stops the remaining slices while leaving already-completed slices intact (no cross-slice undo)."""
    size = MAX_APPLY_PAGES if max_per_batch is None else int(max_per_batch)
    if size > MAX_APPLY_PAGES:
        print("NOTE: batch size above %d was requested (%d); slicing by %d anyway"
              % (MAX_APPLY_PAGES, size, MAX_APPLY_PAGES))
        size = MAX_APPLY_PAGES
    if size < 1:
        size = 1
    # 全量先审: host whitelist over the ENTIRE input, before any slice fetches.
    # select() already rejected URLs not in missing_pages; check_hosts blocks off-whitelist hosts.
    check_hosts(rows)
    chunks = [rows[i:i + size] for i in range(0, len(rows), size)]
    infos: list[dict] = []
    total_added = total_failed = 0
    for i, chunk in enumerate(chunks, 1):
        label = batch if len(chunks) == 1 else "%s-%d" % (batch, i)
        manifest = swd.read_json(MANIFEST_PATH)
        rc, info = apply_pages(chunk, manifest, label)
        infos.append(info)
        total_added += info.get("added", 0)
        total_failed += info.get("failed", 0)
        if rc != 0:
            remaining = len(chunks) - i
            done = ", ".join(x["batch"] for x in infos[:-1]) or "none"
            print("STOPPED at batch %d/%d (label=%s) rc=%d; completed batch(es) kept and NOT "
                  "rolled back; %d batch(es) not run" % (i, len(chunks), label, rc, remaining))
            print("completed batch labels: %s" % done)
            print("per-slice evidence: references/.extension/CHANGELOG.local.md + "
                  "references/.extension/report-*.json (newest holds the whole-run summary)")
            print("TOTAL batches=%d added=%d failed=%d (stopped; %d of %d not run)"
                  % (i, total_added, total_failed, remaining, len(chunks)))
            _patch_newest_report(infos, stopped=True)
            return rc
    print("TOTAL batches=%d added=%d failed=%d" % (len(chunks), total_added, total_failed))
    _patch_newest_report(infos, stopped=False)
    return 0


def repair_image_links() -> int:
    """Ruling D39 local-only repair: fix the '../' depth of every image link in
    references/docs/**.md so it matches each page's own depth, then recompute those
    pages' content_hash through the tool's existing hashing口径. No network, no image
    moves, no CHANGELOG/report writes; text bytes other than the link prefix are unchanged.

    Idempotent: a second run finds every prefix already correct and writes nothing.
    """
    manifest = swd.read_json(MANIFEST_PATH)
    documents = manifest.get("documents")
    if not isinstance(documents, dict):
        raise Refuse("manifest.documents must be an object")
    scanned = pages_with_links = pages_changed = links_changed = already_correct = 0
    samples: list[str] = []
    for path in sorted(DOCS_ROOT.rglob("*.md")):
        if not path.is_file():
            continue
        scanned += 1
        rel = path.relative_to(DOCS_ROOT).as_posix()
        old_text = path.read_text(encoding="utf-8")
        want = asset_link_prefix(rel)
        new_text, n = ASSET_LINK_RE.subn(lambda m: m.group(1) + want + m.group(3), old_text)
        if n == 0:
            continue
        pages_with_links += 1
        if new_text == old_text:
            already_correct += 1
            continue
        new_bytes = new_text.encode("utf-8")
        # safety: the only delta must be inside the link prefix; normalising must be a no-op
        # (proves we added no whitespace/newline and drifted no other byte).
        if swd.normalize_markdown(new_text).encode("utf-8") != new_bytes:
            raise Refuse("repair would change bytes beyond the link prefix: " + rel)
        swd.atomic_write(path, new_bytes)
        entry = documents.get(rel)
        if isinstance(entry, dict):
            entry["content_hash"] = swd.sha256(new_bytes)
        pages_changed += 1
        links_changed += n
        if len(samples) < 5:
            samples.append("%s prefix=%s links=%d" % (rel, want, n))
    if pages_changed:
        swd.atomic_write(MANIFEST_PATH, (json.dumps(manifest, ensure_ascii=False, indent=2,
                                                   sort_keys=True) + "\n").encode("utf-8"))
    print("REPAIR-IMAGE-LINKS scanned=%d pages_with_asset_links=%d pages_changed=%d "
          "links_changed=%d already_correct=%d manifest_updated=%s"
          % (scanned, pages_with_links, pages_changed, links_changed, already_correct,
             bool(pages_changed)))
    for s in samples:
        print("  - " + s)
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--keywords", help="space separated terms matched against t and p")
    group.add_argument("--paths", type=Path, help="file of local_path values, one per line")
    group.add_argument("--url", type=Path, help="file of source_url values, one per line")
    group.add_argument("--repair-image-links", action="store_true",
                       help="local-only D39 fix: rewrite the '../' depth of image links in "
                            "references/docs/**.md to each page's own depth and recompute those "
                            "pages' content_hash; no network, no --apply, no CHANGELOG/report write")
    parser.add_argument("--apply", action="store_true",
                        help="fetch and write; without this flag the run is --suggest")
    parser.add_argument("--batch", default="", help="batch label for CHANGELOG.local.md")
    parser.add_argument("--max-per-batch", type=int, default=None, metavar="N",
                        help="pages per slice when --apply auto-shards the whole list "
                             "(default %d = MAX_APPLY_PAGES; smaller allowed; values above %d "
                             "are announced and still sliced at %d)"
                             % (MAX_APPLY_PAGES, MAX_APPLY_PAGES, MAX_APPLY_PAGES))
    parser.add_argument("--backup-dir", type=Path,
                        help="override where pre-write backups go (default: %s)"
                             % BACKUP_ROOT.as_posix())
    parser.add_argument("--rollback", metavar="STAMP", help="undo an applied run by backup stamp")
    return parser.parse_args()


def main() -> int:
    global BACKUP_ROOT
    args = parse_args()
    if args.backup_dir is not None:
        BACKUP_ROOT = args.backup_dir.expanduser().resolve()
    try:
        if args.rollback:
            return rollback(args.rollback)
        if args.repair_image_links:
            return repair_image_links()
        rows = select(load_missing(), args.keywords, args.paths, args.url)
        manifest = swd.read_json(MANIFEST_PATH)
        if not args.apply:
            return suggest(rows, manifest)
        batch = args.batch or ("LOCAL-%s" % time.strftime("%Y%m%d"))
        return run_in_slices(rows, batch, args.max_per_batch)
    except FileNotFoundError as exc:
        print("FAILED: input file not readable: %s" % exc, file=sys.stderr)
        print("nothing was fetched and nothing was written")
        return 2
    except (Refuse, swd.SyncError) as exc:
        print("REFUSED: %s" % exc, file=sys.stderr)
        print("nothing was fetched and nothing was written; exit %d means refused" % REFUSED_RC)
        return REFUSED_RC


if __name__ == "__main__":
    raise SystemExit(main())
