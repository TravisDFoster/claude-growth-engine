---
name: webinar-promo-emails
description: When the user wants webinar promotional emails — the 3-email sequence (intro at T-10d, value reiteration at T-3d, last reminder at T-1d) for both Cerkl and the partner. Trigger phrases include "promo emails", "webinar emails", "email sequence", "promotional emails", "draft the emails", "T-10 email", "day-before email", "last reminder email". Run this AFTER the brief is filled out.
metadata:
  version: 0.1.0
---

# Webinar Promo Emails

Produce the full 3-email sequence × 2 voices = **6 email drafts** for one webinar. Cerkl voice goes to the Cerkl marketing list; partner voice goes to the partner's list.

## Prerequisites

- Brief is filled out (especially: title, date, time, key learnings, partner perspective)
- Tracking URLs exist: `cerkl_email` and `<partner>_email`

## Cadence

| Email | Send | Purpose |
|---|---|---|
| #1 — Intro | T-10d | Announce, name the problem, list outcomes, register CTA |
| #2 — Value reiteration | T-3d | Deepen the value angle; one specific failure point |
| #3 — Last reminder | T-1d | Urgency; "tomorrow at X EST"; restate giveaway |

## Inputs to gather (if not in brief)

- Partner's preferred sender name + email signature
- Whether to include "Already registered? See you at X" footer (default: yes for #2 and #3)

## What to produce per email

For each of the 6 emails (3 cadence positions × 2 voices):

- **Subject line** (and 2–3 alternates for #2 and #3)
- **Preview text** (50–90 chars)
- **Body** — 150–250 words for #1, 100–200 for #2 and #3
- **CTA button** with the appropriate tracking URL (`cerkl_email` for Cerkl voice; `<partner>_email` for partner voice)
- **Sign-off** matching the voice

## Voice differentiation

- **Cerkl voice**: structured, problem-framed, slightly editorial. Pulls from the Core Message in the brief.
- **Partner voice**: personal, conversational, anecdotal where appropriate. Pulls from the **Partner's Perspective** section of the brief — preserve the partner's framing and idioms.

The two versions should land **the same key points** but should not read as the same email re-skinned. If the partner's voice draft sounds like a Cerkl email with the name swapped, rewrite it.

## Cerkl context to apply

- **Foundations ICP**: subject lines should pattern-match what an HR generalist would open. Avoid IC-director jargon.
- **No demo CTA**: every CTA is webinar registration. The follow-up sell is downstream.
- **Free + no sales pitch** is a recurring trust marker — include it in #1 and #3.

## Reference

- [matt-frost-promo-email.md](../../matt-frost-april-2026/matt-frost-promo-email.md) — gold-standard for tone (note: that file only has emails #1 and the day-before; **produce all three for new webinars**)
- Generic skill (input only): `/Users/travisfoster/claude-code/cerkl/marketing/skills/email-sequence/SKILL.md`

## Output

Write to `<speaker-slug>-promo-email.md` in the event folder. Structure:

```
# Promotional Emails — <Webinar Title>

**Webinar:** ...
**Date:** YYYY-MM-DD
**Cerkl tracking URL:** ...
**Partner tracking URL:** ...

---

## Cerkl voice — Email #1 (T-10d, send YYYY-MM-DD)
...

## Cerkl voice — Email #2 (T-3d, send YYYY-MM-DD)
...

## Cerkl voice — Email #3 (T-1d, send YYYY-MM-DD)
...

## Partner voice — Email #1 (T-10d, send YYYY-MM-DD)
...

## Partner voice — Email #2 (T-3d, send YYYY-MM-DD)
...

## Partner voice — Email #3 (T-1d, send YYYY-MM-DD)
...
```

## Push update

After producing the emails, append an update block to the relevant file in `personal-assistant/projects/`. See [../../CLAUDE.md](../../CLAUDE.md) for the protocol.
