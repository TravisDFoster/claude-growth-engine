# Weekly SEO Blog Production

> Take every SEO brief scheduled for the locked week of [`../../content-plan/rolling-4week.md`](../../content-plan/rolling-4week.md) and produce every cerkl.com blog post: pre-writing → draft → edit → publish. Output: one `_live.md` per post in `blog-posts-live/`, each uploaded to Drive, each Drive URL inserted into that week's Jira CSV at [`../../content-plan/jira/imports/YYYY-Www.csv`](../../content-plan/jira/).

## Trigger

**Default (weekly):**
- "Write next week's blog posts"
- "Run weekly blog production"
- "Write Week 1 of rolling-4week"

**Overrides:**
- *Single post:* `"Write the [slug] blog post"`, `"Run production on the [slug] brief"` — operates on one brief by slug, regardless of which week it's in
- *Multi-week:* `"Write weeks 1-2"`, `"Run production for weeks 1, 2, and 3"`, `"Write the next 3 weeks of blog posts"` — pulls scheduled briefs from multiple weeks of rolling-4week

There is no monthly override — backfilling a whole month means specifying weeks 1–4 explicitly (which by definition spans the rolling 4 weeks).

## Inputs

I'll ask before scaffolding:

1. **Target window** — defaults to Week 1 (locked) of [`../../content-plan/rolling-4week.md`](../../content-plan/rolling-4week.md). Can be overridden with:
   - A single brief slug (single-post mode)
   - One or more rolling-4week week numbers (e.g., `weeks 1-2`, `weeks 1, 2, 3`)
2. **Subset?** — within the target window, all scheduled briefs or a specific list of slugs.

## Context to load

- /Users/travisfoster/claude-code/cerkl/shared/icp.md
- /Users/travisfoster/claude-code/cerkl/shared/broadcast.md
- /Users/travisfoster/claude-code/cerkl/shared/competitors.md
- /Users/travisfoster/claude-code/cerkl/shared/company-info.md
- /Users/travisfoster/claude-code/cerkl/marketing/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/marketing/channels/seo-blog/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/marketing/content-plan/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/marketing/content-plan/content-lifecycle-process.md (the end-to-end cadence — read for the Drive-URL-before-CSV ordering constraint and the Monday-CSV-scaffold expectation)

