---
name: draft-marketing-email
description: "Create a new HubSpot marketing email draft, or update copy on an existing one — subject, body, link text. Stages the change as a draft via the API; the user publishes from the HubSpot UI. Use for routine email-writing work where Claude generates or edits the content."
license: MIT
metadata:
  version: "0.2.0"
  category: content-write
---

# Draft a Marketing Email

Generate or edit copy on a HubSpot marketing email and stage the change as a draft. Two modes:

- **Update mode** — modify an existing email's subject, body, or link text. Use when the target already exists (e.g., a Form Follow-up that needs corrected copy).
- **Create mode** — make a brand-new email draft, typically by cloning a template email and overwriting its content. Use when nothing exists yet (e.g., a new webinar promo email sequence).

## Critical constraint — drafts only, no publishing

**This skill never publishes.** It only PATCHes the draft version of an email. The user reviews the staged draft in HubSpot and clicks publish themselves.

Reasons:
1. **Scope.** Publishing requires `marketing-email` (or `transactional-email`) on the private app. This skill needs only `content`. Cerkl's deployed token has read/draft scopes by default, not publish — by design, because these emails go to live customers.
2. **Safety.** Marketing emails go to real subscribers. Two-pane review (API stages, human eyes-on before publish) catches things the API can't detect — like a download link `href` still pointing at the wrong asset.

If a future token has publish scopes, **still don't publish.** Stage the draft and tell the user where to click in the UI.

## When to use

- User asks Claude to write copy for a specific marketing email (update or new).
- Updating an existing email's subject/body to fit a new asset, season, or campaign.
- Pushing freshly-drafted copy (e.g., webinar promo emails from `webinar-promo-emails`) into HubSpot as new drafts.
- Acting on a finding from `audit-marketing-emails` (correcting a clone-and-edit mismatch).
- Adapting copy across a small set of related emails (run once per email).

**Don't use** for bulk audits across many emails — that's `audit-marketing-emails`.

## Setup

```bash
set -a && source /Users/travisfoster/claude-code/cerkl/.env && set +a
```

`set -a` is required so `python3` subprocesses inherit the token. Use `curl` for HTTP and `python3` for JSON edits (per `hubspot/CLAUDE.md`, urllib hits SSL cert errors).

Required scope: `content`.

## Workflow

Pick the mode first:

- **Create mode** — the email doesn't exist yet. Skip to "Create mode workflow" below.
- **Update mode** — the email exists; you have its ID or name. Continue with Phase 1.

---

## Update mode workflow

### Phase 1 — Identify the target

Ask the user (or take from context):

- **Email ID** if known (the cleanest input — comes from URL or audit output).
- Otherwise, **email name** to look up via the list endpoint:
  ```bash
  curl -s -H "Authorization: Bearer $HUBSPOT_ACCESS_TOKEN" \
    "https://api.hubapi.com/marketing/v3/emails?limit=100&type=AUTOMATED_EMAIL" \
    | python3 -c "import sys,json; d=json.load(sys.stdin); [print(e['id'], e['name']) for e in d['results'] if 'KEYWORD' in e['name']]"
  ```

Confirm the match with the user before proceeding — multiple emails may share keywords.

### Phase 2 — Read current state

```bash
curl -s -H "Authorization: Bearer $HUBSPOT_ACCESS_TOKEN" \
  "https://api.hubapi.com/marketing/v3/emails/$EMAIL_ID" > /tmp/hs-current.json
```

Inspect the relevant fields:
- `name` — internal label, often signals what the email *should* be about
- `subject` — current subject line
- `state` — `AUTOMATED`, `AUTOMATED_DRAFT`, `PUBLISHED`, `DRAFT` (matters for the publish step the user will take, not for the API write)
- `clonedFrom` — if present, this email inherited from another; useful context for cascade clones
- `content.widgets.<module-id>.body.html` — the body HTML

Show the user the current values before writing the new ones — especially the body. Easy to misjudge what to write if the existing copy is fresher than expected.

### Phase 3 — Write the copy

#### Cerkl form follow-up house style (for asset-download follow-up emails)

