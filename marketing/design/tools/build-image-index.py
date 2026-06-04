#!/usr/bin/env python3
"""
Generate an INDEX.md skeleton for any folder of images in branding-assets.

Auto-fills the cheap-to-get columns (file, dimensions, ratio, KB, background)
so future agents only do the judgment work (description, when-to-use, avoid flags).

Usage:
  python3 build-image-index.py "<folder>"           # single folder, write INDEX.md (or INDEX-skeleton.md if INDEX.md exists)
  python3 build-image-index.py "<folder>" --recurse # walk subfolders too, one INDEX per folder
  python3 build-image-index.py "<folder>" --force   # overwrite an existing INDEX.md

Examples:
  python3 build-image-index.py "../branding-assets/Product Illustration/Product Images/Email Blasts"
  python3 build-image-index.py "../branding-assets/Product Illustration/Product Images" --recurse
"""

import argparse
import sys
from pathlib import Path
from PIL import Image
from math import gcd

IMG_EXTS = {".png", ".jpg", ".jpeg", ".webp"}

def aspect_ratio(w: int, h: int) -> str:
    g = gcd(w, h) or 1
    r_w, r_h = w // g, h // g
    # Round to common ratios when close
    common = {(16, 9), (16, 10), (4, 3), (3, 2), (1, 1), (21, 9), (9, 16), (2, 3), (3, 4)}
    val = r_w / r_h
    for cw, ch in common:
        if abs(val - cw/ch) / (cw/ch) < 0.03:
            return f"{cw}:{ch}"
    return f"{r_w}:{r_h}" if r_w < 100 and r_h < 100 else f"{val:.2f}:1"

def background(im: Image.Image) -> str:
    """Best-effort: transparent if alpha exists and has any transparency, else solid."""
    if im.mode in ("RGBA", "LA") or "transparency" in im.info:
        # Check corner pixels for transparency
        try:
            rgba = im.convert("RGBA")
            corners = [rgba.getpixel(p) for p in [(0, 0), (rgba.width-1, 0), (0, rgba.height-1), (rgba.width-1, rgba.height-1)]]
            if any(c[3] < 250 for c in corners):
                return "transparent"
        except Exception:
            pass
    return "solid"

def gather_rows(folder: Path):
    rows = []
    for p in sorted(folder.iterdir()):
        if p.is_dir() or p.suffix.lower() not in IMG_EXTS:
            continue
        try:
            with Image.open(p) as im:
                w, h = im.size
                bg = background(im)
        except Exception as e:
            print(f"  ⚠️  could not read {p.name}: {e}", file=sys.stderr)
            continue
        size_kb = round(p.stat().st_size / 1024)
        rows.append({
            "file": p.name,
            "dim": f"{w}×{h}",
            "ratio": aspect_ratio(w, h),
            "kb": size_kb,
            "bg": bg,
        })
    return rows

def render_index(folder: Path, rows: list[dict]) -> str:
    rel = folder.name
    web_dir = folder / "_web"
    has_web = web_dir.is_dir() and any(p.is_file() for p in web_dir.iterdir())
    out = []
    out.append(f"# {rel}")
    out.append("")
    out.append(f"> {len(rows)} images. Auto-generated skeleton — populate Description, When to use, and Avoid columns as the folder gets used.")
    if has_web:
        out.append(f"> **`_web/` derivatives available** — use the 2000px JPEG/PNG copies for embedded slide / blog / ad assets (~10–60% of source size).")
    out.append(f"> Regenerate physical-metadata columns: `python3 cerkl/marketing/design/tools/build-image-index.py <this folder>`")
    out.append("")
    out.append("| File | Dim | Ratio | KB | BG | Description | When to use | Avoid |")
    out.append("|---|---|---|---:|---|---|---|---|")
    for r in rows:
        out.append(f"| `{r['file']}` | {r['dim']} | {r['ratio']} | {r['kb']} | {r['bg']} |  |  |  |")
    out.append("")
    return "\n".join(out)

def write_index(folder: Path, force: bool) -> str | None:
    rows = gather_rows(folder)
    if not rows:
        return None
    content = render_index(folder, rows)
    target = folder / "INDEX.md"
    if target.exists() and not force:
        target = folder / "INDEX-skeleton.md"
        print(f"   (INDEX.md exists — writing skeleton to {target.name} instead)")
    target.write_text(content)
    return str(target)

def main():
    ap = argparse.ArgumentParser(description="Generate INDEX.md skeletons for image folders.")
    ap.add_argument("folder", help="Folder of images to index.")
    ap.add_argument("--recurse", action="store_true", help="Walk subfolders too; one INDEX per folder.")
    ap.add_argument("--force", action="store_true", help="Overwrite existing INDEX.md (default: write INDEX-skeleton.md).")
    args = ap.parse_args()

    root = Path(args.folder).expanduser().resolve()
    if not root.is_dir():
        print(f"❌ not a folder: {root}", file=sys.stderr)
        sys.exit(1)

    folders = [root]
    if args.recurse:
        folders += [p for p in root.rglob("*") if p.is_dir() and p.name not in {"_web"}]

    written = 0
    for f in folders:
        # Skip folders with no images
        if not any(p.suffix.lower() in IMG_EXTS for p in f.iterdir() if p.is_file()):
            continue
        print(f"\n📂 {f.relative_to(root.parent) if f != root else f.name}")
        result = write_index(f, args.force)
        if result:
            print(f"   ✓ wrote {Path(result).name}")
            written += 1

    print(f"\n✅ done. wrote {written} INDEX file(s).")

if __name__ == "__main__":
    main()
