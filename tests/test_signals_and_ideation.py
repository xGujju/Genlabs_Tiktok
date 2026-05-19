"""End-to-end smoke tests for signals + discovery + ideation."""
from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from genlabs_engine.avatars import AvatarRegistry
from genlabs_engine.cooldown import CooldownDB
from genlabs_engine.discovery.ingest import normalize_x_batch
from genlabs_engine.discovery.plan import build_x_queries
from genlabs_engine.ideation.mint import mint_candidates
from genlabs_engine.ideation.score import (
    score_action_density,
    score_avatar_fit,
    score_local_fit,
    score_pain_acuity,
)
from genlabs_engine.signals import RawSignal, SignalsWriter


def test_avatar_registry_loads_five():
    reg = AvatarRegistry.load()
    assert len(reg) == 5
    assert "jay-noi-salon-clinic" in reg
    assert "pi-tu-fnb" in reg


def test_x_search_plan_built():
    reg = AvatarRegistry.load()
    plan = build_x_queries(reg)
    # 5 avatars × ~6 themes each
    assert len(plan) >= 20
    assert all(q.query and q.avatar_id for q in plan)


def test_normalize_x_batch():
    raw = [
        {
            "id": "1234",
            "text": "ChatGPT prompts for restaurant owners. 7 ways to write better menus.",
            "url": "https://x.com/foo/status/1234",
            "author": {"username": "foo", "name": "Foo", "followers": 1200},
            "public_metrics": {"like_count": 500, "retweet_count": 60, "reply_count": 12},
            "created_at": "2026-05-18T03:00:00+00:00",
            "lang": "en",
        }
    ]
    sigs = normalize_x_batch(raw, avatar_id="pi-tu-fnb", search_theme="menu pricing AI")
    assert len(sigs) == 1
    assert sigs[0].post_id == "1234"
    assert sigs[0].like_count == 500
    assert sigs[0].avatar_id == "pi-tu-fnb"


def test_signals_writer_dedup(tmp_path):
    p = tmp_path / "x_signals.jsonl"
    w = SignalsWriter(p)
    s = RawSignal(
        well="x", discovered_at="2026-05-18T00:00:00+00:00",
        post_id="abc", post_url="https://x.com/foo/status/abc",
        text="hello", avatar_id="pi-tu-fnb",
    )
    assert w.append(s) is True
    assert w.append(s) is False  # dedup
    # Reopen and verify it sees prior rows
    w2 = SignalsWriter(p)
    assert w2.append(s) is False


def test_score_pain_acuity_picks_up_urgency():
    sig = RawSignal(
        well="x", discovered_at="", post_id="x1", post_url="",
        text="I'm drowning in receipts. I waste hours every week. Help.",
    )
    assert score_pain_acuity(sig) > 0.5


def test_score_action_density_picks_up_numbered_tips():
    sig = RawSignal(
        well="x", discovered_at="", post_id="x2", post_url="",
        text="7 ways to use ChatGPT. Step 1: do X. Step 2: do Y. Step 3: do Z. github.com/foo/bar",
    )
    assert score_action_density(sig) > 0.5


def test_score_avatar_fit_matches_relevant_signal():
    reg = AvatarRegistry.load()
    salon = reg["jay-noi-salon-clinic"]
    sig = RawSignal(
        well="x", discovered_at="", post_id="x3", post_url="",
        text="ChatGPT for salon owners — appointment no-show reminder automation via LINE OA",
    )
    fit = score_avatar_fit(sig, salon)
    assert fit > 0.3


def test_mint_end_to_end(tmp_path):
    """Smoke: realistic signals → mint → ranked candidates.

    Signal mentions GrabFood (pi-tu-fnb tool), wasted hours (pain), step 1/2
    (action), so avatar_fit + pain_acuity + action_density should all light up.
    """
    reg = AvatarRegistry.load()
    db = CooldownDB.open(tmp_path / "cd.sqlite")
    try:
        sigs = [
            RawSignal(
                well="x", discovered_at="", post_id=f"sig-{i}", post_url="",
                text=(
                    "7 ways to recover GrabFood reviews with AI. "
                    "Step 1: tag negative reviews. Step 2: draft replies. "
                    "Wasted hours doing this manually before. github.com/foo/bar"
                ),
                created_at=datetime.now(timezone.utc).isoformat(),
                avatar_id="pi-tu-fnb", search_theme="restaurant AI review response",
                language="en",
            )
            for i in range(3)
        ]
        cands = mint_candidates(reg, sigs, db, top_per_avatar=5, min_score=0.3)
        f_and_b = [c for c in cands if c.avatar_id == "pi-tu-fnb"]
        assert len(f_and_b) >= 1
        assert f_and_b[0].final_score > 0.3
    finally:
        db.close()