These are the most common type to update. Pattern observed across the existing 22 form follow-ups:

| Field | Pattern |
|---|---|
| **Subject** | `Access our [asset name]` or `Access the [asset name]` |
| **Opener** | `Thanks for checking out [our] [asset name]. Download the document with the link below:` |
| **Link** | `<a href="<asset URL>">[asset name]</a>` — text matches asset name, href is the actual file URL |
| **Signoff** | `Best regards,<br>{{ contact.hubspot_owner_id.signature }}` |
| **CTA** | `<a href="https://see.cerkl.com/lets-chat">Grab some time to chat here</a>` (font-size 13px) |
| **From name** | `{{ contact.hubspot_owner_id.fullname }}` (personalization token, not a static value) |
| **Reply-to** | `{{ contact.hubspot_owner_id.email }}` |

Full body HTML template (paragraphs styled `margin-bottom: 10px`):

```html
<p style="margin-bottom: 10px;">Thanks for checking out our [ASSET NAME]. Download the document with the link below:</p>
<p style="margin-bottom: 10px;"><a href="[ASSET URL]" rel="noopener">[ASSET NAME]</a></p>
<p style="margin-bottom: 10px;">Best regards,<br>{{ contact.hubspot_owner_id.signature }}<br><br><span style="font-size: 13px;"><a href="https://see.cerkl.com/lets-chat" rel="noopener">Grab some time to chat here</a></span></p>
```

When writing for a new asset, replace the two `[ASSET NAME]` slots and the `[ASSET URL]` href. Don't restructure the HTML — preserving the styling in place keeps the rendered email consistent with the rest of the catalog.

#### Other email types

For non-form-follow-up emails (campaign sends, demo follow-ups, nurture), there is no single house template. Read the existing body to learn the voice, write copy in the same register, and confirm with the user before staging.

### Phase 4 — Stage the draft

**Direct PATCH on a published email returns 400** with the message:
> Cannot directly update a published email. To update the email use PATCH "{emailId}/draft" to update the draft and then POST "{emailId}/publish" to publish the draft.

Always go through `/draft`. Never call `/publish` from this skill (see constraint above).

#### Subject only

```bash
curl -s -X PATCH \
  -H "Authorization: Bearer $HUBSPOT_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"subject":"<new subject>"}' \
  "https://api.hubapi.com/marketing/v3/emails/$EMAIL_ID/draft"
```

#### Body change (with or without subject change)

Read-modify-write the **full** `content` object. Do **not** send a partial `content` payload — partial replacement isn't safe and can drop sibling fields, breaking layout.

```bash
# 1. Build patch payload
python3 <<PY > /tmp/hs-patch.json
import json
e = json.load(open('/tmp/hs-current.json'))
content = e['content']
# Identify the right module (usually module-1-0-0 for form follow-ups; verify in /tmp/hs-current.json)
content['widgets']['module-1-0-0']['body']['html'] = '''<NEW HTML BODY>'''
print(json.dumps({
    'subject': '<new subject>',
    'content': content,
}))
PY

# 2. PATCH the draft
curl -s -X PATCH \
  -H "Authorization: Bearer $HUBSPOT_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  --data-binary @/tmp/hs-patch.json \
  "https://api.hubapi.com/marketing/v3/emails/$EMAIL_ID/draft"
```

#### Verify the write didn't disturb layout

HubSpot normalizes JSON on save — adds explicit nulls for breakpoint defaults, drops some other nulls. This is harmless. To confirm nothing real was disturbed:

```python
before = json.load(open('/tmp/hs-current.json'))['content']
after  = json.load(open('/tmp/hs-result.json'))['content']
assert len(before['widgets']) == len(after['widgets']), 'widget count changed'
assert len(before['flexAreas']['main']['sections']) == len(after['flexAreas']['main']['sections']), 'sections changed'
```

If counts differ, something went wrong. Don't proceed; investigate.

### Phase 5 — Hand off to the user

Tell the user:

