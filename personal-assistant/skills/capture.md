# Skill: Capture

Triggered when Travis says "add a task", "log this", "remember to X", or drops a quick item that needs to land in the system.

Goal: get the task into the right place fast, without losing context, in the canonical format.

## Procedure

1. **Identify the project** — match the task topic against `INDEX.md`'s project links.
   - Clear match → use it.
   - Multiple plausible matches → ask Travis.
   - No match → propose a new project file or fold into the closest adjacent one. Don't silently invent.

2. **Extract the row fields**
   - **Next step** — one-line description of the action. Convert verbose capture into a tight imperative.
   - **Priority** — High/Med/Low. If Travis didn't say, infer from context (deadline, blocker, exploration) and confirm.
   - **Due** — YYYY-MM-DD. Convert relative dates ("Friday", "next week") using today as anchor. If no deadline, leave `—`.
   - **On track** — default to `Yes` for fresh tasks unless context says otherwise.
   - **Owner** — default Travis unless Travis names someone else.

3. **Add to INDEX** — insert row in priority order (High → Med → Low). Use the existing column format.

4. **If the capture has rich context** — append to the project file's narrative section (not as a next-steps list). Examples:
   - Background or motivation
   - References to people, tools, links
   - Constraints or open questions
   The INDEX row stays as the canonical action; the project file holds the *why*.

5. **Show what you wrote** — confirm the row added and any project-file updates so Travis can correct on the spot.

## Format reminder (INDEX row)

```
| [Project Name](projects/<project>.md) | <next step> | <priority> | <due> | <on track> | <owner> |
```

## Don't

- Don't add the same task to multiple projects. Pick one; cross-reference if needed.
- Don't write the next step in two places (INDEX + project file's checklist). INDEX is canonical.
- Don't skip date conversion. "Soon" / "ASAP" / "next week" all need to become YYYY-MM-DD or `—`.
- Don't load domain context to guess. If you don't know which project, ask.
