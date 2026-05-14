# Bulk SEO Blog Production

> Take every SEO brief scheduled for a target month — from [`../../seo/briefs/`](../../seo/briefs/), cross-referenced with [`../../content-plan/rolling-4week.md`](../../content-plan/rolling-4week.md) — and produce every blog post: pre-writing → draft → edit. Output: one `_live.md` per post in `blog-posts-live/`, each also published to Drive.

## Trigger

- "Write the [Month YYYY] blog posts"
- "Run bulk blog production for [Month YYYY]"
- "Produce the [Month] SEO content"
- "Draft and edit every blog post for [Month YYYY]"

## Inputs

I'll ask before scaffolding:

1. **Target month** (e.g., May 2026) — used to filter SEO briefs by `scheduled_for:` falling in that month.
2. **Subset?** — all scheduled briefs for the month, or a specific list of slugs.
3. **Skip Drive upload?** — default is to publish each `_live.md` to Drive; user can opt out.

**For n=1 (single-post runs):** skip the sub-agent dispatch in Steps 2a/2b/2c and run each step inline in the orchestrator's own context. The "dispatch one sub-agent per post" framing exists to parallelize across many posts; with one post, the dispatch overhead is wasted. Same skills, same prompts, same output paths — just inline.

## Context to load

- /Users/travisfoster/claude-code/cerkl/shared/icp.md
- /Users/travisfoster/claude-code/cerkl/shared/broadcast.md
- /Users/travisfoster/claude-code/cerkl/shared/competitors.md
- /Users/travisfoster/claude-code/cerkl/shared/company-info.md
- /Users/travisfoster/claude-code/cerkl/marketing/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/marketing/channels/seo-blog/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/marketing/content-plan/CONTEXT.md

