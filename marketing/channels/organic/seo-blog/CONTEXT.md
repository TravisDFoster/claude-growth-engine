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
3. For each blog post, deploy a subagent that loads the pre-writing guide [/Users/travisfoster/claude-code/cerkl/marketing/channels/organic/seo-blog/blog-pre-writing-guide.md]
4. Each subagent will create new .md file in naming format: YYYY-MM-DD_[slug]_pre-writing.md and then complete the pre-writing for the blog post based on the guide
5. Next for each blog post, deploy new subagents to load the writing guide [/Users/travisfoster/claude-code/cerkl/marketing/channels/organic/seo-blog/blog-post-writing-guide.md], review the pre-writing file, make adjustments based on the additional context, research the given topic, and then write the blog post content in two parts. Save it in the same file, and then rename the file to YYYY-MM-DD_[slug]_draft.md

## Folder Structure

```
seo-blog/
├── CONTEXT.md
├── blog-post-writing-guide.md
├── blog-pre-writing-guide.md
├── blog-posts-draft/        # Draft blog posts (YYYY-MM-DD_[slug]_draft.md)
├── blog-posts-live/         # Published/live blog posts
└── blog-posts-pre-writing/  # Pre-writing documents (YYYY-MM-DD_[slug]_pre-writing.md)
```

## Writing Guide
Before generating any blog post content, load and follow the instructions in [blog-post-writing-guide.md](blog-post-writing-guide.md).
