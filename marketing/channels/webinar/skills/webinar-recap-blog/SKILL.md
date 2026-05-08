---
name: webinar-recap-blog
description: Produce a standalone, SEO-tuned blog post on a topic from the webinar that lives in the SEO blog channel archive — not framed as a "recap." The blog stands on its own as a topic-led piece, references the webinar recording as a CTA inside the body, and pulls quotes from the speakers. Trigger phrases include "recap blog", "post-event blog", "blog from the webinar", "webinar recap blog", "topic blog from the webinar". Run this AFTER `webinar-ingest` has produced cleaned source-of-truth files.
metadata:
  version: 0.1.0
---

# Webinar Recap Blog

A topic-led blog post derived from a webinar's IP, written and published as part of the SEO blog channel's normal archive — not as an obvious "recap of the webinar."

## How this skill relates to the SEO blog channel

This skill **layers on top of** the SEO blog pipeline at [/Users/travisfoster/claude-code/cerkl/marketing/channels/seo-blog/](../../../seo-blog/). It does not duplicate the pre-writing → drafting → editing process — it routes into it.

```
Webinar artifacts (Tier 2)              This skill                              SEO blog pipeline
matt-frost-transcript-clean.md  ──┐
matt-frost-deck-extract.md      ──┤──►  recap-blog-inputs.md  ──►  pre-writing  ──►  draft  ──►  live
recording URL                   ──┘     (topic angle, quotes,
                                         frameworks, outline)
```

The blog post lives in `seo-blog/blog-posts-pre-writing/`, `blog-posts-draft/`, `blog-posts-live/` — the same folders as every other blog post, indistinguishable from the rest of the archive after publication.

## Editorial intent

The blog is **about the topic**, not about the webinar. Title and structure must hold up as a standalone topic piece a reader could reach via organic search without ever hearing of the webinar.

For the Matt Frost session, that topic is something like:
- ✅ *"The Hidden Cost of Benefits Communication"* — topic-led, hooks Tarek's title callback, ranks for the underlying intent
- ✅ *"Why Most Benefits Communication Fails Compliance"* — topic-led, problem framing
- ❌ *"Recap: Matt Frost on Benefits Comms"* — names the speaker; only valuable to people who already know him
- ❌ *"Key Takeaways from Our Webinar with Matt Frost"* — recap framing; loses standalone value

