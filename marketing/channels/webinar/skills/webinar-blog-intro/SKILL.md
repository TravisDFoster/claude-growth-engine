---
name: webinar-blog-intro
description: When the user wants the pre-event blog post that introduces a webinar topic and speakers. Trigger phrases include "webinar blog", "pre-event blog", "blog intro", "webinar blog post", "intro blog for webinar", "write the webinar blog". Run this AFTER the brief is filled out.
metadata:
  version: 0.1.0
---

# Webinar Blog Intro

Draft the pre-event blog post that introduces the webinar topic and speakers. This is a Cerkl-published blog that lives on the Cerkl site and links to the webinar registration page.

## Prerequisites

- Brief is filled out (especially: title, key learnings, partner perspective, target audience)
- Tracking URL `cerkl_email` exists (or whichever URL the blog will link to — confirm with user)
- Speaker bios are settled (raw or polished from `webinar-registration-page`)

## What to produce

A blog post following the Cerkl SEO blog structure:

1. **Title** — SEO-friendly, problem-led. Should match a query the Foundations ICP would search.
2. **Meta description** — 150–160 chars, includes the date and the partner name.
3. **Intro (3–4 short paragraphs)** — establishes the problem, hints at the cost of getting it wrong.
4. **What this webinar covers** — 3–4 bullet outcomes, mirrors the brief's "What Attendees Will Learn".
5. **Why this matters now** — connects the topic to a current trend, regulation, or shift.
6. **Meet the speakers** — 2 short paragraphs (Cerkl presenter + partner), focused on relevance to the topic.
7. **CTA section** — register link with date, time, and giveaway mention.

## Cerkl context to apply

- **Foundations ICP language**: write for the pre-evaluation buyer. Avoid category-aware framing ("internal communications platforms").
- **Diagnosis-and-guiding-policy alignment**: per the marketing guiding policy, content should lead with the problem the buyer is living with, not the product category.
- **SEO**: title and meta should target a problem-led search query, not a brand or category query.

## Reference

- The Cerkl SEO blog writing guides — load the channel CLAUDE.md to invoke them:
  - `/Users/travisfoster/claude-code/cerkl/marketing/channels/organic/seo-blog/CLAUDE.md`
  - `/Users/travisfoster/claude-code/cerkl/marketing/channels/organic/seo-blog/blog-post-writing-guide.md`

## Output

Write to `<speaker-slug>-blog-intro.md` in the event folder. After approval, the user publishes to the Cerkl site (manual).

## Push update

After producing the blog draft, append an update block to the relevant file in `personal-assistant/projects/`. See [../../CLAUDE.md](../../CLAUDE.md) for the protocol.
