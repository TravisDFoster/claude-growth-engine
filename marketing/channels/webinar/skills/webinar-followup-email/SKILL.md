---
name: webinar-followup-email
description: When the user wants the post-event follow-up email that distributes the recording and assets to registrants. Trigger phrases include "follow-up email", "post-event email", "recording email", "send the recording", "webinar follow-up", "thank you email", "post-webinar email". Run this AFTER the live event has happened and the recording is available.
metadata:
  version: 0.1.0
---

# Webinar Follow-up Email

Draft the email sent to all webinar registrants the day after the event with the recording link and any related assets.

## Prerequisites

- Live event has happened
- Recording link is available (Zoom or wherever the recording lives)
- Brief is filled out (used for tone and key takeaway recap)
- Any post-event assets (slidedeck, partner audit signup, blog recap) are linked

## Inputs to gather

- Recording link (URL — required; YouTube by default)
- Slidedeck link (if shared; HubSpot by default)
- Any other post-event assets the speakers want to share (audit form, partner offer, etc.)
- Audience split — **default is two emails**: one for attendees, one "sorry you missed it" for registrants who did not attend. Override to a single email to all registrants only if the user explicitly asks.

If a link isn't ready yet, write the draft with bracketed placeholders (e.g., `[YOUTUBE_RECORDING_LINK]`, `[HUBSPOT_SLIDEDECK_LINK]`, `[FOUNDATIONS_SIGNUP_LINK]`) so the file is final-form once URLs are dropped in.

## What to produce

By default, **two emails** (attendees + did-not-attend). Each includes:

- **Subject line** + 1–2 alternates
- **Preview text** (50–90 chars)
- **Body** (150–250 words):
  - Thank-you / quick framing of what was covered (one short paragraph). For the no-show version, lead with "sorry we missed you" framing instead.
  - 3 bullet recap of the key takeaways from the webinar
  - **Recording link** (clear, prominent)
  - Slidedeck link (if applicable)
  - Giveaway mention if the winner is being announced separately, or the winner reveal if announced here
  - **Foundations CTA** — start a free Foundations account (frictionless, no demo)
  - Partner asset link (if any)
- **Sign-off** — default is `Cerkl Thought Leadership Series Team`. Override only if the user specifies otherwise (e.g., Tarek personally).

## Cerkl context to apply

- **Foundations sign-up is the next step** — the recording is the value delivery; the CTA is the conversion ask.
- **Don't pitch anything else** — no upsell to Omni AI, no "schedule a call". One clear next step.
- **Plain, human tone** — the email is from someone who just ran the event with them. It should read that way.

## Reference

- [matt-frost-promo-email.md](../../matt-frost-april-2026/matt-frost-promo-email.md) — for tone consistency with the promo sequence

## Output

Write to `<speaker-slug>-followup-email.md` in the event folder.

## Push update

After producing the follow-up, append an update block to the relevant file in `personal-assistant/projects/`. See [../../CLAUDE.md](../../CLAUDE.md) for the protocol.
