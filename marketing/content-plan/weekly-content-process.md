# Weekly Content Session

> The one content ritual: review → decide → scaffold → produce → import. Run once a week (usually Monday of the lead week), start to finish in one sitting — pausable anywhere. Output: `jira/imports/YYYY-Www.csv` imported to Jira, with briefs / drafts / Drive docs / Canva URLs behind it, and a chat handoff summary for Furqan.
>
> Replaced `plan-reconcile-process.md`, `monthly-plan-generation-process.md`, and `rolling-4week.md` on 2026-06-10. Brief writing folded in 2026-06-10 — briefs are written just-in-time inside the session, not stocked by an outside process.

## Trigger

- "Run the weekly content session"
- "Plan the content week"
- "Monday content session"

## Inputs

1. **Target publish week** — defaults to next ISO week.
2. **Anything Travis wants to flag** — slips, urgent insertions, capacity changes.

## Context to load

- /Users/travisfoster/claude-code/cerkl/marketing/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/marketing/content-plan/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/marketing/content-plan/inputs.md
- /Users/travisfoster/claude-code/cerkl/marketing/content-plan/jira-csv-guidelines.md
- /Users/travisfoster/claude-code/cerkl/marketing/seo/keyword-strategy.md

(Per PRINCIPLES.md #4, this list is authoritative for this scope. `keyword-strategy.md` is what makes the topic conversation SEO-informed — its "How content-plan should consume this" section applies here. The heavy inventory files stay with the Wave 1 brief subagent. The annual plan `2026-content-plan.md` is **not** a mandatory load — consult it on demand as a suggestion; it goes stale fast and never overrides inputs + SEO status + Travis's call.)

## State model

| State | Lives in | Owner |
|---|---|---|
| Blog schedule + per-post SEO contract | `../seo/briefs/` (frontmatter + body) | this session (writes briefs just-in-time in Wave 1) |
| Dated commitments + week sketches | [`inputs.md`](inputs.md) § Upcoming | this session |
| Idea mailbox | [`inputs.md`](inputs.md) § Ideas | anyone appends; this session triages |
| Editorial stance | [`inputs.md`](inputs.md) § Theme & stance | Travis |
| SEO research set | `../seo/keyword-strategy.md` + `../seo/inventory/` | refreshed occasionally; **staleness checked in Phase 0** |
| The locked week | `jira/imports/YYYY-Www.csv` | **orchestrator is the only writer during the session** |
| What shipped | Jira (and git) | — |

## Context & dispatch model

The top-level conversation is the orchestrator and stays thin. Every unit of work in Phase 3 is **one subagent handed a skill chain** — fresh context, self-contained brief, returns ≤200 words. Subagents never edit the CSV; they return values and the orchestrator fills tokens in single passes (one writer, parallel-safe). No nesting is needed anywhere — fan-out happens at this level. Waves are sequential (LinkedIn wraps blogs; assets need copy); units inside a wave run in parallel.

---

## Phase 0 — Review (orchestrator, read-only, ~5 min)

1. **Upcoming sweep:** read `inputs.md` § Upcoming — what's due this week / next, what needs rework (delays, launches, deadlines)?
2. **Brief table:** read the YAML frontmatter of every file in `../seo/briefs/` (skip `_template.md`, `archive/`) and present one table: `slug · status · scheduled_for · pillar`. This is the whole queue view — scheduled, in-progress, and leftovers.
3. **SEO gap read:** from `keyword-strategy.md` (loaded above), present a short candidate list: Tier 1/2 keywords marked 🔴 (no page), the Coverage-gaps section, 🟡 refresh candidates, and any recent Insights implications not yet acted on — **filtered through the editorial stance** (stance-banned items don't count as candidates). Note pillar balance: which of the 5 pillars look thin across the brief table + recent posts.
4. **SEO freshness check:** report the age of (a) the newest `../seo/inventory/webflow-export-*.csv` (date is in the filename) and (b) keyword-strategy's `Last updated:` line. **Either >30 days → flag**: cannibalization checks may miss recent posts; suggest a refresh (new Webflow export + `inventory/generate-derived.py`, keyword-strategy review) as a separate task. Don't block the session.
5. Only if Travis asks: scan a prior week's CSV tokens, or recap what shipped.

## Phase 1 — Decide (the conversation)

Propose a slate for the target week, drawn from (in rough priority): Upcoming items that are due → ideas worth promoting → keyword gaps from `keyword-strategy.md` (Tier 1/2 🔴, coverage gaps, refresh candidates) → already-scheduled briefs. The annual plan is a suggestion if consulted at all.

- **cerkl.com blog(s):** for each, agree **topic + angle + primary keyword + pillar** in chat — this is the brief review, done up front. Proposals should tie back to the Phase 0 gap read; a topic with no keyword target is allowed but must be **explicitly tagged "editorial — no SEO target"** (bylines, launch announcements, POV pieces). An existing queued brief can fill a slot; nothing requires one.
- **ICPro blog:** topic decided here.
- **LinkedIn wraps:** a menu, not a quota — theme / blog link / poll / carousel; short video is out-of-band.
- **Anything from Upcoming that's due:** webinar emails, PR, launch coverage.

Apply the decisions, then **clean up `inputs.md` before moving on**:
- Pulled into the slate → **delete from Upcoming/Ideas** (the CSV owns it now; git remembers)
- Approved for a later week → move to Upcoming with a date
- Dead → prune; this week's sketch → delete (it's locked now); later sketches → update to match what was decided
- Existing briefs scheduled → frontmatter `status: scheduled` + `scheduled_for:`; shipped briefs → archive
- **Displacement is a swap, not a slide.** Bumping a scheduled item requires naming the slot it lands in (within the ceilings) — or it reverts to `queued` (date cleared) with an Upcoming note saying why. Never assign a date without a slot; reslotting is a future session's call.

Slate confirmed in chat = the week is locked.

## Phase 2 — Scaffold (orchestrator, inline)

Run [`jira/jira-scaffold-process.md`](jira/jira-scaffold-process.md) with the slate: all rows, all placeholder tokens, Epic Link + subtask owner IDs pre-filled. For new cerkl.com posts whose brief doesn't exist yet, the slug is decided here (brief filename = slug) and the Description carries `Slug:` + topic + `[BRIEF_PENDING]` for the keyword/CMS lines — backfilled after Wave 1.

## Phase 3 — Produce (subagent waves; orchestrator fills all CSV tokens)

**Wave 1 — blogs (parallel, one subagent per post):**
- Each cerkl.com subagent: **write the brief if missing** (per [`../seo/seo-brief-production-process.md`](../seo/seo-brief-production-process.md) — cannibalization check against `inventory/derived/keyword-url-map.md`, pillar assignment, ≥2 sibling URLs, CMS properties; topic/angle/keyword come from Phase 1) → pre-write → draft → edit → Drive upload. Returns: slug · brief path · Drive URL · score · CMS props · flags.
- The ICPro subagent: pre-write → draft → edit → Drive upload (slug from the CSV). Returns the same shape, minus brief.
- *Alongside, optional:* a brief-writing subagent for **next week's** approved-but-unwritten topics, if Travis queued any in Phase 1.

Orchestrator: fill Drive URLs (+ backfill any `[BRIEF_PENDING]` lines) in the CSV — one pass. **Checkpoint:** scores, new briefs, flags.

**Wave 2 — LinkedIn copy (parallel, one subagent per post):**
- Each subagent: draft caption + asset spec + hashtags from the wrapped source (per [`../channels/linkedin/linkedin-process.md`](../channels/linkedin/linkedin-process.md) Step 4 + templates). Returns: draft path · copy block.

Orchestrator: fill `Copy:` lines — one pass.

**Wave 3 — LinkedIn assets:**
- Orchestrator builds Canva manifests inline (cheap — per [`../channels/linkedin/linkedin-asset-process.md`](../channels/linkedin/linkedin-asset-process.md) Steps 1–3), then dispatches **parallel render subagents** (template-fill, one per manifest).
- Orchestrator: write `result:` blocks, fill `Asset:` lines — one pass. **Checkpoint:** length-fit / manual-finish warnings.

Pause anywhere; remaining `[…_PLACEHOLDER]` tokens in the CSV are the resume list. Unfilled tokens at import are fine — the team fills gaps in Jira.

## Phase 4 — Import + handoff

1. Travis imports the CSV to Jira (upload-only).
2. Orchestrator prints the handoff summary: slate table (deliverable · date · Drive doc · Canva URL · anything unfilled) + notes for Furqan. The summary is the record that the week went out.

---

## Rules

- **During the session the orchestrator is the only CSV writer.** Subagents return values. (Channel processes run standalone still fill their own tokens — single writer either way.)
- **Briefs are canonical for the blog schedule and are written just-in-time by this session.** Topic/angle/keyword approval happens in the Phase 1 conversation; the research set (`keyword-strategy.md` + inventory) is what keeps them honest — watch its staleness.
- **Capacity limits in `jira-csv-guidelines.md` are ceilings, not quotas.** A thin week is a valid week.

## Future work

- Wire to `/schedule` for a Monday-morning nudge (holiday slide: if Monday is a federal holiday, run Tuesday).
- Fold webinar/PR/email production deeper into Phase 3 — today they're surfaced in Phases 0–1 and produced in their own channels.
- GSC access would make the Phase 1 keyword-gap pull much sharper.

## Learnings

<!-- append "what broke / what we changed" notes here as the session runs -->

### 2026-06-10 — Dry run (Travis test, pre-v2)

- **Raw queue counts lie.** 4 queued briefs passed the old `<4` gate, but 2–3 were stance-banned versus briefs — usable depth was ~2. Fix landed in v2: no count threshold; Phase 0 presents the full table and judgment decides.
- **"Push to early July" assumed capacity that didn't exist.** All sketched July weeks were at the 2/week cerkl.com ceiling, so displaced briefs had nowhere to land. Fix: the "displacement is a swap, not a slide" rule in Phase 1.
- **Session-created blogs (launch announcements, bylines) mint their own slug** — no brief to thread from at scaffold time. Fix landed in v2: slug decided in the conversation, `[BRIEF_PENDING]` backfilled after Wave 1.
- **Epic key had to be guessed.** Pre-fill needs the live Epic key recorded, not just the naming format — now in `jira-csv-guidelines.md` §Epics.
- What worked: writes held at the pause point; capacity saturation correctly *derived* from Upcoming sketches + ceilings (no capacity ledger needed); the `cerkl-vs-firstup` stray date caught independently by the session and the Upcoming note.
- **Topic proposals weren't SEO-informed** — the test proposed a brief with no keyword ideas. Root cause: `keyword-strategy.md` wasn't in the session's `Context to load`; the keyword work was deferred to the Wave 1 brief subagent, which is after the topic decision. Fix: keyword-strategy loaded into the conversation; Phase 0 gained the "SEO gap read" (Tier 🔴 / coverage gaps / refresh candidates / unacted Insights, stance-filtered, + pillar balance); every cerkl.com slate item now names its primary keyword + pillar or is tagged "editorial — no SEO target." **Rule:** if a decision is supposed to be informed by a file, that file must be loaded at the decision, not downstream.
