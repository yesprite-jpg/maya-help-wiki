#!/usr/bin/env python3
"""Regenerate references/missing_pages.json from the build-side roster.

Input is the capture-side name roster (roster.json), which is NOT shipped inside the
pack: run this only where that file exists, otherwise keep the committed
missing_pages.json as-is.

Stdlib only. Deterministic: roster order preserved, compact JSON separators.
"""
from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path

FIELDS = (("t", "title"), ("p", "local_path"), ("u", "source_url"), ("b", "book_id"))


def build(roster_path: Path, zone_key: str, kept_zone: str) -> tuple[list[dict], dict]:
    data = json.loads(roster_path.read_text(encoding="utf-8"))
    rows = data.get("pages")
    if not isinstance(rows, list):
        raise SystemExit("FAILED: roster.pages must be an array")
    entries = []
    for index, raw in enumerate(rows):
        if not isinstance(raw, dict):
            raise SystemExit(f"FAILED: roster.pages[{index}] must be an object")
        if raw.get(zone_key) == kept_zone:
            continue
        missing = [src for _, src in FIELDS if not isinstance(raw.get(src), str) or not raw.get(src).strip()]
        if missing:
            raise SystemExit(f"FAILED: roster.pages[{index}] lacks {missing}")
        entries.append({short: raw[src] for short, src in FIELDS})

    meta = {
        "source_roster": roster_path.name,
        "roster_pages_total": len(rows),
        "zone_field": zone_key,
        "criteria": f"{zone_key} != {kept_zone}",
        "entries": len(entries),
        "generated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "fields": {short: src for short, src in FIELDS},
        "note": (
            "Pages listed in the Autodesk Maya help roster that this pack has not captured yet. "
            "p is the local_path such a page would take under references/docs once added. "
            "Counts are of this file's own entries; verify with scripts/selfcheck.py."
        ),
    }
    return entries, meta


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--roster", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--zone-field", default="zone")
    parser.add_argument("--kept-zone", default="核心层")
    args = parser.parse_args()

    entries, meta = build(args.roster, args.zone_field, args.kept_zone)
    payload = {"_meta": meta, "pages": entries}
    text = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    if any(ord(ch) < 32 for ch in text):
        raise SystemExit("FAILED: control character in generated JSON")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(text + "\n", encoding="utf-8", newline="\n")

    reread = json.loads(args.out.read_text(encoding="utf-8"))
    pages_view = json.dumps(reread["pages"], ensure_ascii=False, separators=(",", ":"))
    print(
        "OK entries=%d roster_total=%d file_bytes=%d pages_view_bytes=%d file=%s"
        % (
            len(reread["pages"]),
            reread["_meta"]["roster_pages_total"],
            os.path.getsize(args.out),
            len(pages_view.encode("utf-8")),
            args.out.as_posix(),
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