Find the **standalone topic angle** in the webinar's IP. Often it's:
- The **title callback** the host or guest delivered live (e.g., Tarek's "this could be a hidden cost of communication that no one is talking about" at ~29:38)
- A **named framework** the speaker introduced (e.g., the four-stage ladder, the four practical moves, the VALUE acronym)
- A **counterintuitive data point** the speaker grounded (e.g., "$28,250 per employee per year, and most employees never fully understand it")
- A **problem reframe** the conversation produced (e.g., "we're in the attention age, not the information age")

Pick the one that has the strongest organic search intent for the Foundations ICP, not the one that sounds smartest.

## Prerequisites

- `webinar-ingest` has been run for the event. Both files exist:
  - `<speaker-slug>-transcript-clean.md`
  - `<speaker-slug>-deck-extract.md`
- Recording URL is known and watchable (YouTube unlisted, on-demand replay, or wherever the recap follow-up email points)
- Brief exists at `<speaker-slug>.md`

## Inputs to gather

If anything below is missing, ask before proceeding:

1. **Recording URL** — used as the in-body CTA
2. **Target publish date** (YYYY-MM-DD) — used in the file slug; defaults to today + 1 week if not provided
3. **Topic angle preference** (optional) — Travis may already have a strong opinion on which angle to take; default to recommending 2–3 candidates and asking him to pick before pre-writing

## Process — four steps

### Step 1 (recap-specific) — Frame the angle and pull the IP

Read both webinar source-of-truth files. Then write `<event-folder>/<speaker-slug>-recap-blog-inputs.md` containing:

- **Recommended topic angle** (1 primary recommendation + 1–2 alternates), each with:
  - Working title (3–7 words, topic-led, no speaker names)
  - Primary search keyword
  - Search intent ("how to send a benefits campaign" vs "what is pay transparency communication" vs "benefits communication best practices")
  - Why this angle: one sentence connecting it back to a moment in the webinar
- **Foundations ICP fit** — which subscriber-growth audience does this topic reach? (Use the ICP file to ground this — pre-evaluation SMB buyer, internal comms director, etc.)
- **Pull quotes inventory** — 4–8 quotable lines with timestamps and speaker attribution. Pull from `transcript-clean.md` (verbal, in-quotes) AND from `deck-extract.md` speaker notes (written, can be paraphrased into the body or used as block quotes). Note any verbal-vs-deck deltas where the deck wording is sharper.
- **Named frameworks / models / data points** — anything teachable the post should anchor on (the four-stage ladder, the VALUE framework, the $28,250 stat, the 84M/74M dependents stat, etc.) with deck-canonical wording.
- **Recommended outline** — H1, 4–6 H2s, with one sentence each describing what that section covers. Outline should follow the standalone topic, not the webinar's runtime order.
- **Recording CTA placement** — recommend where in the body the "watch the conversation" CTA should sit. Default placement: late in the post, after the topic argument is made, framed as "want to go deeper / hear two practitioners debate this →." Not in the intro. Not as a sales pitch.

Pause after Step 1 and confirm the topic angle with Travis before proceeding. The angle decision is the most important call in the whole process — once it's locked, everything downstream follows.

### Step 2 — Pre-writing (standard SEO blog process)

Load and follow [/Users/travisfoster/claude-code/cerkl/marketing/channels/seo-blog/skills/seo-blog-pre-writing/SKILL.md](../../../seo-blog/skills/seo-blog-pre-writing/SKILL.md). Use the topic angle, keyword, and outline from `recap-blog-inputs.md` as the inputs.

**Naming:** `YYYY-MM-DD_<topic-slug>_pre-writing.md` in `seo-blog/blog-posts-pre-writing/`. The date is the **target publish date**, not the webinar date. The slug is **topic-based, no speaker names** (e.g., `hidden-cost-benefits-communication`, not `matt-frost-recap`).

**Solution mapping for the Properties block:**
- Webinar topics that hinge on email workflow, segmentation, or analytics → **Foundations**
- Webinar topics that hinge on multi-channel publishing, AI personalization, or omni-channel analytics → **Omni AI**
- Topics that are pure best-practice / educational → **Educational**

### Step 3 — Drafting (standard SEO blog process)

Load and follow [/Users/travisfoster/claude-code/cerkl/marketing/channels/seo-blog/skills/seo-blog-drafting/SKILL.md](../../../seo-blog/skills/seo-blog-drafting/SKILL.md). Read the pre-writing file first.

**Naming:** `YYYY-MM-DD_<topic-slug>_draft.md` in `seo-blog/blog-posts-draft/`.

**Recap-specific drafting rules layered on top of the standard guide:**
- **Don't open with the webinar.** No "Last week we hosted…" / "In our recent session with…" framing. Open with the topic, exactly like any other blog post in the archive.
- **Pull quotes are body content, not provenance markers.** When citing a speaker, attribute simply: *"As Matt Frost, founder of IC Partners, put it: '…'"* Use a block quote for high-impact lines. Don't say "during our webinar" or "at our session" — say "in a recent conversation with Cerkl" or just attribute the quote directly.
- **Use deck-canonical wording for frameworks**, not the verbal version. (E.g., the VALUE framework's "Literacy," not "Understandable.")
- **Use deck-canonical numbers**, not rounded verbals. (E.g., $28,250 with BLS attribution, not "close to $30,000.")
- **Single recording CTA** — one in-body link, framed as deeper conversation, placed where Step 1 recommended. Not in the intro, not stuffed into headings.
- **Foundations sign-up** appears as the structured Bottom CTA per the standard SEO blog process — not as additional in-body language.

### Step 4 — Editing (standard SEO blog process)

Load and follow [/Users/travisfoster/claude-code/cerkl/marketing/channels/seo-blog/skills/seo-blog-editing/SKILL.md](../../../seo-blog/skills/seo-blog-editing/SKILL.md). Run the full structural pass → rewrite → line edit → score sequence. Exit condition: 35/50.

**Naming:** `YYYY-MM-DD_<topic-slug>_live.md` in `seo-blog/blog-posts-live/`.

## Cerkl context to apply

- **Foundations subscriber growth is the primary KPI.** The blog should reach the pre-evaluation SMB buyer at problem-awareness stage, not the enterprise evaluator. Phrase the problem in the buyer's own language ("you can't tell if your benefits comms are landing" rather than "internal communications measurement maturity").
- **Don't pitch.** No upsell to Omni AI in the body. The Bottom CTA does the work.
- **The webinar adds authority, not the topic itself.** Quotes from a 25-year practitioner make the post more credible than a generic best-practices piece. That's the value the recap-blog format adds over a normal SEO post — the IP is grounded in a real conversation between a practitioner and a vendor CEO.

## Output file map

After running this skill end-to-end:

```
<event-folder>/
└── <speaker-slug>-recap-blog-inputs.md       ← Step 1 (lives with webinar artifacts)

seo-blog/
├── blog-posts-pre-writing/
│   └── YYYY-MM-DD_<topic-slug>_pre-writing.md  ← Step 2
├── blog-posts-draft/
│   └── YYYY-MM-DD_<topic-slug>_draft.md         ← Step 3
└── blog-posts-live/
    └── YYYY-MM-DD_<topic-slug>_live.md           ← Step 4
```

The blog itself lives entirely in the SEO blog channel. Only the **inputs working doc** stays with the webinar artifacts — that file is a record of how the topic angle and pull quotes were derived, useful if we ever need to re-derive content from the same webinar.

## Push update

After producing the final live file, append an update block to the relevant project file in `personal-assistant/projects/` per the protocol in [../../CLAUDE.md](../../CLAUDE.md). Note both the webinar provenance and the topic slug in the update.
