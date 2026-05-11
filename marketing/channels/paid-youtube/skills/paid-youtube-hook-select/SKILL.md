---
name: paid-youtube-hook-select
description: When the user wants to pick winners from a YouTube hook batch, narrow down hook ideas, or capture which hooks to move into production. Trigger phrases include "pick hook winners", "select youtube hooks", "review hook batch", "narrow down the hooks", "these are the winners". Run AFTER `paid-youtube-hook-batch` has produced an `ideas.md` file. Travis picks by hook ID; this skill captures the selection plus reasoning in `winners.md`.
metadata:
  version: 0.1.0
---

# Paid YouTube — Hook Selection

Capture Travis's winning hooks from a batch. He picks by ID (e.g., H03, H07, H14); this skill writes a structured `winners.md` with reasoning and variant ideas.

## Prerequisites

- A batch folder exists with `ideas.md` populated (from `paid-youtube-hook-batch`)

## Inputs to gather

### Fast path: parse the pasted block from `ideas.html`

The `paid-youtube-hook-batch` skill produces an interactive `ideas.html` selection sheet. When Travis pastes its copy-button output into chat, recognize it and parse directly — don't ask for inputs already in the paste. The block looks like:

```
Picks from <YYYY-MM-DD>-batch — paid-youtube hooks

Selected (N):

H## — "<VO line>"
Reason: <Travis's reason, or "[add your reason]" if he forgot>

... (one block per pick)

Next: run paid-youtube-hook-select with these picks.
```

From this, extract: batch folder name (line 1), hook IDs, and per-pick reasons. If any `Reason:` line is still the placeholder `[add your reason]`, **ask for the missing reason inline** ("Reason for H07?") — don't proceed without one.

### Manual path

If Travis specifies picks conversationally instead of pasting, ask in one prompt:

1. **Batch folder** — `YYYY-MM-DD-batch/` (default: most recent)
2. **Winning hook IDs** — comma-separated list, e.g., "H03, H07, H14"
3. **Per-pick reason** — one line each. Why did this beat the other 19? (If Travis can't articulate it, ask: "What about this one made it stand out — the line, the visual, the angle, or pattern?")
4. **Variant ideas** *(optional)* — anything Travis sees worth varying? (e.g., "same VO, swap the visual to outdoor setting"). Captured as inputs for future batches.

## Conventions to enforce

- **File created:** `<batch-folder>/winners.md` — copied from [`../../templates/hook-winners-template.md`](../../templates/hook-winners-template.md)
- **Hook slug per winner:** lowercase kebab-case derived from the VO's first 3–5 distinctive words (strip articles). E.g., "Your most important email" → `most-important-email`. Used as the production folder name.
- **Production status default:** `storyboard pending`

## What to write

For each winning hook ID, copy the relevant block from `ideas.md` into `winners.md`:

- Source idea ID (e.g., H07)
- VO / on-screen text (verbatim from `ideas.md`)
- Visual concept (verbatim)
- Angle (verbatim)
- **Why this one** — Travis's reason, captured in his words. Don't editorialize.
- **Variant ideas** — Travis's variants, if any. Otherwise omit.
- **Production status:** `storyboard pending`

## What NOT to do

- **Don't append to `proven-hooks.md` yet.** That happens AFTER the hook has shipped and you have performance data. Selection ≠ proven.
- **Don't change the VO line.** If Travis wants to tweak a line at selection time, capture his tweak as the new VO and note "tweaked at selection" in the reason. Don't silently refine.
- **Don't pre-populate variant ideas.** Only what Travis says.

## Output

Write `<batch-folder>/winners.md` from the template. Then print to the user:

```
Done. <N> winners locked in <batch-folder>/winners.md.

Next: storyboard each winner. Run:
  paid-youtube-hook-storyboard  (per winner — needs the hook slug)

Once you have performance data on a shipped hook, append to proven-hooks.md.
```

## Push update

After capturing winners, append an update block to the relevant project file in `personal-assistant/projects/`. See [../../CLAUDE.md](../../CLAUDE.md) for the protocol.
