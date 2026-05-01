# GenLabs AI Learning — Carousel Production Process

## Purpose
Turn cleaned AI Signal Radar winners into Thai visual-first carousel image sets for GenLabs AI Learning.

## Boundary
- This is a manual/operator-triggered production stage.
- The scheduled AI Signal Radar must not generate carousels.
- Feedback/analytics learning stays deferred until carousel sets are generated, published, and measurable.

## Input
Use one cleaned winning signal from Airtable or Discord winner posts.

Best source types:
- practical AI tips
- Claude Code / Cursor / coding workflows
- prompt templates
- AI automation workflows
- visual before/after examples
- AI tool stacks that Thai users can try quickly

Raw-signal JSON should include:
- `source_url`
- `author_username` / author
- `text`
- `created_at`
- engagement metrics when available: likes, reposts, replies, quotes, bookmarks

## Process
1. Choose one high-signal winner.
2. Prepare raw-signal JSON.
3. Run dry-run planning first:
   ```bash
   python scripts/generate_ai_signal_carousel.py \
     --input-json /path/to/raw-signal.json \
     --output-dir ~/.hermes/ai_signal_radar/carousels/manual-test \
     --slide-count 5
   ```
4. Inspect `manifest.json`.
5. Confirm the plan has **5–10 slides, never fewer than 5**:
   - hook
   - problem
   - trend/insight
   - tips/actions
   - optional value slides when needed: example, deeper tips, framework, common mistakes, glossary, evidence/proof
   - CTA
   Use 6, 8, or up to 10 images only when extra explanation makes the lesson easier and more valuable for clients. Do **not** pad weak content just to use more slides.
6. Confirm GenLabs visual style:
   - colorful Thai hand-drawn sketchnote
   - white background
   - thick marker-like lines
   - rounded boxes/cards
   - cute robots/icons
   - arrows/checkmarks/section badges
   - simple mini-diagrams
   - low text density
7. Run live FAL generation only after the plan passes:
   ```bash
   python scripts/generate_ai_signal_carousel.py \
     --input-json /path/to/raw-signal.json \
     --output-dir ~/.hermes/ai_signal_radar/carousels/manual-test \
     --slide-count 5 \
     --reference-image-url https://example.com/genlabs-template.png \
     --quality medium \
     --apply
   ```
8. Review every slide manually.
9. Save the manifest path, source URL, reference image URL, and generated assets for future Airtable asset tracking.
10. Publish manually for the first 3–5 carousel sets.

## Visual Rule
Use the reference sketchnote/poster style, but do **not** copy its text density.

Target balance:
- 80% visual explanation
- 20% text

Each slide should have:
- one core visual idea
- one short Thai headline
- at most 1–3 short labels
- no dense paragraphs

If extra explanation is needed, add extra carousel slides up to 10 before relying only on the caption/script. Keep each image simple: one idea per slide, short Thai copy, and strong visuals.

## Visual QA Checklist
A carousel set is publishable only if:
- Thai text is natural, short, spelled correctly, and mobile-readable.
- A viewer understands the hook slide in under 2 seconds.
- Icons/graphics explain the idea even when skimmed.
- Slide sequence tells a mini-story, not disconnected facts.
- The CTA is simple: save, follow, try the workflow, or comment a keyword.
- The design looks like GenLabs AI Learning, not a generic AI news poster.
- It matches the GenLabs handwritten Thai sketchnote style: marker-like Thai lettering or very minimal image text, thick imperfect marker lines, rounded hand-drawn cards/callouts, arrows/checkmarks/highlights, cute AI helper icons, light paper/whiteboard feel, and small subtle GenLabs logo.
- It is not a polished SaaS/HTML screenshot, dark tech poster, generic vector mascot slide, non-GPT Image 2 render, or plain typed white image.
- It has no garbled/pseudo Thai. If the image model cannot render Thai clearly, move detail into the caption and keep image text minimal.
- It does not invent facts beyond the source signal.
- It does not show fake dashboards, fake analytics, or feedback-loop claims.
- Vision QA must pass before the draft is called ready; failed assets should be marked `needs_redesign`, not treated as publishable.

## Current Implementation
Repo: `/home/clawd/.hermes/hermes-agent`

Entry points:
- `tools/ai_signal_radar/carousel.py`
- `scripts/generate_ai_signal_carousel.py`

FAL endpoint:
- `openai/gpt-image-2/edit`
- requires `FAL_KEY`
- live generation requires a reference/template image URL

