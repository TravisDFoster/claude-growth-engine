# Weekly LinkedIn Production

> Take every LinkedIn Task in the target week's Jira CSV ([`../../content-plan/jira/imports/YYYY-Www.csv`](../../content-plan/jira/)) and draft each post. Usually invoked by the [weekly content session](../../content-plan/weekly-content-process.md) (Phase 3). Output: one `.md` per post in `drafts/`, with the copy inserted into the matching Task's `Copy:` line in the CSV.

## Trigger

**Default (weekly):**
- "Write next week's LinkedIn posts"
- "Run weekly LinkedIn production"
- "Draft this week's LinkedIn"

**Overrides:**
- *Single post:* `"Draft this week's carousel"`, `"Write the [topic] poll"` — operates on one row by post type or by source slug
- *Multi-week:* `"Draft LinkedIn for the next 2 weeks"` — pulls LinkedIn Tasks from multiple weekly CSVs

## Inputs

1. **Target week** — defaults to the next publish week (or the week the session just scaffolded).
2. **Subset?** — within the target week, all LinkedIn Tasks or a specific list.

## Context to load

- /Users/travisfoster/claude-code/cerkl/shared/icp.md
- /Users/travisfoster/claude-code/cerkl/shared/broadcast.md
- /Users/travisfoster/claude-code/cerkl/shared/company-info.md
- /Users/travisfoster/claude-code/cerkl/marketing/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/marketing/channels/linkedin/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/marketing/channels/linkedin/linkedin-writing-guide.md

