---
name: paid-youtube-hook-prompts
description: When the user wants to generate Google Flow video prompts from a hook storyboard, write Flow prompts, or convert a shot list into AI video generation prompts. Trigger phrases include "write flow prompts", "generate google flow prompts", "scene prompts", "flow prompts for this hook", "prompts for the storyboard". Run AFTER `paid-youtube-hook-storyboard`. Output goes into the same winner folder, ready to paste into Google Flow video studio.
metadata:
  version: 0.1.0
---

# Paid YouTube — Flow Prompt Generator

Turn a `storyboard.md` into per-shot Google Flow prompts. Output is `prompts.md` in the same winner folder, formatted so each shot's prompt can be copy-pasted directly into Flow.

## Prerequisites

- `storyboard.md` exists for the winner (output of `paid-youtube-hook-storyboard`)

## Inputs to gather

1. **Batch folder + hook slug** — to locate the storyboard. Default: most recent winner that doesn't have `prompts.md` yet.
2. **Anything Travis has learned about Flow** *(optional)* — has he ironed out which descriptors Flow honors well, what styles render badly, etc.? If yes, capture and apply. If no, default to v0.1 conventions below and we'll tune over time.

## Conventions (v0.1 — refine as Flow's behavior firms up)

- **File created:** `<batch-folder>/winners/<hook-slug>/prompts.md` — copied from [`../../templates/hook-prompts-template.md`](../../templates/hook-prompts-template.md)
- **One prompt block per shot** in the storyboard
- **Prompt structure** (until Flow's preferred input format is confirmed): a single comma-separated string in this order — `subject + action, camera angle/framing, camera movement, setting (specific), lighting/mood, style descriptors, consistency notes`. This order goes from concrete (what's there) to abstract (how it looks).
- **Keep prompts concrete.** Replace "office" with "open-plan tech office", "person" with "internal comms manager mid-30s wearing a navy cardigan". Flow rewards specificity.
- **Repeat the subject across shots** for character consistency. Don't write "the woman" in shot 2 — re-describe her with the same details so Flow doesn't drift.
- **VO and text overlays are NOT in the visual prompt.** They go in the separate "On-screen text / VO direction" block. Flow generates visuals; voice and text are added in post.
- **Duration per shot** — copy from storyboard.

## Translation rules — storyboard → prompt

| Storyboard field | Goes into prompt as |
|---|---|
| Subject / focal point | First clause — concrete description |
| Action | Verb-driven phrase right after subject |
| Camera (angle, framing, movement) | "<low/eye/high> angle, <CU/MS/WS>, <static/push/pan/handheld>" |
| Setting | Specific location phrase — never one word |
| Lighting / mood | Light source + quality + warmth |
| Style notes | Final descriptors — "shallow depth of field", "documentary handheld", "polished 35mm commercial" |
| VO / text overlay | NOT in prompt — separate block |

## What to avoid

- **Hedging language in prompts** ("maybe", "could be", "kind of"). Flow takes the prompt literally — be definite.
- **Style soup**: don't pile on 8 style descriptors. Pick 2–3 that define the look and stop.
- **Generic terms**: "office", "person", "feeling stressed". Replace with specifics.
- **Don't reference the brand**: Flow won't render a Cerkl logo correctly anyway. Keep brand assets out of Flow; add them in post.

## Output

Write `<batch-folder>/winners/<hook-slug>/prompts.md` from the template. Then print:

```
Done. Flow prompts at <batch-folder>/winners/<hook-slug>/prompts.md.

Next (manual):
  1. Open Google Flow video studio
  2. Copy each shot's prompt block, paste into Flow, set duration
  3. Render. If the result misses, edit the prompt in prompts.md, regenerate, log the iteration
  4. Stitch the rendered shots in order to assemble the hook
  5. Add VO + on-screen text in post (HeyGen for VO, your editor of choice for text)

Once shipped + you have performance signal: append the hook to proven-hooks.md.
```

## Future work — refine v0.1 prompts

This skill is v0.1. As Travis tests in Flow, capture learnings in `proven-hooks.md` "Pattern observations" and update this skill's conventions. Open questions:

- Optimal prompt length (50 words? 80? a paragraph?)
- Whether Flow honors structured fields vs. free-form text
- Character consistency strategy (re-describe? reference image? Flow project memory?)
- Practical max scene duration in Flow
- Forbidden terms / styles in Flow's content policy

## Push update

After generating prompts, append an update block to the relevant project file in `personal-assistant/projects/`. See [../../CLAUDE.md](../../CLAUDE.md) for the protocol.
