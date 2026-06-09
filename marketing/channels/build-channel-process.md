# Building a Channel: Process and Standards

A reusable process for adding a new marketing channel (or rebuilding an existing one) so that:

- The user can invoke Cerkl-specific Claude skills naturally as they work
- Every artifact lives in the right folder, named consistently, scaffolded from a template
- Context loading is precise — no shared docs loaded "just in case"
- The channel folder is high-signal: every file earns its place

First applied to `webinar/` (May 2026). The same shape applies to any channel that has a planning phase, content production, promotion cadence, an execution moment, and follow-up. Section at the end shows how to adapt for non-marketing domains.

---

## The 8-phase build

### Phase 1 — Audit context loading from the top down

Before adding anything new, walk the routing chain that leads to your target channel and read each `CLAUDE.md` along the way:

1. `cerkl/CLAUDE.md` — what does the root load by default?
2. `marketing/CLAUDE.md` — what does the marketing layer load?
3. The target channel's `CLAUDE.md` (if it exists) — what does it load?

For each loaded file, ask: **is this needed for *every* task in this scope, or just *some* tasks?** If only some, push it down to where it's actually used.

Common findings:
- `competitors.md` loaded at the marketing root → only relevant for blog and comparison work
- `company-info.md` loaded everywhere → only needed for content that names the company
- Feature deep-dives loaded → only needed for product-positioning work
- Broken paths (e.g., `/claude-code/shared/` should be `/claude-code/cerkl/shared/`) — verify by listing each path

**Outcome:** a list of context loads to remove from upstream files, plus the channels they should move into.

### Phase 2 — Establish channel-local foundations

Every channel should have its own `CLAUDE.md` that:

