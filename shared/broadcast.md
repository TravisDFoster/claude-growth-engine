# Cerkl Broadcast — Product Reference

> Internal working document. Treat as source of truth for Broadcast product context.
> For company/market context, see [company-info.md](company-info.md).
> For full feature detail, see individual files in [features/](features/).

---

## What Broadcast Does

Cerkl Broadcast is internal communications software. It helps companies create, target, deliver, and measure employee communications — starting with a better internal email workflow than Outlook/Gmail, then extending across other employee channels like Teams, Slack, SharePoint/intranet, web, and mobile.

Platform scale: reaches nearly 6 million employees monthly.

---

## Plans

### All Plans Include

Drag-and-drop email builder, Audience Manager, email analytics, pulse surveys, employee acknowledgments, email template library, retargeting, translation (133 languages), GDPR/CCPA/encryption compliance, WCAG 2.1 Level AA.

---

### Foundations (Free Forever)

| Feature | Detail |
|---|---|
| Price | Free forever — no credit card, no contract, no setup fees |
| Email sends | 5,000/month (overages: $0.09/email) |
| Communicator seats | 3 (additional: $75/month each) |
| Instances | 1 |
| SSO | Available as add-on (not included) |
| Calendar invites | Not included |
| API access | Not included |

Foundations accounts have access to Blasts, Audience Manager, and Insights. Blasts can be built with drag-and-drop elements, pre-made templates, or HTML uploads. Sending speed: 25,000 emails/minute. Pretested on 60+ email clients — no broken layouts in Outlook or Gmail.

Account note: subscription auto-renews monthly even at $0. Turning off auto-renew eventually freezes the account after a grace period — this is an account mechanic, not a trial expiration.

---

### Foundations+

Audience-based pricing, annual agreement typical. Contact sales for pricing.

**Adds over Foundations:**
- Unlimited email sends (no overage meter)
- Unlimited communicator seats
- **Calendar Invites** — real Outlook and Google Calendar events (not ICS files); updates overwrite originals; cancellations remove from calendar; rules-based targeting by role, location, department, tenure; can be sent on behalf of leadership
- API access
- SSO included (Okta, Azure AD, Google Workspace; SAML-based; MFA supported through SSO)
- 3 instances

---

### Omni AI

Audience-based pricing, annual agreement typical. Contact sales for pricing.

**Adds over Foundations+:**
- AI-powered personalization (News Digests / AI Newsletters)
- Omni-channel publishing: SharePoint, Microsoft Teams, Slack, Mobile App, Microsites
- Omni-channel analytics (cross-channel dashboards)
- Content Management System (CMS / Content Hub)
- Enterprise implementation and support
- 6 instances

---

## SMB Value Proposition

Foundations solves for SMB teams in a sequence:
1. **Stop using Outlook/Gmail as an internal comms hack**
2. **Start free with something purpose-built**
3. **Upgrade only when complexity actually shows up** (more scale, seats, domains, calendar invites, API, or omni-channel needs)

### Why Foundations vs. Alternatives

**vs. Gmail/Outlook:** Not built for internal comms. Neither provides audience segmentation, internal analytics, branded templates, or a communicator workflow. Foundations replaces mailbox hacks with a purpose-built internal email system.

**vs. free Mailchimp:** Mailchimp's free plan is built for external marketing. Foundations is built for employee communication: internal audience structure, communicator seats, read insights, and internal messaging workflows. Different product for a different job.

**vs. ContactMonkey:** More direct comparison, but ContactMonkey is sales-led with custom pricing. Foundations is self-serve and free forever — no procurement, no renewals, no budget defense, no contract pressure.

**Sharpest summary:** Foundations gives SMBs a real internal email system, not a workaround — free forever, purpose-built for employees, with a clear growth path.

---

## Features (Summary)

Load the linked file for full detail on whichever feature is relevant.

| Feature Area | What It Does | Plans | Detail |
|---|---|---|---|
| **Dynamic audience sync & segmentation** | Pulls live employee data from HRIS/IdP; auto-updating segments without IT dependency | All | [features/audience-segmentation.md](features/audience-segmentation.md) |
| **Email workflow (Blasts)** | Drag-and-drop builder, templates, retargeting, translation, compliance — built for internal comms | All | [features/email-blasts.md](features/email-blasts.md) |
| **Pulse surveys & acknowledgments** | Surveys and timestamped read receipts embedded directly in blasts | All | [features/pulse-surveys-acknowledgments.md](features/pulse-surveys-acknowledgments.md) |
| **Analytics & Insights** | Email analytics on all plans; omni-channel analytics on Omni AI; redesigned May 2026 | All / Omni AI | [features/analytics-insights.md](features/analytics-insights.md) |
| **AI personalization (News Digest)** | ML-curated personalized newsletters per employee; subject line generator | Omni AI | [features/ai-personalization.md](features/ai-personalization.md) |
| **Omni-channel publishing** | Publish once across Teams, Slack, SharePoint, mobile, microsites | Omni AI | [features/omni-channel-publishing.md](features/omni-channel-publishing.md) |
| **Content Management (CMS)** | Single system to plan, create, approve, and schedule content for every channel | Omni AI | [features/content-management.md](features/content-management.md) |

---

## Integrations

| Category | Systems |
|---|---|
| People data / HRIS | Workday, SAP, PeopleSoft, ADP, Paycor, Active Directory (multiple sources supported simultaneously) |
| Employee channels | SharePoint, Microsoft Teams, Slack, Outlook, Gmail, mobile app, microsites |
| Identity / SSO | Okta, Azure AD, Google Workspace (SAML-based; MFA through SSO; included on Foundations+/Omni AI, add-on on Foundations) |
| APIs / content sync | REST API, RSS/Atom feeds, SFTP, CSV/manual uploads |

---

## Security & Compliance

SOC 2 Type II, GDPR, CCPA/CPRA, WCAG 2.1 Level AA. AES-256 encryption at rest, TLS 1.2+ in transit. HSTS enforced. Point-in-time recovery backups. OWASP Top 10-aligned vulnerability scanning.
