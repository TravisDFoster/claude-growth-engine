---
name: seo-blog-pre-writing
description: Use when preparing a Cerkl SEO blog post for drafting. Reads the upstream SEO brief from `seo/briefs/<slug>.md`, carries its schema decisions (pillar, solution, keywords, internal links) into a Webflow-ready pre-writing file, and adds the per-post decisions the brief doesn't cover (Top/Middle/Bottom CTA variants, meta description, full H1/H2/H3 outline). Triggers on phrases like "pre-writing for [topic]", "set up the blog brief for [post]", "outline this blog post". Output: `blog-posts-pre-writing/YYYY-MM-DD_[slug]_pre-writing.md`.
metadata:
  version: 0.3.0
---

# SEO Blog Pre-Writing

Pre-writing turns a queued **SEO brief** into a draft-ready pre-writing file. The brief (produced by the SEO function in [`seo/briefs/`](/Users/travisfoster/claude-code/cerkl/marketing/seo/briefs/)) already decided pillar, solution, keywords, hub link, sibling URLs, and angle. Pre-writing's job is to (a) carry those forward verbatim, (b) pick the specific CTA variants the brief doesn't specify, (c) write meta tags, and (d) expand the angle into a full outline.

## Inputs

1. **The SEO brief** — `/Users/travisfoster/claude-code/cerkl/marketing/seo/briefs/<slug>.md`. This is the source of truth for pillar, solution, keywords, and internal links. If the brief is missing, **stop and ask** — pre-writing should not invent these properties.
2. **The brief's `status:` field** — should be `scheduled` (or `in-progress`). If it's `queued`, the planner hasn't picked it up yet; verify with Travis before proceeding.

## Output

Create the pre-writing file at:

`/Users/travisfoster/claude-code/cerkl/marketing/channels/seo-blog/blog-posts-pre-writing/YYYY-MM-DD_[slug]_pre-writing.md`

