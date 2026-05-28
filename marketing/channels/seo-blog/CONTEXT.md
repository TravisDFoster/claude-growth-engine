# SEO / Blog Channel Context

## What this channel does

Organic search and content marketing on cerkl.com. Active blog with a large archive of best-practice, search-intent, and comparison content. Primary driver of top-of-funnel awareness for internal comms and HR buyers.

## Current state

- Large existing archive of published posts
- Comparison ("versus") pages for Simpplr, LumApps, Firstup, Workvivo, Poppulo (live in `marketing/channels/comparison-seo/`, not here)
- Covers internal comms best practices, templates, benchmarks, and product-adjacent topics

## What this channel produces

- **Pre-writing files** (`blog-posts-pre-writing/`) — Webflow publishing properties (title, slug, keywords, CTAs, categories, meta) plus an outline. Output of the `seo-blog-pre-writing` skill.
- **Drafts** (`blog-posts-draft/`) — full markdown drafts with Webflow CTA placeholders. Output of the `seo-blog-drafting` skill.
- **Live posts** (`blog-posts-live/`) — finalized, edited posts with edit log and a published Drive Doc. Output of the `seo-blog-editing` skill.

## What this channel does **not** produce

- Versus / comparison landing pages — see `marketing/channels/comparison-seo/`
- Webinar recap blogs — owned by `marketing/channels/webinar/skills/webinar-recap-blog/`
- ICPro (unaffiliated) blog content — see `marketing/channels/icpro-blog/` (phase 2; will mirror this channel)

## Voice

Cerkl voice: practical, direct, concise, zero-fluff. Written for internal communications practitioners who are overloaded and under-resourced. The voice rules and AI-pattern checklist live in the [`seo-blog-drafting`](skills/seo-blog-drafting/SKILL.md) and [`seo-blog-editing`](skills/seo-blog-editing/SKILL.md) skills — that is the source of truth, not this file.

## Webflow body shape

Cerkl's blog template renders as: Top CTA → Content 1 (Rich Text) → Middle CTA → Content 2 (Rich Text) → Bottom CTA → FAQ. The body splits into two Rich Text fields, not one. The editing skill inserts five visible bold-bracket markers (`[Top CTA — variant]`, `[Content 1]`, `[Middle CTA — variant]`, `[Content 2]`, `[Bottom CTA — variant]`) into every `_live.md` to mark CTA insertion points and the Content 1 / Content 2 boundary. These markers render as visible bold text in the Drive Doc Furqan stages from. Canonical spec lives in [`skills/seo-blog-editing/SKILL.md`](skills/seo-blog-editing/SKILL.md#step-1--insert-the-five-visible-body-markers).

## Source of truth for what to write

The monthly content plan: `/Users/travisfoster/claude-code/cerkl/marketing/content-plan/monthly-content-plans/[month-year].md` and `[month-year]-jira.csv`. The "Blog Posts" channel rows in the CSV are this channel's queue for the month.
