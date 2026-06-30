<!-- ZG-ISSUE-CHECK-CURRENT -->
- **Issue-check 2026-06-30T03:57:20Z:** exact factory command and required recovery both returned `draft_count=0/results=[]`; current factory anchor is `latest_social_draft_factory.json@2026-06-30T03:57:00.537744+00:00` / `manual-exact-run+recovery-2026-06-30T0357Z_zero_draft_source_saturation`. Diagnosis: source-lane/anti-repetition saturation (Canonical 0/98; Matrix 0/436; Evergreen 0/42; AI Words 0/8; KPI 0/8; existing source IDs 466; partial source IDs 34; combined 489; blocked content families 68). No current Airtable record, Zernio draft, outbound payload, media, or new `auto-*` manifest folder exists for this tick, so Zernio/platform verification is not applicable. Cron `a97a7703af32` remains enabled/future-scheduled `2026-06-30T04:54:57.507227+00:00`; no lingering factory/radar process at `2026-06-30T03:57:20Z`. No public posting/live publishing.

<!-- ZG-FACTORY-CURRENT-2026-06-30-0357-ZERO-DRAFT-SOURCE-SATURATION -->
- Current factory readback `latest_social_draft_factory.json@2026-06-30T03:57:00.537744+00:00`: exact production command and required recovery rerun both exited 0 with `draft_count=0/results=[]`.
- Verification: no current Airtable/Zernio payload/post and no new current-run `auto-*` folder/manifest/media; latest auto folder remains historical 2026-06-29T23:02Z. Zernio/platform verification is not applicable because no outbound post exists.
- Source diagnosis: deterministic lanes are saturated by duplicate/source-family guards — Canonical 0/98; Matrix 0/436; Evergreen 0/42; AI Words 0/8; KPI 0/8; existing source IDs 466; partial source IDs 34; combined 489; blocked content families 68.
- Scheduler/process: cron `a97a7703af32` enabled/future-scheduled `2026-06-30T04:54:57.507227+00:00`; no lingering factory/radar process at `2026-06-30T03:57:20Z`.
- Next action: urgent source replenishment with fresh non-repeating Thai software-tip sources, prioritizing ChatGPT and NotebookLM numbered tips before Canva AI, CapCut AI, Perplexity, Gamma, Gemini Sheets/Docs, Claude Artifacts/Projects, and Zapier/Make. Keep factory enabled/draft-only.

<!-- ZG-FACTORY-HISTORICAL-2026-06-30-0246-ZERO-DRAFT-SOURCE-SATURATION -->
- Historical 02:46 zero-draft/source-lane saturation readback is superseded by the 03:57 current readback above. Exact command and required recovery both returned `draft_count=0/results=[]`; no Airtable/Zernio payload existed for that historical tick.

<!-- ZG-FACTORY-CURRENT-2026-06-29-0338-ZERO-DRAFT-SOURCE-SATURATION -->
- Current factory readback manual-exact-run+recovery-2026-06-29T0338Z_zero_draft_source_lane_saturation plus state token latest_social_draft_factory.json@2026-06-29T03:38:55.641350+00:00: exact production command exited 0 at 03:38 with `draft_count=0/results=[]`; source-lane diagnostic showed deterministic lanes saturated; the required exact recovery run then exited 0 at 03:38 with `draft_count=0/results=[]`.
- Verification: latest state file refreshed at 2026-06-29T03:38:55.641350+00:00; no current `auto-*` folder/manifest/media after the 03:38Z run start (latest auto folder remains 2026-06-28T21:46Z), no Airtable/Zernio payload/post for this tick, and Zernio/platform verification is not applicable because no outbound post exists. No lingering factory/radar process at 2026-06-29T03:39:20Z; cron `a97a7703af32` remains enabled/future-scheduled for 2026-06-29T04:36:06.999045+00:00.
- Diagnosis: source-lane/anti-repetition saturation: canonical selectable 0; matrix selectable 0/436; evergreen 0/42; AI Words 0/8; KPI backstop 0/8; existing source IDs 463; partial source IDs 34; combined existing/partial 486; blocked content families 68. This is a KPI source-replenishment blocker, not a Zernio API failure.
- Next action: keep production cron enabled/draft-only; urgently replenish fresh non-repeating Thai software-tip sources, prioritizing ChatGPT and NotebookLM numbered work-output tips, then Canva AI, CapCut AI, Perplexity, Gamma, Gemini Sheets/Docs, Claude, and Zapier/Make.

