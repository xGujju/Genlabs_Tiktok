#!/usr/bin/env python3
"""Read x_search results from stdin (JSON array of posts), normalize, append.

Used by the genlabs-x-discover skill — Hermes runs x_search for each
query in the plan, then pipes the result list into this script along
with --avatar-id and --theme.

Usage (skill side):
    hermes x_search ... | python x_discover_ingest.py --avatar-id <id> --theme <theme>
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from genlabs_engine.discovery.ingest import normalize_x_batch  # noqa: E402
from genlabs_engine.signals import X_SIGNALS_PATH, SignalsWriter  # noqa: E402


def main() -> int:
    p = argparse.ArgumentParser(description="Ingest x_search results into x_signals.jsonl")
    p.add_argument("--avatar-id", required=True)
    p.add_argument("--theme", required=True)
    p.add_argument("--input-file", type=Path, default=None,
                   help="Read JSON from file instead of stdin")
    p.add_argument("--output", type=Path, default=X_SIGNALS_PATH)
    args = p.parse_args()

    if args.input_file:
        raw_text = args.input_file.read_text(encoding="utf-8")
    else:
        raw_text = sys.stdin.read()

    try:
        data = json.loads(raw_text)
    except json.JSONDecodeError as e:
        print(f"ERROR: input is not valid JSON: {e}", file=sys.stderr)
        return 2

    if isinstance(data, dict):
        # Common shapes: {"data": [...]}, {"results": [...]}, {"posts": [...]}
        for key in ("data", "results", "posts", "tweets"):
            if isinstance(data.get(key), list):
                data = data[key]
                break
        else:
            data = [data]

    if not isinstance(data, list):
        print("ERROR: expected a list of posts", file=sys.stderr)
        return 2

    signals = normalize_x_batch(data, avatar_id=args.avatar_id, search_theme=args.theme)
    writer = SignalsWriter(args.output)
    written, skipped = writer.append_many(signals)

    summary = {
        "avatar_id": args.avatar_id,
        "theme": args.theme,
        "input_posts": len(data),
        "normalized": len(signals),
        "written": written,
        "skipped_dup": skipped,
        "output": str(args.output),
    }
    print(json.dumps(summary, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
