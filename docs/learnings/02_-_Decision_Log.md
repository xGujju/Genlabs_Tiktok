# Decision Log

## 2026-04-20 — Discord + Obsidian communication system
- **Project:** [[Aion OS/Projects/discord-ops]]
- **Decision:** Discord is the conversation layer; Obsidian is the durable memory layer and source of truth.
- **Why:** Discord is fast for discussion but poor for long-term structured recall.
- **Consequences:** Important context must be summarized into Obsidian notes instead of being left only in chat.
- **Revisit Trigger:** Revisit if the workflow becomes too heavy or if automation is added.

## 2026-04-20 — Daily notes and support systems are part of Aion OS
- **Project:** [[Aion OS/Projects/discord-ops]]
- **Decision:** Daily notes, weekly reviews, an Aion command center, and open-loop tracking are standard parts of the operating system.
- **Why:** They reduce context loss between sessions and create a repeatable review cadence.
- **Consequences:** Active work should touch the daily note, and unresolved items should be surfaced instead of hidden in chat.
- **Revisit Trigger:** Revisit if the system becomes too heavy for actual use.

## 2026-04-20 — Base operating structure is standardized
- **Project:** [[Aion OS/Projects/discord-ops]]
- **Decision:** Goal stack, people memory, SOP index, file organization rules, intake/triage, and supporting templates are now part of the base system.
- **Why:** They create clear memory, predictable file organization, and repeatable operating processes.
- **Consequences:** New work should be routed through the standardized structure instead of being improvised ad hoc.
- **Revisit Trigger:** Revisit if the structure becomes too heavy or misses a critical operating need.

## 2026-04-20 — Control systems for scaling and cleanup are standardized
- **Project:** [[Aion OS/Projects/discord-ops]]
- **Decision:** Master dashboard, subagent command structure, archive/review system, and decision-quality framework are standard parts of the operating base.
- **Why:** They improve control, scaling, cleanup, and decision consistency.
- **Consequences:** Aion can scale more cleanly, keep quality higher, and reduce clutter over time.
- **Revisit Trigger:** Revisit if the system becomes too heavyweight or if different scaling patterns emerge.

## 2026-04-26 — New GenLabs-linked Thai AI media business is a free-value TikTok trust funnel
- **Project:** [[Aion OS/Projects/genlabs-thai-ai-media-engine]]
- **Decision:** Build the new business as a Thai-language AI media brand on TikTok that shares free news, prompts, guides, tools, and explainers while feeding long-term trust toward GenLabs.
- **Why:** This preserves broad top-of-funnel growth while keeping strategic alignment with the actual SaaS business.
- **Consequences:** Content should stay free-value-first, broad enough to grow, and useful enough to support future GenLabs trust and discovery.
- **Revisit Trigger:** Revisit if broad audience growth fails to translate into meaningful trust or if a narrower audience converts substantially better.

## 2026-04-26 — Primary early optimization target is views and follower growth
- **Project:** [[Aion OS/Projects/genlabs-thai-ai-media-engine]]
- **Decision:** Optimize the launch system primarily for views and follower growth, using saves, shares, profile visits, and resource clicks as secondary indicators.
- **Why:** The first job of the media engine is reach and audience formation, not immediate conversion.
- **Consequences:** Topic selection, hooks, formatting, and analytics should prioritize reach and repeat audience demand before deeper funnel optimization.
- **Revisit Trigger:** Revisit after the channel achieves stable audience growth or if reach grows without meaningful trust signals.

## 2026-04-26 — Launch with carousel-first workflow before video and motion automation
- **Project:** [[Aion OS/Projects/genlabs-thai-ai-media-engine]]
- **Decision:** Start with handwritten Thai carousel/slideshow content, then expand into video explainers and motion graphics later.
- **Why:** Carousel production is the fastest path to a stable publishing workflow and clean automation foundation.
- **Consequences:** The first operating system should focus on discovery, Thai rewrite, carousel asset generation, publishing, and analytics before building heavier media workflows.
- **Revisit Trigger:** Revisit once the carousel system is stable and repeated winning patterns are visible.

## 2026-04-26 — Public brand name is GenLabs AI Learning
- **Project:** [[Aion OS/Projects/genlabs-thai-ai-media-engine]]
- **Decision:** Use `GenLabs AI Learning` as the public-facing TikTok/media brand name.
- **Why:** It keeps direct brand continuity with GenLabs while making the educational value proposition explicit.
- **Consequences:** Discord, project notes, content system, and future resource packaging should all align around this name.
- **Revisit Trigger:** Revisit only if the public audience strongly resists the name or a clearer Thai-facing brand proves substantially stronger.

