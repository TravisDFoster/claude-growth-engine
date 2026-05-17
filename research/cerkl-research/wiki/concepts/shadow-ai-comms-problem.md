---
type: concept
tags: [ai-in-internal-comms, change-management-communications]
---

# Shadow AI as a Comms Problem

## Definition

The IC-relevant reframe of "shadow AI" — the use of personal/unsanctioned AI tools (ChatGPT, Claude, Gemini) on company work despite enterprise AI being available. Most security and IT trade press treats this as a tooling and governance problem (block ChatGPT, deploy enterprise AI, enforce DLP). [[gartner]]'s May 2026 release reframed it as primarily a **UX-and-communications problem with security consequences**: employees use personal AI *to save time* because enterprise AI is harder to use, they don't know which tool is sanctioned for which job, and rollout messaging hasn't reached them.

## Why It Matters

This is the most blog-portable insight from the four-source May 2026 cluster. It (a) names a specific failure mode every enterprise IC reader recognizes, (b) shifts ownership from CISO/CIO to CHRO+CIO co-buyer (analyst-validated by Gartner), and (c) maps directly onto Cerkl's "delivery + measurement layer" pitch — solving shadow AI requires the right rollout message reaching the right employee on the channel they use, with read-through proof.

For sales: it's now a Gartner-validated discovery question. *"When you rolled out Copilot / ChatGPT Enterprise, how did you communicate it? How do you know employees got the message?"*

## How It Works

The mechanism, per Gartner's 1Q26 survey (n=12,004):

1. **88% of employees with enterprise AI access also use personal AI tools** for business tasks.
2. **The driver is time-saved** — hybrid users (enterprise + personal) are 1.7× more likely to report significant time saved than enterprise-only users.
3. **The proximate cause is UX + comms** — employees don't know which tools are sanctioned for which job, managers don't model behavior, and rollout messaging didn't land or didn't differentiate use cases.
4. **The consequence is bifurcated** — corporate data leaks into personal AI tools (security risk) *and* the enterprise AI investment shows no ROI (the [[enablement-illusion]]) *and* talent walks (the attrition risk Gartner predicts).

The IC playbook the frame implies:

- **Pre-launch awareness** — what the tool is, what it's sanctioned for, what it isn't
- **Role-specific rollout messages** — managers, individual contributors, frontline differ
- **Manager enablement** — managers as AI-use modelers, not just policy-enforcers
- **Ongoing pulse** — quarterly check-ins on which use cases land, which don't

This is the same workflow Cerkl pitches for *any* enterprise change-comms moment — the AI rollout is just the most acute current instance.

## Seen In

- [[gartner-people-centric-ai-2026-05-15]] — primary source; reframe articulated
- [[diana-sanchez]] — Gartner analyst who voiced the shadow-AI quote
- [[gartner]] — publisher

## Related Concepts

- [[enablement-illusion]] — org-level frame; shadow-ai-comms-problem is its on-the-ground manifestation
- [[ai-rollout-comms]] — the playbook this concept implies
- [[ai-adoption-gap]] — Forrester's parallel — *vendor* AI adoption is 49%; this concept explains the *behavioral* gap
- [[people-amplification]] — the inverse — when rollout works, employees use AI to amplify themselves, not silently route around sanctioned tools

## Tensions / Criticisms

- The "shadow AI as comms problem" reframe is contested. IT/security buyers will still read it primarily as a tooling/policy problem. Be explicit when citing — Gartner explicitly broadens the diagnosis.
- The 88% figure is across orgs already rolling out enterprise AI; not generalizable to orgs without enterprise AI yet.
- "Save time" as a stated motivation may understate other drivers (privacy from employer, AI tool preference, etc.).
- Cerkl can solve the comms half; it doesn't solve the UX half (that's Microsoft / OpenAI / Anthropic / the enterprise AI vendor). Don't overclaim.

## Open Questions

- Vertical or function-specific shadow-AI rates — IC and marketing teams may be among the heaviest personal-AI users themselves.
- The role of manager-modeling — does manager AI-use predict team AI-use, and which tool?
- How fast does this reframe land with IT/security buyers vs HR buyers? IT buyers may resist (it shifts ownership); HR buyers may welcome (it adds budget rationale).
