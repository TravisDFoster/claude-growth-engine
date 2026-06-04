# Weekly LinkedIn Production

> Take every LinkedIn row scheduled for the locked week of [`../../content-plan/rolling-4week.md`](../../content-plan/rolling-4week.md) and draft each post. Output: one `.md` per post in `drafts/`, with the copy inserted into the matching `Copy` subtask of that week's Jira CSV at [`../../content-plan/jira/imports/YYYY-Www.csv`](../../content-plan/jira/).

## Trigger

**Default (weekly):**
- "Write next week's LinkedIn posts"
- "Run weekly LinkedIn production"
- "Draft Week 1 LinkedIn"

**Overrides:**
- *Single post:* `"Draft this week's carousel"`, `"Write the [topic] poll"` — operates on one row by post type or by source slug
- *Multi-week:* `"Draft weeks 1-2 LinkedIn"` — pulls all LinkedIn rows from multiple weeks

## Inputs

I'll ask before drafting:

1. **Target window** — defaults to Week 1 (locked) of rolling-4week. Can be overridden with a single post or multiple weeks.
2. **Subset?** — within the target window, all LinkedIn rows or a specific list.

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

### Step 1 — Load LinkedIn rows for the target window

- **Owner:** Claude
- **Inputs:** [`../../content-plan/rolling-4week.md`](../../content-plan/rolling-4week.md), the resolved target window
- **Produces:** an in-memory list of LinkedIn rows: `{post_type, working_title, publish_date, owner, source_pointer, iso_week}`

Filter rows where `Channel` contains "LinkedIn" and `Publish` falls within the target window. Map the `Channel` string to the type slug:

| `Channel` string | Type slug |
|---|---|
| LinkedIn carousel | `carousel` |
| LinkedIn static/theme | `static-theme` |
| LinkedIn static/blog | `static-blog` |
| LinkedIn poll | `poll` |
| LinkedIn short video | `short-video` |

The `Source brief` column points at what the post wraps. Confirm the resolved list with the user before proceeding.

### Step 2 — Load the wrapped source

- **Owner:** Claude
- **Inputs:** Each row's `Source brief` pointer
- **Produces:** Loaded context for the source asset

Typical sources:
- **Blog (cerkl.com):** read the `_live.md` from `channels/seo-blog/blog-posts-live/` (or the brief from `seo/briefs/` if pre-publish)
- **ICP blog:** read the equivalent from `channels/icpro-blog/`
- **Webinar:** read the brief from the event folder under `channels/webinar/`
- **Press release:** read from `channels/newsroom-pr/`

If multiple posts wrap the same source (typical for blog-wrap weeks), load it once.

### Step 3 — Verify Jira CSV has LinkedIn Task rows

- **Owner:** Claude
- **Inputs:** Each post's `iso_week` and working title
- **Produces:** Verified `{post → CSV Copy-subtask row}` mappings

For each post, confirm the week's CSV at `../../content-plan/jira/imports/YYYY-Www.csv` has a Task row whose Summary matches the LinkedIn deliverable, whose Description contains a `[COPY_PLACEHOLDER]` token (on its `Copy:` line).

**If any LinkedIn Task row is missing:** stop and surface the gap. This process does not create CSV rows — Monday reconcile owns that.

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
- Caption (the text above the asset)
- Asset spec or content (slide copy for carousels; poll question + options; image direction for statics; video script for video)
- Hashtags

### Step 5 — Insert copy into the Jira CSV

- **Owner:** Claude
- **Inputs:** Draft file path + target CSV path + the matching LinkedIn Task row
- **Produces:** Updated CSV Task Description

For each draft, find the Task row in the target week's CSV whose Summary matches the LinkedIn deliverable. Replace `[COPY_PLACEHOLDER]` in that **Task's** Description (on its `Copy:` line) with the draft contents (caption + asset spec + hashtags). The `LinkedIn – Copy` subtask stays as the plain production step — don't write copy into it.

Use a real CSV library (Python `csv`, or equivalent) — Description fields contain newlines.

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

- `drafts/YYYY-MM-DD_[type]_[slug].md` — one per post
- An updated Jira CSV at `../../content-plan/jira/imports/YYYY-Www.csv` with the LinkedIn Task Description filled in (copy inserted on the `Copy:` line) for each post
- A chat-printed roll-up

## Push-update protocol

Per [PRINCIPLES.md #8](/Users/travisfoster/claude-code/cerkl/PRINCIPLES.md), append an update block to the relevant project file in `personal-assistant/projects/` when weekly LinkedIn production completes:

```
## Update — YYYY-MM-DD (from marketing/channels/linkedin/)
- Completed: Week N (YYYY-MM-DD – YYYY-MM-DD) LinkedIn production — N posts drafted, N CSV rows updated in YYYY-Www.csv
- Status change: <if any, otherwise "none">
- New blocker: <if any, otherwise "none">
- Proposed next step: <one line>
```

## Future work

- **Per-post-type templates need depth.** Carousel is the most fleshed out (from 2026-05-20 work). The other 4 (static-theme, static-blog, poll, short-video) are skeletons. Refine after each runs.
- **Voice divergence.** LinkedIn voice currently matches blog voice exactly. Revisit after 2–3 weeks.
- **Archive automation.** Once a draft's CSV row is filled and the post publishes, move the draft to `archive/`. Manual move for now.
- **Per-type drafting skills.** If a particular type (e.g., carousel) develops Cerkl-specific drafting complexity, extract it into `skills/linkedin-carousel/SKILL.md`. Today the templates + this process are enough.

## Learnings

- 2026-05-21 — Monday reconcile now scaffolds LinkedIn Tasks + 4 social-media subtasks by default, with `Post type` lines on the Task and `[COPY_PLACEHOLDER]` tokens on the `LinkedIn – Copy` subtask. Step 3 no longer blocks on a hand-rolled fallback. Starts clean from the next reconcile (W23); W21/W22 stay on their hand-rolled state.
- 2026-05-28 — Moved the `[COPY_PLACEHOLDER]` / drafted copy from the `LinkedIn – Copy` subtask to the parent Task Description (a `Copy:` line) so the caption + asset spec + hashtags are visible on the card itself; the Copy subtask reverts to a plain production step. Applied retroactively to W23's LinkedIn Tasks.
