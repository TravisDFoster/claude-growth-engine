---
type: concept
tags: [ai-in-internal-comms]
---

# AI Slop

## Definition

The low-quality output produced when AI-generated content lacks human-supplied taste, judgment, and voice. Articulated as IC-shorthand by [[austin-roth-eagle]] in [[cisco-comms-leader-ai-content]]: "AI-generated content without voice or taste is bad."

## Why It Matters

"AI slop" is the most useful single-frame for the failure mode IC teams should worry about with AI-generated content. It's portable for blog writing because it (1) names a specific bad outcome rather than a generic warning, (2) is becoming widely-used industry shorthand, and (3) implies a non-trivial fix (taste/voice/judgment) rather than just "use AI carefully."

The concept complements [[ai-adoption-gap]] (analyst-tier) — *AI slop is one reason why customers don't adopt vendor AI features even when vendors invest heavily*. The vendor AI doesn't preserve their voice.

## How It Works

Roth-Eagle's prescription (per [[cisco-comms-leader-ai-content]]):

- **Break workflows into small, specific steps** — not a one-shot prompt with end-stage human review.
- **Insert human judgment at each step** — not just at publication approval.
- **Use AI as a formatting/amplification tool** — for ideas and outlines you've already shaped, not as a voice replacement.
- **Combine deep domain expertise + AI fluency** — neither alone produces the best output.

The implied measurement question: does your AI workflow preserve the human-authored "fingerprint" through to publication, or does it dilute it?

## Seen In

- [[cisco-comms-leader-ai-content]] — primary source
- [[austin-roth-eagle]] — primary advocate

## Related Concepts

- [[ai-adoption-gap]] — vendor-side phenomenon; AI slop is one reason customers don't adopt vendor AI
- [[people-intelligence]] — vendor framings of action-oriented AI may sidestep slop by focusing on dashboards / analysis rather than generated content

## Tensions / Criticisms

- "Taste" is fuzzy and hard to measure — practitioners may disagree on whether output is slop.
- Single-practitioner framing; would benefit from broader corroboration (other IC leaders, academic perspective).
- Risks becoming a thought-terminating cliché — every poor AI output gets dismissed as "slop" without examining why.

## Open Questions

- Are there published examples comparing "slop" vs "voice-preserved" AI output side by side?
- Which workflow tools / patterns most reliably preserve voice through AI augmentation?