## 2026-04-26 — Airtable is the operational database for GenLabs AI Learning
- **Project:** [[Aion OS/Projects/genlabs-thai-ai-media-engine]]
- **Decision:** Use Airtable base `GenLabs AI Learning OS` as the structured operational database for research, content, assets, experiments, performance, resources, funnel logic, and decisions.
- **Why:** Discord is too fast and noisy for structured operations, while Obsidian should stay focused on durable strategy and memory rather than day-to-day production records.
- **Consequences:** Live work flows through Discord, structured records live in Airtable, and durable operating knowledge is summarized back into Obsidian.
- **Revisit Trigger:** Revisit if Airtable creates too much admin drag or if analytics/reporting needs exceed the current structure.

## 2026-04-26 — Aion must stay locked on views-first self-improvement for GenLabs AI Learning
- **Project:** [[Aion OS/Projects/genlabs-thai-ai-media-engine]]
- **Decision:** Aion's main operating responsibility is to maximize views by finding trend-aligned viral TikTok content opportunities, extracting performance learnings, and pushing the channel toward the `100,000 views` milestone.
- **Why:** The business wins or loses on reach, topic selection, hooks, and repeated learning, not on generic admin neatness.
- **Consequences:** Trend hunting, performance review, and durable learning promotion should outrank low-leverage organization work. Cron-based self-improvement reviews are part of the operating system.
- **Revisit Trigger:** Revisit if the channel reaches a stage where another KPI clearly matters more than views and follower growth.

---

## 2026-04-28 — GenLabs carousel length is adaptive 5–10 images
- **Project:** [[Aion OS/Projects/genlabs-ai-learning-state]]
- **Decision:** GenLabs AI Learning carousels must use **at least 5 images**, and may use **6, 8, or up to 10 images** when extra explanation makes the lesson easier and more valuable for clients.
- **Why:** Some AI workflows/prompts/resources need more room to teach clearly. Forcing every carousel into 5 images can reduce usefulness and client learning.
- **Consequences:** Draft generation should choose slide count based on explanation need. Extra slides should carry real educational value such as examples, deeper tips, frameworks, common mistakes, glossary/evidence, or CTA. Never pad weak content just to reach a higher image count.
- **Implementation:** Hermes repo carousel code now supports 5–10 slide plans, CLI accepts `--slide-count {5..10}`, and the scheduled draft factory uses adaptive slide count for future drafts. SOP updated at [[Aion OS/SOPs/genlabs-ai-carousel-production-process]].
- **Revisit Trigger:** Revisit if TikTok performance shows longer carousels reduce completion/saves, or if specific topics consistently perform better at a fixed length.

---

## 2026-05-03 — Prompt Drop topics and visuals use a structured mix, not random style choice
- **Project:** [[Aion OS/Projects/genlabs-ai-learning-state]]
- **Decision:** GenLabs Prompt Drop planning must choose audience/use-case first, then visual world. The default 10-post mix is 4 product/commerce visuals, 2 fashion/styling/creator editorial, 2 marketing/ad/business assets, 1 experimental/grunge aesthetic world, and 1 analytics/seasonal practical remix.
- **Why:** GenLabs AI Learning must stay practically useful for Thai sellers, creators, SMEs, and marketers while still using premium visuals to stop the scroll. Cool styles such as grunge are allowed, but only when attached to a real output people can use.
- **Consequences:** Prompt Drop candidates must state bucket, audience, real use case, output, visual world, GenLabs fit, novelty, and score before generation. No more choosing visual styles only because they feel cool in the moment.
- **Implementation:** SOP added at [[Aion OS/SOPs/genlabs-prompt-drop-selection-and-scheduling]]. Skills `genlabs-prompt-drop-series` and `genlabs-prompt-drop-visual-first` updated with the mix/selection rule.
- **Revisit Trigger:** Revisit after enough Prompt Drop posts are published to compare saves, shares, follows, and views by bucket/style.

---

## 2026-05-03 — GPT Image/FAL generation defaults to low quality for speed
- **Project:** [[Aion OS/Projects/genlabs-ai-learning-state]]
- **Decision:** GenLabs GPT Image/FAL carousel and Prompt Drop generation should default to `quality=low`, not `high` or `medium`.
- **Why:** Sway corrected that high-quality GPT Image generation takes too long. Faster iteration matters more for the draft factory and Prompt Drop experiments, as long as QA still protects output quality.
- **Consequences:** Production scripts, manual Prompt Drop scripts, YouTube draft CLI, and the hourly Zernio draft cron should use `--quality low` by default. Use QA/regeneration for bad outputs; only use medium/high when Sway explicitly asks for a special final-quality exception.
- **Implementation:** Hermes code defaults updated in `tools/ai_signal_radar/carousel.py`, `scripts/generate_ai_signal_carousel.py`, `scripts/scheduled_ai_social_draft_factory.py`, `scripts/create_youtube_genlabs_draft.py`, and Prompt Drop generation scripts. Skills and SOPs updated.
- **Revisit Trigger:** Revisit only if low quality consistently fails visual QA or if a specific final asset needs higher quality by explicit approval.

