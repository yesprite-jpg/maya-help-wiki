#!/usr/bin/env python3
"""Health check for this pack: last line EVIDENCE_ALL_OK means nothing is broken.

Read-only and stdlib-only. Run it after add_pages.py --apply, and before trusting any
extension batch. A non-zero rc means do not use that batch.

Checks (order fixed, each prints one line):
  1 documents in wiki-manifest.json vs references/docs on disk, both directions
  2 per-document sha256 recomputed and compared with content_hash
  3 coverage identity: discovered == captured + failed, captured == len(documents)
  4 assets: registered count vs disk, per-file sha256, zero-byte files
  5 relative markdown links resolve inside the pack (broken links)
  6 encoding hygiene: UTF-8, no CRLF, no control characters, first line is H1
  7 '* -text' present in the pack root's .gitattributes (ruling D33; ancestor reading also printed)
  8 references/missing_pages.json exists and its counts are self-consistent
  9 extension batches from .extension/CHANGELOG.local.md + baseline pages untouched
  10 in-pack references/.extension/ stays small (<= 256 KiB); backups belong outside the pack
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import unicodedata
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit

SCRIPTS_DIR = Path(__file__).resolve().parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import sync_wiki_docs as swd  # noqa: E402  (reused: normalize_markdown / sha256)

PACK_ROOT = SCRIPTS_DIR.parent
REFERENCES = PACK_ROOT / "references"
DOCS_ROOT = REFERENCES / "docs"
ASSETS_ROOT = REFERENCES / "assets"
MANIFEST_PATH = REFERENCES / "wiki-manifest.json"
MISSING_PATH = REFERENCES / "missing_pages.json"
CHANGELOG_PATH = REFERENCES / ".extension" / "CHANGELOG.local.md"
EXTENSION_ROOT = REFERENCES / ".extension"

LINK_RE = re.compile(r"\]\(([^)\s]+)\)")


class Report:
    def __init__(self) -> None:
        self.failures: list[str] = []

    def line(self, ok: bool, label: str, detail: str) -> None:
        print("%s %s | %s" % ("OK  " if ok else "FAIL", label, detail))
        if not ok:
            self.failures.append(label)


def disk_docs() -> dict[str, Path]:
    return {path.relative_to(DOCS_ROOT).as_posix(): path
            for path in DOCS_ROOT.rglob("*.md") if path.is_file()}


def check_manifest_vs_disk(rep: Report, documents: dict) -> None:
    on_disk = disk_docs()
    only_manifest = sorted(set(documents) - set(on_disk))
    only_disk = sorted(set(on_disk) - set(documents))
    rep.line(not only_manifest and not only_disk, "1 manifest<->disk diff",
             "manifest=%d disk=%d missing_on_disk=%d missing_in_manifest=%d%s"
             % (len(documents), len(on_disk), len(only_manifest), len(only_disk),
                "" if not (only_manifest or only_disk) else " e.g. "
                + ", ".join((only_manifest + only_disk)[:3])))


def check_hashes(rep: Report, documents: dict) -> list[str]:
    bad, checked = [], 0
    for local_path, entry in sorted(documents.items()):
        path = DOCS_ROOT / PurePosixPath(local_path).as_posix()
        if not path.is_file():
            continue
        data = swd.normalize_markdown(path.read_text(encoding="utf-8", errors="replace")).encode("utf-8")
        checked += 1
        if swd.sha256(data) != entry.get("content_hash"):
            bad.append(local_path)
    rep.line(not bad, "2 content_hash vs disk",
             "checked=%d mismatch=%d%s" % (checked, len(bad),
                                           "" if not bad else " e.g. " + ", ".join(bad[:3])))
    return bad


def check_coverage(rep: Report, coverage: dict, documents: dict) -> None:
    discovered = coverage.get("discovered")
    captured = coverage.get("captured")
    failed = coverage.get("failed")
    ok = (isinstance(discovered, int) and isinstance(captured, int)
          and isinstance(failed, list) and discovered == captured + len(failed)
          and captured == len(documents))
    excluded = coverage.get("excluded")
    rep.line(ok, "3 coverage identity",
             "discovered=%s captured=%s failed=%d documents=%d excluded=%s"
             % (discovered, captured, len(failed) if isinstance(failed, list) else -1,
                len(documents),
                len(excluded) if isinstance(excluded, list) else excluded))


def check_assets(rep: Report, assets: dict) -> None:
    on_disk = {path.relative_to(ASSETS_ROOT).as_posix(): path
               for path in ASSETS_ROOT.rglob("*") if path.is_file()} if ASSETS_ROOT.is_dir() else {}
    only_manifest = sorted(set(assets) - set(on_disk))
    only_disk = sorted(set(on_disk) - set(assets))
    bad, zero = [], []
    for local_path, entry in sorted(assets.items()):
        path = on_disk.get(local_path)
        if not path:
            continue
        data = path.read_bytes()
        if not data:
            zero.append(local_path)
        if swd.sha256(data) != entry.get("content_hash"):
            bad.append(local_path)
    ok = not (only_manifest or only_disk or bad or zero)
    rep.line(ok, "4 assets",
             "registered=%d disk=%d only_manifest=%d only_disk=%d hash_mismatch=%d zero_byte=%d"
             % (len(assets), len(on_disk), len(only_manifest), len(only_disk), len(bad), len(zero)))


def relative_targets(root: Path, documents: dict) -> list[tuple[str, str]]:
    out = []
    for local_path in sorted(documents):
        path = root / PurePosixPath(local_path).as_posix()
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for target in LINK_RE.findall(text):
            if urlsplit(target).scheme or target.startswith("#") or "<" in target:
                continue
            clean = unquote(target.split("#")[0].split("?")[0])
            if not clean:
                continue
            out.append((local_path, clean))
    return out


def check_links(rep: Report, links: list[tuple[str, str]]) -> None:
    broken = []
    for local_path, target in links:
        base = DOCS_ROOT / PurePosixPath(local_path).as_posix()
        if not (base.parent / target).resolve().exists():
            broken.append("%s -> %s" % (local_path, target))
    rep.line(not broken, "5 relative links",
             "relative_targets=%d broken=%d%s"
             % (len(links), len(broken), "" if not broken else " e.g. " + broken[0]))


def check_encoding(rep: Report, documents: dict) -> None:
    not_utf8 = crlf = control = no_h1 = 0
    for local_path in sorted(documents):
        path = DOCS_ROOT / PurePosixPath(local_path).as_posix()
        if not path.is_file():
            continue
        raw = path.read_bytes()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            not_utf8 += 1
            continue
        if b"\r\n" in raw:
            crlf += 1
        if any(unicodedata.category(ch) == "Cc" and ch not in "\n\t" for ch in text):
            control += 1
        if not text.split("\n", 1)[0].startswith("# "):
            no_h1 += 1
    ok = not (not_utf8 or crlf or control or no_h1)
    rep.line(ok, "6 encoding hygiene",
             "docs=%d not_utf8=%d crlf=%d control_chars=%d missing_h1=%d"
             % (len(documents), not_utf8, crlf, control, no_h1))


def check_gitattributes(rep: Report) -> None:
    """Ruling D33 (2026-10-10): the pack root must carry it; both readings reported, never merged."""
    pack_file = PACK_ROOT / ".gitattributes"
    hit_pack = pack_file.is_file() and "* -text" in pack_file.read_text(encoding="utf-8")
    governed = None
    for parent in PACK_ROOT.resolve().parents:
        candidate = parent / ".gitattributes"
        if candidate.is_file() and "* -text" in candidate.read_text(encoding="utf-8"):
            governed = candidate
            break
    rep.line(bool(hit_pack), "7 gitattributes '* -text' (pack root required)",
             "pack_root=%s bytes=%d | governing_ancestor=%s"
             % ("present" if hit_pack else "ABSENT",
                os.path.getsize(pack_file) if pack_file.is_file() else 0,
                governed.as_posix() if governed else "none"))


def check_missing_list(rep: Report) -> None:
    if not MISSING_PATH.is_file():
        rep.line(False, "8 missing_pages.json", "file absent")
        return
    data = json.loads(MISSING_PATH.read_text(encoding="utf-8"))
    pages = data.get("pages", [])
    meta = data.get("_meta", {})
    fields_ok = all(isinstance(r, dict) and all(isinstance(r.get(k), str) and r.get(k)
                  for k in ("t", "p", "u", "b")) for r in pages)
    in_pack = sum(1 for r in pages if r.get("p") and (DOCS_ROOT / PurePosixPath(r["p"]).as_posix()).is_file())
    ok = fields_ok and meta.get("entries") == len(pages) and in_pack == 0
    rep.line(ok, "8 missing_pages.json",
             "entries=%d meta.entries=%s fields_ok=%s already_on_disk=%d bytes=%d"
             % (len(pages), meta.get("entries"), fields_ok, in_pack, os.path.getsize(MISSING_PATH)))


def check_batches(rep: Report, documents: dict, baseline_file: Path | None) -> None:
    batches: list[str] = []
    lines = 0
    if CHANGELOG_PATH.is_file():
        for raw in CHANGELOG_PATH.read_text(encoding="utf-8").splitlines():
            if raw.startswith("|"):
                lines += 1
                cells = [c.strip() for c in raw.strip("|").split("|")]
                if len(cells) > 1 and cells[1] not in batches:
                    batches.append(cells[1])
    touched, compared = 0, 0
    if baseline_file is not None:
        snapshot = swd.read_json(baseline_file).get("docs", {})
        for local_path, digest in sorted(snapshot.items()):
            path = PACK_ROOT / Path(local_path)
            if not path.is_file():
                touched += 1
                continue
            compared += 1
            if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
                touched += 1
        detail = "baseline=%s docs_compared=%d changed_vs_baseline=%d" % (
            baseline_file.name, compared, touched)
    else:
        for local_path, entry in sorted(documents.items()):
            path = DOCS_ROOT / PurePosixPath(local_path).as_posix()
            if path.is_file() and swd.sha256(swd.normalize_markdown(
                    path.read_text(encoding="utf-8")).encode("utf-8")) != entry.get("content_hash"):
                touched += 1
        detail = "no --baseline, compared against manifest.content_hash docs=%d mismatch=%d" % (
            len(documents), touched)
    rep.line(touched == 0, "9 batches + baseline untouched",
             "changelog_rows=%d batches=%s %s" % (lines, batches or ["(none)"], detail))


def check_extension_footprint(rep: Report) -> None:
    """Gate for backups creeping back into the pack (they belong outside, see add_pages.py)."""
    limit = 256 * 1024
    files = [p for p in EXTENSION_ROOT.rglob("*") if p.is_file()] if EXTENSION_ROOT.is_dir() else []
    total = sum(os.path.getsize(p) for p in files)
    names = sorted(p.relative_to(EXTENSION_ROOT).as_posix() for p in files)
    rep.line(total <= limit, "10 in-pack .extension footprint",
             "files=%d bytes=%d limit=%d exceeded=%s names=%s"
             % (len(files), total, limit, total > limit, names[:6]))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", type=Path,
                        help="optional snapshot json with a docs map of path -> sha256 hex")
    args = parser.parse_args()

    rep = Report()
    manifest = swd.read_json(MANIFEST_PATH)
    documents = manifest.get("documents", {})
    assets = manifest.get("assets", {})
    coverage = manifest.get("coverage", {})
    if not isinstance(documents, dict) or not isinstance(assets, dict):
        print("FAIL manifest documents/assets must be objects")
        print("EVIDENCE_NOT_OK")
        return 1

    links = relative_targets(DOCS_ROOT, documents)
    check_manifest_vs_disk(rep, documents)
    check_hashes(rep, documents)
    check_coverage(rep, coverage, documents)
    check_assets(rep, assets)
    check_links(rep, links)
    check_encoding(rep, documents)
    check_gitattributes(rep)
    check_missing_list(rep)
    check_batches(rep, documents, args.baseline)
    check_extension_footprint(rep)

    print("summary docs=%d assets=%d failures=%d"
          % (len(documents), len(assets), len(rep.failures)))
    if rep.failures:
        print("failed checks: " + ", ".join(rep.failures))
        print("EVIDENCE_NOT_OK")
        return 1
    print("EVIDENCE_ALL_OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
