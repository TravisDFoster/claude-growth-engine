# Weekly ICPro Blog Production

> Take every Internal Comms Pro (internalcommspro.com) blog Task in the target week's Jira CSV and produce every post: pre-writing → draft → edit → publish. Usually invoked by the [weekly content session](../../content-plan/weekly-content-process.md) (Phase 3). Output: one `_live.md` per post in `blog-posts-live/`, each uploaded to Drive with `ICP` in the filename, each Drive URL inserted into that week's Jira CSV at [`../../content-plan/jira/imports/YYYY-Www.csv`](../../content-plan/jira/).

## Trigger

**Default (weekly):**
- "Write next week's ICPro blog posts"
- "Run weekly ICPro production"
- "Write this week's ICPro post"

**Overrides:**
- *Single post:* `"Write the [slug] ICPro post"`, `"Run production on the [date] ICPro row"` — operates on one row, regardless of which week
- *Multi-week:* `"Write ICPro for the next 2 weeks"` — pulls ICPro Tasks from multiple weekly CSVs

## Inputs

1. **Target week** — defaults to the next publish week (or the week the session just scaffolded).
2. **Subset?** — within the target week, all ICPro rows or a specific list of slugs.

## Context to load

- /Users/travisfoster/claude-code/cerkl/shared/icp.md
- /Users/travisfoster/claude-code/cerkl/shared/broadcast.md
- /Users/travisfoster/claude-code/cerkl/shared/competitors.md
- /Users/travisfoster/claude-code/cerkl/shared/company-info.md
- /Users/travisfoster/claude-code/cerkl/marketing/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/marketing/channels/icpro-blog/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/marketing/content-plan/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/marketing/content-plan/content-lifecycle-process.md (end-to-end cadence — read for the Drive-URL-before-CSV ordering and the weekly-session context)