---

## 2026-05-03 — Prompt Drop daily KPI is 15 complete carousel/image sets
- **Project:** [[Aion OS/Projects/genlabs-ai-learning-state]]
- **Decision:** Prompt Drop now targets **15 complete carousel/image sets per day**. A set only counts when it has candidate intake, visual inspiration/source category, JSON manifest, complete image folder, QA status, Airtable tracking, and Zernio draft ID when ready for Sway review.
- **Why:** Sway wants the Prompt Series to become an execution engine, not occasional experiments. The KPI forces enough volume to test visual styles and prompt use cases while keeping QA gates.
- **Consequences:** Daily planning uses a 15-slot mix: 6 product/commerce, 3 fashion/styling/creator, 3 marketing/ad/business assets, 1 experimental visual world, and 2 performance/seasonal practical remixes. Pinterest/Behance/Dieline/Branding in Asia can be used for inspiration, but exact layouts/compositions are not copied.
- **Implementation:** Execution plan saved at `/home/clawd/.hermes/hermes-agent/docs/superpowers/plans/2026-05-03-genlabs-prompt-drop-15-sets-daily-execution.md`; Obsidian SOP saved at [[Aion OS/SOPs/genlabs-prompt-drop-15-sets-daily-plan]].
- **Revisit Trigger:** Revisit after first 3 production days or if completion rate is below 10 QA-pass sets/day due to generation/QA bottlenecks.

---

## 2026-05-03 — Prompt Drop visuals require intention and realistic packaging
- **Project:** [[Aion OS/Projects/genlabs-ai-learning-state]]
- **Decision:** Prompt Drop visuals must have explicit business/use-case intention before generation. Product/commerce posts must specify realistic designed packaging; skin/macro/beauty realism is allowed only when it strengthens a real brand/product/output.
- **Why:** Sway rejected arbitrary drop-on-skin/skin-close-up visuals that looked cool but did not explain the product, brand, or usable output. GenLabs AI Learning must stay useful for Thai sellers, creators, SMEs, and marketers, not become random aesthetics.
- **Consequences:** Candidate manifests must include `visual_intention` and product posts must include `packaging_requirement`. QA rejects blank/plain/unbranded packaging, decorative liquid drops/props without meaning, fake claims/logos, and any visual world chosen only because it looks cool.
- **Implementation:** First technical pilot `thai-realistic-skin-serum-prompt-drop-2026-05-03` / Zernio draft `69f706f2fc6b7a5c36445f00` is marked creatively rejected and must not be used as an accepted template.
- **Revisit Trigger:** Revisit after replacement Prompt Drop drafts generate enough performance data to compare saves/shares/follows by product packaging, fashion styling, marketing asset, and experimental buckets.

---

## 2026-05-03 — Prompt Drop Zernio drafts require long Thai prompt-giveaway descriptions with no promo by default
- **Project:** [[Aion OS/Projects/genlabs-ai-learning-state]]
- **Decision:** Prompt Drop Zernio/TikTok photo drafts should use long-form Thai descriptions of about 2,000+ characters in `tiktokSettings.description`. They must include the actual copyable prompt giveaway, customization guidance, Thai use cases, visual intention, product packaging requirement when relevant, and max 5 relevant hashtags.
- **Why:** The Prompt Drop series wins when viewers can save and use the prompt immediately. Short captions waste the format and make the post feel like only a cool image instead of a useful GenLabs AI Learning asset.
- **Consequences:** Existing short `caption_draft_th` text in generation manifests is not enough for Zernio. Zernio-ready Prompt Drop posts should route through the dedicated Prompt Drop draft factory/CLI, which builds the long Thai caption and uses the safe draft-only Zernio client. GenLabs promotional endings/CTA, `genlabs.in.th`, and no-prompt sales bridges are omitted unless Sway explicitly re-approves them.
- **Implementation:** Added `tools/ai_signal_radar/prompt_drop_draft_factory.py` and `scripts/create_prompt_drop_zernio_draft.py`. After Sway's correction, tests/code enforce no default GenLabs promo, required `visual_intention`, required `packaging_requirement` for product posts, and no `#GenLabsTH` default hashtag. The earlier live draft `69f706f2fc6b7a5c36445f00` remains technically draft-safe but creatively rejected.
- **Revisit Trigger:** Revisit if long descriptions reduce performance, if TikTok/Zernio caption limits/behavior change, or if Sway explicitly re-approves Prompt Drop promo endings.