(Per [PRINCIPLES.md #4](/Users/travisfoster/claude-code/cerkl/PRINCIPLES.md), this list is authoritative for this scope — parent loads do not apply unless re-listed here.)

**Parallelization fallback:** if any step is parallelizable and the runtime has the `Agent`/`Task` tool, dispatch sub-agents in one message. If not, parallelize via multiple Tool calls (e.g., `WebSearch`, `WebFetch`, `Read`) in a single message — same effect.

---

## Steps

### Step 1 — Load scheduled briefs

- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** —
- **Inputs:** [`../../seo/briefs/`](../../seo/briefs/) (the SEO brief queue) and [`../../content-plan/rolling-4week.md`](../../content-plan/rolling-4week.md)
- **Produces:** an in-memory list of seo-blog briefs scheduled for the month, each with `{brief_path, slug, scheduled_for, title, target_pillar, primary_solution}` parsed from the brief's YAML frontmatter.
- **What to do:** List files in `seo/briefs/` (exclude `_template.md` and `archive/`). Parse each file's YAML frontmatter. Filter to briefs where **all** of:
  - `target_channel: seo-blog`, **AND**
  - `status: scheduled` or `in-progress`, **AND**
  - `scheduled_for:` falls in the target month (`YYYY-MM-*`).

  Cross-check against `rolling-4week.md`: every brief surfaced should also have a row in the rolling 4-week plan whose `Source brief` column links the same brief file. Flag any discrepancy to the user (brief scheduled but not in plan, or plan row pointing at a brief whose `status` ≠ `scheduled`/`in-progress`) before proceeding.

  If `Subset?` was specified, narrow the list. Confirm the list with the user before proceeding.

  ICPro posts are out of scope — they're a separate property with their own production path under [`../icpro-blog/`](../icpro-blog/).

### Step 2a — Pre-writing (per post)

- **Owner:** Claude (sub-agent per post — parallelizable)
- **Parallelizable with:** every other 2a instance (one per post)
- **Needs:** [`skills/seo-blog-pre-writing/SKILL.md`](skills/seo-blog-pre-writing/SKILL.md) (v0.2.0+ — reads from SEO brief)
- **Inputs:** the brief path from Step 1 (one per post)
- **Produces:** `blog-posts-pre-writing/YYYY-MM-DD_[slug]_pre-writing.md`
- **What to do:** Dispatch one sub-agent per brief. Each sub-agent loads the pre-writing skill, reads the SEO brief at the given path, carries Group A properties verbatim (pillar, solution, keywords, hub link, sibling URLs, all-categories), decides Group B (CTA variants, Meta Title, Meta Description, full outline), and writes the pre-writing file. After writing, the sub-agent flips the brief's `status:` from `scheduled` to `in-progress`.

**Sub-agent brief must say:**
- Inputs verbatim: full path to the SEO brief (`/Users/travisfoster/claude-code/cerkl/marketing/seo/briefs/<slug>.md`).
- Output path: `/Users/travisfoster/claude-code/cerkl/marketing/channels/seo-blog/blog-posts-pre-writing/YYYY-MM-DD_[slug]_pre-writing.md` (use the brief's `scheduled_for:` as `YYYY-MM-DD`).
- Read the SEO brief first. Carry Group A properties verbatim — do not re-derive. Decide Group B (Top/Middle/Bottom CTA variants per the skill's CTA tables, Meta Title, Meta Description, full H1/H2/H3 outline expanding the brief's angle).
- If any Group A property in the brief is missing or contradictory, **stop and flag** — do not invent.
- Length cap: pre-writing is structured properties + outline, not prose; aim ≤300 lines.
- Conventions: dates in `YYYY-MM-DD`; slug lowercase-hyphenated, ≤60 chars.
- After writing the file, update the brief's `status:` from `scheduled` to `in-progress`.

### Step 2b — Drafting (per post)

- **Owner:** Claude (sub-agent per post — parallelizable)
- **Parallelizable with:** every other 2b instance, but **must run after that post's 2a finishes** (sequential per-post, parallel across posts).
- **Needs:** [`skills/seo-blog-drafting/SKILL.md`](skills/seo-blog-drafting/SKILL.md)
- **Inputs:** the post's pre-writing file from 2a
- **Produces:** `blog-posts-draft/YYYY-MM-DD_[slug]_draft.md`
- **What to do:** Dispatch one sub-agent per post. Each sub-agent loads the drafting skill, reads its pre-writing file, researches the topic if needed, and writes the full markdown draft.

**Sub-agent brief must say:**
- Inputs verbatim: full path to the pre-writing file.
- Output path: `/Users/travisfoster/claude-code/cerkl/marketing/channels/seo-blog/blog-posts-draft/YYYY-MM-DD_[slug]_draft.md`.
- Voice: Cerkl voice (practical, direct, zero-fluff) per the drafting skill — never blend with partner or generic B2B voice.
- Length: match the post type (supporting 1,000–1,500 words; pillar 2,000–3,000). Don't pad for word count.
- SEO bar: focus keyword in title, H1, ≥1 H2/H3, body. Strict H1 → H2 → H3 nesting. Direct answer in first 2 paragraphs or right after first H2.
- Structure: emit the 7-section structure from the drafting skill; do **not** generate Top/Middle/Bottom CTA copy (placeholders only).
- Conventions: dates `YYYY-MM-DD`; markdown only; no em-dashes.

### Step 2c — Editing (per post)

- **Owner:** Claude (sub-agent per post — parallelizable)
- **Parallelizable with:** every other 2c instance, but **must run after that post's 2b finishes**.
- **Needs:** [`skills/seo-blog-editing/SKILL.md`](skills/seo-blog-editing/SKILL.md)
- **Inputs:** the post's draft file from 2b
- **Produces:** `blog-posts-live/YYYY-MM-DD_[slug]_live.md` plus a Drive Doc URL
- **What to do:** Dispatch one sub-agent per post. Each runs the full editing process (structural pass → rewrite → line edit → score), exits at ≥ 35/50, writes the live file with edit log, and uploads to Drive (unless `Skip Drive upload` was set).

**Sub-agent brief must say:**
- Inputs verbatim: full path to the draft file.
- Output path: `/Users/travisfoster/claude-code/cerkl/marketing/channels/seo-blog/blog-posts-live/YYYY-MM-DD_[slug]_live.md`. Preserve the original date and slug.
- Do not modify or delete the draft.
- Exit condition: 35/50 across Directness, Rhythm, Trust, Authenticity, Density.
- Append the edit log block specified in the editing skill.
- Drive upload: invoke `/Users/travisfoster/claude-code/cerkl/skills/md-to-drive/SKILL.md` with the live file, default destination, edit-log strip recipe applied. Skip only if user opted out at Step 1.
- Return: live file path + Doc URL + final score line.

### Step 3 — Roll up and report

- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** —
- **Inputs:** sub-agent return values from each 2c
- **Produces:** chat-printed summary
- **What to do:** Print one line per post: `slug — score X/50 — <Doc URL>`. Flag any post that didn't exit 35/50 (those should be flagged for human review, not silently shipped).

---

## Output

- `blog-posts-pre-writing/YYYY-MM-DD_[slug]_pre-writing.md` — one per post
- `blog-posts-draft/YYYY-MM-DD_[slug]_draft.md` — one per post (kept after editing)
- `blog-posts-live/YYYY-MM-DD_[slug]_live.md` — one per post, with edit log appended
- A Drive Doc per live file (Claude-Uploads folder, `YYYY-MM-DD — <H1 title>` naming)
- A chat-printed roll-up summary
- Each brief's `status:` is `in-progress` after Step 2a runs. **Do not flip to `shipped` here** — that happens when the post actually goes live in Webflow, after Travis copies the Drive Doc over. The planner archives shipped briefs on the next Monday reconcile.

## Push-update protocol

Per [PRINCIPLES.md #8](/Users/travisfoster/claude-code/cerkl/PRINCIPLES.md), append an update block to `personal-assistant/projects/seo-strategy-plan.md` (or the relevant blog project file — no dedicated `cerkl-blog.md` PA project exists yet) when bulk production completes:

```
## Update — YYYY-MM-DD (from marketing/channels/seo-blog/)
- Completed: [Month YYYY] bulk blog production — N posts shipped
- Status change: <if any, otherwise "none">
- New blocker: <if any, otherwise "none">
- Proposed next step: <one line>
```

## Future work

- Promote the per-post sequential chain (2a → 2b → 2c) into a sub-process file when ICPro-blog comes online and we need to share orchestration logic. For now the linear within-post flow is short enough to keep inline.
- When `seo-blog-pre-writing-guide.md` evolves into per-post research lookups (e.g., SERP intent, competitor coverage), consider splitting Step 2a into 2a-research + 2a-properties.

## Learnings

Append "what broke / what we changed" notes here as the process matures.
