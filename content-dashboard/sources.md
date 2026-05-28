# Content Dashboard — Source Registry

Authoritative list of what the content dashboard surfaces. The refresh process reads this file, scans/parses declared sources, and regenerates `data.json`.

**Convention**: filename + folder parsing where possible. Three declared exceptions to the parse-only rule (read contents):

1. **Brief frontmatter** — read `status:` (and `title:`, `scheduled_for:`) only. No body content.
2. **Rolling 4-week markdown tables** — parse the table rows under each `## Week N` heading.
3. **Jira import CSVs** — parse rows to count Drive URLs filled and LinkedIn copy filled vs placeholders.

Everything else is filename-parsed (blog post state from folder + filename suffix).

---

## Sources

### Source order

`jira-imports` first (it's the spine and the end goal), then `rolling-4week`, briefs, blog posts, and the derived `linkedin` view.

### rolling-4week
- **path**: `/Users/travisfoster/claude-code/cerkl/marketing/content-plan/rolling-4week.md`
- **parser**: markdown-table
- **sections**:
  - `## Carryover from prior week (in flight)` → `carryover[]`
  - `## Week 1 — …` → `weeks[0]` (also surfaces as `this_week` since W1 is locked)
  - `## Week 2 — …` → `weeks[1]`
  - `## Week 3 — …` → `weeks[2]`
  - `## Week 4 — …` → `weeks[3]`
- **columns** (table header order, in this file's convention): `Deliverable | Channel | Publish | Owner | Status | Source brief`
- **brief link**: when `Source brief` cell contains a markdown link `[slug](../seo/briefs/slug.md)`, capture the slug and rewrite the URL to `/cerkl/marketing/seo/briefs/<slug>.md`. When it contains plain text (`wraps leadership-story blog`, `—`, `**needs brief from SEO by 2026-05-22**`), keep as text.
- **last_reconciled**: parse the line `**Last reconciled:** YYYY-MM-DD` near the top.

### briefs
- **path**: `/Users/travisfoster/claude-code/cerkl/marketing/seo/briefs/`
- **match**: `*.md`
- **exclude**: `_template.md`, `*-process.md`
- **parser**: yaml-frontmatter
- **read fields**: `title`, `status`, `scheduled_for`, `slug`, `target_channel`
- **buckets** (by `status:` value): `queued` · `scheduled` · `in-progress` · `shipped`
- **dashboard shows**: `queued`, `scheduled`, `in-progress` only (shipped briefs hidden; they're effectively archived once live).

### seo-blog-posts
- **label**: Cerkl Blog (cerkl.com)
- **subtitle**: Webflow · primary growth channel
- **paths**:
  - `pre_writing`: `/Users/travisfoster/claude-code/cerkl/marketing/channels/seo-blog/blog-posts-pre-writing/` (match: `*_pre-writing.md`)
  - `draft`: `/Users/travisfoster/claude-code/cerkl/marketing/channels/seo-blog/blog-posts-draft/` (match: `*_draft.md`; exclude: `archive/**`)
  - `live`: `/Users/travisfoster/claude-code/cerkl/marketing/channels/seo-blog/blog-posts-live/` (match: `*_live.md`)
- **title parser**: filename pattern is `YYYY-MM-DD_slug-with-dashes_state.md` (or `TBD_slug_state.md`). Strip the leading `YYYY-MM-DD_` (or `TBD_`) and the trailing `_state`, replace `-` with space, title-case. State is folder-derived (not parsed from filename).
- **new_run_prompt**:
  ```
  Draft this week's planned Cerkl blog post(s) for cerkl.com.

  Check the rolling 4-week plan: /Users/travisfoster/claude-code/cerkl/marketing/content-plan/rolling-4week.md
  Process: /Users/travisfoster/claude-code/cerkl/marketing/channels/seo-blog/seo-blog-process.md
  ```

### icpro-blog-posts
- **label**: Internal Comms Pro (internalcommspro.com)
- **subtitle**: Wix · ICP-aligned secondary
- **paths**:
  - `pre_writing`: `/Users/travisfoster/claude-code/cerkl/marketing/channels/icpro-blog/blog-posts-pre-writing/` (match: `*_pre-writing.md`)
  - `draft`: `/Users/travisfoster/claude-code/cerkl/marketing/channels/icpro-blog/blog-posts-draft/` (match: `*_draft.md`)
  - `live`: `/Users/travisfoster/claude-code/cerkl/marketing/channels/icpro-blog/blog-posts-live/` (match: `*_live.md`)
- **title parser**: same as `seo-blog-posts`.
- **new_run_prompt**:
  ```
  Draft this week's planned Internal Comms Pro blog post(s) for internalcommspro.com.

  Check the rolling 4-week plan: /Users/travisfoster/claude-code/cerkl/marketing/content-plan/rolling-4week.md
  Process: /Users/travisfoster/claude-code/cerkl/marketing/channels/icpro-blog/icpro-blog-process.md
  ```

### linkedin
- **derivation**: read-only from `rolling-4week` rows whose `Channel` cell starts with `LinkedIn` (any variant: `LinkedIn poll`, `LinkedIn static/theme`, `LinkedIn static/blog`, `LinkedIn short video`, `LinkedIn carousel`).
- **buckets**: rows are bucketed by `Status` column → `planned` · `in-progress` · `shipped` · `pulled` · `blocked`.
- **dashboard shows**: planned · in-progress · shipped (pulled / blocked are kept off the main view but counted in `stats`).
- **notes**: LinkedIn has no per-post artifact on disk today, so there's nothing to filename-parse. If a `linkedin/posts-{state}/` folder convention is adopted later, add it as its own source and the dashboard will absorb it (the rolling-4week derivation can stay as the fallback / source-of-truth for scheduled rows that don't have draft files yet).

### jira-imports
- **path**: `/Users/travisfoster/claude-code/cerkl/marketing/content-plan/jira/imports/`
- **match**: `*.csv`
- **parser**: csv-rows
- **filename → week**: `YYYY-Www.csv` → ISO publish week. Compute `week_monday` (Monday date of that ISO week) and `week_range` (Mon → Fri).
- **status inference** (date-based, no separate state file):
  - `imported` — `today >= week_monday` (publish week has started; Travis has presumably imported it)
  - `ready-to-import` — `today < week_monday` AND every blog Task has a real Drive URL AND every `LinkedIn – Copy` subtask has filled copy
  - `in-prep` — otherwise
- **per-row counts** (parse the CSV; respect quoted multi-line cells):
  - **Tasks**: rows where `Issue Type = Task`. Classify by Summary prefix:
    - `Content - Blog (Cerkl.com) -…` → `cerkl_blog`
    - `Content - Blog (ICP) -…` → `icpro_blog`
    - `Social Media - LinkedIn -…` → `linkedin`
  - **Drive URL fill** (blog Tasks only): count Description blocks containing `[DRIVE_URL_PLACEHOLDER]` vs an actual `https://docs.google.com/...` URL on the `Draft (Google Doc):` line.
  - **LinkedIn copy fill** (LinkedIn Tasks only): the post copy lives in the LinkedIn **Task** Description under a `Copy:` section (`[CAPTION]` / `[POLL]`, `[ASSET SPEC]`, `[HASHTAGS]`). A Task counts as copy-drafted when its Description has a `Copy:` line and no remaining `[COPY_PLACEHOLDER]`. Count filled vs. total LinkedIn Tasks. The `LinkedIn – Copy` subtask is a Jira workflow step, **not** where copy is stored — don't read it for readiness.
- **import_ready**: `true` iff both fill ratios are 100%.
- **what the dashboard shows**: each CSV gets a card (filename, week, status badge, readiness bars). The "current" CSV (the most recent one whose `week_monday` is today or in the future) is featured. Past CSVs appear in a compact "Recent CSVs" strip.
- **notes**: this is the dashboard's primary handoff signal — the Jira CSV is the end-goal artifact of the content-plan system. Don't try to mutate CSVs from the dashboard; the dashboard is read-only on them. Mutations happen via the channel writing pipelines (which fill Drive URLs) and the LinkedIn drafting process (which fills `[COPY_PLACEHOLDER]`).

---

## Refresh trigger phrases

Routed via `cerkl/CLAUDE.md`:

- "Refresh my content dashboard" / "Refresh the content dashboard"
- "Update my content dashboard" / "Update the content dashboard"
- "Sync the content dashboard"
- "Rebuild the content dashboard"

---

## Future work

- LinkedIn `posts-{draft,live}/` state convention — would mirror the blog channels; until then we derive from rolling-4week.
- "Wraps X blog" backlinks — if a LinkedIn row says `wraps leadership-story blog`, the dashboard could resolve that to the actual brief slug and show the LinkedIn rows clustered under their parent blog post. Useful but more parsing logic.
- Brief tier / channel filters — the registry already declares `tier` and `target_channel` on briefs; could surface as facets in the Briefs zone.
- Diff against previous refresh — persist `data.previous.json` to power a "what changed since last refresh" summary.
