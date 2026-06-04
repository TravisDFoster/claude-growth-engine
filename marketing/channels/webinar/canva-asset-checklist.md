# Canva Asset Checklist

> **What this file is now:** the **inputs-to-gather pre-flight** — what you need on hand before rendering can run cleanly (headshot, partner logo if any, finalized title, etc.).
>
> **What this file is NOT:** the list of assets to render. That list now lives in [`asset-packs.md`](asset-packs.md) (the 9-template IC Thought Leadership pack + 5-template Generic pack). The [`template-fill`](/Users/travisfoster/claude-code/cerkl/marketing/design/canva-skills/template-fill/SKILL.md) skill renders each role from a manifest written at init into `<event-folder>/canva-manifests/`.

## Inputs to gather before rendering

- [ ] **Speaker headshot** — raw file uploaded as a Canva asset; resolve to an asset ID via the canva-asset-index. Manifests are written at init with `headshot: ["TBD"]`; fill the asset ID once available.
- [ ] **Partner logo** — only for partner webinars (solo/internal: N/A)
- [ ] **Final webinar title** — working title is OK at init; refine via `webinar-brief` and re-render if the title shifts materially
- [ ] **Date, time, timezone** — already on the brief metadata header
- [ ] **Speaker role string** — e.g. "Head of Product, Cerkl" (used in the speaker-card "Title" slot)

## Output flow

1. `webinar-project-init` writes 9 (or 5) manifest YAMLs to `<event-folder>/canva-manifests/` at scaffold.
2. Once inputs are gathered, invoke `template-fill` per manifest. Each invocation returns a Canva edit URL.
3. Paste each returned URL into the matching row of the Drive MAP and the markdown project-plan task row.

## Legacy default-4 list (retained for cross-reference)

Pre-2026-06-02, this checklist listed 4 manual default assets. The 9-template IC Thought Leadership pack supersedes them; the mapping:

| Legacy asset | Replaced by role |
|---|---|
| Banner (reg page hero) | `share-1200x628` |
| Social rectangle (1200×628) | `share-1200x628` |
| Social square (1080×1080) | `speaker-card` |
| 2-days-to-go reminder | `countdown` |
