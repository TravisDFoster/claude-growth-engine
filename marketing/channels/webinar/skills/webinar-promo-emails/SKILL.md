---
name: webinar-promo-emails
description: When the user wants webinar promotional emails — the 3-email sequence (intro at T-10d, value reiteration at T-3d, last reminder at T-1d) for both Cerkl and the partner, plus the 1:1 sales outreach snippet reps paste into active deals. Trigger phrases include "promo emails", "webinar emails", "email sequence", "promotional emails", "draft the emails", "T-10 email", "day-before email", "last reminder email", "sales outreach snippet", "sales email template", "something for sales to send", "1:1 rep outreach". Run this AFTER the brief is filled out.
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

## Push the 3 Cerkl-voice emails into HubSpot

After writing the markdown file, automatically push the **3 Cerkl-voice emails** into HubSpot as new drafts. The partner-voice emails stay in markdown only — the partner sends those from their own system.

Use the [`draft-marketing-email`](/Users/travisfoster/claude-code/cerkl/hubspot/skills/draft-marketing-email/SKILL.md) skill in **create mode**, cloning from the standing template.

### Template reference

| Field | Value |
|---|---|
| **Template name** | Webinar Promo Template |
| **Template ID** | `212619094633` |
| **Created** | 2026-05-10 (cloned from `211471728030` — "April 2026 Webinar - Matt Frost") |

The template carries Cerkl's standard webinar promo layout, button styling, and (importantly) the **Cerkl marketing list / audience settings**. Cloning preserves all of these — that's the whole reason this template exists. To update the audience or styling going forward, edit `212619094633` directly in HubSpot; every future clone will inherit the change.

If the template ID stops resolving (404), it was archived or deleted in HubSpot. Find its replacement, update this section, and continue. Don't fall back to cloning a random recent webinar email — the audience settings won't match.

### Naming convention for clones

Name each cloned draft consistently so they're easy to find in the HubSpot UI:

```
[Speaker] [Month YYYY] - Webinar Promo Email #N
```

Examples:
- `Matt Frost April 2026 - Webinar Promo Email #1`
- `Matt Frost April 2026 - Webinar Promo Email #2`
- `Matt Frost April 2026 - Webinar Promo Email #3`

### Steps

For each of the 3 Cerkl-voice emails:

1. **Clone** the Webinar Promo Template (ID `212619094633`) with the name above. Use the create-mode workflow in `draft-marketing-email`.
2. **PATCH the draft** with the new subject and body. The body HTML should follow the cloned template's structure — replace the inner copy via the read-modify-write pattern from `draft-marketing-email`, don't reconstruct the layout.
3. **Capture the new email ID** and add it to the speaker event folder for future reference (see "Output" addition below).

### After all 3 drafts are staged

Tell the user:
- The 3 draft IDs and where to find them in HubSpot (Marketing → Email → Drafts).
- **What still needs human review/edits before publishing**: send time, A/B variants if any, and a content check against the markdown source-of-truth.
- The partner-voice emails are in the markdown file — those go to the partner directly.

Never call `/publish`. The user clicks publish in the HubSpot UI for each draft after review.

### Update to output structure

Append a "HubSpot drafts" footer to the markdown file after staging:

```
---

## HubSpot drafts (Cerkl voice)

| Email | HubSpot ID | Draft name |
|---|---|---|
| #1 (T-10d) | `<new-id>` | [Speaker Month YYYY] - Webinar Promo Email #1 |
| #2 (T-3d) | `<new-id>` | [Speaker Month YYYY] - Webinar Promo Email #2 |
| #3 (T-1d) | `<new-id>` | [Speaker Month YYYY] - Webinar Promo Email #3 |

Cloned from Webinar Promo Template (`212619094633`). Partner-voice emails sent by partner from their own system.
```

## Sales 1:1 outreach snippet (NOT a blast)

Separate from the 6 marketing emails above. This is a short, personal note a **sales rep pastes into an existing thread** with a prospect they're actively working — not a designed campaign. Produce it alongside the promo emails whenever the webinar has an active sales motion (default: yes for prospect/lead-facing webinars).

**How it differs from the blasts — keep these straight:**

| | Marketing blasts (#1–#3) | Sales 1:1 snippet |
|---|---|---|
| Audience | Cerkl marketing list (cold-ish) | Named prospects a rep is mid-conversation with |
| Voice | Editorial, branded | Personal, references the ongoing conversation |
| Chrome | Banner, buttons, HubSpot layout | Plain text — pastes into a live thread |
| Tracking link | `cerkl_email` | Per-rep `cerkl_<rep>` link (attributes to the rep) |
| Delivery | HubSpot draft → user publishes | Rep sends manually from their own inbox |
| HubSpot draft | Yes | **No** — never stage this in HubSpot |

**Prerequisite:** per-rep tracking links exist in `<speaker-slug>-tracking-urls.md` (e.g. `cerkl_marc`, `cerkl_josh`). If only `cerkl_email` exists, mint per-rep links first per [`../../tracking-urls-convention.md`](../../tracking-urls-convention.md).

### Template (generalize the bracketed slots from the brief)

```
Subject line options:
- Thought of you — quick thing on [Weekday, Month D]
- This is basically the conversation we've been having

Hi [First Name],

Quick one that's relevant to what we've been talking through. [Speaker + role] is
running a 60-minute session on [Weekday, Month D at Time TZ] on [one-line promise —
pull from the brief's Core Message].

[One sentence tying the webinar to THIS prospect's situation — reference the specific
pain they raised.] Figured it'd be worth an hour given where you're at.

Register here: [your tracking link]

Happy to compare notes after if you make it — and either way, I can walk you through
the same thing 1:1 whenever's useful.

[Rep name]
```

Keep it under ~120 words. No "free in Foundations" hard-sell — these people are already in a sales conversation; the value is the content and the rep's soft 1:1 offer.

### Output

Write to `<speaker-slug>-sales-outreach.md` in the event folder with: the template above, a **rep tracking-link table** (one row per `cerkl_<rep>` slug from the tracking-urls file), and an optional "asset/press-release to forward" line. Reference: [rachel-maddy-sales-outreach.md](../../rachel-maddy-july-2026/rachel-maddy-sales-outreach.md) (gold standard). Do **not** push this to HubSpot.

## Push update

After producing the emails AND staging the HubSpot drafts, append an update block to the relevant file in `personal-assistant/projects/`. See [../../CLAUDE.md](../../CLAUDE.md) for the protocol.