(Per [PRINCIPLES.md #4](/Users/travisfoster/claude-code/cerkl/PRINCIPLES.md), this list is authoritative for this scope — parent loads do not apply unless re-listed here.)

**Parallelization fallback:** if any step is parallelizable and the runtime has the `Agent`/`Task` tool, dispatch sub-agents in one message. If not, parallelize via multiple Tool calls in a single message — same effect.

---

## Steps

### Step 1 — Load scheduled briefs for the target window

- **Owner:** Claude
- **Inputs:** [`../../seo/briefs/`](../../seo/briefs/), [`../../content-plan/rolling-4week.md`](../../content-plan/rolling-4week.md), and the resolved target window from input #1
- **Produces:** an in-memory list of seo-blog briefs to process, each with `{brief_path, slug, scheduled_for, title, target_pillar, primary_solution, iso_week}` parsed from the brief's YAML frontmatter

**What to do:**

Resolve the target window into a set of publish dates:
- **Default (Week 1):** read rolling-4week.md, take the date range of the "Week 1" section header
- **Multi-week:** union of the date ranges of each requested Week N section
- **Single-post (slug override):** skip the date math — load the brief directly and derive its `iso_week` from `scheduled_for`

For multi-post runs, list files in `seo/briefs/` (exclude `_template.md` and `archive/`) and filter to briefs where **all** of:
- `target_channel: seo-blog`, **AND**
- `status: scheduled` or `in-progress`, **AND**
- `scheduled_for:` falls within the target window's date range

Cross-check against rolling-4week.md: every brief surfaced should have a matching row whose `Source brief` column links the same brief file. Flag discrepancies (brief scheduled but not in plan, or plan row pointing at a brief whose `status` ≠ `scheduled`/`in-progress`) before proceeding.

If `Subset?` was specified, narrow the list. Confirm the list with the user before proceeding.

ICPro posts are out of scope — they have their own production path under [`../icpro-blog/`](../icpro-blog/).

### Step 1.5 — Verify Jira CSV scaffold exists

- **Owner:** Claude
- **Inputs:** `iso_week` for each post; [`../../content-plan/jira/imports/`](../../content-plan/jira/imports/)
- **Produces:** a verified set of `{slug → CSV path}` mappings

For each distinct ISO week in the batch, confirm a CSV scaffold exists at `../../content-plan/jira/imports/YYYY-Www.csv` and that it contains a row for each brief slug in the batch (look for `Slug: <slug>` in the Description column of a Task row).

If any CSV is missing or any expected row is absent: **stop and surface the gap.** Monday reconcile is supposed to create the scaffold; this skill does not. Surface which week(s) and which slug(s) are missing so Travis can fix the scaffold before re-running.

### Step 2a — Pre-writing (per post)

- **Owner:** Claude (sub-agent per post — parallelizable across posts)
- **Sequencing:** parallelizable with every other 2a instance
- **Needs:** [`skills/seo-blog-pre-writing/SKILL.md`](skills/seo-blog-pre-writing/SKILL.md)
- **Inputs:** brief path from Step 1
- **Produces:** `blog-posts-pre-writing/YYYY-MM-DD_[slug]_pre-writing.md`

**Batch size rule:** for `n ≤ 2` posts (typical weekly batch), run inline in the orchestrator — sub-agent dispatch overhead exceeds the per-post cost. For `n ≥ 3` (multi-week or catch-up runs), dispatch one sub-agent per post.

**Sub-agent brief (or inline run) must:**
- Take the full path to the SEO brief as input
- Write to `/Users/travisfoster/claude-code/cerkl/marketing/channels/seo-blog/blog-posts-pre-writing/YYYY-MM-DD_[slug]_pre-writing.md` (use the brief's `scheduled_for:` as `YYYY-MM-DD`)
- Carry Group A properties (pillar, solution, keywords, hub link, sibling URLs, all-categories) verbatim from the brief — do not re-derive
- Decide Group B (Top/Middle/Bottom CTA variants, Meta Title, Meta Description, full H1/H2/H3 outline expanding the brief's angle)
- Stop and flag if any Group A property is missing or contradictory — do not invent
- Cap length at ~300 lines
- After writing the file, flip the brief's `status:` from `scheduled` to `in-progress`

### Step 2b — Drafting (per post)

- **Owner:** Claude (sub-agent per post for `n ≥ 3`; inline for `n ≤ 2`)
- **Sequencing:** must run after that post's 2a completes; parallelizable across posts otherwise
- **Needs:** [`skills/seo-blog-drafting/SKILL.md`](skills/seo-blog-drafting/SKILL.md)
- **Inputs:** the pre-writing file from 2a
- **Produces:** `blog-posts-draft/YYYY-MM-DD_[slug]_draft.md`

**Sub-agent brief (or inline run) must:**
- Take the full path to the pre-writing file as input
- Write to `blog-posts-draft/YYYY-MM-DD_[slug]_draft.md`
- Hold Cerkl voice (practical, direct, zero-fluff) per the drafting skill — never blend with partner or generic B2B voice
- Match length to post type (supporting 1,000–1,500 words; pillar 2,000–3,000); don't pad for word count
- Hit SEO bar: focus keyword in title, H1, ≥1 H2/H3, body; strict H1 → H2 → H3 nesting; direct answer in first 2 paragraphs or right after first H2
- Emit the 7-section structure from the drafting skill; do not generate Top/Middle/Bottom CTA copy (placeholders only)
- Use markdown only; no em-dashes; dates in `YYYY-MM-DD`

### Step 2c — Editing (per post)

- **Owner:** Claude (sub-agent per post for `n ≥ 3`; inline for `n ≤ 2`)
- **Sequencing:** must run after that post's 2b completes; parallelizable across posts otherwise
- **Needs:** [`skills/seo-blog-editing/SKILL.md`](skills/seo-blog-editing/SKILL.md)
- **Inputs:** the draft file from 2b
- **Produces:** `blog-posts-live/YYYY-MM-DD_[slug]_live.md` with edit log + image candidates block appended

**Sub-agent brief (or inline run) must:**
- Take the full path to the draft file as input
- Write to `blog-posts-live/YYYY-MM-DD_[slug]_live.md` (preserve the original date and slug)
- Not modify or delete the draft
- Exit at score ≥ 35/50 across Directness, Rhythm, Trust, Authenticity, Density
- Append the edit log block specified in the editing skill
- Append an **image candidates block** per the editing skill's step 6 — 0–3 brand-aligned image template suggestions (or explicit "none") for downstream rendering via `cerkl/marketing/design/blog-assets/render.sh`. Stays inside the publishing-skill strip zone, so it never reaches the Drive doc.
- Return: live file path + final score line

Editing **does not** upload to Drive anymore — that moves to Step 2d.

### Step 2d — Publishing (per post)

- **Owner:** Claude (sub-agent per post for `n ≥ 3`; inline for `n ≤ 2`)
- **Sequencing:** must run after that post's 2c completes; parallelizable across posts otherwise
- **Needs:** [`skills/seo-blog-publishing/SKILL.md`](skills/seo-blog-publishing/SKILL.md)
- **Inputs:** the live file from 2c + brief slug + target week's CSV path (from Step 1.5)
- **Produces:** a Drive Doc URL + an updated row in the target week's Jira CSV

**Sub-agent brief (or inline run) must:**
- Take the live file path, brief slug, and target CSV path as inputs
- Upload the live file to Drive (via `md-to-drive` with Edit-log strip)
- Find the Task row in the target CSV whose Description contains `Slug: <slug>` and replace `[DRIVE_URL_PLACEHOLDER]` with the actual Drive URL
- Preserve all other rows and fields; CSV must still parse cleanly after the edit
- Return: Drive Doc URL + CSV row updated confirmation + final score line (passed through from editing)

Per the publishing skill: this skill does **not** flip brief `status` (stays `in-progress` until Furqan ships in Webflow) and does **not** create the CSV (Monday reconcile owns that).

### Step 3 — Roll up and report

- **Owner:** Claude
- **Inputs:** return values from each 2d
- **Produces:** chat-printed summary

Print one line per post: `slug — score X/50 — <Doc URL> — CSV row updated in YYYY-Www.csv`. Flag any post that:
- Didn't exit editing at ≥ 35/50 (human review needed before publishing — should not have reached 2d)
- Failed publishing (Drive upload failed, CSV row mismatch, etc.)

---

## Output

- `blog-posts-pre-writing/YYYY-MM-DD_[slug]_pre-writing.md` — one per post
- `blog-posts-draft/YYYY-MM-DD_[slug]_draft.md` — one per post (kept after editing)
- `blog-posts-live/YYYY-MM-DD_[slug]_live.md` — one per post, with edit log appended
- A Drive Doc per live file (Claude-Uploads folder, `YYYY-MM-DD — <H1 title>` naming)
- An updated Jira CSV at `../../content-plan/jira/imports/YYYY-Www.csv` — one row per post has its `[DRIVE_URL_PLACEHOLDER]` replaced with the actual URL
- A chat-printed roll-up summary
- Each brief's `status:` is `in-progress` after Step 2a runs. **Do not flip to `shipped` here** — that happens when the post actually goes live in Webflow, after Furqan copies the Drive Doc over. The planner archives shipped briefs on the next Monday reconcile.

## Future work

- When `seo-blog-pre-writing` evolves into per-post research lookups (e.g., SERP intent, competitor coverage), consider splitting Step 2a into 2a-research + 2a-properties.
- Consider extracting the per-post 2a → 2b → 2c → 2d chain into a sub-process file when ICPro-blog comes online with the same shape and we want to share orchestration logic.

## Learnings

Append "what broke / what we changed" notes here as the process matures.
