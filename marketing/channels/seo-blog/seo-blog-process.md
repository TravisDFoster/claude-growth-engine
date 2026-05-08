# Bulk SEO Blog Production

> Take a target month from the content plan and produce every blog post on the calendar — pre-writing, draft, edit — into the seo-blog channel folder. Output: one `_live.md` per post in `blog-posts-live/`, each also published to Drive.

## Trigger

- "Write the [Month YYYY] blog posts"
- "Run bulk blog production for [Month YYYY]"
- "Produce the [Month] SEO content"
- "Draft and edit every blog post for [Month YYYY]"

## Inputs

I'll ask before scaffolding:

1. **Target month** (e.g., May 2026) — used to find `monthly-content-plans/[month-year].md` and `[month-year]-jira.csv` in the content-plan folder.
2. **Subset?** — all blog posts on the plan, or a specific list of slugs.
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

### Step 1 — Load the monthly plan

- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** —
- **Inputs:** `/Users/travisfoster/claude-code/cerkl/marketing/content-plan/monthly-content-plans/[month-year].md` and `[month-year]-jira.csv`
- **Produces:** an in-memory list of cerkl.com blog posts for the month, each with `{publish_date, slug, working_title, summary}` parsed from the Jira CSV.
- **What to do:** Read both files. Filter the CSV to rows where:
  - `Channel` column = `Blog Posts`, **AND**
  - `Summary` column begins with `Content - Blog (Cerkl.com) -`
  
  This is the rule that splits cerkl.com posts from internalcommspro.com posts in a shared content plan — both have channel = "Blog Posts", but only Cerkl-branded rows carry the `(Cerkl.com)` marker. (ICPro posts use `(ICP)` and are owned by [`channels/icpro-blog/icpro-blog-process.md`](../icpro-blog/icpro-blog-process.md).)
  
  For each, extract publish date (`YYYY-MM-DD`), slug, working title, and the post summary. If `Subset?` was specified, narrow the list. Confirm the list with the user before proceeding.

### Step 2a — Pre-writing (per post)

- **Owner:** Claude (sub-agent per post — parallelizable)
- **Parallelizable with:** every other 2a instance (one per post)
- **Needs:** [`skills/seo-blog-pre-writing/SKILL.md`](skills/seo-blog-pre-writing/SKILL.md)
- **Inputs:** post summary + working title from Step 1
- **Produces:** `blog-posts-pre-writing/YYYY-MM-DD_[slug]_pre-writing.md`
- **What to do:** Dispatch one sub-agent per post. Each sub-agent loads the pre-writing skill, completes every property (title, slug, keywords, CTAs, categories, meta, outline), and writes the file.

**Sub-agent brief must say:**
- Inputs verbatim: post summary, working title, publish date, channel = seo-blog (Cerkl-branded).
- Output path: `/Users/travisfoster/claude-code/cerkl/marketing/channels/seo-blog/blog-posts-pre-writing/YYYY-MM-DD_[slug]_pre-writing.md`.
- Length cap: pre-writing is structured properties + outline, not prose; aim ≤300 lines.
- Conventions: dates in `YYYY-MM-DD`; slug lowercase-hyphenated, ≤60 chars.
- Use the property tables in the pre-writing skill verbatim — do not invent CTA or category names.

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

## Push-update protocol

Per [PRINCIPLES.md #8](/Users/travisfoster/claude-code/cerkl/PRINCIPLES.md), append an update block to `personal-assistant/projects/icpro-seo.md` (or the relevant blog project file) when bulk production completes:

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
