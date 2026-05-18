"""Parser for legacy ai_signal_radar carousel manifests.

Extracts the fields the cooldown DB needs from the existing
assets/carousels/<folder>/manifest.json artefacts.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from ._thai import detect_all_tools, detect_primary_tool

_TS_RE = re.compile(r"(\d{8}T\d{6}Z)")


def classify_source_type(folder: str) -> tuple[str, str | None]:
    """Infer (source_type, source_id) from a carousel folder name.

    Folder name patterns observed in /assets/carousels:
      auto-<ts>-yt-<videoid>               → youtube
      auto-<ts>-evergreen-<slug>            → evergreen
      auto-<ts>-kpi<n>-<slug>               → kpi
      auto-<ts>-ai-word-<term>-<style>      → vocab_explainer
      auto-<ts>-sig-<n>                     → apify
      sig-<n>-...                           → apify
      kpi20-<date>-...                      → kpi_batch
      manual-<ts>-...                       → manual
      money-<ts>-... / money-extra-<ts>-... → money_pack
      oneoff-<...> / oneoff-v<n>-<...>      → oneoff
      replacement-no-source-meta-<...>      → replacement
      first-public-cdn-live[-v<n>]          → infra_test
      genlabs-cta-<slug>                    → cta_asset
      youtube-pilot-jeffsu*                 → pilot
      hydration-sig-<n>                     → hydration_test
    """
    name = folder.lower()
    if "-yt-" in name:
        vid = name.split("-yt-", 1)[1]
        return ("youtube", vid)
    if "-evergreen-" in name or name.startswith("evergreen-"):
        slug = name.split("-evergreen-", 1)[-1] if "-evergreen-" in name else name
        return ("evergreen", slug)
    if "-ai-word-" in name:
        return ("vocab_explainer", name.split("-ai-word-", 1)[1])
    if "-kpi" in name or name.startswith("kpi"):
        return ("kpi", name)
    if name.startswith("money-extra-"):
        return ("money_pack", name)
    if name.startswith("money-"):
        return ("money_pack", name)
    if name.startswith("manual-"):
        return ("manual", name)
    if name.startswith("oneoff"):
        return ("oneoff", name)
    if name.startswith("sig-"):
        return ("apify", name)
    if name.startswith("replacement-"):
        return ("replacement", name)
    if name.startswith("first-public-cdn"):
        return ("infra_test", name)
    if name.startswith("genlabs-cta-"):
        return ("cta_asset", name)
    if name.startswith("youtube-pilot"):
        return ("pilot", name)
    if name.startswith("hydration-"):
        return ("hydration_test", name)
    if name.startswith("auto-"):
        return ("apify", name)
    return ("other", name)


def extract_ts(folder: str) -> datetime | None:
    m = _TS_RE.search(folder)
    if not m:
        return None
    try:
        return datetime.strptime(m.group(1), "%Y%m%dT%H%M%SZ").replace(tzinfo=timezone.utc)
    except ValueError:
        return None


@dataclass
class ParsedCarousel:
    folder_name: str
    manifest_path: str
    source_type: str
    source_id: str | None
    source_url: str | None
    topic_raw: str
    hook_thai: str
    primary_tool: str | None
    secondary_tools: list[str]
    slide_count: int
    published_at: datetime
    full_text: str
    clean_headline: str | None
    format: str = "carousel_sketchnote"
    hook_frame: str = "tutorial_numbered"
    avatar_id: str | None = None


def _first_hook_thai(slides: list[dict[str, Any]]) -> str:
    for s in slides:
        if (s.get("role") or "").lower() == "hook":
            return str(s.get("thai_copy") or "").strip()
    if slides:
        return str(slides[0].get("thai_copy") or "").strip()
    return ""


def parse_manifest(manifest_path: Path) -> ParsedCarousel | None:
    """Parse a manifest.json into a ParsedCarousel, or None if unreadable."""
    folder = manifest_path.parent.name
    try:
        data: dict[str, Any] = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None

    plan = data.get("carousel_plan") or {}
    slides = list(plan.get("slides") or [])
    clean_brief = data.get("clean_brief") or {}

    source_type, source_id_inferred = classify_source_type(folder)
    source_id = clean_brief.get("source_id") or source_id_inferred or folder
    source_url = clean_brief.get("source_url") or plan.get("source_url")

    hook_thai = _first_hook_thai(slides)
    topic_raw = clean_brief.get("clean_headline") or hook_thai
    full_text_parts: list[str] = [hook_thai] if hook_thai else []
    for s in slides:
        tc = str(s.get("thai_copy") or "").strip()
        if tc and tc != hook_thai:
            full_text_parts.append(tc)
    full_text = "\n".join(full_text_parts)

    detect_corpus = "\n".join(
        x for x in [topic_raw, full_text, clean_brief.get("raw_text", "")] if x
    )
    primary_tool = detect_primary_tool(detect_corpus)
    secondary_tools = [t for t in detect_all_tools(detect_corpus) if t != primary_tool]

    published_at = extract_ts(folder) or datetime.now(timezone.utc)

    return ParsedCarousel(
        folder_name=folder,
        manifest_path=str(manifest_path),
        source_type=source_type,
        source_id=source_id,
        source_url=source_url,
        topic_raw=topic_raw,
        hook_thai=hook_thai,
        primary_tool=primary_tool,
        secondary_tools=secondary_tools,
        slide_count=int(plan.get("slide_count") or len(slides) or 0),
        published_at=published_at,
        full_text=full_text,
        clean_headline=clean_brief.get("clean_headline"),
    )