<!-- ZG-FACTORY-HISTORICAL-2026-06-29-0230-ZERO-DRAFT-SOURCE-SATURATION -->
- Historical 02:30 zero-draft/source-lane saturation readback was superseded by the 03:38 current readback above. Exact command and required recovery both returned `draft_count=0/results=[]`; no Airtable/Zernio payload existed for that historical tick.

- 2026-06-28T23:00:52Z: Hourly factory exact run + required recovery both returned zero drafts; latest_social_draft_factory.json@2026-06-28T22:59:18.894146+00:00; no current media/Airtable/Zernio payload; source-lane/anti-repetition saturation remains active; cron enabled/future-scheduled 2026-06-28T23:56:39.360192+00:00.
- 2026-06-28T18:17:34Z: Hourly factory exact run + required recovery both returned zero drafts; latest_social_draft_factory.json@2026-06-28T18:16:59.032127+00:00; no current media/Airtable/Zernio payload; source-lane/anti-repetition saturation remains active; cron enabled/future-scheduled 2026-06-28T19:14:45.340986+00:00.
- 2026-06-28T14:42:25Z: Hourly factory exact run + required recovery both returned zero drafts; latest_social_draft_factory.json@2026-06-28T14:39:30.906269+00:00; no current media/Airtable/Zernio payload; source-lane/anti-repetition saturation remains active; cron enabled/future-scheduled 2026-06-28T15:38:20.933604+00:00.
- Historical 13:28 UTC hourly factory zero-draft/source-lane saturation superseded by 2026-06-28T14:39Z current readback; no media/Airtable/Zernio payload existed for that historical tick.
- Historical 12:22 UTC hourly factory zero-draft/source-lane saturation superseded by 2026-06-28T13:28Z current readback; no media/Airtable/Zernio payload existed for that historical tick.
- 2026-06-27T23:18:16Z: Hourly factory exact run + required recovery both returned zero drafts; latest_social_draft_factory.json@2026-06-27T23:17:27.559483+00:00; no current media/Airtable/Zernio payload; source-lane/anti-repetition saturation remains active; cron enabled/future-scheduled 2026-06-28T00:15:56.691316+00:00.
# GenLabs AI Learning

## Objective
Build a Thai-language AI media system that turns global AI news, tools, prompts, guides, and trends into simple free TikTok content that grows attention and trust, then feeds qualified users toward [[genlabs.in.th]].

## Status
active

## Scope
Included:
- Thai AI TikTok content brand
- free-value-only content strategy
- X and other AI signal source discovery
- Thai translation and adaptation
- handwritten Thai carousel-first asset generation
- analytics ingestion and performance tracking
- self-improving content loop
- free guides/resources hosted on GenLabs
- trust funnel into GenLabs
- Discord operator workflow for discovery, production, analytics, and decisions

Excluded for now:
- hard-selling GenLabs directly inside every TikTok post
- paid products as the primary monetization model
- video-first or motion-first launch workflow
- broad community operations before content engine works
- over-automation that sacrifices quality

## Current State
The business is now defined as a Thai AI media funnel, not a pure news page and not a direct sales channel.

Core truths:
- Public brand name is `GenLabs AI Learning`.
- Audience is broad Thai mass audience interested in AI.
- TikTok content stays free-value-first.
- GenLabs remains the downstream SaaS trust destination.
- Primary early KPI is views and follower growth.
- Launch format is carousel/slideshow first.
- Video and motion graphics come later after the workflow is stable.
- The long-term moat is the learning system: discovery -> content -> analytics -> improvement.
- The Airtable operational base `GenLabs AI Learning OS` is now the structured execution database for research, content, assets, experiments, performance, resources, funnel, and decisions.

## Brand Positioning
### Core promise
Turn global AI signal into simple, useful Thai content people can use immediately.

### Tone
- simple teacher
- friendly Thai internet brand
- business-useful AI advisor

### Content pillars
- AI news that matters
- AI prompts people can copy
- AI tools people can use now
- simple how-to guides
- free downloadable resources
- clear explainers of new AI trends

