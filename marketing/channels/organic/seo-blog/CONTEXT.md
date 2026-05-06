# SEO / Blog Channel Context

## What this channel does
Organic search and content marketing. Active blog with a large archive of best-practice, search-intent, and comparison content. Primary driver of top-of-funnel awareness for internal comms and HR buyers.

## Current state
- Large existing archive of published posts
- Comparison ("versus") pages for Simpplr, LumApps, Firstup, Workvivo, Poppulo
- Covers internal comms best practices, templates, benchmarks, and product-adjacent topics

## Channel-specific instructions
For writing bulk blog posts:
1. Access the target month's content plan [/Users/travisfoster/claude-code/cerkl/marketing/channels/organic/content-plan/monthly-content-plans]
2. Read each blog posts' summary from month-year-jira.csv
3. **Pre-writing** — for each blog post, deploy a subagent that loads the pre-writing guide [/Users/travisfoster/claude-code/cerkl/marketing/channels/organic/seo-blog/blog-pre-writing-guide.md]. Each subagent creates a new .md file in naming format: `YYYY-MM-DD_[slug]_pre-writing.md` in `blog-posts-pre-writing/` and completes the pre-writing.
4. **Drafting** — for each blog post, deploy a new subagent that loads the writing guide [/Users/travisfoster/claude-code/cerkl/marketing/channels/organic/seo-blog/blog-post-writing-guide.md], reviews the pre-writing file, researches the topic, and writes the blog post content in two parts. Save the draft as `YYYY-MM-DD_[slug]_draft.md` in `blog-posts-draft/`.
5. **Editing** — for each draft, deploy a new editing subagent that loads the editing guide [/Users/travisfoster/claude-code/cerkl/marketing/channels/organic/seo-blog/blog-editing/editing-guide.md], reads the draft from `blog-posts-draft/`, runs the full editing process (structural pass → rewrite → line edit → score), and saves the final post as `YYYY-MM-DD_[slug]_live.md` in `blog-posts-live/`. The original draft remains untouched in `blog-posts-draft/` for reference.

## Folder Structure

```
seo-blog/
├── CONTEXT.md
├── blog-pre-writing-guide.md
├── blog-post-writing-guide.md
├── blog-editing/
│   ├── editing-guide.md
│   └── references/
│       ├── phrases.md      # Banned words, jargon, throat-clearing openers
│       ├── structures.md   # Banned structural patterns (binary contrasts, false agency, etc.)
│       └── examples.md     # Before/after rewrite anchors
├── blog-posts-pre-writing/ # Pre-writing documents (YYYY-MM-DD_[slug]_pre-writing.md)
├── blog-posts-draft/       # Draft blog posts (YYYY-MM-DD_[slug]_draft.md)
└── blog-posts-live/        # Published/live blog posts
```

## Writing Guide
Before generating any blog post content, load and follow the instructions in [blog-post-writing-guide.md](blog-post-writing-guide.md).

## Editing Guide
After drafting any blog post, run it through [blog-editing/editing-guide.md](blog-editing/editing-guide.md).

The editing process:
1. **Pass 1 — structural edit** — flag issues at the structure level (argument order, paragraph length, list overuse, tone consistency, redundancy). No sentence-level rewrites yet.
2. **Rewrite pass** — fix flagged structural issues, then work through sentence-level issues using the lookup tables: [`blog-editing/references/phrases.md`](blog-editing/references/phrases.md) for banned words/jargon, [`blog-editing/references/structures.md`](blog-editing/references/structures.md) for banned structural patterns, [`blog-editing/references/examples.md`](blog-editing/references/examples.md) for before/after anchors.
3. **Pass 2 — line edit and score** — re-run the line-level checklist, then score 1–10 on directness, rhythm, trust, authenticity, and density.
4. **Exit condition** — score ≥ 35/50. If below, targeted rewrite on failing dimensions only, then re-score.
