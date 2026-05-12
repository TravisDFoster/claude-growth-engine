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

## Push both emails into HubSpot

After writing the markdown file, automatically push **both** follow-up emails into HubSpot as new drafts (one Attendees, one Did-not-attend).

Unlike promos, follow-up emails do not clone from a standing template. **Clone from the most recent promo email for this same webinar** so the new drafts inherit that webinar's audience list and subscription type — the lists you'll send to (Attendees vs. Registered-but-did-not-attend) are sliced from the same audience the promos targeted, so cloning the promo is the right starting point.

### Step 1 — Check if drafts already exist (safety check)

Travis sometimes pre-clones the follow-up drafts manually before this skill runs. Before cloning, list `BATCH_EMAIL` emails and look for an existing pair matching the naming convention below:

Use the listing pattern from [`audit-marketing-emails`](/Users/travisfoster/claude-code/cerkl/hubspot/skills/audit-marketing-emails/SKILL.md) Phase 2 — just the list call, not a full audit. Filter results by name containing the speaker's last name plus `Follow-up`.

- **If both drafts exist** → use `draft-marketing-email` in **update mode**: read-modify-write each draft's body HTML and preview text. Don't re-clone.
- **If neither exists** → continue to Step 2.

### Step 2 — Find the clone source

The clone source is the most recent promo email for this webinar — typically the day-before reminder (Email #3 from `webinar-promo-emails`). Cerkl-voice promos follow the naming convention `[Speaker] [Month YYYY] - Webinar Promo Email #N`.

Use the lookup pattern from [`draft-marketing-email`](/Users/travisfoster/claude-code/cerkl/hubspot/skills/draft-marketing-email/SKILL.md) Phase A to find it by speaker name. Confirm the source ID with the user before cloning.

If the promo emails were never pushed to HubSpot (unusual — `webinar-promo-emails` does this automatically), fall back to cloning any recent webinar promo for the same audience (e.g., `211471728030` "April 2026 Webinar - Matt Frost").

### Step 3 — Clone the source twice and PATCH each

Use [`draft-marketing-email`](/Users/travisfoster/claude-code/cerkl/hubspot/skills/draft-marketing-email/SKILL.md) in **create mode** for each follow-up email.

**Naming convention** (matches the existing Matt Frost follow-ups):

```
[Speaker] Webinar - Follow-up - Attendees
[Speaker] Webinar - Follow-up - Missed
```

Examples:
- `Matt Frost Webinar - Follow-up - Attendees`
- `Matt Frost Webinar - Follow-up - Missed`

For each clone:

1. **Clone** the promo source with the name above (create-mode workflow in `draft-marketing-email`).
2. **PATCH the draft** with the new subject (use the primary subject from the markdown — not an alternate), preview text, and body HTML. Use the read-modify-write pattern; do not reconstruct the layout.
3. **Capture the new email ID** for the markdown footer.

### Step 4 — Hand off to the user

After both drafts are staged, tell the user:

- The 2 draft IDs and where to find them (HubSpot → Marketing → Email → Drafts).
- **What still needs human review/edits before publishing**:
  - Slidedeck `href` (the `[HUBSPOT_SLIDEDECK_LINK]` placeholder in the body — HubSpot's rich-text editor is the right place to set the actual file attachment)
  - Foundations sign-up `href` (same — `[FOUNDATIONS_SIGNUP_LINK]` placeholder)
  - **Audience list selection** — cloning carries the promo's list forward, but the Attendees draft needs the Attendees segment and the Missed draft needs the Registered-but-did-not-attend segment. These are different lists and must be switched manually.
  - Send time.
  - Subject line is set by Claude from the markdown file — review and swap to an alternate if desired.

Never call `/publish`. The user clicks publish in the HubSpot UI for each draft after review.

### Step 5 — Append a HubSpot drafts footer to the markdown file

```
---

## HubSpot drafts

| Audience | HubSpot ID | Draft name |
|---|---|---|
| Attendees | `<new-id>` | [Speaker] Webinar - Follow-up - Attendees |
| Did-not-attend | `<new-id>` | [Speaker] Webinar - Follow-up - Missed |

Cloned from `<source-id>` (`<source-name>`).
```

## Push update

After producing the follow-up AND staging the HubSpot drafts, append an update block to the relevant file in `personal-assistant/projects/`. See [../../CLAUDE.md](../../CLAUDE.md) for the protocol.