---

## 2026-05-03 — Prompt Drop cron cadence established for research, execution, and verification
- **Project:** [[Aion OS/Projects/genlabs-ai-learning-state]]
- **Decision:** Prompt Drop production runs through three recurring jobs: research/style-bank slate, 5-set draft factory batches, and QA/Zernio verification.
- **Why:** The 15-set/day target needs a repeatable operating cadence, not random manual selection.
- **Consequences:** Candidate intake, visual sourcing, generation, Zernio draft-only handoff, and verification are split into clear lanes that can learn from daily results.
- **Implementation:** Cron jobs created: `c0968d77c962` / `GenLabs Prompt Drop research + style-bank slate` at `15 */4 * * *`; `465464d576f2` / `GenLabs Prompt Drop 5-set draft factory` at `0 1,7,13 * * *`; `faf32927c4a1` / `GenLabs Prompt Drop QA + Zernio verifier` at `45 2,8,14 * * *`.
- **Revisit Trigger:** Revisit cadence after the first 3 production days or if either research backlog, image generation, QA, or Zernio verification becomes the bottleneck.

---

## 2026-05-04 — GenLabs/Zernio production crons stay enabled
- **Project:** [[Aion OS/Projects/genlabs-ai-learning-state]]
- **Decision:** GenLabs/Zernio production cron jobs must not be left paused as the default safety response. If blockers appear, Aion fixes/unblocks, uses safe draft-only recovery, and keeps the KPI loop active.
- **Why:** Pausing production prevents daily draft output and blocks the 100k-view KPI learning loop.
- **Consequences:** Manual-batch reconciliation, QA, and source repair run in parallel with enabled production crons. Public publishing remains manual/draft-only safe.
- **Implementation:** Resumed `a97a7703af32` and `465464d576f2`; patched skills, memory, cron prompt, and source backstop tests at 2026-05-04T13:03:56Z.
- **Revisit Trigger:** Revisit only if Sway explicitly orders a temporary pause in the current task.

---