1. Defines **identity** — what kind of work happens here
2. Loads **only what this channel needs** — no aspirational extras
3. Documents **channel-specific conventions** — folder naming, date formats, file naming
4. **Restates parent rules locally** when they apply to this channel — voice guidelines, conventions (don't trust routing to carry behavior)
5. Lists **channel-local skills** — the table the agent uses to route within the channel
6. Lists **reference docs and templates** — the foundations the skills build on

**Quality bar:**
- A new contributor reads it in under 90 seconds
- Every linked path resolves
- Conventions are testable (a slug rule with examples; a date format with a sample)

### Phase 3 — Read what already exists in the channel folder

Before designing skills, read the actual artifacts already in the folder:

- Past event/project folders
- Existing `CONTEXT.md` and strategy docs
- Spreadsheets, briefs, plans the user already maintains
- Any drafts, even partial ones

Goal: **understand the actual workflow as it's done today**, not the workflow you'd design fresh. Real artifacts beat assumptions.

If the user has a project-management spreadsheet, parse it (xlsx → openpyxl). The phases, owners, due-date offsets, and naming conventions are sitting there waiting to be templated.

### Phase 4 — Map the user's process step by step

Have a conversation with the user about their actual process. For each step, classify:

| Field | Values |
|---|---|
| Owner | Claude / User / Joint / Partner |
| Type | Decision / Content production / Tool action / Meeting |
| Inputs | What from prior steps, what from outside |
| Outputs | Files (with paths), artifacts (URLs, designs, decisions) |
| Manual or automatable? | Why it's one or the other |

**Be honest about what Claude can't do.** Claude can't log into Zoom / HubSpot / Webflow / Canva, send emails, post to LinkedIn, run a live event, or make decisions about partner relationships. Skills built on fantasy capabilities fail on first real use.

**Outcome:** a numbered step list with owners and a short description of what each owner does. This becomes the basis for the skill set.

### Phase 5 — Define the skill set

For each Claude-owned step, propose a skill:

- **Name** — `<channel>-<artifact>` pattern (e.g., `webinar-promo-emails`)
- **Trigger phrases** — what the user would naturally say
- **Prerequisites** — what files / state must exist first
- **Inputs to gather** — what to ask the user (don't guess)
- **What it produces** — file path, structure, voice
- **References** — past examples for tone, generic skills for input

**Trim aggressively.** Combine near-duplicates. If a "skill" is a one-liner, it's a template. If it requires zero customization per project, it's a static doc. If it just wraps a generic skill with no Cerkl-specific value, drop it and use the generic directly.

Validate the skill list with the user before building anything. Cheap to redesign now; expensive after 8 SKILL.md files exist.

### Phase 6 — Build in dependency order

Build foundations before content:

1. **Reference docs** (conventions, checklists) — single-page, low-content, high-leverage
2. **Templates** (scaffolds with placeholders) — what the orchestrator copies into new project folders
3. **Orchestrator skill** (the one that creates a new project folder from inputs) — uses #1 and #2
4. **Validate the orchestrator** with a dry run before building any content skill
5. **Content skills** — parallel-buildable once the orchestrator is settled

Why this order: the orchestrator forces decisions about file naming, folder structure, and date conventions that downstream skills inherit. Build content skills first and you'll rewrite them all when the orchestrator changes.

### Phase 7 — Validate with a hypothetical dry run

Before declaring the channel "built," dry-run the orchestrator with realistic-but-fake inputs:

- Pick a plausible partner / topic / date
- Show the user what files would be created (preview content)
- Walk through date conversions (offsets → absolute `YYYY-MM-DD`)
- Show the next-step reminder output
- **Don't actually write the files yet**

The user will spot issues: cadence wrong, owner mislabeled, naming awkward, edge case unhandled. Cheap to fix here. Make the tweaks and only then declare done.

### Phase 8 — Update channel CLAUDE.md and commit

1. Update the channel `CLAUDE.md` to list every built skill (with phase mapping), reference docs, templates folder, and conventions
2. Trim or remove the TODO list as items are completed
3. Stage **only this session's files** (avoid `git add -A` so unrelated WIP doesn't ride along)
4. Commit with a message that explains the *why* of the structural changes, not just the file count

---

## What good user experience looks like

### Ideal interaction with an orchestrator skill

```
User: "let's start a new webinar"

Skill: "Got it. I need 4 things before scaffolding:
        1. Speaker / partner name?
        2. Event date (YYYY-MM-DD)?
        3. Working title (placeholder OK)?
        4. Cerkl presenter? (default: Tarek)"

User: [provides]

Skill: 
  - Creates folder sarah-chen-september-2026/
  - Writes 3 files: brief skeleton, project plan with absolute dates, tracking-URL inventory
  - Prints:
      "Done. Next manual steps:
        1. Create MAP in Google Docs
        2. Create Zoom webinar + tracking URLs (use sarah-chen-tracking-urls.md as the slug list)
        3. Gather Canva inputs (logo, headshots) — see canva-asset-checklist.md
       
       Next Claude skills as you progress:
        webinar-brief → webinar-registration-page → webinar-promo-emails → ..."
```

### Properties that make a skill feel good to use

- **Asks for missing inputs explicitly** — never guesses what the user meant
- **Produces real files in predictable paths** — the user can find what was made without searching
- **Surfaces manual next steps as a checklist** — the user knows exactly what they have to do outside Claude
- **Lists the next skill in the workflow** — orients the user to what comes after
- **Writes in the right voice** — Cerkl voice for Cerkl assets, partner voice for partner assets, never blended

### Properties that make outputs high-quality

- **Bake Cerkl-specific context into the skill itself** — Foundations ICP, diagnosis-and-guiding-policy alignment, no-demo CTA rule
- **Reference gold-standard examples by path** — "see `matt-frost.md` for tone"
- **Differentiate voice when applicable** — partner-voice email should not read like a Cerkl email with the name swapped
- **Templates have meaningful placeholders** — `[Working title — refine after kickoff with partner]`, not `[FILL THIS IN]`
- **One skill = one file output** — clear ownership, easy to revise

---

## What lives where in the channel folder

```
<channel>/
├── CLAUDE.md                       Router only: identity, context, conventions, skills table, ≤3 rules
├── CONTEXT.md                      Channel context (program goals, what we build, what to avoid)
├── <channel>-strategy.md           Channel-specific strategy (built from diagnosis-and-guiding-policy)
├── <reference-doc>.md              Conventions and checklists (naming rules, asset lists)
├── templates/
│   ├── <artifact>-template.md      Scaffolds with meaningful placeholders
│   └── ...
├── skills/
│   ├── <channel>-project-init/
│   │   └── SKILL.md                Orchestrator: scaffolds new project folders
│   ├── <channel>-<content>/
│   │   └── SKILL.md                Content skills: produce specific artifacts
│   └── ...
└── <project-name>/                 Live and past project folders (e.g., matt-frost-april-2026/)
    └── ...
```

**What does not belong in the channel folder:**

- Generic marketing skills (those live in `marketing/skills/` and are referenced as inputs)
- Shared context (lives in `cerkl/shared/` and is loaded explicitly by `CLAUDE.md`)
- Strategy guidance that applies across channels (lives in `marketing/marketing-strategy/`)

---

## Anti-patterns to avoid

- **Loading every shared doc "just in case"** — costs context, dilutes focus, breaks when paths change
- **Designing skills before reading the actual workflow** — produces skills that don't match how work is done
- **Mixing reference docs and skills in the same folder** — keep `templates/`, `skills/`, and root reference docs visually separated
- **`CLAUDE.md` as a content document** — it's a router; detail goes in `CONTEXT.md`, skill files, or strategy docs
- **Skills that wrap generic skills with no Cerkl-specific value** — if all you're doing is calling `email-sequence`, just use `email-sequence` directly
- **Pre-creating empty placeholder files at scaffold time** — clutters the folder; let content skills create files when invoked
- **A new skill for every micro-task** — combine where possible; trim before building
- **Trusting routing to carry rules** — restate cross-channel rules locally
- **Hidden dependencies on transcripts/recordings/exports** — list explicit prerequisites in the skill so the user knows what's needed before invoking

---

## Validation checklist — run before declaring done

- [ ] Root and parent `CLAUDE.md` files load only what every task in their scope needs
- [ ] Channel `CLAUDE.md` loads only what every task in this channel needs
- [ ] All `Context to load` paths resolve (test by listing each)
- [ ] Channel has its own conventions section (folder naming, dates, file naming)
- [ ] Every skill folder has a `SKILL.md` with: name, description (with trigger phrases), prerequisites, output path
- [ ] Skills table in `CLAUDE.md` lists every built skill with the phase it belongs to
- [ ] Reference docs and templates referenced in `CLAUDE.md` exist
- [ ] At least one past project folder demonstrates the conventions in practice (rename old folders to match the new convention if needed)
- [ ] Dry-run executed with hypothetical inputs and reviewed by the user
- [ ] No `Untracked files` from this work in `git status` — everything intentional is staged
- [ ] Commit message explains the *why* of structural changes, not just the file count

---

## Adapting this for non-marketing domains

The phase structure (planning → content dev → promotion → event → follow-up) is marketing-channel-specific. For other domains, replace the phases but keep the principles:

- **Sales sequence**: research → first-touch → follow-up → meeting → handoff
- **HubSpot ops**: audit → cleanup → enrichment → segment → workflow → measurement
- **Personal assistant project**: capture → triage → plan → execute → review

Everything else carries over: audit context loading top-down, owner classification per step, orchestrator + content skill split, build in dependency order, dry-run validation, restate cross-context rules locally.
