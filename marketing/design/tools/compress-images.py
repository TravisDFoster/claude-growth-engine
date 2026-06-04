#!/usr/bin/env python3
"""
Batch-compress large PNGs in the branding-assets library into sibling _web/
folders for fast inclusion in decks, ads, blog posts, and Claude context.

Scope (high-payoff only — ~80% of disk + token savings):
  - branding-assets/Cerkl Photography/
  - branding-assets/Product Illustration/
  - branding-assets/Social Assets/

Behavior:
  - Walks each scope folder recursively
  - For every PNG above the size or dimension threshold, writes a 2000px-long-edge
    copy into a sibling `_web/` folder, preserving filename
  - Idempotent: skips re-processing if _web/<file>.png is newer than the source
  - Preserves transparency
  - Reports before/after totals at the end

Usage:
  python3 compress-images.py            # process all scope folders
  python3 compress-images.py --dry-run  # show what would happen, don't write
  python3 compress-images.py --folder "Cerkl Photography"   # restrict scope
"""

import argparse
import os
import sys
from pathlib import Path
from PIL import Image

BRAND_ROOT = Path(__file__).resolve().parent.parent / "branding-assets"

SCOPE = [
    "Cerkl Photography",
    "Product Illustration",
    "Social Assets",
]

LONG_EDGE = 2000          # target pixels on long edge
MIN_SIZE_KB = 200         # skip files already smaller than this (likely icons/logos)
JPEG_QUALITY = 85         # photo derivative quality (visually indistinguishable from source)
WEB_DIR = "_web"

def needs_processing(path: Path) -> bool:
    """Skip files already small enough to not need a web derivative."""
    return path.stat().st_size >= MIN_SIZE_KB * 1024

def is_up_to_date(src: Path, dst: Path) -> bool:
    return dst.exists() and dst.stat().st_mtime >= src.stat().st_mtime

def has_real_transparency(im: Image.Image) -> bool:
    """True only if the image actually uses its alpha for layering (UI screenshots),
    not just slight alpha artifacts on photo exports. We require any sampled
    pixel to be nearly fully transparent (< 30/255)."""
    if im.mode not in ("RGBA", "LA", "P"):
        return False
    rgba = im.convert("RGBA")
    w, h = rgba.size
    # Sample corners + edge midpoints + center — covers most UI mockup shapes
    pts = [(0, 0), (w-1, 0), (0, h-1), (w-1, h-1),
           (w//2, 0), (w//2, h-1), (0, h//2), (w-1, h//2),
           (w//2, h//2)]
    return any(rgba.getpixel(p)[3] < 30 for p in pts)

def derivative_path(src: Path, format_: str) -> Path:
    """_web/<name>.{png|jpg} sibling to source."""
    ext = ".jpg" if format_ == "JPEG" else ".png"
    return src.parent / WEB_DIR / (src.stem + ext)

def resize_to_web(src: Path, dst: Path, format_: str, dry_run: bool):
    if dry_run:
        return
    dst.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(src) as im:
        if max(im.size) > LONG_EDGE:
            im.thumbnail((LONG_EDGE, LONG_EDGE), Image.LANCZOS)
        if format_ == "JPEG":
            im = im.convert("RGB")
            im.save(dst, "JPEG", quality=JPEG_QUALITY, optimize=True, progressive=True)
        else:
            if im.mode == "P":
                im = im.convert("RGBA")
            im.save(dst, "PNG", optimize=True)

def choose_format(src: Path) -> str:
    """JPEG for solid-background photos/screenshots, PNG for anything with real transparency."""
    try:
        with Image.open(src) as im:
            return "PNG" if has_real_transparency(im) else "JPEG"
    except Exception:
        return "PNG"

def process_folder(scope_folder: Path, dry_run: bool):
    if not scope_folder.is_dir():
        print(f"  ⚠️  not found: {scope_folder}", file=sys.stderr)
        return 0, 0, 0, 0  # processed, skipped, src_bytes, dst_bytes

    processed = skipped = 0
    src_total = dst_total = 0

    for src in sorted(scope_folder.rglob("*.png")):
        # Don't process files already inside a _web/ folder
        if WEB_DIR in src.parts:
            continue
        if not needs_processing(src):
            skipped += 1
            continue

        fmt = choose_format(src)
        dst = derivative_path(src, fmt)

        if is_up_to_date(src, dst):
            skipped += 1
            continue

        src_kb = src.stat().st_size / 1024
        try:
            resize_to_web(src, dst, fmt, dry_run)
        except Exception as e:
            print(f"  ❌  {src.relative_to(BRAND_ROOT)}: {e}", file=sys.stderr)
            continue

        dst_kb = (dst.stat().st_size / 1024) if (dst.exists() and not dry_run) else 0
        src_total += src_kb
        dst_total += dst_kb
        processed += 1
        rel = src.relative_to(scope_folder)
        if dry_run:
            print(f"  → {rel}  ({src_kb:.0f} KB → {fmt.lower()})  [dry-run]")
        else:
            ratio = (dst_kb / src_kb * 100) if src_kb else 0
            print(f"  → {rel}  {src_kb:.0f} KB → {dst_kb:.0f} KB ({fmt.lower()}, {ratio:.0f}%)")

    return processed, skipped, src_total, dst_total

def main():
    ap = argparse.ArgumentParser(description="Batch-compress branding-assets PNGs into sibling _web/ folders.")
    ap.add_argument("--dry-run", action="store_true", help="Show what would happen, don't write.")
    ap.add_argument("--folder", help="Restrict to a single scope folder (e.g. 'Cerkl Photography').")
    args = ap.parse_args()

    folders = [args.folder] if args.folder else SCOPE
    grand_p = grand_s = 0
    grand_src = grand_dst = 0.0

    for name in folders:
        scope = BRAND_ROOT / name
        print(f"\n📂 {name}")
        p, s, src_kb, dst_kb = process_folder(scope, args.dry_run)
        print(f"   processed={p}  skipped={s}  {src_kb/1024:.1f} MB → {dst_kb/1024:.1f} MB")
        grand_p += p; grand_s += s; grand_src += src_kb; grand_dst += dst_kb

    print(f"\n✅ done. processed={grand_p}  skipped={grand_s}")
    print(f"   {grand_src/1024:.1f} MB → {grand_dst/1024:.1f} MB"
          f"  ({(grand_dst/grand_src*100 if grand_src else 0):.0f}% of original)")
    if args.dry_run:
        print("   (dry run — no files written)")

if __name__ == "__main__":
    main()