(Per [PRINCIPLES.md #4](/Users/travisfoster/claude-code/cerkl/PRINCIPLES.md), this list is authoritative for this scope — parent loads do not apply unless re-listed here.)

`broadcast.md` is loaded so the rare *"tools like Cerkl Broadcast"* mention is accurate when it occurs. `competitors.md` is loaded so we know **who not to mention** — naming Simpplr/LumApps/Firstup/Workvivo/Poppulo/Staffbase/Haiilo on internalcommspro.com is forbidden.

**Parallelization fallback:** if any step is parallelizable and the runtime has the `Agent`/`Task` tool, dispatch sub-agents in one message. If not, parallelize via multiple Tool calls in a single message — same effect.

---

## Steps

### Step 1 — Load ICPro Tasks from the week's CSV

- **Owner:** Claude
- **Inputs:** [`../../content-plan/jira/imports/YYYY-Www.csv`](../../content-plan/jira/imports/) for the target week
- **Produces:** an in-memory list of ICPro posts to process, each with `{publish_date, deliverable_title, slug, iso_week, csv_path}`

**What to do:**

Parse the week's CSV (real CSV library — Descriptions contain newlines). **Row-matching rule:** `Issue Type = Task` AND `Summary` starts with `Content - Blog (ICP) -`. (The `Channel` column is `Blog Posts` for both Cerkl and ICP rows; the `(ICP)` marker in `Summary` differentiates them.)

For each matched row, read `Slug:` and the topic from the Description, and `Due Date` as the publish date. **The slug comes from the CSV** — it was synthesized once at scaffold time (see the [slug threading rule](../../content-plan/jira/CONTEXT.md#slug-threading-the-canonical-identity)); never re-derive it here.

ICPro has no brief queue — the Task Description is the source of truth for "what to write." If `Subset?` was specified, narrow the list. Confirm the list with the user before proceeding.

If the week's CSV is missing or has no ICPro row you expected: report it and ask Travis — the [weekly session](../../content-plan/weekly-content-process.md) owns row creation and can patch it; this process doesn't create rows.

Cerkl.com posts are out of scope — they have their own production path under [`../seo-blog/`](../seo-blog/).

### Step 2a — Pre-writing (per post)

- **Owner:** Claude (sub-agent per post for `n ≥ 3`; inline for `n ≤ 2`)
- **Sequencing:** parallelizable across posts
- **Needs:** [`skills/icpro-blog-pre-writing/SKILL.md`](skills/icpro-blog-pre-writing/SKILL.md)
- **Inputs:** deliverable title + publish date + slug from Step 1
- **Produces:** `blog-posts-pre-writing/YYYY-MM-DD_[slug]_pre-writing.md`

**Batch size rule:** for `n ≤ 2` posts (typical weekly batch — usually exactly 1 ICPro post per week), run inline in the orchestrator. For `n ≥ 3` (multi-week or catch-up), dispatch one sub-agent per post.

**Sub-agent brief (or inline run) must:**
- Take deliverable title, publish date, channel (icpro-blog), and pre-computed slug as inputs
- Write to `/Users/travisfoster/claude-code/cerkl/marketing/channels/icpro-blog/blog-posts-pre-writing/YYYY-MM-DD_[slug]_pre-writing.md`
- Complete every property (title, slug, keywords, category, meta, featured image brief, outline) using the 13-category list and Wix property structure in the pre-writing skill — do not invent categories or add Cerkl-style CTA tables
- Length cap: pre-writing is structured properties + outline, not prose; aim ≤300 lines
- Author defaults to `ICP Staff`

### Step 2b — Drafting (per post)

- **Owner:** Claude (sub-agent per post for `n ≥ 3`; inline for `n ≤ 2`)
- **Sequencing:** must run after that post's 2a completes; parallelizable across posts otherwise
- **Needs:** [`skills/icpro-blog-drafting/SKILL.md`](skills/icpro-blog-drafting/SKILL.md)
- **Inputs:** the pre-writing file from 2a
- **Produces:** `blog-posts-draft/YYYY-MM-DD_[slug]_draft.md`

**Sub-agent brief (or inline run) must:**
- Take the full path to the pre-writing file as input
- Write to `blog-posts-draft/YYYY-MM-DD_[slug]_draft.md`
- Hold ICPro voice (peer expert / authoritative on IC trends) — never Cerkl product copy
- **Brand-mention rules — strict:** Cerkl mentions are rare and only as *"tools like Cerkl Broadcast"* in a list context. **Never** name competitors (Simpplr, LumApps, Firstup, Workvivo, Poppulo, Staffbase, Haiilo)
- Length: 700–900 words for supporting posts; up to 1,200–2,000 for pillar pieces
- SEO bar: focus keyword in title, H1, ≥1 H2/H3, body; strict H1 → H2 → H3 nesting; direct answer in first 2 paragraphs or right after first H2
- Structure: start with H1 (post title from pre-writing), then opening paragraphs, then H2 sections. No FAQ schema block. No CTA copy (single site-wide newsletter CTA renders in Wix footer).
- Markdown only; no em-dashes; dates in `YYYY-MM-DD`

### Step 2c — Editing (per post)

- **Owner:** Claude (sub-agent per post for `n ≥ 3`; inline for `n ≤ 2`)
- **Sequencing:** must run after that post's 2b completes; parallelizable across posts otherwise
- **Needs:** [`skills/icpro-blog-editing/SKILL.md`](skills/icpro-blog-editing/SKILL.md)
- **Inputs:** the draft file from 2b
- **Produces:** `blog-posts-live/YYYY-MM-DD_[slug]_live.md` with edit log appended

**Sub-agent brief (or inline run) must:**
- Take the full path to the draft file as input
- Write to `blog-posts-live/YYYY-MM-DD_[slug]_live.md` (preserve the original date and slug)
- Not modify or delete the draft
- Exit at score ≥ 35/50 across Directness, Rhythm, Trust, Authenticity, Density
- Run the brand-mention check; append the edit log block (including brand-mention line)
- Return: live file path + final score line + brand-mention check result

Editing **does not** upload to Drive anymore — that moves to Step 2d.

### Step 2d — Publishing (per post)

- **Owner:** Claude (sub-agent per post for `n ≥ 3`; inline for `n ≤ 2`)
- **Sequencing:** must run after that post's 2c completes; parallelizable across posts otherwise
- **Needs:** [`skills/icpro-blog-publishing/SKILL.md`](skills/icpro-blog-publishing/SKILL.md)
- **Inputs:** the live file from 2c + synthesized slug + target week's CSV path (from Step 1.5)
- **Produces:** a Drive Doc URL + an updated row in the target week's Jira CSV

**Sub-agent brief (or inline run) must:**
- Take the live file path, slug, and target CSV path as inputs
- Upload the live file to Drive with `YYYY-MM-DD — ICP — <H1 title>` naming (the `ICP` segment distinguishes ICPro from Cerkl posts in the shared folder)
- Find the Task row in the target CSV (`Issue Type = Task`, `Summary` starts with `Content - Blog (ICP) -`) whose `Description` contains `Slug: <slug>` and replace `[DRIVE_URL_PLACEHOLDER]` with the actual Drive URL
- Preserve all other rows and fields; CSV must still parse cleanly
- Return: Drive Doc URL + CSV row updated confirmation + score line + brand-mention check result

Per the publishing skill: it does **not** synthesize the slug (the orchestrator passes it) and does **not** create the CSV (Monday reconcile owns that).

### Step 3 — Roll up and report

- **Owner:** Claude
- **Inputs:** return values from each 2d
- **Produces:** chat-printed summary

Print one line per post: `slug — score X/50 — brand-check <pass/fixed> — <Doc URL> — CSV row updated in YYYY-Www.csv`. Flag any post that:
- Didn't exit editing at ≥ 35/50 (human review needed)
- Required brand-mention rewrites (to spot voice drift over time)
- Failed publishing (Drive upload failed, CSV row mismatch — likely slug divergence with scaffold creator)

---

## Output

- `blog-posts-pre-writing/YYYY-MM-DD_[slug]_pre-writing.md` — one per post
- `blog-posts-draft/YYYY-MM-DD_[slug]_draft.md` — one per post (kept after editing)
- `blog-posts-live/YYYY-MM-DD_[slug]_live.md` — one per post, with edit log appended
- A Drive Doc per live file (`YYYY-MM-DD — ICP — <H1 title>` naming, Claude-Uploads folder)
- An updated Jira CSV at `../../content-plan/jira/imports/YYYY-Www.csv` — one row per ICPro post has its `[DRIVE_URL_PLACEHOLDER]` replaced with the actual URL
- A chat-printed roll-up summary

ICPro has no brief queue, so there's no `status` field to flip anywhere. The Jira task itself tracks lifecycle.

## Future work

- When internalcommspro.com starts featuring named author bylines, swap the `ICP Staff` default in the pre-writing skill for an author-selection step.
- If individual ICPro posts start using FAQ blocks (Wix supports it via custom embeds), add an FAQ section back into the drafting skill behind a per-post flag.
- If posts begin including in-body CTAs (lead magnets, downloads), add a CTA placement step to pre-writing.
- If ICPro grows enough that a brief queue becomes useful (e.g., for keyword targeting and refresh tracking), spin up `icpro-blog/briefs/` parallel to `seo/briefs/` and update this orchestrator to read from briefs the way `seo-blog-process.md` does.

## Learnings

Append "what broke / what we changed" notes here as the process matures.

- **2026-06-01 — CSV row-matching rule corrected.** Step 1.5, Step 2d sub-agent brief, and the publishing skill (pre-flight + Step 2) all instructed matching on `Channel = Blog — internalcommspro.com`. The actual Jira CSV scaffold uses `Channel = Blog Posts` for both Cerkl and ICP rows and differentiates ICP rows via the `Content - Blog (ICP) -` prefix in the `Summary` column (per [`CONTEXT.md`](CONTEXT.md#source-of-truth-for-what-to-write)). Surfaced when publishing the 2026-06-09 single-post override failed to find row T002 in 2026-W24.csv. All four match locations updated to `Issue Type = Task AND Summary starts with "Content - Blog (ICP) -" AND Description contains "Slug: <slug>"`.
