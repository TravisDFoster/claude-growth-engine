# Google Flow Prompts — [HOOK_SLUG]

> Per-shot prompts ready to paste into Google Flow video studio. Output of `paid-youtube-hook-prompts`. Generated from `storyboard.md` in this same folder.

## How to use this file

1. Open Google Flow video studio
2. For each shot below, copy the **Prompt** block and paste it into Flow
3. Set the **Duration** as listed
4. Render. If the result misses the mark, edit the prompt block here in this file (don't re-edit Flow), regenerate, and append a note to "Iteration log" at the bottom
5. Stitch the rendered shots in order to assemble the hook

## Source

- **Storyboard:** [./storyboard.md](./storyboard.md)
- **Generated:** [YYYY-MM-DD]
- **Total duration target:** [N] seconds

---

## Shot 1

**Duration:** [X] seconds

**Prompt:**

```
[Subject + action], [camera angle and framing], [camera movement], [setting/location with specificity], [lighting and mood], [style descriptors], [any continuity / consistency notes].
```

**On-screen text / VO direction (separate from visual prompt):**
- Text overlay: "[exact text or 'none']"
- VO line for this shot: "[exact line or 'none — body VO continues from here']"

---

## Shot 2

**Duration:** [X] seconds

**Prompt:**

```
[...]
```

**On-screen text / VO direction:**
- Text overlay:
- VO line for this shot:

---

## Shot 3 [optional]

**Duration:** [X] seconds

**Prompt:**

```
[...]
```

**On-screen text / VO direction:**
- Text overlay:
- VO line for this shot:

---

## Iteration log

> Append notes as you regenerate. Format:

```
### YYYY-MM-DD — Shot N
- Issue: <what was wrong>
- Prompt change: <what you tweaked>
- Outcome: <better / worse / same>
```

(Empty until first iteration.)

---

## Notes for `paid-youtube-hook-prompts` skill

This template is **v0.1**. Google Flow's prompt format will tighten as Travis tests in production. When the format firms up, update the prompt block structure here (then back-port to the skill file). Open questions:

- Does Flow accept structured fields (camera, lighting, style) as separate inputs, or is it one free-form text box?
- Does Flow honor character/object consistency across multiple generations in the same project, or do prompts need to spell it out per shot?
- What's the practical max duration per scene generation in Flow?
- Are there forbidden terms / styles in Flow's content policy that affect ad creative?

Capture answers in [`../../../proven-hooks.md`](../../../proven-hooks.md) "Pattern observations" once known.