1. **Which draft was staged** — email ID, name, what changed (subject, body, both).
2. **Where to publish** — HubSpot → Marketing → Email → find by name → "Review and send" (or "Publish") on the draft.
3. **What you couldn't fix via API** — most often, the **download link `href`**. The text inside the link tag is patchable; swapping the actual file attachment behind a CTA is best done in HubSpot's drag-and-drop editor. Always flag this when the link text changes.

Never claim the email is "live" or "fixed." It's "staged in draft." The user closes the loop.

---

## Create mode workflow

Use when the email doesn't exist yet. The recommended path is **clone-then-modify**: pick an existing email with the right layout/styling and clone it via the API, then overwrite the name, subject, and body. Cloning preserves header, footer, button styles, fonts, and personalization tokens — all of which are tedious to construct from a blank `content` payload.

### Phase A — Pick a template to clone

Identify an existing email whose layout matches what you want (header, footer, button styling, sender, design pattern). For webinar promos, clone the most recent published webinar promo email — they share a pattern.

Look it up by name:
```bash
curl -s -H "Authorization: Bearer $HUBSPOT_ACCESS_TOKEN" \
  "https://api.hubapi.com/marketing/v3/emails?limit=100&type=BATCH_EMAIL" \
  | python3 -c "import sys,json; d=json.load(sys.stdin); [print(e['id'], e['state'], e['name']) for e in d['results'] if 'KEYWORD' in e['name']]"
```

Confirm the template ID with the user before cloning.

### Phase B — Clone the template

The clone endpoint is `POST /marketing/v3/emails/clone` (note: **not** `/{id}/clone` — that path returns 404). The source ID goes in the body:

```bash
curl -s -X POST \
  -H "Authorization: Bearer $HUBSPOT_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"id":"'"$TEMPLATE_ID"'","cloneName":"<new email name, internal label only>"}' \
  "https://api.hubapi.com/marketing/v3/emails/clone"
```

Returns the full new email JSON. Capture the new `id` from the response — that's the target for the next step.

The clone arrives in `DRAFT` state by default, so you can PATCH it directly (no `/draft` indirection needed for unpublished emails — but `/draft` works on drafts too, so use it for consistency).

### Phase C — Overwrite name, subject, and body

Read the cloned email's current state, modify, then PATCH back the full content:

```bash
curl -s -H "Authorization: Bearer $HUBSPOT_ACCESS_TOKEN" \
  "https://api.hubapi.com/marketing/v3/emails/$NEW_ID" > /tmp/hs-clone.json

python3 <<PY > /tmp/hs-clone-patch.json
import json
e = json.load(open('/tmp/hs-clone.json'))
content = e['content']

# Replace body HTML — identify the right module by inspecting /tmp/hs-clone.json
new_body_html = '''<NEW HTML BODY>'''
content['widgets']['module-1-0-0']['body']['html'] = new_body_html

print(json.dumps({
    'name':    '<final email name, internal label>',
    'subject': '<final subject>',
    'content': content,
}))
PY

curl -s -X PATCH \
  -H "Authorization: Bearer $HUBSPOT_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  --data-binary @/tmp/hs-clone-patch.json \
  "https://api.hubapi.com/marketing/v3/emails/$NEW_ID/draft"
```

The same read-modify-write rule applies — never send a partial `content` object.

### Phase D — Hand off

Tell the user:
1. The new draft was created with ID `$NEW_ID`.
2. Where to find it in the UI: HubSpot → Marketing → Email → Drafts tab → search by the new name.
3. **What's NOT set automatically**: send list / segments, send time, A/B variants, subscription type, business unit. Cloning carries the template's settings forward, but list selection often needs to change for the new audience. Flag this explicitly.
4. **Manual review and publish** — same constraint as update mode. Never call `/publish` from this skill.

### Alternative — POST a blank email

If no good template exists, `POST /marketing/v3/emails` with a minimal payload creates a blank email:
```json
{
  "name": "...",
  "subject": "...",
  "type": "BATCH_EMAIL",
  "from": {"fromName": "...", "replyTo": "..."}
}
```
But the resulting email has no body content or layout. Reconstructing the `content.flexAreas` and `content.widgets` structure from scratch is fragile — every working email in the system was built from either a HubSpot template or a clone. Use this path only when the user explicitly wants a stripped-down email.

---

