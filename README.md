# Cerkl Ops Workspace

Internal ops repository for Travis Foster, Head of Marketing & Growth Operations at Cerkl. Contains strategy, marketing programs, sales tooling, CRM operations, and project management.

> Private repo. Contains company strategy, ICP, sales content, and API integrations.

---

## Structure

| Folder | What's inside |
|---|---|
| [`shared/`](shared/) | Company-wide context: company info, ICP, Broadcast product, competitors, feature deep-dives |
| [`strategy/`](strategy/) | Growth diagnosis, guiding policy, 12-month roadmap, 90-day sprint, resources |
| [`marketing/`](marketing/) | Demand gen, content channels (webinar, LinkedIn, YouTube, newsletter, PR), website, design, marketing strategy |
| [`sales/`](sales/) | Outbound sequences, discovery, objection handling, sales enablement, email review |
| [`hubspot/`](hubspot/) | CRM ops — 31 reusable skills + Python scripts for cleanup, enrichment, segments, workflows |
| [`personal-assistant/`](personal-assistant/) | Travis's projects, meeting notes, calendar, running task list |

---

## Setup

```bash
# Clone
git clone https://github.com/YOUR_USERNAME/cerkl.git

# Add credentials (see .env.example for structure)
cp .env.example .env
# Fill in real values in .env
```

API credentials are loaded from `.env` at the repo root. Scripts in any subdirectory will find it automatically via python-dotenv's directory-walk behavior. For shell commands, run `source .env` from the repo root or `source ../.env` from a subdirectory.

---

## Key Files

- [`shared/company-info.md`](shared/company-info.md) — Cerkl overview, product, positioning
- [`shared/icp.md`](shared/icp.md) — Ideal customer profile
- [`marketing/marketing-strategy/diagnosis-and-guiding-policy.md`](marketing/marketing-strategy/diagnosis-and-guiding-policy.md) — Strategic diagnosis
- [`hubspot/CONTEXT.md`](hubspot/CONTEXT.md) — HubSpot portal state and history
- [`personal-assistant/running-task-list.md`](personal-assistant/running-task-list.md) — Active task list
