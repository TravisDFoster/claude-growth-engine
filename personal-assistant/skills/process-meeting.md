# Skill: Process Meeting

Triggered when Travis asks you to read a meeting note and extract action items, or when a new file appears in `meetings/`.

Goal: turn meeting notes into INDEX rows + project file updates so nothing is lost. Never apply changes without showing the proposed diff first.

## Procedure

1. **Read the meeting note** — the full file, since meeting notes are usually small.

2. **Extract**:
   - **Decisions** — anything resolved or agreed in the meeting. Goes to the relevant project file's narrative section.
   - **Action items** — must include: owner, what, due date (convert relative → absolute YYYY-MM-DD).
   - **Blockers** — anything explicitly waiting on a person or external dependency.
   - **Context shifts** — scope changes, priority changes, status changes that affect a project's Status block.

3. **Map each item to a project** — use `INDEX.md`'s project links as the registry. If an action item doesn't fit an existing project:
   - Call `skills/new-project.md`. That skill applies the create-vs-fold criteria and either auto-creates a new project file or folds into the closest adjacent one.
   - For multiple new initiatives surfaced in the same meeting, batch the create-vs-fold decisions before showing Travis the diff (avoid a flurry of mid-process confirmations).

4. **Build the proposed diff** — show Travis before writing:
   ```
   ## Proposed updates from meetings/<file>

   ### INDEX.md
   - ADD row: <project> | <next step> | <priority> | <due> | <on track> | <owner>
   - MODIFY row "<existing next step>": <change>
   - REMOVE row "<completed>": done in this meeting

   ### projects/<project>.md
   - Update Status block: <what changes>
   - Append decision/note to narrative: "<text>"
   - Move row "<x>" to ## Completed (date: <meeting date>)
   ```

5. **Apply on approval** — only after Travis confirms.

6. **Annotate the meeting file** — at the bottom, append:
   ```
   ## Processed — YYYY-MM-DD
   - INDEX rows added/modified: <count + brief>
   - Project files updated: <list>
   ```
   So `refresh` can tell at a glance which meetings have been processed.

## Date discipline

If the meeting note says "by Thursday", "next sprint", "after launch" — convert to YYYY-MM-DD using today's date as anchor. If ambiguous, ask Travis.

## Don't

- Don't load domain context (`marketing/`, `sales/`, etc.). Meeting notes give you what you need.
- Don't write speculative tasks. If an action item has no clear owner, flag it as a question rather than inventing one.
- Don't duplicate decisions across multiple project files. Pick the most relevant project; cross-reference the others.
