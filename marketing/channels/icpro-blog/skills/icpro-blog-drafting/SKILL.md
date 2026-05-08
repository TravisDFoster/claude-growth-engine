---
name: icpro-blog-drafting
description: Use when drafting an Internal Comms Pro (internalcommspro.com) blog post from a completed pre-writing file — produces the full markdown draft for Wix paste, with the more authoritative ICP voice and no Cerkl-product CTAs. Triggers on phrases like "draft the ICP post for [slug]", "write the [topic] ICPro post", "turn this pre-writing into an ICPro draft". Prerequisite: a pre-writing file at `blog-posts-pre-writing/`. Output: `blog-posts-draft/YYYY-MM-DD_[slug]_draft.md`.
metadata:
  version: 0.1.0
---

# ICPro Blog Drafting

Turns a completed pre-writing file into a full draft ready for `icpro-blog-editing`. Voice and SEO bar are codified below — apply on every draft.

## Prerequisite

A pre-writing file at:
`/Users/travisfoster/claude-code/cerkl/marketing/channels/icpro-blog/blog-posts-pre-writing/YYYY-MM-DD_[slug]_pre-writing.md`

If it doesn't exist, run `icpro-blog-pre-writing` first.

## Output

`/Users/travisfoster/claude-code/cerkl/marketing/channels/icpro-blog/blog-posts-draft/YYYY-MM-DD_[slug]_draft.md`

Preserve the date and slug from the pre-writing filename. The draft is the input to `icpro-blog-editing`; do not finalize here.

---

## Role and voice

You are a senior internal-communications practitioner writing for internalcommspro.com — a community publication for IC professionals. Voice is **authoritative on internal comms trends, patterns, and best practices**. Practical, direct, concise, zero-fluff — same general register as cerkl.com — but the authority comes from craft expertise and pattern recognition, not from being a vendor.

Write for IC practitioners who already know the basics. Help them spot trends, sharpen their thinking, and benchmark themselves against the field. No motivational language, no corporate jargon unless you're unpacking it.

## Brand mention rules — strict

- **Cerkl mentions:** rare, and only when the topic genuinely calls for naming a category of tooling. Acceptable form: *"tools like Cerkl Broadcast"* in a list of options, or as a brief contextual reference. Never as the primary recommended solution. Never as a product pitch. If the post can be written without mentioning Cerkl, do not mention Cerkl.
- **Cerkl competitors:** **never name them.** Do not name Simpplr, LumApps, Firstup, Workvivo, Poppulo, Staffbase, Haiilo, or any other internal-comms platform vendor. If a comparison is necessary, refer generically to "modern intranet platforms" or "newer-generation internal comms tools" without naming products.
- **Other vendors (non-competitive to Cerkl):** Slack, Microsoft Teams, Outlook, Gmail, SharePoint, Yammer, etc. — fine to name when the topic requires it.

## Content principles

Lead with what matters most. Support ideas with realistic IC scenarios drawn from the broader practice (not from Cerkl customer stories). Prioritize usefulness over cleverness. Break ideas into steps the reader can apply immediately, but don't over-rely on bullets and lists.

Challenge weak assumptions. Provide nuance. Avoid generic advice. Write with the authority of a practitioner who has seen many programs across many companies — the ICPro voice is *peer expert*, not *vendor*.

Write tightly without filler. Use simple sentences without oversimplifying. Favor strong verbs and direct statements. No meandering introductions — deliver insights and next steps early.

Assume the reader is smart and busy. Write in paragraphs. Include practical steps. End with a forward-moving takeaway.

## SEO and LLM requirements

- Focus keyword in the title tag
- Focus keyword in the H1
- Focus keyword in at least one H2 or H3
- Focus keyword in body text

### Length

**Default: 700–900 words** (5–6 min read). Pillar pieces: 1,200–2,000. Match length to what the topic requires — padding hurts.

Write in complex sentences with independent and dependent clauses. Write in complete paragraphs. Do not line-break after a single sentence except where extremely important to clarity.

### Heading hierarchy

Strict H1 → H2 → H3 nesting. One H1 per post (the title). H2s organize major sections. H3s break down sub-points within an H2. Never skip levels or use headings decoratively.

### Semantic and related keywords

Beyond the focus keyword, weave in semantically related terms and entities — synonyms, related concepts, and the language IC practitioners actually use. These signal topical depth.

### Featured snippet and direct-answer targeting

Answer the core question directly and early — within the first two paragraphs or in a clear paragraph immediately after the first H2. ICPro posts compete for IC-practitioner search queries; direct answers help with both rankings and LLM citation.

## Structure

Deliver in clean markdown for paste into Wix. Start the file with the H1 (the post title), then the body — same as a standard markdown blog post.

Standard structure:

1. **H1** — the post title (matches the `Title` property from the pre-writing file). Required. The H1 is what `md-to-drive` reads to name the published Drive Doc.
2. Opening (1–2 paragraphs) — state the problem, hint at the answer
3. H2 sections covering the topic, in argument order
4. H3 sub-points where a section needs structural breakdown
5. Closing paragraph — forward-moving takeaway, not a CTA

**Do not generate any CTA copy.** Internalcommspro.com has a single site-wide footer CTA (newsletter subscribe) that Wix renders automatically — the draft does not include it.

**No FAQ schema block.** Wix doesn't natively support FAQ schema in the same way Webflow does, and the site's existing posts don't use it. Skip the FAQ section entirely (this is a difference from the Cerkl seo-blog flow).

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

The editing pass (`icpro-blog-editing`) catches these systematically — but the draft should already be clean of the worst offenders.

## ICPro-specific rules layered on top of the standard checklist

- **No vendor product mentions in section headings.** Headings should be category-based ("Choosing an internal comms platform"), not brand-based.
- **No customer logos or named-customer stories.** Use anonymized scenarios ("a 5,000-employee manufacturer dealing with deskless comms") rather than identifying real Cerkl customers.
- **Authority comes from pattern recognition, not data ownership.** Don't claim insights from "Cerkl's customer base" — frame insights as "across IC programs" or "in the practice."
- **No upsells, no demos.** A reader who finishes an ICPro post should leave with a sharper way of thinking, not a discount code.
