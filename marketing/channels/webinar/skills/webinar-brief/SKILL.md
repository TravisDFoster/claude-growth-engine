---
name: webinar-brief
description: When the user wants to draft, write, refine, or fill out a webinar brief. Trigger phrases include "write the brief", "draft the brief", "fill out the brief", "webinar brief content", "structure the outline", "polish the brief", "objective and core message". Run this AFTER `webinar-project-init` has scaffolded the brief skeleton AND the user has had at least one topic-defining conversation with the partner.
metadata:
  version: 0.1.0
---

# Webinar Brief

Fill out the brief content (`<speaker-slug>.md`) section by section, working from notes the user provides from partner conversations.

## Prerequisites

- The brief file exists (created by `webinar-project-init`)
- Frontmatter is filled (title, date, partner, etc.)
- The user has notes / transcripts / themes from partner discussions

## Inputs to gather

If not already in the file or provided by the user, ask for:
1. Partner's POV on the topic — their angle, what they want to say
2. Specific failure points or problems being addressed
3. Giveaway details (what + value to attendee)
4. Polling question ideas (if any)

## Sections to fill, in order

Each builds on the previous — don't jump around:

1. **Objective** (Primary, Secondary, Strategic) — anchors everything else
2. **Core Message** — single sentence + 2–4 supporting pillars
3. **Description for Marketing Copy / Key Learnings** — feeds emails, LinkedIn, registration page
4. **Structure / Outline (60 minutes)** — section by section, with leads/supports per segment
5. **Target Audience** — Roles, Org Profile, Psychographic
6. **What Attendees Will Learn** — concrete takeaways per learning area
7. **Partner's Perspective** — partner's title, synopsis, attendee outcomes (in their voice)
8. **Polling Questions** — 3–5 self-diagnostic questions
9. **Promotion Plan** — themes, sample subject lines, sample post angle

## Cerkl context to apply

- **Foundations ICP fit**: test each section against the Foundations buyer (HR generalist, ops lead, 50–500 person company). If a section reads like enterprise-evaluator content, flag it.
- **Diagnosis-and-guiding-policy alignment**: per the marketing guiding policy, webinars should reach pre-evaluation buyers, not category-aware ones. The CTA must be Foundations sign-up (frictionless), never "request a demo".
- **Voice differentiation**: the **Partner's Perspective** section preserves the partner's voice. Don't sanitize it into Cerkl voice.

## Reference

The [Matt Frost brief](../../matt-frost-april-2026/matt-frost.md) is the gold-standard example for tone, depth, and structure. Mine it for patterns when stuck.

## Output

Write directly to `<speaker-slug>.md`. Replace placeholder brackets with content; keep the existing structure intact.

## Push update

After substantive brief revisions, append an update block to the relevant file in `personal-assistant/projects/`. See [../../CLAUDE.md](../../CLAUDE.md) for the protocol.