## 2026-05-12 — GenLabs software-tip expansion prioritizes ChatGPT and NotebookLM numbered tips
- **Project:** [[Aion OS/Projects/genlabs-ai-learning-state]]
- **Decision:** Expand ChatGPT + NotebookLM practical numbered tips first; then test other software only when the carousel can visibly deliver clear numbered actions: Canva AI, CapCut AI, Perplexity, Gamma, Gemini Sheets/Docs, Claude, and Zapier/Make.
- **Why:** Current Thai audience evidence directly supports ChatGPT practical productivity/work-output tips; NotebookLM is a priority controlled experiment because Sway flagged Thailand resonance and document/onboarding workflows are showing demand. Generic tool explainers and news posts are weaker than concrete tip/action carousels.
- **2026-05-13 3-day self-improvement reaffirmation:** ChatGPT practical productivity/workflow remains the only directly proven Thailand lane (`7634027210248097042` at 25,219 views / 362 shares, +6,577 views vs 2026-05-10). NotebookLM remains the next controlled priority for SOP/PDF/team-knowledge numbered tips. Factory can create safe drafts again (`6a044eb36e2545748376f613` via `2026-05-13_10-21-58.md`) and current scheduler/readback resolved, but generic/non-priority software output is not KPI-ready; result closure and source-topic QA must happen before scaling.
- **2026-05-14 daily self-improvement reaffirmation:** Latest Open Loops evidence shows best/closest post `7634027210248097042` / ChatGPT 8 productivity tips at 26,924 views / 383 shares, while the current Airtable sample still has 0 sampled `Performance` and 0 sampled `Experiments` rows. Thai audience evidence therefore directly supports more ChatGPT practical numbered tips; NotebookLM remains the priority controlled test for SOP/PDF/team-knowledge workflows, not yet a ChatGPT-level proven winner. Source exhaustion plus repeated/generic or wrong-topic factory output is a production bug: replenish fresh non-repeating ChatGPT/NotebookLM/software-tip source IDs and keep the pre-FAL source-topic/promised-tip gate strict.
- **2026-05-15 daily self-improvement reaffirmation:** Current Open Loops evidence shows best/closest post `7634027210248097042` / ChatGPT 8 productivity tips at 28,211 views / 393 shares, while the current Airtable sample still has 0 sampled `Performance` and 0 sampled `Experiments` rows. Thai audience evidence directly supports more ChatGPT practical numbered tips. NotebookLM remains a priority controlled test, not yet a ChatGPT-level proven winner, because sampled Airtable performance proof is still missing but Sway's Thailand signal and document/onboarding workflows justify testing SOP/PDF/team-knowledge tips. Latest factory output generated manifest/Airtable but collapsed a broad ChatGPT workflow source into generic meeting-notes/action-follow-up and hit Zernio POST 403, so repeated/generic output and source-topic drift remain production bugs; expansion must be source-specific, promise-counted, duplicate-checked, and draft-only until API permissions are fixed.
- **2026-05-16 daily self-improvement reaffirmation:** Current Open Loops evidence shows best/closest post `7634027210248097042` / ChatGPT 8 productivity tips at 29,703 views / 407 shares / gap 70,297, while the pre-run Airtable sample still has 0 sampled `Performance` and 0 sampled `Experiments` rows. Thai audience evidence directly supports more ChatGPT practical numbered tips; NotebookLM remains a priority controlled test rather than a proven ChatGPT-level winner, because current sampled performance proof is missing but Sway's Thailand signal and document/SOP/FAQ workflows justify testing it. Source-lane exhaustion (`draft_count=0`, Canonical 0/98 eligible, evergreen 0/42, AI Words 0/8, KPI backstop 0/8) plus generic/wrong-topic factory output remain production bugs: replenish fresh non-repeating ChatGPT/NotebookLM/software-tip source IDs and keep promise-count/source-topic gates strict.
- **2026-05-16 3-day self-improvement reaffirmation:** Best/closest post `7634027210248097042` / ChatGPT 8 productivity tips reached 29,703 views / 407 shares / gap 70,297 (+4,484 views and +45 shares since 2026-05-13 3-day review), confirming ChatGPT practical numbered tips as the proven Thai-audience lane. NotebookLM remains the next priority controlled lane for SOP/PDF/source-grounded FAQ/team-knowledge workflows because Sway reports Thailand resonance, but it must be measured before being treated as proven. The current blocker is not strategy ambiguity: it is result-closure/backfill, source-lane exhaustion, source-topic/promise-count QA, and Zernio POST 403.
- **2026-05-17 daily self-improvement reaffirmation:** Current Open Loops evidence shows the ChatGPT 8 productivity winner `7634027210248097042` at 30,761 views / 418 shares / gap 69,239, while the current Airtable sample still has 0 sampled `Performance` and 0 sampled `Experiments` rows. Thai audience evidence therefore directly supports more ChatGPT practical numbered tips. NotebookLM remains a priority controlled test, not yet a ChatGPT-level proven winner, because sampled performance proof is still missing but Sway's Thailand signal and SOP/PDF/FAQ/team-knowledge workflows justify testing it. Repeated/generic/wrong-topic factory output and Zernio POST 403 remain production bugs/blockers; expansion must use fresh non-repeating source IDs, source-topic preservation, promised-tip accounting, duplicate-family checks, and draft-only safety.
- **2026-05-18 daily self-improvement reaffirmation:** Current Open Loops evidence shows the ChatGPT 8 productivity winner `7634027210248097042` at 31,556 views / 426 shares / gap 68,444, while the current Airtable sample still has 0 sampled `Performance` and 0 sampled `Experiments` rows. Thai audience evidence directly supports more ChatGPT practical numbered tips. NotebookLM remains a priority controlled test rather than a proven ChatGPT-level winner because sampled performance proof is still missing, but Thailand demand plus SOP/PDF/FAQ/team-knowledge use cases justify testing it next. The active production bug is source-lane exhaustion plus repeated/generic or wrong-topic outputs; latest factory state returned `draft_count=0/results=[]`, and prior manifest recovery still has Zernio POST 403 plus editorial/source-topic QA open. Replenish fresh non-repeating ChatGPT/NotebookLM/software-tip sources and keep source-topic/promise-count gates strict before FAL/Zernio.
- **2026-05-19 daily self-improvement reaffirmation:** Current Open Loops evidence still shows the ChatGPT 8 productivity winner `7634027210248097042` at 31,556 views / 426 shares / gap 68,444, while the current Airtable sample again has 0 sampled `Performance` and 0 sampled `Experiments` rows. Thai audience evidence directly supports more ChatGPT practical numbered tips. NotebookLM remains the next priority controlled test, not yet a ChatGPT-level proven winner, because sampled performance proof is still missing; test it through SOP/PDF/FAQ/team-knowledge numbered carousels. Today's AI Signals/Content Pipeline sample has useful practical sources (privacy checklist, logo animation workflow, Google/Kaggle agent course), but the factory/run-log state still shows source-lane exhaustion and repeated/generic or wrong-topic output as production bugs. Replenish fresh non-repeating ChatGPT/NotebookLM/software-tip source IDs, dedupe repeated course records, and keep source-topic/promise-count gates strict before FAL/Zernio.
- **2026-05-19 3-day self-improvement reaffirmation:** ChatGPT practical numbered tips remain the proven Thai-audience lane (`7634027210248097042` at 31,556 views / 426 shares / gap 68,444, +1,853 views since 2026-05-16 3-day review). NotebookLM remains the priority controlled Thailand test, not a proven winner yet, until 2h/4h/24h Performance/Experiments rows exist. Source-lane replenishment and result closure now outrank creating more generic backlog; other software tools stay one-at-a-time differentiated tips tests with visible promised counts and protected CTA separated.
- **2026-05-20 daily self-improvement reaffirmation:** Current Open Loops evidence shows the ChatGPT 8 productivity/workflow winner `7634027210248097042` at 32,072 views / 429 shares / gap 67,928, while the current Airtable sample still has 0 sampled `Performance` and 0 sampled `Experiments` rows. Thai audience evidence directly supports more ChatGPT practical numbered tips. NotebookLM remains the next controlled Thailand test for SOP/PDF/FAQ/source-grounded team workflows, not yet a proven ChatGPT-level winner until 2h/4h/24h rows exist. Current factory state (`2026-05-20_09-05-15.md`, `draft_count=0/results=[]`) confirms source-lane/anti-repetition exhaustion, so repeated/generic/wrong-topic content is a production bug; replenish fresh non-repeating ChatGPT/NotebookLM/software-tip sources before spending on FAL/Zernio.
- **2026-05-21 daily self-improvement reaffirmation:** Current Open Loops/run-log evidence shows the ChatGPT 8 productivity/workflow winner `7634027210248097042` at 32,072 views / 429 shares / gap 67,928, with 0 formal candidates, 0 refresh-window candidates, 0 watched/all-post movers, and sampled Airtable `Performance`/`Experiments` still empty. Thai audience evidence directly supports more ChatGPT practical numbered tips. NotebookLM remains the next controlled Thailand test for SOP/PDF/FAQ/source-grounded team workflows, not yet a proven ChatGPT-level winner until 2h/4h/24h rows exist. Factory output `2026-05-21_09-41-22.md` returned `draft_count=0/results=[]` from source-lane / anti-repetition exhaustion (Canonical 0/98, Evergreen 0/42, AI Words 0/8, 09Z KPI backstop 0/8), so repeated/generic/wrong-topic content is a production bug; feed fresh non-repeating ChatGPT/NotebookLM/service-industry software-tip sources and keep source-topic/promised-tip gates strict before FAL/Zernio.
- **Consequences:** Every software-tip carousel must account for the promised number of tips in visible Thai slide copy, keep the reusable GenLabs CTA separate, preserve the exact tool/workflow, and pass duplicate/source-topic gates before FAL/Zernio.
- **Revisit Trigger:** Revisit after ChatGPT and NotebookLM numbered-tip posts have reliable 2h/4h/24h performance entries in Airtable `Performance`/`Experiments`, or if another tool clearly breaks out.



