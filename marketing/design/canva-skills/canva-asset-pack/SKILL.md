---
name: canva-asset-pack
description: "PLACEHOLDER — not yet built. When the user wants to generate a set of on-brand Canva assets from existing Cerkl brand templates — e.g. a webinar banner, social rectangle/square, and a countdown/reminder graphic. Trigger phrases: 'create the Canva assets', 'generate the webinar graphics', 'make the social cards from the template', 'build the asset pack'. Until this skill is built, fall back to the manual checklist it will eventually automate."
metadata:
  version: 0.0.0
  status: placeholder
---

# Canva Asset Pack (PLACEHOLDER)

> **Status: stub.** Created 2026-05-28 to reserve the routing slot. Not yet built.
> Until it is built, produce the assets manually using the checklist this skill will automate:
> `/Users/travisfoster/claude-code/cerkl/marketing/channels/webinar/canva-asset-checklist.md`

## Intended deliverable

A set of on-brand Canva designs generated from **existing Cerkl brand templates** — not designed from scratch. First consumer is the webinar channel (banner, social rectangle 1200×628, social square 1080×1080, 2-days-to-go reminder), but the skill is generic enough to reuse for other campaigns.

## Intended foundation (existing templates)

- Canva source templates in `design/branding-assets/Canva Assets/` and/or Canva brand templates reachable via the Canva MCP tools.
- Cerkl brand kit (colors, typography, logo lockups) per [`design/CONTEXT.md`](../../CONTEXT.md) and the Brand Guidelines.

## Inputs (to finalize at build time)

- Asset set + dimensions (webinar default: see `canva-asset-checklist.md`)
- Final title, date/time
- Headshot(s) and any logo(s) — note: solo/internal webinars have no partner logo
- Output destination (event folder `canva-exports/`, or pasted Canva design links in the brief)

## Open questions to resolve when building

- Canva MCP (programmatic generate/duplicate) vs. human-in-the-loop template duplication — which is reliable enough to be the default path?
- Which existing template maps to each asset?
- Export + save-back flow (filenames, where links/exports land).

## Build & dry-run plan

When ready: build per [`skills/build-process`](../../../../skills/build-process/SKILL.md), then **dry-run with a real webinar** (candidate: Rachel Folz solo, 2026-06-25) and review the actual output before declaring done.

## Future work

- Wire the finished skill into the webinar follow-up phase if recap graphics are also templated.
