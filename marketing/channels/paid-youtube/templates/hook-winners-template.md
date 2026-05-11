# Hook Winners — [BATCH_DATE]

> Selected hooks from `ideas.md` to move into production (storyboard → Flow prompts → render).

## Selection criteria reference

A winner should:
- Land its angle (pain or positioning) within the first 2 seconds of read
- Be visually feasible in Google Flow (no complex multi-character scenes, no dialogue)
- Differ enough from existing live ads + other winners in this batch to be a real test, not a near-duplicate
- Map to a specific ICP segment (Foundations or Paid) — never both

## Winners

### W1 — [hook-slug derived from H## ID]

- **Source idea:** H## (from `ideas.md`)
- **VO / text:** [restate the line]
- **Visual concept:** [restate]
- **Angle:** [pain | positioning] — [specific]
- **Why this one:** [Travis's reason — what made this beat the other 19. One sentence.]
- **Variant ideas (optional):** [same VO, different visual? same visual, sharper VO? — feeds future batches]
- **Production status:** [storyboard pending | storyboard done | rendered | live]

### W2 — [hook-slug]

- **Source idea:** H##
- **VO / text:**
- **Visual concept:**
- **Angle:**
- **Why this one:**
- **Variant ideas:**
- **Production status:**

<!-- Add W3, W4, etc. as needed. Typically 3–5 winners per batch of 20. -->

---

## Storyboard folder map

Each winner gets its own subfolder under `winners/`:

```
[BATCH_DATE]-batch/
├── ideas.md
├── winners.md            ← you are here
└── winners/
    ├── <W1-hook-slug>/
    │   ├── storyboard.md
    │   └── prompts.md
    └── <W2-hook-slug>/
        ├── storyboard.md
        └── prompts.md
```

Run `paid-youtube-hook-storyboard` per winner once selection is locked.

---

## Promotion to `proven-hooks.md`

After a winner has been rendered, shipped, and you have performance signal (CTR, watch-through, vibe — whatever you've got), append it to [`../../proven-hooks.md`](../../proven-hooks.md) under "What worked" or "What didn't work" with the date and observed outcome. That file feeds every future batch.