## 2026-04-28 — Carousel length rule updated
- Sway changed the carousel length rule: every GenLabs carousel must have **minimum 5 images**, but can expand to **6, 8, or up to 10 images** when the post needs more explanation or information.
- The purpose is client learning/value: make complex AI workflows, prompts, resources, or examples easier to understand instead of forcing everything into 5 images.
- Do not pad weak/simple posts just to use more slides. Extra slides should carry one clear useful idea each: example, deeper tip, framework, common mistake, glossary, evidence/proof, or CTA.
- Current code update: `tools/ai_signal_radar/carousel.py` supports 5–10 slide plans and `scripts/scheduled_ai_social_draft_factory.py` chooses an adaptive count for future drafts.

## 2026-04-28 — Reusable final GenLabs CTA slide locked
- Use the same final CTA slide for all future GenLabs carousel posts; do not regenerate it unless Sway explicitly asks.
- Local reusable asset: `/home/clawd/.hermes/ai_signal_radar/carousels/genlabs-cta-10baht-sme/slide-1.png`
- Public asset URL: `https://v3b.fal.media/files/b/0a980b4a/B8_OT-mhnVyBXQUoZL-Ir_dDsmugPy.png`
- CTA message: GenLabs.in.th helps SMEs/businesses generate brand graphics and AI visuals for their brand without needing prompts, starting at 10 baht.
- Workflow rule: append this CTA as the last slide in Zernio carousel drafts and future manifests, preserving draft-only/no-live-publish safety.

## 2026-04-28 — Draft selector quality gate after sig-77 timeout
- Root cause from failed hourly factory run: the selector allowed a weak C-bucket Canonical Signal (`sig-77`) because the text contained AI/image-prompt keywords, even though the Thai angle said `Watch for more corroboration before converting` and the weighted score was low.
- Autonomous draft factory must only spend FAL/Zernio work on A/B Canonical Signals.
- Never auto-draft C-bucket sources or sources whose Thai angle says to wait/watch for corroboration. Those belong in scout/backlog until stronger evidence or a manual Sway decision exists.
- If a run times out with partial `auto-*` assets but no `manifest.json`, treat the folder as incomplete/unusable for Zernio. Do not publish from stale `latest_social_draft_factory.json`; check newest carousel folder, Airtable `Carousel Posts`, and source quality before retrying.

## 2026-04-28 — YouTube source lane pilot
- New source lane: YouTube videos can supply deeper how-to/tips/learning concepts when X/Twitter backlog quality is thin.
- Implementation plan saved in repo: `/home/clawd/.hermes/hermes-agent/docs/superpowers/plans/2026-04-28-youtube-genlabs-carousel-source-lane.md`.
- Manual entrypoint: `/home/clawd/.hermes/hermes-agent/scripts/create_youtube_genlabs_draft.py`.
- Source module: `/home/clawd/.hermes/hermes-agent/tools/ai_signal_radar/youtube_source.py`.
- Output path stays the same: GenLabs Thai handwritten/sketchnote carousel, 5–10 slides, reusable GenLabs CTA as final media, Airtable-first when publishing, Zernio Creator Inbox draft-only, no `publishNow`, no `scheduledFor`.
- Copywriting gate: use skill `genlabs-carousel-copywriting` before image generation. If the hook promises 8 tips/steps/prompts, slide copy must visibly deliver 8 distinct items; do not count the reusable GenLabs CTA as content, do not show `YouTube title` in public slide copy, and reject repeated fallback wording.
- Current environment note: `youtube-transcript-api` may be blocked by YouTube/cloud IP restrictions. The workflow falls back to `r.jina.ai` YouTube page metadata/chapters and labels it as `jina_youtube_page_metadata_fallback`; do not claim full transcript grounding unless transcript fetch succeeds.

## Linked Notes
- [[Aion OS/Projects/genlabs-ai-learning-state]]
- [[Aion OS/Projects/genlabs-thai-ai-media-engine]]
- [[Aion OS/SOPs/genlabs-thai-ai-media-loop]]

## 2026-04-27 — Zernio TikTok carousel draft rules locked
- For TikTok photo carousel drafts, the top-level `content` is the short title/hook and should aim for 65–90 Thai characters, include one relevant Thai hashtag, and explain the post at a glance.
- The long TikTok photo description must be sent as `tiktokSettings.description` per Zernio TikTok docs. It can use up to 4,000 characters.
- Long descriptions should be Thai-first, beginner/mid-user friendly, educational, save-worthy, and skimmable. For how-to guides, prompt explanations, workflows, or resource posts, use the space: target roughly 2,500–3,500 Thai characters within the 4,000-character Zernio/TikTok photo description limit. Include who it is for, why it matters, step-by-step actions, examples/prompt frameworks, common mistakes, one task to try today, and useful resource links when central.
- Use friendly section emojis such as 👋 💡 📌 ✅ ✨ 🧪 🧭 🌱 🔖 🚀 to make the description warmer and easier to scan.
- Do not include Twitter/X handles or source URLs in the public caption/description. Preserve source attribution internally in Airtable and manifests.
- Use Thai-first discovery hashtags, e.g. `#GenLabsTH`, `#เรียนAI`, `#AIมือใหม่`, `#aiสร้างภาพ`, `#aiทำรูป`, `#ขายของออนไลน์`, `#ถ่ายรูปสินค้า`, and related Thai tags.
- Current GPT-5.5 review draft was updated with emoji-rich `tiktokSettings.description` and remains draft-only.

