# Skill: New Project

Triggered:
- Directly when Travis says "let's start a project for X", "spin up a new project", "create a project file for X"
- Indirectly when `capture` or `process-meeting` detects an action item that doesn't fit any existing project

Goal: spin up a new project file from the template, add the first INDEX row, and surface what was created so Travis can adjust on the spot. Auto-create when criteria are met; fold into an existing project otherwise.

## Decision: create vs. fold

Count how many of these are true for the proposed project:

1. Distinct deliverable / completion criteria (not just one task)
2. Plan has 3+ steps in sequence
3. Likely to generate its own meetings, decisions, or history over time
4. Has its own stakeholders or external partners
5. Scope doesn't substantially overlap an existing project

**≥2 true → create the project.** Auto-create using the procedure below.

**<2 true → fold into the closest existing project.** Add the task to that project's `## Plan / Sequence` and add a row in INDEX with that project's link. Don't create a new file.

If the call came from `capture` or `process-meeting`, return control to that skill after the decision — don't double-process the task.

## Procedure (auto-create)

1. **Derive a kebab-case filename**
   - From the project name. e.g. "Partner Co-Marketing with Crescenzo" → `partner-co-marketing-crescenzo.md` (trim aggressively — under 40 chars where possible).
   - Check for collisions in `projects/` and `projects/archive/`. If a collision, append a disambiguator and surface it to Travis.

2. **Populate the template** (below) with what's known
   - For unknown fields, write `<pending — to fill in>` and surface them in the post-create summary. Don't block on them.
   - `Last updated: <today's date>` in YYYY-MM-DD.

3. **Write `projects/<filename>.md`** using the template.

4. **Add to INDEX**
   - One row for the project's immediate next step (use abstracted phrasing — don't restate the Plan section verbatim).
   - If hard deadline → also add a `Calendar Anchors` entry.
   - If High priority + blocked or at-risk → also add to `Top of Mind`.

5. **Surface to Travis**
   ```
   Created projects/<filename>.md
   - Next step (in INDEX): <text>
   - Plan: <N> steps drafted
   - Pending fields to confirm: <list, if any>
   - Anything to adjust?
   ```

## Template

```markdown
# <Project Name>

## Status
- **State:** <Active | In progress | Exploration | Blocked | Decision pending>
- **Next step:** <abstracted one-line — matches the INDEX row>
- **Due:** <YYYY-MM-DD or —>
- **On track:** <Yes | At risk | Blocked | n/a>
- **Last updated:** <YYYY-MM-DD>

---

## Overview
<1–3 sentences: what this project is and why it exists. Include the original trigger if it came from a meeting or capture.>

## Plan / Sequence
- [ ] <step 1 — the current next step, more detailed than the INDEX row>
- [ ] <step 2>
- [ ] <step 3>

## Notes / References
- <key contacts, links, constraints, open questions>
```

## Don't

- Don't create a project with an empty `## Plan / Sequence` — at minimum draft the immediate next step. If you can't, that's a signal the criteria aren't met (fold instead).
- Don't restate the INDEX row verbatim inside `## Plan / Sequence`. Plan section can be more detailed; INDEX is the abstracted pointer.
- Don't create when criteria say "fold." Return control to the caller.
- Don't load `marketing/`, `sales/`, `hubspot/`, `strategy/`, or `shared/`.
- Don't populate the project file with speculative future phases beyond what's actually decided. Phase 1 should be concrete; later phases can be one-liners.

## Edge cases

- **Filename collision** with archived project: append a year/qualifier (e.g. `webinars-2026.md`). Surface clearly so Travis knows there's a related historical file.
- **Insufficient information to draft a Plan**: ask Travis for the first 2–3 steps before writing the file. Don't auto-create with placeholder steps.
- **Two new initiatives that might be one project**: surface the question to Travis rather than creating both. Better to delay 30 seconds than to split scope wrong.
- **Project is blocked from day 1**: still create. Status `Blocked`, Plan section's first step is the unblock action (e.g. "Engage IT to resolve account access"). This matches the `meta-ads-channel-launch.md` pattern.