## 2026-05-22 — GenLabs/Zernio tool-topic direction after 3-day review
- **Project:** [[Aion OS/Aion Learning Lab/Zernio Growth/Zernio Growth Memory]] / [[Aion OS/Aion Learning Lab/GenLabs Self Improvement Reviews]]
- **Decision:** Prioritize practical numbered Thai carousels for ChatGPT first and NotebookLM second; run Canva AI, CapCut AI, Perplexity, Gamma, Gemini Sheets/Docs, Claude tools, and Zapier/Make only as distinct software-tip tests with visible promised tip counts before the reusable CTA.
- **Why:** The CTA-stripped ChatGPT productivity/workflow post `7634027210248097042` remains the only direct high-performance proof at 32,072 views / 429 shares. NotebookLM is the highest-priority controlled Thailand lane for source-grounded SOP/PDF/FAQ/team workflows. The factory is currently blocked by source-lane/anti-repetition exhaustion, so generic or repeated drafts would not improve the 100k KPI.
- **Consequences:** Source replenishment and experiment result closure come before more near-duplicate remixes. Every new software-tip post must pass duplicate-family, source-topic, promised-tip, CTA-separation, and draft-only safety gates before FAL/Zernio.
- **2026-05-22 daily analyst reaffirmation:** Re-anchor at 10:35 UTC still shows direct Thai proof for ChatGPT practical numbered work-output tips (`7634027210248097042` at 32,072 views / 429 shares) while sampled `Performance`/`Experiments` remain empty. NotebookLM stays the priority controlled Thailand test for SOP/PDF/FAQ/source-grounded team workflows; other software must be one-at-a-time visible-tip tests, not generic tool explainers.
- **2026-05-23 daily analyst reaffirmation:** Re-anchor at 10:40 UTC still shows the same ChatGPT proof (`7634027210248097042` at 32,072 views / 429 shares / gap 67,928), while sampled `Performance`/`Experiments` remain empty and the factory is source-lane/anti-repetition saturated (`draft_count=0/results=[]`; canonical 0/98, evergreen 0/42, AI Words 0/8, KPI backstop 0/8). Strategic rule remains: expand ChatGPT + NotebookLM practical numbered tips first; test Canva AI, CapCut AI, Perplexity, Gamma, Gemini Sheets/Docs, Claude, and Zapier/Make only as distinct visible-tip carousels. Treat repeated/generic or wrong-topic output as a production bug, not a volume win.
- **2026-05-24 daily analyst reaffirmation:** Re-anchor at 10:52 UTC showed direct Thai proof for ChatGPT practical numbered tips (`7634027210248097042` at 32,072 views / 429 shares / gap 67,928), while sampled `Performance`/`Experiments` remained empty. The latest factory readback refreshed the same source-lane/anti-repetition blocker at `latest_social_draft_factory.json@2026-05-24T11:54:01.437553+00:00` with `draft_count=0/results=[]`. NotebookLM remains a priority controlled Thailand test for SOP/PDF/FAQ/source-grounded team workflows, not a proven ChatGPT-level winner yet. Current strategy is unchanged but urgent: expand fresh non-repeating ChatGPT + NotebookLM practical numbered tips first; then test Canva AI, CapCut AI, Perplexity, Gamma, Gemini Sheets/Docs, Claude, and Zapier/Make only as distinct clear-tip carousels with exact tool/workflow fit, visible promised-tip count, duplicate-family guard, source/meta leak check, long Thai caption, and CTA separated.
- **2026-05-25 3-day self-improvement reaffirmation:** Re-anchor at 10:12 UTC showed KPI flat: ChatGPT productivity/workflow `7634027210248097042` remains at 32,072 views / 429 shares / gap 67,928, with 0 formal breakout candidates and no posts in the last 72h. The strategic rule remains, but execution priority is sharper: backfill/close active results and feed fresh non-repeating ChatGPT + NotebookLM practical numbered service-workflow sources into production before adding variants. Other software tools (Canva AI, CapCut AI, Perplexity, Gamma, Gemini Sheets/Docs, Claude tools, Zapier/Make) stay one-at-a-time visible-tip tests after source-lane, Zernio, and editorial gates clear.
- **2026-05-25 daily analyst reaffirmation:** Pre-run Airtable sample still has 0 sampled `Experiments` / 0 sampled `Performance` rows and shows useful but unmeasured shortlisted topics: Privacy Filter checklist, GPT Image 2 + Seedance logo animation, duplicated Google/Kaggle AI Agents course, and one safety-watch appearance-audit source. Open Loops/run log keep ChatGPT practical numbered work tips as the only direct Thai audience proof (`7634027210248097042` at 32,072 views / 429 shares), while factory source-lane exhaustion remains active (`latest_social_draft_factory.json@2026-05-25T10:51:30.880543+00:00`, `draft_count=0/results=[]`). Therefore the promoted rule remains: expand fresh ChatGPT + NotebookLM practical numbered tips first; test Canva AI, CapCut AI, Perplexity, Gamma, Gemini Sheets/Docs, Claude tools, and Zapier/Make only as distinct clear-tip carousels with visible promised counts, exact tool/workflow fit, duplicate-family guard, public source-meta scan, long Thai caption, and CTA separated.
- **2026-05-26 daily analyst reaffirmation:** Pre-run Airtable sample still has 0 sampled `Experiments` / 0 sampled `Performance` rows and shows useful but unmeasured shortlisted topics: OpenAI Privacy Filter / ChatGPT privacy checklist, GPT Image 2 + Seedance logo animation workflow, Claude seller prompt blocks, and duplicated Google/Kaggle AI Agents course records. Open Loops shows current factory source-lane / anti-repetition exhaustion refreshed at `latest_social_draft_factory.json@2026-05-26T11:00:23.168563+00:00` with exact + recovery both `draft_count=0/results=[]`, Canonical 0/98 eligible, evergreen 0/42, AI Words 0/8, KPI current-hour 0/8. Therefore the promoted rule remains: expand fresh ChatGPT + NotebookLM practical numbered tips first; test Canva AI, CapCut AI, Perplexity, Gamma, Gemini Sheets/Docs, Claude tools, and Zapier/Make only as distinct clear-tip carousels with visible promised counts, exact tool/workflow fit, duplicate-family guard, public source-meta scan, long Thai caption, and CTA separated. Repeated/generic or wrong-topic output is a production bug, not a volume win.
- **2026-06-04 3-day self-improvement reaffirmation:** 2026-06-04 3-day review: ChatGPT practical numbered work-output tips remain the only direct proven Thailand lane (best post 43,875 views / 524 shares / gap 56,125, +11,803 views since 2026-05-25). NotebookLM remains the priority controlled source-grounded lane. Other tools (Canva AI, CapCut AI, Perplexity, Gamma, Gemini Sheets/Docs, Claude, Zapier/Make) stay one-at-a-time visible-tip tests only after result-closure, source-topic, duplicate-family, promised-tip, and draft-only safety gates pass. Current evidence: best post `7634027210248097042` at 43,875 views / 524 shares / gap 56,125; 10:00 baseline and 10:03 read-only comparison found 0 movers/candidates, so no amplification this tick. Current blockers are result closure, source-topic routing for matrix/software-tip factory drafts, one import HTTP 500 watch, and self-improvement readback verification.
- **2026-06-10 3-day self-improvement reaffirmation:** ChatGPT practical numbered work-output tips remain the only direct proven Thailand lane (`7634027210248097042` at 46,154 views / 545 shares / gap 53,846, +2,279 views since the 2026-06-04 3-day review). NotebookLM remains the priority controlled source-grounded lane for SOP/PDF/FAQ/team workflows. Other tools (Canva AI, CapCut AI, Perplexity, Gamma, Gemini Sheets/Docs, Claude tools, Zapier/Make) stay one-at-a-time visible-tip tests only after result-closure, source-topic, duplicate-family, promised-tip, CTA-separation, and draft-only safety gates pass. Off-topic/generic safe drafts are review-only, not KPI-ready.
- **Revisit Trigger:** Revisit after ChatGPT/NotebookLM posts have reliable 2h/4h/24h Performance/Experiments rows or when another tool produces breakout evidence.