Where `YYYY-MM-DD` is the publish date (from the brief's `scheduled_for:` or the content plan row) and `[slug]` is the URL slug from the brief.

After creating the file, flip the brief's `status:` to `in-progress`.

---

## Properties to complete

### Group A — Carry from the SEO brief (no re-derivation)

| Field | Source in brief |
|---|---|
| Title | `title:` |
| Slug | `slug:` |
| Primary Keyword | `primary_keyword:` |
| Secondary Keywords (3) | `secondary_keywords:` |
| Primary Solution | `primary_solution:` |
| Primary Category | `target_pillar:` (Webflow value) |
| All Categories (cross-cutting tags) | `all_categories:` |
| Hub page link | "Internal linking" section |
| Sibling links (≥2, same pillar) | "Internal linking" section |
| Why-now context (for writer) | "Why now" section |
| Pre-flight checks (cannibalization, refresh-vs-new) | "Pre-flight checks" section |

If any of these are blank or contradictory in the brief, **stop and flag back to SEO** — don't fill them in here.

**Output shape:** render Group A as a `## Properties` block at the top of the pre-writing file. Include every field above — hub link, sibling URLs (with planned H2/H3 placement noted), why-now, and pre-flight checks all carry forward into the file so drafting and editing can see them. Recent pre-writing outputs have dropped these; don't.

### Group B — Decided in pre-writing

| Field | Notes |
|---|---|
| Top CTA | Pick the variant — see table below. Driven by Primary Solution + topic focus. |
| Middle CTA | Pick the variant — see table below. Driven by Primary Solution + topic focus. |
| Bottom CTA | Pick the variant — see table below. Always required. |
| Meta Title | Typically the same as Title; tune if title is >60 chars. |
| Meta Description | 140–160 chars; lead with the primary keyword; include the value promise. |
| Outline for Writing | Full H1 / H2 / H3 outline. Include primary keyword in H1 and ≥1 H2/H3. Expand on the brief's angle. |

---

## CTA variant selection

### Top CTA

Leave blank when Primary Solution is **Educational** or **Omni AI**.

| Option | When to use |
|---|---|
| Email General Top | Article discusses both Gmail and Outlook, or is tool-agnostic |
| Gmail General Top | Article focuses specifically on Gmail |
| Outlook General Top | Article focuses specifically on Outlook |
| *(blank)* | Primary Solution is Educational or Omni AI |

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
| *(blank)* | Primary Solution is Educational |

### Bottom CTA

Always required — never blank.

| Option | When to use |
|---|---|
| Email General Bottom | Tool-agnostic or both Gmail and Outlook |
| Gmail General Bottom | Gmail-specific |
| Outlook General Bottom | Outlook-specific |

---

## Categories reference

Webflow's `Primary Category` (= pillar) is set by the brief. Pick the matching label:

| Webflow value (from brief `target_pillar:`) | Display label |
|---|---|
| `employee-email` | Internal Email Communication |
| `internal-communication-strategy` | Internal Communication Strategy |
| `employee-engagement-articles` | Employee Engagement and Experience |
| `internal-communications-measurement` | Internal Communications Measurement |
| `mobile-employee-experience` | Frontline and Mobile Workforce |

**All Categories** (the multi-tag field) comes from the brief's `all_categories:` list. Use it to tag cross-cutting themes like *AI in IC*, *Audience Segmentation*, *Healthcare*, *Remote/Hybrid*. There is no "Secondary Category" anymore — Webflow uses multi-tag.

---

## Optional research lookup

If the brief's frontmatter has `needs_research: true`, read the IC research wiki before writing the outline. Otherwise skip this section.

**Read directly — no sub-agent dispatch:**
1. [`/Users/travisfoster/claude-code/cerkl/research/cerkl-research/wiki/index.md`](/Users/travisfoster/claude-code/cerkl/research/cerkl-research/wiki/index.md) — find topic / concept / entity pages relevant to the brief's primary keyword and angle.
2. The 3–8 pages identified above (across `wiki/topics/`, `wiki/concepts/`, `wiki/entities/`).
3. Source pages in `wiki/sources/` linked from those pages when their stats or claims would strengthen the outline.

**How to use it:**
- Pull stats, frameworks, and named practitioners into the outline as concrete anchors — the brief gives the angle; the wiki gives the proof points.
- Cite `[[source-slug]]` references inline in the pre-writing outline so drafting can resolve them to URLs.
- **Apply Blog Post Research Mode** ([cerkl-research/CLAUDE.md:136-149](/Users/travisfoster/claude-code/cerkl/research/cerkl-research/CLAUDE.md)): exclude competitor-sourced stats and citations. The competitor list is in that file; competitors can be discussed as subject matter, just not cited as evidence.
- At the end of the outline, list `**Competitor sources excluded:** [names]` so Travis sees what was held back.

If the wiki has nothing relevant for this brief, note that in the pre-writing file and proceed with the brief alone — don't fabricate citations.

---

## Outline for writing

Expand the brief's "Angle / outline" section into a full H1 / H2 / H3 structure:
- H1 includes the primary keyword (verbatim or close paraphrase)
- ≥1 H2 or H3 includes the primary keyword or a secondary keyword
- Structure should commit to the search intent — for "how-to" intent, sections are steps; for "best X" intent, sections are options
- Where the brief lists sibling links, note in the outline which H2/H3 will host the link (so the writer knows where to place it, not just that links exist)
- **Mark the planned Content 1 / Content 2 split point** in the H2 list — typically the H2 where the post pivots from diagnosis to operational fixes. Webflow's blog template renders Content 1 (first half, diagnosis arc) and Content 2 (second half, operational arc) as separate Rich Text fields, and the editing skill drops a `**[Middle CTA — variant]**` marker at this boundary. Balance the two halves so each can stand alone — outlines with 5 diagnosis H2s and 1 operational H2 will force the writer to over- or under-build a half. See [`seo-blog-editing/SKILL.md`](../seo-blog-editing/SKILL.md#step-1--insert-the-five-visible-body-markers) for the full marker spec.

---

## When done

1. Save the pre-writing file at the path above.
2. Flip the brief's `status:` from `scheduled` to `in-progress`.
3. The pre-writing file is the direct input for [`seo-blog-drafting`](../seo-blog-drafting/SKILL.md).
