# LinkedIn Canva Manifests

Per-draft Canva render manifests. **Canonical store** for what was rendered, when, and where the design lives.

## Convention

One file per eligible LinkedIn draft:

```
canva-manifests/<draft-slug>.yml
```

The `<draft-slug>` matches the draft `.md` filename slug (the kebab part after the post-type prefix). Example:

- Draft: `drafts/2026-06-09_static-theme_financial-services-double-mandate.md`
- Manifest: `canva-manifests/financial-services-double-mandate.yml`

## Lifecycle

1. **Scaffolded** by [`linkedin-asset-process.md`](../linkedin-asset-process.md) Step 2 from the draft's `## Asset` section + [`asset-packs.md`](../asset-packs.md) selector table.
2. **Consumed** by parallel sub-agents (one per manifest) that invoke [`template-fill`](../../design/canva-skills/template-fill/SKILL.md).
3. **Updated** by the orchestrator (Step 5) — `result:` block appended with the rendered design's URL, timestamp, warnings, and any `manual_drag_required` entries.
4. **Mirrored** to the Jira CSV `Asset:` line on the matching Task (Step 6).

The manifest is the audit trail. To re-render a single asset, edit its manifest and re-run the process with `subset: [<slug>]`.

## Schema

See [`asset-packs.md` § Manifest generation rule](../asset-packs.md#manifest-generation-rule). Same schema as `webinar/<event>/canva-manifests/<role>.yml` — cross-channel consistency.

## Eligibility

Only drafts of type `carousel`, `static-theme` (non-webinar-wrap), get manifests. Skipped types and their reasons:

| Post type / case | Skip reason |
|---|---|
| `static-blog` | LinkedIn auto-renders the link card from blog OG image |
| `poll` | Native LinkedIn poll widget — no Canva asset |
| `short-video` | Video pipeline, not Canva |
| Any post wrapping a webinar | Webinar process owns the render; LinkedIn process reads the URL from `webinar/<event>/canva-manifests/<role>.yml` |
