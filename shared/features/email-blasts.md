# Feature: Internal Email Workflow — Blasts

> Part of Cerkl Broadcast. For product overview, see [broadcast.md](../broadcast.md).

**Available on:** All plans

---

## What It Does

The core email creation and delivery experience in Broadcast, built specifically for internal communicators — not adapted from external marketing tools. A "Blast" is a single email message created in the Blast editor and sent to a targeted set of subscribers pulled from live HRIS/IdP data.

Sending speed: 25,000 emails per minute, no recipient limits. Layouts pretested on 60+ email clients — no broken rendering in Outlook or Gmail. After **Send Now**, Broadcast takes up to 5 minutes to start, sends at 25,000/min, and moves the Blast to Sent within ~10 minutes total.

---

## Four Ways To Start

Create a new Blast from scratch, **Duplicate** any Draft or Sent Blast, **Create from Template**, or **Upload HTML**. Permissions gate which options a Team Member sees — a "Create from Templates" user lands directly on the Templates tab.

---

## Building

Drag-and-drop editor with responsive, email-safe Elements (text, image, button, signature, divider, video, pulse survey, acknowledgment). Branding defaults, button styles, footer rules, and a typographic system (Type Scale: 6 Headings + Paragraph, with font/size/line-height) are set centrally in **Blasts > Controls** and inherited by every new Blast. Defaults can be overridden per-Blast inside **Email Settings**.

**Autosave** is on by default and fires when a Blast has a name + ≥1 Element and the user clicks **Keep** on an Element or **Delete** an Element. Disabled on Scheduled Blasts (to avoid kicking them to Drafts) and unavailable on HTML uploads. Concurrent editing isn't supported — last save wins.

**Full Width Email** mode strips a Blast to Text, Image, and Signature Elements only, rendering full-width like a plain Outlook/Gmail email (internal orgs only). **Private Blasts** restrict visibility (Blast + Insights) to the creator and Admins, marked with a lock icon (internal orgs only).

---

## Templates

Templates preserve layout, content, and email settings as a starting point. Access tiers: **Global** (anyone with permission) or **Restricted**. Build from scratch or save any Draft/Sent Blast as a Template (Elements + Email Settings only — audience, attachments, sending info, custom time zones do not carry).

Parent Cerkl Instances can push Templates down to Child Cerkls, keeping branding consistent across multi-instance enterprise deployments.

---

## HTML Uploads

For pre-designed creative or teams needing full control. Once uploaded, Elements cannot be added or edited — only Subject Line, Audience, and a limited subset of Email Settings remain configurable.

| Constraint | Detail |
|---|---|
| File size | 80 KB max for sending (larger uploads can be reviewed but not sent) |
| Width | 600px max recommended |
| Code | Table-based layout, no DIV floats, no JavaScript |
| Images | Self-hosted, full URL referenced; assume some may be blocked |
| Fonts | Cross-platform only (Arial, Verdana, Georgia, Times New Roman) |
| Autosave / Preview Text | Not supported |

---

## Sending Info

Subject Line supports inline Personalization Fields. **Preview Text** (up to 100 chars) shows in inbox preview panes alongside the subject — critical when a Blast leads with an image, since clients will otherwise scrape an image URL into the preview. Not supported on HTML uploads.

**Attachments** — up to 2 per Blast, 1 MB each. Accepted: DOC/DOCX, XLS/XLSX, PDF, TXT, CSV, JPEG/JPG, GIF, PNG, HTML, XML, ICS, ZIP.

---

## Sender Profiles (Sender Proxies)

Pre-defined Sender identities Admins curate centrally. Each profile carries Profile Name (internal), Sender Name (what recipients see), Send From email, optional separate Reply-To, and permissions (Everyone or Restricted).

