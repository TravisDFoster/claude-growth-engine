# Skill: Process Meeting

Triggered when Travis asks you to read a meeting note and extract action items, or when a new file appears in `meetings/`.

Goal: turn meeting notes into project `## Log` entries (and INDEX changes when warranted) so nothing is lost. Never apply changes without showing the proposed diff first.

## Procedure

1. **Read the meeting note** — the full file; meeting notes are usually small.

2. **Extract**:
   - **Decisions** — anything resolved or agreed. → dated `## Log` entry in the relevant project.
   - **Action items** — owner, what, due date (relative → absolute YYYY-MM-DD). → dated `## Log` entry.
   - **Blockers** — anything waiting on a person or external dependency. → log entry naming who/what.

3. **Map each item to a project** — match against `projects/`. If an item doesn't fit an existing project, call `skills/new-project.md` (batch the create-vs-fold decisions before showing the diff).

4. **Build the proposed diff** — show Travis before writing:
   ```
   ## Proposed updates from meetings/<file>

   ### projects/<project>.md — ## Log
   - YYYY-MM-DD — <entry>

   ### INDEX.md (only if warranted)
   - Calendar Anchor: <date — what>
   - Top of Mind: <proposed change>
   ```

5. **Apply on approval** — only after Travis confirms.

6. **Annotate the meeting file** — append at the bottom:
   ```
   ## Processed — YYYY-MM-DD
   - Log entries written: <count + projects>
   ```
   So `refresh` can tell which meetings have been processed.

## Date discipline

"By Thursday", "next sprint", "after launch" → YYYY-MM-DD using today as anchor. If ambiguous, ask.

## Don't

- Don't load domain context. Meeting notes give you what you need.
- Don't write speculative tasks. No clear owner → flag as a question, don't invent one.
- Don't duplicate decisions across project files. Pick the most relevant; cross-reference the others.
