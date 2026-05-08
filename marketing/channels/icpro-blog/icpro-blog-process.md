# Bulk ICPro Blog Production

> Take a target month from the content plan and produce every Internal Comms Pro (internalcommspro.com) blog post on the calendar — pre-writing, draft, edit — into the icpro-blog channel folder. Output: one `_live.md` per post in `blog-posts-live/`, each also published to Drive with `ICP` in the filename.

## Trigger

- "Write the [Month YYYY] ICPro blog posts"
- "Run bulk ICP production for [Month YYYY]"
- "Produce the [Month] internalcommspro.com content"
- "Draft and edit every ICPro post for [Month YYYY]"

## Inputs

I'll ask before scaffolding:

1. **Target month** (e.g., May 2026) — used to find `monthly-content-plans/[month-year].md` and `[month-year]-jira.csv` in the content-plan folder.
2. **Subset?** — all ICPro posts on the plan, or a specific list of slugs.
3. **Skip Drive upload?** — default is to publish each `_live.md` to Drive; user can opt out.

**For n=1 (single-post runs):** skip the sub-agent dispatch in Steps 2a/2b/2c and run each step inline in the orchestrator's own context. The "dispatch one sub-agent per post" framing exists to parallelize across many posts; with one post, the dispatch overhead is wasted. Same skills, same prompts, same output paths — just inline.

## Context to load

- /Users/travisfoster/claude-code/cerkl/shared/icp.md
- /Users/travisfoster/claude-code/cerkl/shared/broadcast.md
- /Users/travisfoster/claude-code/cerkl/shared/competitors.md
- /Users/travisfoster/claude-code/cerkl/shared/company-info.md
- /Users/travisfoster/claude-code/cerkl/marketing/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/marketing/channels/icpro-blog/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/marketing/content-plan/CONTEXT.md

