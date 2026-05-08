---
name: seo-blog-pre-writing
description: Use when preparing a Cerkl SEO blog post for drafting — gather the topic, fill out Webflow publishing properties (title, slug, keywords, CTAs, categories, meta), and produce an outline before any prose is written. Triggers on phrases like "pre-writing for [topic]", "set up the blog brief for [post]", "outline this blog post", "fill out the blog properties". Output: `blog-posts-pre-writing/YYYY-MM-DD_[slug]_pre-writing.md` in the seo-blog channel folder.
metadata:
  version: 0.1.0
---

# SEO Blog Pre-Writing

Pre-writing scopes a single blog post: it locks the title, slug, target keywords, CTAs, categories, meta tags, and outline before any prose is written. Output feeds directly into `seo-blog-drafting`.

## Output

Create the pre-writing file at:

`/Users/travisfoster/claude-code/cerkl/marketing/channels/seo-blog/blog-posts-pre-writing/YYYY-MM-DD_[slug]_pre-writing.md`

Where `YYYY-MM-DD` is the publish date and `[slug]` is the URL slug (lowercase, hyphenated, ≤60 chars).

## Properties to complete

- **Title**
- **Slug**
- **Top 3 Organic Search Keywords**
- **Primary Solution**
- **Top CTA**
- **Middle CTA**
- **Bottom CTA**
- **Primary Category**
- **Secondary Category**
- **Meta Description**
- **Meta Title** (typically the same as the Title)
- **Outline for Writing**

---

## Field guidelines

### Primary Solution

| Option | When to use |
|---|---|
| **Omni AI** | Content covers multiple channels (email + Teams, mobile, etc.) or a channel that is not email |
| **Foundations** | Content covers only email or email-specific features (including email analytics) |
| **Educational** | All other blog post topics |

### Top CTA

Leave blank when Primary Solution is **Educational** or **Omni AI**.

| Option | When to use |
|---|---|
| Email General Top | Article discusses both Gmail and Outlook, or is tool-agnostic |
| Gmail General Top | Article focuses specifically on Gmail |
| Outlook General Top | Article focuses specifically on Outlook |
| Nothing | Primary Solution is Educational or Omni AI |

### Middle CTA

Leave blank when Primary Solution is **Educational**.

| Option | When to use |
|---|---|
| Email Design Middle | Designing emails |
| Email Distribution Lists Middle | Managing distribution lists |
| Email Surveys Middle | Email surveys |
| Email Analytics Middle | Email analytics or measurement |
| Email Newsletter Middle | Internal newsletters |
| Email Acknowledgments Middle | Email acknowledgments or read receipts |
| Omni AI Channel Complexity Middle | Omni AI multi-channel management |
| Omni AI Deskless Workforce Middle | Omni AI for frontline/deskless workers |
| Omni AI Personalization Middle | Omni AI personalization |
| Nothing | Primary Solution is Educational |

### Bottom CTA

Always required — never blank.

| Option | When to use |
|---|---|
| Email General Bottom | Tool-agnostic or both Gmail and Outlook |
| Gmail General Bottom | Gmail-specific |
| Outlook General Bottom | Outlook-specific |

### Categories

Pick one **Primary** and one different **Secondary** from:

- Internal Email Communication
- Internal Communication Strategy
- Frontline and Mobile Workforce
- Internal Communications Measurement
- Employee Engagement and Experience

### Outline for Writing

A working H1 / H2 / H3 outline that reflects search intent and the answer the post commits to. Include the focus keyword in the H1 and at least one H2/H3.
