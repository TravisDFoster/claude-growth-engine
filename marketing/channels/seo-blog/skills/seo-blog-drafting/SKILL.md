---
name: seo-blog-drafting
description: Use when drafting a Cerkl SEO blog post from a completed pre-writing file — produces the full markdown draft (with Webflow CTA placeholders) ready for the editing pass. Triggers on phrases like "draft the blog post for [slug]", "write the [topic] post", "turn this pre-writing into a draft", "draft this blog". Prerequisite: a pre-writing file at `blog-posts-pre-writing/`. Output: `blog-posts-draft/YYYY-MM-DD_[slug]_draft.md`.
metadata:
  version: 0.1.0
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

Deliver in clean markdown for copy-paste into Webflow. CTAs are reference-only — do not generate them.

1. Top CTA — do not generate
2. Content 1
3. Middle CTA — do not generate
4. Content 2
5. Bottom CTA — do not generate
6. FAQ or How-to Section
7. FAQ or How-to Schema

### FAQ vs. How-to

Instructional posts (e.g., "How to send a survey in Outlook") use a **How-to section** with How-to schema. All others use an **FAQ** with FAQ schema.

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
