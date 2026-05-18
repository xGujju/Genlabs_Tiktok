#!/usr/bin/env python3
"""Backfill the cooldown DB from existing /assets/carousels/<folder>/manifest.json."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE.parent))

from genlabs_engine.cooldown import CooldownDB  # noqa: E402
from genlabs_engine.manifest import parse_manifest  # noqa: E402


def main() -> int:
    p = argparse.ArgumentParser(description="Backfill cooldown DB from carousel manifests")
    p.add_argument(
        "--carousels-dir",
        type=Path,
        default=Path("/home/clawd/Genlabs_Tiktok/assets/carousels"),
    )
    p.add_argument("--db", type=Path, default=None, help="DB path (default: $GENLABS_COOLDOWN_DB)")
    p.add_argument("--limit", type=int, default=0, help="Process at most N folders (0=all)")
    p.add_argument("--dry-run", action="store_true", help="Parse only; do not write")
    p.add_argument("--verbose", "-v", action="store_true")
    args = p.parse_args()

    if not args.carousels_dir.exists():
        print(f"ERROR: carousels dir not found: {args.carousels_dir}", file=sys.stderr)
        return 2

    db: CooldownDB | None = None if args.dry_run else CooldownDB.open(args.db)
    folders = sorted(p for p in args.carousels_dir.iterdir() if p.is_dir())
    if args.limit:
        folders = folders[: args.limit]

    n_total = n_inserted = n_skipped = n_no_manifest = n_parse_err = 0
    for folder in folders:
        n_total += 1
        manifest = folder / "manifest.json"
        if not manifest.exists():
            n_no_manifest += 1
            if args.verbose:
                print(f"  NO_MANIFEST {folder.name}", file=sys.stderr)
            continue
        parsed = parse_manifest(manifest)
        if parsed is None:
            n_parse_err += 1
            print(f"  PARSE_ERR  {folder.name}", file=sys.stderr)
            continue
        if args.dry_run:
            n_inserted += 1
            if args.verbose:
                print(
                    f"  WOULD_INSERT [{parsed.source_type:14s}] tool={parsed.primary_tool or '-':12s}"
                    f" hook={parsed.hook_thai[:60]}"
                )
            continue
        post_id = db.ingest_parsed_carousel(parsed)  # type: ignore[union-attr]
        if post_id is None:
            n_skipped += 1
        else:
            n_inserted += 1

    print(
        f"\nBackfill complete:"
        f"\n  total folders:    {n_total}"
        f"\n  inserted:         {n_inserted}"
        f"\n  skipped (dup):    {n_skipped}"
        f"\n  no manifest:      {n_no_manifest}"
        f"\n  parse errors:     {n_parse_err}",
        file=sys.stderr,
    )
    if db is not None:
        print(f"\nDB total rows: {db.total_posts()}", file=sys.stderr)
        db.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