## 2026-04-27 — Hashtag cap + Zernio draft setting
- Final public caption/description must include **no more than 5 hashtags**.
- Use Thai-first tags, but choose the five most relevant tags rather than dumping the whole watchlist.
- For Zernio, the automation should create TikTok Creator Inbox drafts by sending `isDraft=true` and `tiktokSettings.draft=true`.
- Treat this as Sway's “Schedule Now / save as draft” path: drafts are ready for review inside Zernio, but the automation must still omit `publishNow` and `scheduledFor`.

## 2026-04-27 — One-off post and approved-account production lanes
- One-off lane: when Sway sends a good post URL, scrape/hydrate it immediately with Apify or other available scraping tools, then create one GenLabs Thai carousel draft from the idea.
- Approved-account lane: when Sway provides accounts, add them to the monitored source list and run a daily scrape to find the best recent posts for original GenLabs drafts.
- Do not copy source posts verbatim. Convert the idea into a Thai, beginner-friendly, save-worthy lesson with GenLabs examples, steps, and hook.
- Keep source URL/account attribution inside Airtable/manifest only. Public TikTok caption stays clean.
- Final Zernio draft must follow the locked rules: max 5 hashtags, long caption in `tiktokSettings.description`, Creator Inbox draft flags, no live publish and no scheduled future publish.

## 2026-04-27 — Airtable source tracking rule
- Do not treat Sway-sent URLs or approved accounts as chat-only context. Record them in Airtable.
- One-off source posts: track source URL, source ID, author/account, scrape metadata, duplicate status, carousel record, manifest path, and Zernio draft ID/status.
- Approved accounts: track in `Source Watchlist` with handle/profile URL, status/priority, scan cadence, last scanned, and notes before the daily scanner uses them.
- Airtable is the audit trail for what we used, skipped, remixed, drafted, and later measured.

## 2026-04-27 — One-off source media usage
- Trigger phrase: `One off post:` + URL means create a one-off GenLabs draft now.
- Always record the source in Airtable first.
- If the scraped source has image/media URLs, analyze them and use useful safe images as FAL references alongside GenLabs logo references.
- Use source media for broad visual cues such as layout, UI structure, palette, and interaction metaphor; do not copy exact text, brand styling, or UI composition.

## 2026-04-27 — Mandatory image QA gate
- After live FAL image generation, run vision QA on at least three slides: hook, one middle/trend/teaching slide, and CTA.
- Check that every icon, diagram, UI mockup, and visual metaphor directly supports the exact Thai copy on that slide.
- Check the reverse too: the Thai copy must accurately describe the generated graphic.
- Image prompts/manifest must carry source facts, allowed keywords, exact Thai copy, visual direction, and anti-hallucination rules. If QA finds mismatch, regenerate or edit before treating the Zernio draft as ready.

## 2026-04-27 — 10/day production cadence
- Target is 10 Zernio-ready carousel drafts/day.
- A draft only counts if it has complete assets, Airtable tracking, Zernio draft/review mode, max 5 hashtags, no public source URL/handle, and vision QA passed.
- Distributed production is preferred over huge batches: max 1 draft every 120m plus an evening catch-up of up to 3.
- If the system is short, scrape more high-signal sources rather than reducing quality.

## 2026-04-27 — Dedicated source hydration workflow
- Broad radar and deep one-off hydration are now separate workflows.
- Radar finds likely winners at scale; source hydration turns one diverse/complex post into a high-value Thai draft.
- For Sway-sent URLs, prompt-list posts, GitHub/resource-list posts, giveaway posts, visual demo posts, and posts where value may live in comments, use skill `genlabs-source-hydration-to-draft`.
- Main post text alone is not enough for many resource posts. Scrape thread/replies/comments before drafting when relevant.
- Check author follow-ups first for prompts, GitHub repos, docs, free resources/giveaways, demos, and tool links.
- Extract prompts/resources into Airtable/manifest and classify links as `include_in_caption`, `internal_only`, or `needs_review`.
- Add useful client-facing resource links to `tiktokSettings.description` when they help viewers act on the post; keep generic source attribution internal.
- Analyze source images before visual generation. Use them as reference for structure and understanding, not as copied graphics.
- Self-improvement learnings from comments, links, actor reliability, image QA, and performance must be promoted into Obsidian/skills/workflows.