(Per [PRINCIPLES.md #4](/Users/travisfoster/claude-code/cerkl/PRINCIPLES.md), this list is authoritative for this scope — parent loads do not apply unless re-listed here.)

`broadcast.md` is loaded so the rare *"tools like Cerkl Broadcast"* mention is accurate when it occurs. `competitors.md` is loaded so we know **who not to mention** — naming Simpplr/LumApps/Firstup/Workvivo/Poppulo/Staffbase/Haiilo on internalcommspro.com is forbidden.

**Parallelization fallback:** if any step is parallelizable and the runtime has the `Agent`/`Task` tool, dispatch sub-agents in one message. If not, parallelize via multiple Tool calls in a single message — same effect.

---

## Steps

### Step 1 — Load the monthly plan and filter for ICPro

- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** —
- **Inputs:** `/Users/travisfoster/claude-code/cerkl/marketing/content-plan/monthly-content-plans/[month-year].md` and `[month-year]-jira.csv`
- **Produces:** an in-memory list of ICPro blog posts for the month, each with `{publish_date, slug, working_title, summary}` parsed from the Jira CSV.
- **What to do:** Read both files. Filter the CSV to rows where:
  - `Channel` column = `Blog Posts`, **AND**
  - `Summary` column begins with `Content - Blog (ICP) -`
  
  This is the rule that splits ICPro posts from Cerkl posts in a shared content plan — both have channel = "Blog Posts", but only ICPro rows carry the `(ICP)` marker. (Cerkl posts use `(Cerkl.com)`.)
  
  For each, extract publish date (`YYYY-MM-DD`), slug, working title, and the post summary. If `Subset?` was specified, narrow the list. Confirm the list with the user before proceeding.

### Step 2a — Pre-writing (per post)

- **Owner:** Claude (sub-agent per post — parallelizable)
- **Parallelizable with:** every other 2a instance (one per post)
- **Needs:** [`skills/icpro-blog-pre-writing/SKILL.md`](skills/icpro-blog-pre-writing/SKILL.md)
- **Inputs:** post summary + working title from Step 1
- **Produces:** `blog-posts-pre-writing/YYYY-MM-DD_[slug]_pre-writing.md`
- **What to do:** Dispatch one sub-agent per post. Each sub-agent loads the pre-writing skill, completes every property (title, slug, keywords, category, meta, featured image brief, outline), and writes the file.

**Sub-agent brief must say:**
- Inputs verbatim: post summary, working title, publish date, channel = icpro-blog (internalcommspro.com).
- Output path: `/Users/travisfoster/claude-code/cerkl/marketing/channels/icpro-blog/blog-posts-pre-writing/YYYY-MM-DD_[slug]_pre-writing.md`.
- Length cap: pre-writing is structured properties + outline, not prose; aim ≤300 lines.
- Conventions: dates in `YYYY-MM-DD`; slug lowercase-hyphenated, ≤60 chars.
- Use the 13-category list and Wix property structure in the pre-writing skill verbatim — do not invent categories or add Cerkl-style CTA tables.
- Author defaults to `ICP Staff`.

### Step 2b — Drafting (per post)

- **Owner:** Claude (sub-agent per post — parallelizable)
- **Parallelizable with:** every other 2b instance, but **must run after that post's 2a finishes** (sequential per-post, parallel across posts).
- **Needs:** [`skills/icpro-blog-drafting/SKILL.md`](skills/icpro-blog-drafting/SKILL.md)
- **Inputs:** the post's pre-writing file from 2a
- **Produces:** `blog-posts-draft/YYYY-MM-DD_[slug]_draft.md`
- **What to do:** Dispatch one sub-agent per post. Each sub-agent loads the drafting skill, reads its pre-writing file, researches the topic if needed, and writes the full markdown draft.

**Sub-agent brief must say:**
- Inputs verbatim: full path to the pre-writing file.
- Output path: `/Users/travisfoster/claude-code/cerkl/marketing/channels/icpro-blog/blog-posts-draft/YYYY-MM-DD_[slug]_draft.md`.
- Voice: ICPro voice (peer expert / authoritative on IC trends) per the drafting skill — never Cerkl product copy.
- **Brand-mention rules — strict:** Cerkl mentions are rare and only as *"tools like Cerkl Broadcast"* in a list context. **Never** name competitors (Simpplr, LumApps, Firstup, Workvivo, Poppulo, Staffbase, Haiilo).
- Length: 700–900 words for supporting posts; up to 1,200–2,000 for pillar pieces — match length to topic.
- SEO bar: focus keyword in title, H1, ≥1 H2/H3, body. Strict H1 → H2 → H3 nesting. Direct answer in first 2 paragraphs or right after first H2.
- Structure: start with the H1 (the post title from the pre-writing file), then opening paragraphs, then H2 sections. No FAQ schema block. No CTA copy (single site-wide newsletter CTA renders in Wix footer).
- Conventions: dates `YYYY-MM-DD`; markdown only; no em-dashes.

### Step 2c — Editing (per post)

- **Owner:** Claude (sub-agent per post — parallelizable)
- **Parallelizable with:** every other 2c instance, but **must run after that post's 2b finishes**.
- **Needs:** [`skills/icpro-blog-editing/SKILL.md`](skills/icpro-blog-editing/SKILL.md)
- **Inputs:** the post's draft file from 2b
- **Produces:** `blog-posts-live/YYYY-MM-DD_[slug]_live.md` plus a Drive Doc URL
- **What to do:** Dispatch one sub-agent per post. Each runs the full editing process (structural pass → rewrite → line edit → score), exits at ≥ 35/50, writes the live file with edit log, and uploads to Drive (unless `Skip Drive upload` was set).

**Sub-agent brief must say:**
- Inputs verbatim: full path to the draft file.
- Output path: `/Users/travisfoster/claude-code/cerkl/marketing/channels/icpro-blog/blog-posts-live/YYYY-MM-DD_[slug]_live.md`. Preserve the original date and slug.
- Do not modify or delete the draft.
- Exit condition: 35/50 across Directness, Rhythm, Trust, Authenticity, Density.
- Append the edit log block specified in the editing skill — including the brand-mention check line.
- Drive upload: invoke `/Users/travisfoster/claude-code/cerkl/skills/md-to-drive/SKILL.md` with the live file, default destination, edit-log strip recipe applied, and **`YYYY-MM-DD — ICP — <H1 title>` naming convention** (the `ICP` segment is required to distinguish ICPro posts from Cerkl posts in the shared Claude-Uploads folder). Skip only if user opted out at Step 1.
- Return: live file path + Doc URL + final score line.

### Step 3 — Roll up and report

- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** —
- **Inputs:** sub-agent return values from each 2c
- **Produces:** chat-printed summary
- **What to do:** Print one line per post: `slug — score X/50 — <Doc URL>`. Flag any post that didn't exit 35/50 and any post where the brand-mention check required rewrites (so we can spot voice drift over time).

---

## Output

- `blog-posts-pre-writing/YYYY-MM-DD_[slug]_pre-writing.md` — one per post
- `blog-posts-draft/YYYY-MM-DD_[slug]_draft.md` — one per post (kept after editing)
- `blog-posts-live/YYYY-MM-DD_[slug]_live.md` — one per post, with edit log appended
- A Drive Doc per live file (Claude-Uploads folder, `YYYY-MM-DD — ICP — <H1 title>` naming)
- A chat-printed roll-up summary

## Push-update protocol

Per [PRINCIPLES.md #8](/Users/travisfoster/claude-code/cerkl/PRINCIPLES.md), append an update block to `personal-assistant/projects/icpro-seo.md` when bulk production completes:

```
## Update — YYYY-MM-DD (from marketing/channels/icpro-blog/)
- Completed: [Month YYYY] bulk ICPro production — N posts shipped
- Status change: <if any, otherwise "none">
- New blocker: <if any, otherwise "none">
- Proposed next step: <one line>
```

## Future work

- When internalcommspro.com starts featuring named author bylines, swap the `ICP Staff` default in the pre-writing skill for an author-selection step.
- If individual ICPro posts start using FAQ blocks (Wix supports it via custom embeds), add an FAQ section back into the drafting skill behind a per-post flag.
- If posts begin including in-body CTAs (lead magnets, downloads), add a CTA placement step to pre-writing.

## Learnings

Append "what broke / what we changed" notes here as the process matures.