## 2026-06-13 — GenLabs software-tip production must preserve exact tool workflow before Zernio
- **Project:** [[Aion OS/Projects/genlabs-ai-learning-state]]
- **Decision:** For GenLabs/Zernio software-tip carousels, a draft is not KPI-ready unless the public slides visibly preserve the promised tool + industry workflow and deliver every promised numbered tip before the reusable CTA.
- **Why:** 2026-06-13 self-improvement evidence shows the KPI winner is still CTA-stripped ChatGPT practical workflow content at 47,973 views, while repeated safe factory drafts collapsed matrix/software sources into generic prompt-context advice.
- **Consequences:** Prioritize ChatGPT practical numbered tips and NotebookLM source-grounded SOP/PDF/FAQ/team workflows. Test Canva AI, CapCut AI, Perplexity, Gamma, Gemini Sheets/Docs, Claude tools, and Zapier/Make only as one-at-a-time exact-workflow visible-tip experiments after duplicate-family, source-topic, promised-tip, CTA, and draft-only gates pass.
- **Revisit Trigger:** Revisit after a non-ChatGPT/NotebookLM software-tip carousel beats the channel average with strong shares/saves or after the factory source-topic QA issue is closed for multiple consecutive drafts.

## 2026-06-16 — GenLabs tool/topic priority for next growth cycle
<!-- ZG-DECISION-TOOL-TOPIC-PRIORITY-2026-06-16 -->
- **Decision:** For the next 3-day GenLabs/Zernio growth cycle, prioritize ChatGPT practical numbered-tip carousels first and NotebookLM source-grounded numbered-tip carousels second. Expansion tools are allowed only as concrete software-tip workflow tests: Canva AI, CapCut AI, Perplexity, Gamma, Gemini Sheets/Docs, Claude tools, and Zapier/Make.
- **Rationale:** The CTA-stripped ChatGPT productivity/workflow winner is at 49,675 views / 592 shares and remains the clearest evidence toward the 100k KPI. Sway also says ChatGPT and NotebookLM are popular in Thailand.
- **Consequences:** Source replenishment and factory routing should favor practical Thai SME work-output templates, not generic AI news or vague tool explainers. Do not force GenLabs product-photo CTA into performance analysis.
- **Revisit trigger:** Revisit when a non-ChatGPT/NotebookLM software-tip post beats 2,500 views in 24h or reaches share_rate >=0.8%, or when a new post breaks 100,000 views.

