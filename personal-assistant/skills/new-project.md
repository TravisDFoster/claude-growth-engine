# Skill: New Project

Triggered:
- Directly when Travis says "let's start a project for X", "spin up a new project", "create a project file for X"
- Indirectly when `capture` or `process-meeting` detects an action item that doesn't fit any existing project

Goal: spin up a new project file from the template and surface what was created so Travis can adjust on the spot. Auto-create when criteria are met; fold into an existing project otherwise.

## Decision: create vs. fold

Count how many of these are true for the proposed project:

1. Distinct deliverable / completion criteria (not just one task)
2. Plan has 3+ steps in sequence
3. Likely to generate its own meetings, decisions, or history over time
4. Has its own stakeholders or external partners
5. Scope doesn't substantially overlap an existing project

**≥2 true → create the project.** **<2 true → fold:** append a dated `## Log` line to the closest existing project instead. Don't create a new file.

If the call came from `capture` or `process-meeting`, return control to that skill after the decision — don't double-process.

## Procedure (auto-create)

1. **Derive a kebab-case filename** from the project name (under 40 chars where possible). Check for collisions in `projects/` and `projects/archive/`; disambiguate and surface if needed.

2. **Clarify, then populate** — ask Travis briefly for whatever isn't obvious: **context** (why now), **scope** (in/out), **acceptance criteria** (what makes it done). One question per gap; skip what's clear. Owner defaults to Travis silently.

3. **Write `projects/<filename>.md`** using the template.

4. **Escalate only if warranted** — hard deadline → Calendar Anchors line in `INDEX.md`; commands Travis's attention now → propose a Top of Mind slot (≤5; his call). Otherwise INDEX is untouched.

5. **Surface to Travis**
   ```
   Created projects/<filename>.md
   - First step: <text>
   - Plan: <N> steps drafted
   - Pending fields to confirm: <list, if any>
   - Anything to adjust?
   ```

## Template

```markdown
# <Project Name>

## Overview
<1–3 sentences: what this project is and why it exists. Include the original trigger if it came from a meeting or capture.>

## Plan / Sequence
- [ ] <step 1 — concrete first step>
- [ ] <step 2>
- [ ] <step 3>

## Notes / References
- **Context / why now:** <one line>
- **Scope:** <what's in / out>
- **Acceptance criteria:** <what makes this done>
- <other: contacts, links, constraints, open questions>

## Log
- YYYY-MM-DD — project created (<trigger: capture / meeting / direct>)
```

The `## Log` is append-only — dated entries, newest at the bottom. It is the project's state: the latest entry tells you where things stand. No Status block to maintain.

**Entry format:** a simple item is one line — `- YYYY-MM-DD — <entry>`. A multi-point update (e.g. a meeting batch) is a dated sub-block — `### Update — YYYY-MM-DD (from <source>)` followed by bullet lines. Both live under the single `## Log` section. `## Log` is the one canonical name — earlier files used `## History` / `## Update`; those were unified to `## Log` on 2026-06-19, so don't reintroduce them.

## Don't

- Don't create a project with an empty `## Plan / Sequence` — at minimum draft the first step. If you can't, fold instead.
- Don't create when criteria say "fold." Return control to the caller.
- Don't load `marketing/`, `sales/`, `hubspot/`, `strategy/`, or `shared/`.
- Don't populate speculative future phases. Phase 1 concrete; later phases one-liners.

## Edge cases

- **Filename collision** with archived project: append a year/qualifier (e.g. `webinars-2026.md`) and surface it.
- **Insufficient information for a Plan**: ask for the first 2–3 steps before writing. Don't auto-create with placeholders.
- **Two new initiatives that might be one project**: ask rather than creating both.
- **Blocked from day 1**: still create; first Plan step is the unblock action, first Log entry names the blocker.
