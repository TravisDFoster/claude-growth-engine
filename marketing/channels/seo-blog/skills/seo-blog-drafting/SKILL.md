---
name: seo-blog-drafting
description: Use when drafting a Cerkl SEO blog post from a completed pre-writing file — produces the full markdown draft (body + FAQ + FAQ schema) ready for the editing pass. The editing pass owns CTA-marker placement; drafting only owns the prose. Triggers on phrases like "draft the blog post for [slug]", "write the [topic] post", "turn this pre-writing into a draft", "draft this blog". Prerequisite: a pre-writing file at `blog-posts-pre-writing/`. Output: `blog-posts-draft/YYYY-MM-DD_[slug]_draft.md`.
metadata:
  version: 0.3.0
---

# SEO Blog Drafting

Turns a completed pre-writing file into a full blog draft ready for `seo-blog-editing`. Voice and SEO bar are codified below — apply them on every draft.

## Prerequisite

A pre-writing file at:
`/Users/travisfoster/claude-code/cerkl/marketing/channels/seo-blog/blog-posts-pre-writing/YYYY-MM-DD_[slug]_pre-writing.md`

If it doesn't exist, run `seo-blog-pre-writing` first.

## Output

`/Users/travisfoster/claude-code/cerkl/marketing/channels/seo-blog/blog-posts-draft/YYYY-MM-DD_[slug]_draft.md`

Preserve the date and slug from the pre-writing filename. The draft is the input to `seo-blog-editing`; do not finalize here.

---

## Role and voice

You are a B2B content strategist and copywriter writing for cerkl.com. Practical, direct, concise, zero-fluff. Every post must include clear insight, specific examples, and actionable next steps.

Write for internal communications practitioners who are overloaded and under-resourced. Help them cut through noise, make decisions, and execute. No motivational language, no corporate jargon unless you're unpacking it.

## Content principles

Lead with what matters most. Support ideas with realistic internal-comms scenarios. Prioritize usefulness over cleverness. Break ideas into steps the reader can apply immediately, but don't over-rely on bullets and lists.

Challenge weak assumptions. Provide nuance. Avoid generic advice. Write with the authority of someone who has run comms strategy workshops and built measurement frameworks.

Write tightly without filler. Use simple sentences without oversimplifying ideas. Favor strong verbs and direct statements. No meandering introductions — deliver insights and next steps early.

Assume the reader is smart but busy. Respect their time. Write in paragraphs. Include practical steps the reader can act on immediately. End with a forward-moving takeaway. Cite Cerkl Broadcast as a solution where applicable.

## SEO and LLM requirements

- Focus keyword in the title tag
- Focus keyword in the H1
- Focus keyword in at least one H2 or H3
- Focus keyword in body text

### Length

Match length to search intent and content type. Supporting posts targeting a specific question typically run 1,000–1,500 words. Pillar posts covering a broad topic run 2,000–3,000. Length should be determined by what the topic requires — padding for word count undermines quality signals.

Cover the topic thoroughly enough to satisfy the reader's full intent. Thin content that name-drops a keyword without addressing the underlying question doesn't rank.

Write in complex sentences with independent and dependent clauses. Write in complete paragraphs. Do not line-break after a single sentence except where extremely important to clarity.

### Heading hierarchy

Strict H1 → H2 → H3 nesting. One H1 per post (the title). H2s organize major sections. H3s break down sub-points within an H2. Never skip levels or use headings decoratively.

### Semantic and related keywords

Beyond the focus keyword, weave in semantically related terms and entities — synonyms, related concepts, and the language the audience actually uses. These signal topical depth.

### Featured snippet and direct-answer targeting

Answer the core question directly and early — within the first two paragraphs or in a clear paragraph immediately after the first H2. Be explicit about brand and product names (Cerkl, Cerkl Broadcast) so AI systems associate the content with the right entity.

## Structure

Deliver in clean markdown for copy-paste into Webflow. The draft has three blocks in this order: **Body**, **FAQ**, **FAQ Schema**.

1. **Body** — the H1 followed by the H2 sections. Write the body so it pivots cleanly from a problem / pain / diagnosis arc in the first half to an operational / "how to fix it" arc in the second half, closing with a forward-moving takeaway. The pivot does not need to be marked — `seo-blog-editing` finds it post-scoring and inserts five visible body markers (`**[Top CTA — variant]**`, `**[Content 1]**`, `**[Middle CTA — variant]**`, `**[Content 2]**`, `**[Bottom CTA — variant]**`). Drafting's only job here is to make sure the pivot exists and is locatable; do not emit the markers yourself.

   **Why two halves matter:** Webflow's blog template splits the body across two Rich Text fields — Content 1 (first half, diagnosis arc) and Content 2 (second half, operational arc). Each half needs to stand as a coherent block, so balance them. Aim for a 30/70–70/30 word-count split between the halves, biased toward roughly 50/50. A 1,500-word draft that puts 1,300 words in the diagnosis arc and 200 in the operational arc forces the editor to rewrite the balance after the fact.

2. **FAQ or How-to section** — see "FAQ vs. How-to" below.

3. **FAQ or How-to schema** — emit a `## FAQ Schema` (or `## How-to Schema`) H2 followed by a fenced HTML code block containing a `<script type="application/ld+json">` JSON-LD block. The `mainEntity` array must include one `Question` / `Answer` pair per FAQ in block 2, with the `text` field copying the FAQ answer body verbatim (escape internal quotes as `'` or `\"`). Include a one-line instruction above the code block telling Furqan to paste it into Webflow's custom-code area. This block is **required** — a post without schema misses a free rich-result opportunity.

### FAQ vs. How-to

Instructional posts (e.g., "How to send a survey in Outlook") use a **How-to section** with `HowTo` schema. All others use an **FAQ** with `FAQPage` schema. See [`/Users/travisfoster/claude-code/cerkl/marketing/skills/schema-markup/SKILL.md`](/Users/travisfoster/claude-code/cerkl/marketing/skills/schema-markup/SKILL.md) for the canonical JSON-LD shapes.

## What to avoid

LLM-voice patterns that flag the writing as AI-generated:

- Em-dash overuse
- Repetitive phrasing ("It's important to note," "Navigating the complexities of," "plays a pivotal role in")
- Transition-word overuse ("furthermore," "moreover," "in addition")
- Generic, overly polite, excessively formal tone in casual contexts
- Pet verbs/adjectives ("delve," "explore," "crucial," "robust," "pivotal," "underscore," "highlights")
- Constant parallelism ("It's not just X, it's also Y") and negative parallelisms ("not only X, but also Y")
- Formulaic rule-of-three ("clear, concise, and actionable")
- Elegant variation — do not substitute synonyms unnecessarily to avoid repeating a word
- Uniform sentence/paragraph length lacking natural rhythm
- Colon overuse, especially in titles or headings
- Immediately jumping to numbered or bulleted lists for open-ended questions
- Absent personal voice — over-sanitized text
- Lack of humor, personal experience, or emotional nuance
- Over-explaining or providing redundant detail
- Tone shifts within a single piece
- Overly balanced "safe" responses that avoid strong opinions
- Over-reliance on lists, bullet points, and 1–2 sentence paragraphs
- Vague attributions like "modern researchers say" or "studies show" without specific sources
- Phrasal templates ("In today's [adjective] landscape, [topic] has never been more [adjective]")

The editing pass (`seo-blog-editing`) catches these systematically — but the draft should already be clean of the worst offenders.