(Per [PRINCIPLES.md #4](/Users/travisfoster/claude-code/cerkl/PRINCIPLES.md), this list is authoritative for this scope.)

---

## Steps

### Step 1 — Load LinkedIn Tasks from the week's CSV

- **Owner:** Claude
- **Inputs:** [`../../content-plan/jira/imports/YYYY-Www.csv`](../../content-plan/jira/) for the target week
- **Produces:** an in-memory list of LinkedIn posts: `{post_type, working_title, publish_date, wraps, iso_week, task_summary}`

Parse the CSV (real CSV library — Descriptions contain newlines). Take every Task row whose `Channel` is Social Media / Summary starts with `Social Media - LinkedIn`, excluding barebones short-video rows. From each Task Description, read `Post type:` (the type slug: `carousel`, `static-theme`, `static-blog`, `poll`) and `Wraps: <blog-slug>` (what the post wraps); the `Copy:` line should carry `[COPY_PLACEHOLDER]`.

If a post you expected is missing from the CSV, report it and ask Travis — the [weekly session](../../content-plan/weekly-content-process.md) owns row creation and can patch it; this process doesn't create rows. Posts whose `Copy:` is already filled: skip (or confirm a re-draft).

Confirm the resolved list with the user before proceeding.

### Step 2 — Load the wrapped source

- **Owner:** Claude
- **Inputs:** Each post's `Wraps:` pointer
- **Produces:** Loaded context for the source asset

Typical sources:
- **Blog (cerkl.com):** read the `_live.md` from `channels/seo-blog/blog-posts-live/` (or the brief from `seo/briefs/` if pre-publish)
- **ICP blog:** read the equivalent from `channels/icpro-blog/`
- **Webinar:** read the brief from the event folder under `channels/webinar/`
- **Press release:** read from `channels/newsroom-pr/`

If multiple posts wrap the same source (typical for blog-wrap weeks), load it once.

### Step 4 — Draft each post

- **Owner:** Claude (sub-agent per post for `n ≥ 3`; inline for `n ≤ 2`)
- **Sequencing:** Parallelizable across posts
- **Inputs:** Row metadata from Step 1, wrapped source from Step 2, template from [`templates/`](templates/)
- **Produces:** `drafts/YYYY-MM-DD_[type]_[slug].md`

For each post:

1. Open the matching template from `templates/` based on the type slug
2. Read the wrapped source (already loaded in Step 2)
3. Fill the template, holding Cerkl voice per [`linkedin-writing-guide.md`](linkedin-writing-guide.md)
4. Write to `drafts/YYYY-MM-DD_[type]_[slug].md` using the publish date and a kebab-case slug (≤60 chars)

The draft is the source of truth. It contains:
- Caption (the text above the asset, including any destination link)
- Asset spec or content (slide copy for carousels; poll question + options; image direction for statics; video script for video)

### Step 4.5 — Edit each post

- **Owner:** Claude (sub-agent per post for `n ≥ 3`; inline for `n ≤ 2` — same dispatch rule as Step 4)
- **Sequencing:** must run after that post's Step 4 completes; parallelizable across posts
- **Needs:** [`skills/linkedin-editing/SKILL.md`](skills/linkedin-editing/SKILL.md)
- **Inputs:** the draft file from Step 4
- **Produces:** the same draft, edited in place, with a `## Edit log` block appended

Run `linkedin-editing` on each draft: two passes (hook/tightness, then the hard compliance gate) plus the scaled score. This is a **separate pass from drafting on purpose** — the guardrails in [`linkedin-writing-guide.md`](linkedin-writing-guide.md) only bite when a fresh check enforces them, instead of the drafter self-grading. The compliance gate (no hashtags, link in the caption not the comments, no em-dashes, no banned adverbs, no binary contrasts) must fully pass before the copy is eligible for Step 5. A draft that can't clear the gate is surfaced, not inserted.

### Step 5 — Insert copy into the Jira CSV

- **Owner:** Claude
- **Inputs:** Draft file path + target CSV path + the matching LinkedIn Task row
- **Produces:** Updated CSV Task Description

For each draft, update the Task row it was loaded from in Step 1 (matched by `Post type:` + `Wraps:` in the Description — not by free-text Summary). Replace `[COPY_PLACEHOLDER]` in that **Task's** Description (on its `Copy:` line) with the draft contents (caption + asset spec). The `LinkedIn – Copy` subtask stays as the plain production step — don't write copy into it.

Use a real CSV library (Python `csv`, or equivalent) — Description fields contain newlines.

**Invocation modes:** when this runs as a Wave subagent inside the weekly content session, do **not** edit the CSV — return the values (the orchestrator fills all tokens in one pass). Only edit the CSV directly when running standalone (single writer either way).

### Step 6 — Roll up and report

- **Owner:** Claude
- **Produces:** Chat-printed summary + next-step suggestion

Print one line per post: `[type] [slug] — drafts/YYYY-MM-DD_[type]_[slug].md → CSV Task Description updated in YYYY-Www.csv`. Flag any post that:
- Couldn't find a matching CSV Task row (scaffold gap — surface back to Travis)
- Couldn't find a matching template (post type not yet templated — future work)

After the roll-up, walk the drafted posts and classify each by asset-route (matches [`linkedin-asset-process.md`](linkedin-asset-process.md) Step 1):

- **`render`** — `carousel` or `static-theme` not wrapping a webinar → needs `linkedin-asset-process.md` to scaffold a manifest + dispatch `template-fill`
- **`webinar-lookup`** — any type wrapping a webinar event folder → needs `linkedin-asset-process.md` to look up the rendered URL from the webinar's `canva-manifests/` (no render)
- **`skip-*`** — `static-blog` (LinkedIn auto-renders link card), `poll` (native widget), `short-video` (video pipeline)

If any post is `render` or `webinar-lookup`, suggest running `linkedin-asset-process.md` next, naming the eligible slugs and which route each falls into. Use this phrasing:

> Next: run `linkedin-asset-process.md` with `commit_mode: auto` to render Canva assets for:
> - **Render** (template-fill dispatch): `<slug1>`, `<slug2>`
> - **Webinar lookup**: `<slug3>` (from `<webinar-event-folder>`)
>
> Skipped this week: `<slug4>` (static-blog), `<slug5>` (poll).

If every drafted post is `skip-*`, no asset process needed — the roll-up ends here.

---

## Output

- `drafts/YYYY-MM-DD_[type]_[slug].md` — one per post, each carrying a `## Edit log` (compliance gate + score) after Step 4.5
- An updated Jira CSV at `../../content-plan/jira/imports/YYYY-Www.csv` with the LinkedIn Task Description filled in (copy inserted on the `Copy:` line) for each post — only copy that cleared the Step 4.5 compliance gate
- A chat-printed roll-up

## Future work

- **Per-post-type templates need depth.** Carousel is the most fleshed out. The other 4 (static-theme, static-blog, poll, short-video) are skeletons. Refine after each runs.
- **Voice divergence.** LinkedIn voice matches blog voice. Revisit if a distinct LinkedIn voice becomes warranted.
- **Archive automation.** Once a draft's CSV row is filled and the post publishes, move the draft to `archive/`. Manual move for now.
- **Per-type drafting skills.** If a particular type (e.g., carousel) develops Cerkl-specific drafting complexity, extract it into `skills/linkedin-carousel/SKILL.md`. Today the templates + this process are enough.
