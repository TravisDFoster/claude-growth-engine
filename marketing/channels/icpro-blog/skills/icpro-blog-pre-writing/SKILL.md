---
name: icpro-blog-pre-writing
description: Use when preparing an Internal Comms Pro (internalcommspro.com) blog post for drafting — gather the topic, fill out the Wix publishing properties (title, slug, keywords, category, meta), and produce an outline before any prose is written. Triggers on phrases like "ICP pre-writing for [topic]", "set up the ICPro brief for [post]", "outline this ICPro post". Output: `blog-posts-pre-writing/YYYY-MM-DD_[slug]_pre-writing.md` in the icpro-blog channel folder.
metadata:
  version: 0.1.0
---

# ICPro Blog Pre-Writing

Pre-writing scopes a single post for internalcommspro.com: title, slug, target keywords, category, meta tags, and outline before any prose is written. Output feeds directly into `icpro-blog-drafting`.

## Output

Create the pre-writing file at:

`/Users/travisfoster/claude-code/cerkl/marketing/channels/icpro-blog/blog-posts-pre-writing/YYYY-MM-DD_[slug]_pre-writing.md`

Where `YYYY-MM-DD` is the publish date and `[slug]` is the URL slug (lowercase, hyphenated, ≤60 chars).

## Properties to complete

- **Title**
- **Slug**
- **Top 3 Organic Search Keywords**
- **Author** — `ICP Staff` (default; do not change unless explicitly directed)
- **Primary Category**
- **Secondary Category** (optional — only if a clear second-best fit exists)
- **Meta Description** (155–160 chars)
- **Meta Title** (typically the same as the Title; ≤60 chars for SERP truncation)
- **Featured Image Brief** — one-line description for the hero image (Wix expects ~454×256 optimized; the image itself is sourced separately)
- **Read-Time Estimate** — `X min read` (computed from target word count: 200 words ≈ 1 min)
- **Outline for Writing**

---

## Field guidelines

### Categories

Pick one **Primary Category** from the 13 internalcommspro.com topical categories:

- Showing Value
- Saving Time
- Content
- Intranet
- Mobile Workers
- Internal Comms Tools
- Collaboration
- Measurement
- Change Communications
- Strategic Planning
- Employee Retention
- Job Opportunity
- Crisis Communication

**Secondary Category** is optional. Use only when a second category genuinely applies; leave blank rather than force-fit. Must be different from the Primary.

### CTA

Internalcommspro.com has a **single site-wide CTA**: subscribe to the Internal Comms Pro newsletter. It renders in the page footer via Wix — **do not generate CTA copy in the pre-writing or draft.** No mid-post CTAs, no lead magnets, no Cerkl product CTAs.

### Author

Default byline is `ICP Staff`. Individual author bylines are not currently used on the site. Do not list a real name unless the user explicitly requests it.

### Outline for Writing

A working H1 / H2 / H3 outline that reflects search intent and the answer the post commits to.

- Include the focus keyword in the H1 and at least one H2/H3.
- The H1 doubles as the on-page title and the meta title; keep it under 60 characters where possible.
- ICPro posts skew shorter than Cerkl posts — typical outline is 4–6 H2s for a 700–900-word post; longer pillars (1,200–2,000 words) can run 6–10 H2s with H3 sub-points.

### Length target

Default to **700–900 words** for supporting posts (5–6 min read). Use **1,200–2,000 words** only when the topic genuinely requires depth (pillar pieces, comprehensive guides, frameworks). Match length to search intent — padding for word count hurts.

### Featured image brief

Internalcommspro.com posts always have a hero. The pre-writing should include a one-line image direction (e.g., *"flat-illustration of an internal comms manager reviewing analytics on a dashboard, blue/teal palette, no stock-photo handshake clichés"*). The image itself is sourced/produced separately and not part of this skill's output.
