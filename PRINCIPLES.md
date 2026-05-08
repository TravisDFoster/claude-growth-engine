# Workspace Principles

This workspace operates by routing AI to the right context, not by stuffing every prompt with everything. These principles govern how files are organized so Claude does the right thing with the fewest tokens.

Read this once before building or modifying anything structural (a `CLAUDE.md`, a new `SKILL.md`, or a new `[job]-process.md`).

---

## 1. The folder is the app

Folders + markdown files are the UI. No code, no frameworks, no agent classes. English is the routing language. A new "app" is a new folder with a `CLAUDE.md`.

## 2. Routing layers — variable depth, fixed invariant

Routing is layered, but the depth is whatever the work demands. Some jobs route once (root → process). Others route through four or five levels (root → dept → subdomain → channel → project → process). The invariant is **load only what this layer needs** — not "exactly three layers."

The standard layers, in order:

- **Routers** — `CLAUDE.md`. Identity + context-to-load + routing table + file structure + ≤3 rules. Nothing else.
- **Context loaders** — `CONTEXT.md`, `REFERENCES.md`, `*-strategy.md`. Stable knowledge the work in this folder draws from.
- **Executors** — `SKILL.md` (atomic, auto-triggered) and `[job]-process.md` (orchestrator that composes skills and context across steps).

## 3. CLAUDE.md is a router, not a content doc

If a `CLAUDE.md` is more than a screen, it's leaking. Identity, paths, table, structure, three rules. Detail goes in `CONTEXT.md`, strategy docs, or skill files.

## 4. Context loading: load only what every task in this scope needs

Every `Context to load:` entry is a tax paid by every task that hits this router. If only some tasks need it, push it down to where it's actually used.

**Child routers are authoritative for their scope.** When a router has its own `Context to load:` block, that block *replaces* the parent's loads — it does not union with them. If a child has no `Context to load:` block, the parent's loads apply. This makes each leaf router self-sufficient and prevents a parent's mandatory load from leaking into a scope where it's just noise. (Discovered the hard way 2026-05-07; see `cerkl/skills/build-process/SKILL.md` Learnings.)

## 5. Naming conventions replace databases

Predictable filenames (`speaker-month-YYYY/`, `2026-05-07.md`, `post-cancel-v2.md`) let Claude find files without indexes, vector DBs, or queries. The naming convention IS the index.

## 6. SKILL.md vs. `[job]-process.md`

|  | `SKILL.md` | `[job]-process.md` |
|---|---|---|
| Purpose | Atomic capability | Multi-step deliverable |
| Auto-triggers | Yes (YAML description) | Only via routing table |
| Composes | Itself | Skills + context |
| Cardinality | Many per folder | Usually one per folder |
| Reusable | Across processes | Within its job |

A process file *uses* skills. A skill that needs three other skills probably wants to be a process.

## 7. Sub-agent dispatch lives in process files

A `[job]-process.md` step declares `Parallelizable with: [step IDs]`. When the symmetric flag exists, the orchestrator dispatches both steps in one message with multiple `Agent` tool calls. Parallel steps must not write to overlapping output paths.

## 8. Push-update protocol crosses folder boundaries

When work in folder A affects state tracked in folder B, A appends an update block to B's relevant file using a declared format. B owns reconciliation. Folders never reach across silently.

## 9. Token discipline is structural, not editorial

The system enforces token efficiency through routing, not through asking Claude to "be brief." If Claude is loading something it doesn't need, the structure is wrong — fix the structure.

## 10. Introduce a router only when the folder has multiple executors

A folder with one process file doesn't need a `CLAUDE.md` of its own — the parent's routing table can point straight at the process. Add a child `CLAUDE.md` when the folder grows to ≥3 executors or when its conventions diverge from the parent's.

## 11. The job is the unit of design

Skills and processes exist to deliver outcomes. If a folder accumulates capabilities without a clear deliverable, it's a junk drawer. Every folder should answer: **what does this produce, and for whom?**

## 12. Format conventions

Codify these consistently across both workspaces (`cerkl/` and `personal/`) so Claude's parsing stays reliable:

- **Process files:** `<job>-process.md` inside the folder that owns the job. Examples: `ic-trends-daily-process.md`, `cc-tool-deepdive-process.md`, `weekly-planning-process.md`. The job name lives in the filename, not just the folder — so processes are discoverable by `ls` and a folder can host multiple processes without name collisions.
- **Routing tables:** `| Task | Go to |` columns. The "Go to" column points at a folder, file, or anchor.
- **Skill folders:** `skills/<skill-name>/SKILL.md` (Anthropic's standard, with YAML frontmatter for auto-trigger).
- **Dates:** `YYYY-MM-DD` everywhere. Convert relative phrases ("Thursday", "next week") to absolute dates before writing them down.
- **Daily output files:** `daily/YYYY-MM-DD.md`. Weekly: `weekly/YYYY-WNN.md`.
