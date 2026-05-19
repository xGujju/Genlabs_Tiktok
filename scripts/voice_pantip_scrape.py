#!/usr/bin/env python3
"""Harvest recent Pantip topics into voice_signals.jsonl."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from genlabs_engine.signals import VOICE_SIGNALS_PATH, SignalsWriter  # noqa: E402
from genlabs_engine.voice.pantip import PANTIP_FORUMS_OF_INTEREST, harvest  # noqa: E402

# Forum → primary avatar mapping. Tunable.
FORUM_TO_AVATAR = {
    "business":     "khun-ae-accountant",
    "sinthorn":     "jay-noi-salon-clinic",
    "food":         "pi-tu-fnb",
    "home":         "pi-nok-contractor",
    "condo":        "khun-nat-real-estate",
    "supachalasai": "",  # tech forum — used for global context, not per-avatar
}


def main() -> int:
    p = argparse.ArgumentParser(description="Pantip → voice_signals.jsonl")
    p.add_argument("--forum", action="append",
                   help="Forum slug; repeatable. Default = all known SME forums.")
    p.add_argument("--per-forum", type=int, default=25)
    p.add_argument("--delay-sec", type=float, default=1.0)
    p.add_argument("--output", type=Path, default=VOICE_SIGNALS_PATH)
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    forums = args.forum or list(PANTIP_FORUMS_OF_INTEREST)
    signals = harvest(
        forums,
        per_forum=args.per_forum,
        delay_sec=args.delay_sec,
        forum_to_avatar=FORUM_TO_AVATAR,
    )

    summary: dict = {
        "forums_scraped": forums,
        "signals_normalized": len(signals),
        "per_forum_counts": {
            f: sum(1 for s in signals if s.raw_payload.get("forum") == f) for f in forums
        },
    }

    if args.dry_run:
        summary["written"] = 0
        summary["dry_run"] = True
    else:
        writer = SignalsWriter(args.output)
        written, skipped = writer.append_many(signals)
        summary["written"] = written
        summary["skipped_dup"] = skipped
        summary["output"] = str(args.output)

    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
