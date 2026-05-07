---
name: webinar-registration-page
description: When the user wants registration page copy for a webinar — headline, subhead, value props, agenda, speaker bios, CTA. Trigger phrases include "registration page copy", "landing page copy", "webinar registration page", "reg page", "write the registration page", "polish the speaker bio". Run this AFTER the brief is filled out.
metadata:
  version: 0.1.0
---

# Webinar Registration Page

Write copy for the Webflow registration page from the brief. Includes light bio polish for the speaker bio (raw bio comes from the partner; output is the version that goes on the page).

## Prerequisites

- Brief (`<speaker-slug>.md`) is filled out — at minimum: title, date, time, featuring, key learnings, target audience
- Tracking URL `cerkl_email` exists in `<speaker-slug>-tracking-urls.md` (for the page CTA)
- Partner has provided raw bio + headshot

## Inputs to gather

- Raw partner bio (paragraph form, supplied by partner)
- Cerkl presenter bio (default: pull Tarek's standard bio if not provided)
- Any specific positioning the partner wants emphasized

## Sections to produce

1. **Headline** — the single sharpest value statement (8–12 words). Test against the brief's Core Message.
2. **Subhead** — 1–2 sentences expanding the headline; names the audience and the outcome.
3. **What You'll Learn** — 3–4 outcome-led bullets. Pull from the brief's "What Attendees Will Learn" but compress to scannable lines.
4. **Agenda** — 3–5 bullets reflecting the brief's outline (the 60-minute structure). Don't list timestamps; list section titles.
5. **Speaker bios** — 2 short bios (Cerkl presenter + partner). 50–80 words each. Polished from raw input. Lead with credibility marker, follow with relevance to the topic.
6. **Giveaway callout** — 1–2 sentences naming the giveaway and what it does for the winner.
7. **CTA** — single primary action: "Register now" linking to the `cerkl_email` Zoom URL (this page is part of the email funnel).

## Cerkl context to apply

- **Foundations ICP language**: write for the HR generalist / ops lead at a 50–500 person company. Avoid jargon that signals enterprise evaluation.
- **No demo requests**: the CTA is webinar registration, full stop. No "talk to sales" secondary action.
- **Voice**: clear, plain, problem-led. Mirror the matt-frost-april-2026 reg page tone if the partner skews professional; ask if you're unsure.

## Reference

- [matt-frost.md](../../matt-frost-april-2026/matt-frost.md) — see "Description for Marketing Copy" section for headline/subhead patterns
- Generic skill (input only): `/Users/travisfoster/claude-code/cerkl/marketing/skills/copywriting/SKILL.md`

## Output

Write to `<speaker-slug>-registration-page.md` in the event folder.

## Push update

After producing the page copy, append an update block to the relevant file in `personal-assistant/projects/`. See [../../CLAUDE.md](../../CLAUDE.md) for the protocol.
