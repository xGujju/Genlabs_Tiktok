"""Smoke tests for cooldown DB + Thai helpers.

Run with: python -m pytest tests/ -q
"""
from __future__ import annotations

import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from genlabs_engine._thai import (  # noqa: E402
    char_bigrams,
    detect_all_tools,
    detect_primary_tool,
    jaccard,
    normalize_text,
    text_similarity,
)
from genlabs_engine.cooldown import CooldownDB, PublishedPost  # noqa: E402


def test_normalize_text():
    assert normalize_text("  ChatGPT 5.5 ใช้!! ") == "chatgpt ใช้"
    assert normalize_text("") == ""


def test_char_bigrams_thai():
    # "เจ๊หน่อย" = 8 Unicode code points (Thai combining tone marks are
    # separate code points: เ จ ๊ ห น ่ อ ย) → 7 bigrams.
    bg = char_bigrams("เจ๊หน่อย")
    assert len(bg) == 7


def test_jaccard_basic():
    assert jaccard({"a", "b"}, {"a", "b"}) == 1.0
    assert jaccard({"a"}, {"b"}) == 0.0


def test_text_similarity_identical():
    s = "ใช้ ChatGPT ตอบลูกค้าใน LINE OA"
    assert text_similarity(s, s) == 1.0


def test_text_similarity_clearly_different():
    sim = text_similarity(
        "ใช้ ChatGPT ตอบลูกค้าใน LINE OA",
        "ตีราคางานรับเหมาให้ลูกค้า",
    )
    assert sim < 0.3


def test_detect_primary_tool():
    assert detect_primary_tool("ใช้ ChatGPT ตอบลูกค้า") == "chatgpt"
    assert detect_primary_tool("Claude Code ทำเว็บ") == "claude_code"
    assert detect_primary_tool("เนื้อหาทั่วไปไม่มีเครื่องมือ") is None


def test_detect_all_tools_ordered():
    tools = detect_all_tools("เริ่มที่ ChatGPT แล้วใช้ Claude ต่อ แล้วเปิด NotebookLM")
    assert tools[0] == "chatgpt"
    assert set(tools) == {"chatgpt", "claude", "notebooklm"}


def test_cooldown_db_ingest_and_check(tmp_path):
    db = CooldownDB.open(tmp_path / "test.sqlite")
    try:
        post = PublishedPost(
            source_key="test-001",
            source_type="manual",
            topic_raw="ใช้ ChatGPT ตอบลูกค้าใน LINE OA",
            hook_thai="ใช้ ChatGPT ตอบลูกค้าใน LINE OA",
            full_text="ใช้ ChatGPT ตอบลูกค้าใน LINE OA. ขั้นตอน 1 2 3",
            format="carousel_sketchnote",
            published_at=datetime.now(timezone.utc) - timedelta(days=2),
            primary_tool="chatgpt",
            avatar_id="jay-noi-salon-clinic",
        )
        post_id = db.ingest_published(post)
        assert post_id is not None
        # Re-ingest same source_key → skip
        assert db.ingest_published(post) is None

        # Near-duplicate → should be flagged non-novel (hook trigger)
        result = db.check_novelty(
            topic="ใช้ ChatGPT ตอบลูกค้าใน LINE OA",
            hook="ใช้ ChatGPT ตอบลูกค้าใน LINE OA",
            primary_tool="chatgpt",
            avatar_id="jay-noi-salon-clinic",
            lookback_days=30,
        )
        assert not result.is_novel
        assert result.hook_jaccard >= 0.35

        # Different topic → novel
        result2 = db.check_novelty(
            topic="ตีราคางานรับเหมาให้ลูกค้าโดยไม่ขาดทุน",
            primary_tool="chatgpt",
            avatar_id="pi-nok-contractor",
        )
        assert result2.is_novel

        # Stats
        assert db.total_posts() == 1
        assert "chatgpt" in db.posts_by_primary_tool()
    finally:
        db.close()


def test_cooldown_db_variety_stats(tmp_path):
    db = CooldownDB.open(tmp_path / "test.sqlite")
    try:
        for i in range(3):
            db.ingest_published(
                PublishedPost(
                    source_key=f"v-{i}",
                    source_type="manual",
                    topic_raw=f"topic {i}",
                    hook_thai=f"hook {i}",
                    full_text=f"full {i}",
                    format="carousel_sketchnote",
                    published_at=datetime.now(timezone.utc),
                    primary_tool="chatgpt",
                    avatar_id="jay-noi-salon-clinic",
                )
            )
        counts = db.daily_counts()
        assert counts["avatar"]["jay-noi-salon-clinic"] == 3
        assert counts["primary_tool"]["chatgpt"] == 3
    finally:
        db.close()