## Endpoint cheat-sheet

| Path | Method | Purpose | Scope |
|---|---|---|---|
| `/marketing/v3/emails` | GET | List emails (filter `?type=`) | `content` |
| `/marketing/v3/emails` | POST | Create blank email | `content` |
| `/marketing/v3/emails/{id}` | GET | Read full email | `content` |
| `/marketing/v3/emails/{id}` | PATCH | **Blocked on published** — returns 400 redirecting to `/draft` | — |
| `/marketing/v3/emails/clone` | POST | Clone an existing email — source ID in body as `{"id":"..."}`. **NOT** `/{id}/clone` (that returns 404). | `content` |
| `/marketing/v3/emails/{id}/draft` | PATCH | Stage draft change | `content` |
| `/marketing/v3/emails/{id}/publish` | POST | Publish — **never call from this skill** | `marketing-email` |

Wrong publish-endpoint guesses to skip: `/revisions/push-live` returns 405. Read HubSpot's 400 error messages — they name the correct path.

## Anti-patterns

- **Calling `/publish`.** Even with scope. Even when "the user said yes once earlier in the session." Confirm at draft time, then hand off.
- **Partial `content` PATCH.** Always read-modify-write the full content object.
- **Inferring "fixed" from a 200 on `/draft`.** A 200 means staged, not published. Live email is unchanged until the user clicks publish.
- **Patching link text without flagging the href.** If the asset name changed, the link target almost certainly changed too — the API can't update file attachments cleanly.
- **Restructuring the body HTML when the user only asked for a copy edit.** Preserve the existing `<p>`, `<span>`, and class styling in place. Only swap the text values.
- **Writing copy without reading the current body first.** The user may have edited it manually since the last clone, and an LLM generating from scratch will overwrite that work.

## Output

This skill doesn't save artifacts by default. The "output" is the staged draft in HubSpot. If the work is part of a larger initiative tracked in `personal-assistant/projects/`, follow the push-update protocol from `hubspot/CLAUDE.md` and append an update block.

## Cross-references

- `audit-marketing-emails` — find which emails need updating in the first place.
- `hubspot/CLAUDE.md` — env load convention, curl-vs-python rule, push-update protocol.

## Learnings (append-only)

### 2026-05-10 — webinar promo template created

- **Clone endpoint is `/marketing/v3/emails/clone` with source ID in the body**, not `/marketing/v3/emails/{id}/clone` as the analog endpoints might suggest. The `{id}/clone` path returns 404. Body shape: `{"id": "<source-id>", "cloneName": "..."}`.
- **Cloned email arrives in DRAFT state** with `clonedFrom` populated. Carries forward: campaign association, subscription type, sender, audience list/segment, content/layout. Does NOT carry forward: send time, A/B variants. The DRAFT state is exactly what we want — no risk of accidental send.
- **Created "Webinar Promo Template" (ID `212619094633`)** as the standing template for `webinar-promo-emails`. Sourced from `211471728030` ("April 2026 Webinar - Matt Frost"). The webinar skill references this ID directly.

### 2026-05-10 — first run, form follow-ups fix

- **Subject-only PATCH was simple.** A `{"subject": "..."}` payload to `/draft` returned 200 with the new subject reflected. Three subject-only fixes ran in seconds.
- **Body PATCH via read-modify-write of full content was surgical.** Replacing the asset name in two spots inside `body.html` preserved all surrounding styling, the `{{ contact.hubspot_owner_id.signature }}` token, and adjacent paragraphs. No round-trip through Markdown needed.
- **HubSpot normalizes JSON on save.** After a body PATCH, the returned JSON had different null/default fields than what was sent — added breakpoint defaults, dropped some sibling nulls. Widget and section counts were unchanged; only the null-default presence shifted. Safe to ignore.
- **Verified the form follow-up house style** by reading 22 emails: subject pattern (`Access our [asset name]`), opener pattern (`Thanks for checking out [our] [asset name]`), signoff with `{{ contact.hubspot_owner_id.signature }}` token, "Grab some time to chat here" CTA at 13px font. Any new form follow-up should match this template unless the user explicitly wants a divergence.
