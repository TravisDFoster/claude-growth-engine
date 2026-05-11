---
name: paid-youtube-hook-storyboard
description: When the user wants to storyboard a selected YouTube hook, turn a winning hook into a shot list, or plan camera/visual direction for a 5–10s video ad opener. Trigger phrases include "storyboard this hook", "create youtube storyboard", "shot list for the hook", "storyboard the winner". Run AFTER `paid-youtube-hook-select` has produced a `winners.md`. Run once per winner.
metadata:
  version: 0.1.0
---

# Paid YouTube — Hook Storyboard

Turn one winning hook into a 2–3 shot storyboard for a 5–10s clip. Output is `storyboard.md` in the winner's production folder, ready for `paid-youtube-hook-prompts` to consume.

## Prerequisites

- `winners.md` exists in a batch folder
- The user has named the winner to storyboard (by hook slug or W#)

## Inputs to gather

1. **Batch folder** — `YYYY-MM-DD-batch/` (default: most recent)
2. **Winner reference** — W# from `winners.md`, OR the hook slug (e.g., `most-important-email`)
3. **Total duration** — 5, 6, 7, 8, 9, or 10 seconds (default: 7s — gives room for 2–3 shots without rushing)
4. **Shot count preference** *(optional)* — 1, 2, or 3 shots (default: let the storyboard determine — usually 2 for a punchy opener, 3 if there's a clear setup→twist→reveal arc)
5. **Visual style notes** *(optional)* — Travis's direction (e.g., "documentary handheld", "polished commercial", "dry deadpan"). If absent, infer from the hook's tone.

## Conventions to enforce

- **Production folder:** `<batch-folder>/winners/<hook-slug>/` — created if it doesn't exist
- **File created:** `<batch-folder>/winners/<hook-slug>/storyboard.md` — copied from [`../../templates/hook-storyboard-template.md`](../../templates/hook-storyboard-template.md)
- **Shot duration minimum:** 2 seconds per shot (Flow generates short clips best at ≥2s)
- **Shot count:** 1–3 max for a 5–10s hook

## How to storyboard

For each shot, fill out:

- **Subject / focal point** — be specific. Not "person", but "internal comms manager mid-30s, frustrated expression at her desk". Specificity helps Flow.
- **Action** — what happens. One verb-driven sentence.
- **Camera** — angle (low/eye/high), framing (CU/MS/WS), movement (static/push/pan/handheld). Pick what serves the moment, don't overload.
- **Setting** — concrete location. Not "office", but "open-plan tech office, mid-afternoon, half-empty desks visible behind her".
- **Lighting / mood** — descriptive. "Bright daylight from a tall window", "harsh fluorescent overhead", "warm tungsten from a desk lamp".
- **VO / text overlay during this shot** — which portion of the hook line lands here, or what text appears on screen.
- **Style notes** — depth of field, grade, motion characteristics if they matter.

## Apply Cerkl context

- **Authentic to the ICP**: if the angle is Foundations / SMB pain, the visual should feel like a 50–500 person org — not a giant enterprise floor. If the angle is Paid / enterprise, the visual can lean bigger, more distributed, more enterprise-y.
- **Avoid stock-ad clichés**: no generic "person looking stressed at laptop", no fake collaboration smiles. The ICP recognizes those instantly as ads.
- **Pattern-break is high-value**: if the hook is a pattern-break (unexpected setting, dry humor, unusual subject), the visual should commit to it. Don't soften the unusual choice into something safe.

## Continuity to body

The polished body of the ad runs immediately after the hook. Note the **final frame** and how it hands off:

- A match-cut visual into the body? (Same subject, different setting.)
- A hard cut with a text-card? (Logo, tagline, then body.)
- A natural narrative bridge? (Hook poses a question, body answers it.)

The handoff matters — a hook that doesn't lead anywhere kills the watch-time gain.

## Output

Write `<batch-folder>/winners/<hook-slug>/storyboard.md` from the template. Then print to the user:

```
Done. Storyboard at <batch-folder>/winners/<hook-slug>/storyboard.md.

Review the shot list. Tweak in the file if anything feels off.

Next: generate Flow prompts. Run:
  paid-youtube-hook-prompts  (with this hook slug)
```

## Push update

After producing a storyboard, append an update block to the relevant project file in `personal-assistant/projects/`. See [../../CLAUDE.md](../../CLAUDE.md) for the protocol.
