# design/tools

> Reusable scripts that operate on `branding-assets/`. Cross-channel: any agent producing a deck, one-pager, blog post, ad, or social asset can use these.

## Scripts

| Script | What it does |
|---|---|
| [`compress-images.py`](compress-images.py) | Walks the 3 high-payoff folders (Cerkl Photography, Product Illustration, Social Assets) and writes 2000px-long-edge derivatives into sibling `_web/` folders. Format-aware: JPEG for photos (no transparency), PNG for UI screenshots (real transparency). Idempotent — re-run any time. Typical savings: ~80% on photos, ~60% on screenshots. |
| [`build-image-index.py`](build-image-index.py) | Generates an `INDEX.md` skeleton for a folder of images. Auto-fills physical metadata (file, dim, ratio, KB, BG). Leaves Description / When to use / Avoid blank for the human or next agent to populate. |

## When to use

- **New product screenshots or photos land in branding-assets/** → run `compress-images.py` (no args; it's idempotent and only processes new/changed files)
- **Starting a new project that'll pull from a folder without an INDEX.md** → run `build-image-index.py <folder>` to scaffold one before picking
- **A deck or ad is too big** because of full-res source images → confirm `_web/` exists for the assets used; swap in derivatives

## Usage

```bash
PY=/Library/Frameworks/Python.framework/Versions/3.11/bin/python3

# Compress all 3 scope folders (idempotent)
$PY compress-images.py

# Just one folder
$PY compress-images.py --folder "Cerkl Photography"

# Preview without writing
$PY compress-images.py --dry-run

# Build INDEX skeleton for one folder
$PY build-image-index.py "../branding-assets/Product Illustration/Product Images/Email Blasts"

# Walk subfolders, one INDEX per folder
$PY build-image-index.py "../branding-assets/Product Illustration/Product Images" --recurse
```

## Conventions

- **`_web/` folders are derivatives.** Source files are the truth. Delete `_web/` to regenerate. Use derivatives in decks/ads/blog posts; reference source paths in brand docs.
- **Format choice is automatic.** If you need a specific format, edit the source or hand-convert. Don't fight the script.
- **INDEX-skeleton.md vs INDEX.md.** Builder writes `INDEX.md` when none exists, `INDEX-skeleton.md` when one does, so it never clobbers human judgment. Merge manually if needed.

## Scope (intentionally narrow)

Compression targets only the 3 folders where the 80/20 payoff lives:
- `Cerkl Photography/` — 22 photos, ~140 MB
- `Product Illustration/` — 157 PNGs, ~127 MB
- `Social Assets/` — 61 PNGs, ~53 MB

The other 11 branding-assets folders (Brand Icons, lockups, Customer Logos, Canva sources, etc.) are either already small, vector, or shouldn't be downsized (logos are served at exact sizes; lossy compression breaks them). Expand scope only if a specific folder starts blocking work.

## Dependencies

- Python 3.11+
- Pillow (`pip install pillow`)