## Funnel Model
1. Discover high-value AI information from X and adjacent sources.
2. Translate and adapt it into Thai-native useful content.
3. Publish high-clarity TikTok carousel content.
4. Optimize for views and follower growth.
5. Move the best audience toward free guides/resources on GenLabs.
6. Build trust that later supports GenLabs product discovery.

## Operating System
### Discord operator channels
Category: `OPERATOR HQ`
- `#mission-control`
- `#ai-signal-radar`
- `#carousel-pipeline`
- `#asset-forge`
- `#analytics-loop`
- `#free-resource-lab`
- `#genlabs-funnel`
- `#decision-log`

### Channel roles
- `#mission-control` = current priorities, pinned rules, launch checklist, and top-level coordination
- `#ai-signal-radar` = raw discoveries from X, AI tools, updates, prompts, and trends
- `#carousel-pipeline` = content selection, rewrite queue, prioritization, and publishing pipeline
- `#asset-forge` = carousel style, handwritten Thai visuals, asset generation system
- `#analytics-loop` = TikTok analytics, KPI review, experiment tracking, self-improvement loop
- `#free-resource-lab` = downloadable guides, prompt packs, website free resources
- `#genlabs-funnel` = trust path from media attention to GenLabs
- `#decision-log` = final calls only

### Airtable operating base
Base: `GenLabs AI Learning OS`
- `AI Signals` = raw research intake and signal ranking
- `Content Pipeline` = shortlisted ideas through draft, design, and posting
- `Assets` = handwritten Thai visual system and reusable design components
- `Experiments` = structured hook/topic/format/CTA tests
- `Performance` = post-level KPI tracking for views, saves, shares, follows, and clicks
- `Resources` = free guides, prompt packs, and lead-generating educational assets
- `Funnel` = trust path from content to resource to GenLabs consideration
- `Decisions` = final operating and strategy calls

### System rule
- Discord = live discussion and execution
- Airtable = structured operational database
- Obsidian = durable strategy, handoffs, memory, and decisions
## Analytics and Self-Improvement Loop
### Primary KPI
- views
- follower growth

### Secondary KPI
- saves
- shares
- profile visits
- clicks to free resources

### Learning loop
- collect TikTok performance data
- cluster winning hooks
- cluster winning topics
- identify follower-converting formats
- compare high-view vs low-view posts
- update future content selection rules
- improve CTA placement and resource strategy

### Improvement questions to answer repeatedly
- Which topics reliably get reach?
- Which hook patterns turn views into follows?
- Which visual styles retain attention best?
- Which content types push users toward free resources?
- Which categories are broad enough to grow but still relevant to GenLabs?

## Next Actions
- [x] Create the `OPERATOR HQ` Discord category and channels for this business.
- [x] Define channel descriptions/topics and pinned operating rules.
- [x] Prepare the `GenLabs AI Learning` operating message for `#mission-control`.
- [x] Create the Airtable base structure for research, content, assets, experiments, performance, resources, funnel, and decisions.
- [x] Define the source stack for AI discovery from X and adjacent channels.
- [x] Define the ranking logic for what is worth turning into content.
- [x] Define the Thai carousel asset system and handwritten visual style.
- [ ] Generate and QA the first full live carousel set using a GenLabs reference image URL.
- [ ] Define the first data-entry and review rhythm for Airtable + Discord + Obsidian.
- [ ] Define the first set of free resources to host on GenLabs.
- [ ] Publish the first batch of carousel content manually before full automation.

## Open Questions
- Which sources beyond X should be in the first discovery stack?
- What is the first best free resource to offer on GenLabs?
- What level of human review should remain before auto-posting?
- What should the first weekly review cadence look like for the analytics loop?

## Blockers
- Source ranking logic not yet defined.
- TikTok analytics ingestion path not yet defined.
- Visual template system not yet defined.
- First resource offer not yet chosen.

## Linked Decisions
- [[Aion OS/02 - Decision Log]]

## Linked Session Handoffs
- [[Aion OS/Session Handoffs/2026-04-26 - genlabs-thai-ai-media-engine-setup]]

## References
- [[Aion OS/Projects/genlabs-ai-learning-state]]
- [[Aion OS/03 - Operating Manual]]
- [[Aion OS/06 - Aion Command Center]]
- [[Aion OS/07 - Open Loops]]
- [[Aion OS/16 - Master Dashboard]]
- https://genlabs.in.th