When **Sender Proxies** is toggled **on** in Controls, communicators must pick from the approved list. When off, they enter Name + Send From themselves (constrained to the org's domain). Multi-person sender illusion ("Maria & Robbie") is just a multi-name string in the Name field; the Send From email is still singular.

Every org has one un-editable **Organization Default** profile. Deleting any Sender Profile is destructive: associated Sent Blasts lose retargeting eligibility, Scheduled Blasts using it drop back to Drafts. Separate Reply-To addresses raise spam-flag risk and trigger an in-app warning.

---

## Audience Targeting

Pulled live from dynamic segments — see [audience-segmentation.md](../audience-segmentation.md). Inside a Blast, the Audience tab offers:

- **Everyone** — every subscriber (can be disabled in Controls)
- **Targeted** — Segments (My / Shared with Me / Global / All), Category Interests, and/or up to 20 Individual Recipients

**Match: Any vs. All** governs how Segments and Interests combine:

| Match | Behavior |
|---|---|
| **Any** (default) | In a selected Segment OR has a selected Category Interest |
| **All** | In a selected Segment AND has a selected Category Interest |

Overlapping subscribers across Segments are deduplicated — each person gets one email. Bounced subscribers stay in Segment counts but are skipped at send. The Audience Preview window lets communicators spot-check the recipient list before send.

---

## Personalization Fields

Insert any enabled subscriber attribute (First Name, Full Name, Email, hire date, work location, gender, custom attributes) into either the body or the Subject Line. Up to 20 unique fields per Blast.

**Fallbacks are essential** — without one, the raw token (`*|FULLNAME|*`) sends. Org-wide fallbacks live in **Controls > Personalization Fields** for every attribute; per-Blast fallbacks (Email, First Name, Full Name only) live in Email Settings. Broadcast warns before sending when audience members have missing data. Available attributes are gated by **Settings > Attributes**.

---

## Translation — 133 Languages

Supports 133 languages via Google Cloud Translation API. **Duplicate & Translate** (Blast editor ellipsis) creates a new Draft in the chosen target language. Translates: Text Elements, Subject Line, Preview Text, Image Alt-Text, Button Text, Acknowledgment Confirmation pages. Personalization Fields are not translated (they resolve per-subscriber from attributes).

Currently in Beta. Each translation is a separate Draft sent independently. One-way snapshots — edits to the original don't sync. Ineligible: already-translated Blasts, scheduled Blasts, HTML uploads. Cerkl recommends native-speaker review before send.

---

## Scheduling

Pick date and time in the **Schedule or Send** tab. Defaults to browser time zone; **Set Custom** overrides with any IANA zone. The calendar surfaces **Important Days** (org-defined dates) inline with callouts.

For time-zone-staggered global sends (same local hour worldwide): build the master Blast, save as Draft, duplicate per time-zone Segment, target each duplicate to its Segment + schedule in its custom time zone. Time-zone Segments are built from subscriber time-zone attributes in Audience Manager.

Foundations tier tracks the running 5,000-send/month free allotment in the Schedule or Send panel.

---

## Send Sample

Send a working preview to up to 10 email addresses — recipients don't need to be in the audience. Personalization Fields render as fallback placeholders for non-subscribers and as real values for subscribers. Samples don't appear in Sent or Insights. Convention: prefix the sample subject with `[sample]`.

---

## Retargeting

Follow-up sends to subscribers who didn't engage with a prior Blast. Triggered from **Sent > ⋮ > Retarget Blast**.

| Trigger | Audience sent to |
|---|---|
| Opened | Did not open the original |
| Clicked | Did not click any link |
| Opened or Clicked | Did neither |
| Acknowledgment | Did not confirm the embedded Acknowledgment |
| Responded to Survey | Did not respond to the embedded Pulse Survey |

Schedule window: up to **180 days** after original send. Broadcast dynamically removes subscribers who engage between scheduling and the retarget firing. Retargeted Blast inherits the original's sender, attachments, audience targeting, privacy, and campaigns — and tracks its own analytics. Pulse Survey insights are combined across original + retarget.

**Ineligibility:** Blasts sent before 9/30/2023, already-retargeted Blasts, retargeted Blasts themselves, deleted-Sender-Profile Blasts, orgs not in Live Mode. Manual fallback: export non-engagers from Insights, upload a manual Segment, duplicate the Blast against it.

---

## Campaigns

Tagging layer that groups related Blasts (and Content) for cross-asset reporting in Insights. Created from the Campaigns tab or inline from any Blast's ellipsis via **Manage Campaigns**. Names are unique, capped at 55 characters. Used heavily for multi-Blast initiatives — open enrollment, all-hands rollout, training waves.

---

## Suppress Auto-Responses

Adds a header that signals email clients (Outlook in particular) not to fire OOO replies back to the Send From address. Toggle globally in **Controls > Sending Options** or per-Blast in Email Settings. Useful for large internal sends where the sender mailbox would otherwise drown in vacation replies.

---

## Shareable Links

Any Sent Blast can be turned into a public web URL via **Sent > ⋮ > Shareable Link**. Share to intranet, Teams, Slack, social. SSO-Everyone orgs still require SSO to view. Toggling the link off retroactively kills any previously shared URL.

---

## Open Rate Inflation — Read This Before Quoting Numbers

Open rates approaching 100% are usually artifacts, not engagement. Microsoft Defender / Exchange security opens emails to inspect links and attachments. Mimecast, Proofpoint, Barracuda do the same. AI assistants (Copilot, Gemini) open and summarize. Apple Mail Privacy Protection pre-downloads to Apple servers. Preview panes count as opens.

For true read-confirmation use **Acknowledgments**; for sentiment use **Pulse Surveys**. Mitigations on the open-rate side: Safe-Sender list with IT, avoid spam-trigger punctuation/words in subjects, use Preview Text instead of leading with an image, keep Sender Profiles on real active addresses, minimize separate Reply-To addresses.

---

## Cross-Cutting Features

- **Pulse Surveys** — in-email response capture. See [pulse-surveys-acknowledgments.md](pulse-surveys-acknowledgments.md).
- **Employee Acknowledgments** — timestamped read receipts for compliance. See [pulse-surveys-acknowledgments.md](pulse-surveys-acknowledgments.md).
- **Image Gallery** — centralized image library for Blast Image Elements. See [image-gallery.md](image-gallery.md).
- **Calendar Invites** — real Outlook/Google Calendar events; Foundations+ and above. See [calendar-invites.md](calendar-invites.md).

---

## Compliance

GDPR / CCPA compliant. WCAG 2.1 Level AA accessible. SOC 2 Type II. AES-256 at rest, TLS 1.2+ in transit. External organizations cannot disable the email footer or use Private Blasts — legal requirements for sending to addresses they don't own.
