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
