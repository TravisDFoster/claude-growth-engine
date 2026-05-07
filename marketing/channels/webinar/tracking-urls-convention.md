# Tracking URL Naming Convention

Each webinar registration source gets its own Zoom registration URL so we can attribute registrants to the channel that referred them. URLs are created manually in the Zoom portal; **this doc governs the naming**.

## Format

`<source>_<channel>`

- `<source>` — `cerkl` or the partner slug used in the event folder name (e.g., `matt-frost`)
- `<channel>` — the promo channel that will use the URL

## Standard channels (create these for every webinar)

| Slug | Used by | Description |
|---|---|---|
| `cerkl_linkedin` | Cerkl | LinkedIn posts from the Cerkl company page (and Tarek's account) |
| `cerkl_email` | Cerkl | Promotional email blasts to the marketing list |
| `cerkl_customer-success` | Cerkl | CS team outreach to existing customers |
| `cerkl_cerklular` | Cerkl | The Cerkular newsletter |
| `cerkl_icpro` | Cerkl | IC Pro audience |
| `cerkl_sales` | Cerkl | Sales team outreach |
| `cerkl_innercerkl-news` | Cerkl | Internal Cerkl team newsletter |
| `<partner>_linkedin` | Partner | LinkedIn posts from the partner's account |
| `<partner>_email` | Partner | Email sends from the partner's list |
| `<partner>_website` | Partner | The partner's website / link in bio |

Add additional `<source>_<channel>` slugs as new promo channels are activated.

## Where the URLs live

Each event folder has a `<speaker-slug>-tracking-urls.md` file scaffolded by the `webinar-project-init` skill. It lists the slugs above with empty Zoom URL slots for you to fill in after creating them in the Zoom portal.
