#!/usr/bin/env bash
# html-to-pdf — render an HTML file to PDF via Chrome headless.
#
# By default, runs the html-overflow-detector first as a verify gate. If the
# HTML has layout overflow, the render is skipped and the script exits with
# the detector's exit code — so the caller can apply remediation BEFORE a
# flawed PDF exists on disk.
#
# Usage:
#   run.sh <path-to-html> [output-pdf-path] [--skip-verify]
#
# Defaults:
#   output-pdf-path: same dir + same basename + .pdf  (e.g., foo.html → foo.pdf)
#   --skip-verify : bypass the overflow detector (use ONLY when you know the
#                   HTML doesn't follow the .page convention — e.g., generic
#                   single-flow docs the detector wouldn't understand)
#
# Exit codes:
#   0  — PDF written successfully
#   1  — overflow detector found issues; PDF NOT written
#   2  — bad arguments
#   3  — Chrome render failed
#   4  — output file unexpectedly empty/missing

set -uo pipefail

if [ $# -lt 1 ]; then
  echo "usage: $0 <path-to-html> [output-pdf-path] [--skip-verify]" >&2
  exit 2
fi

SRC="$1"
shift || true

OUT=""
SKIP_VERIFY=0
while [ $# -gt 0 ]; do
  case "$1" in
    --skip-verify) SKIP_VERIFY=1 ;;
    *) OUT="$1" ;;
  esac
  shift
done

if [ ! -f "$SRC" ]; then
  echo "ERROR: html file not found: $SRC" >&2
  exit 2
fi

# Resolve output path: default = sibling .pdf
if [ -z "$OUT" ]; then
  SRC_DIR="$(cd "$(dirname "$SRC")" && pwd)"
  SRC_BASE="$(basename "$SRC")"
  OUT="$SRC_DIR/${SRC_BASE%.html}.pdf"
fi

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
if [ ! -x "$CHROME" ]; then
  echo "ERROR: Chrome not found at $CHROME" >&2
  exit 2
fi

# --- VERIFY GATE -----------------------------------------------------------
SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DETECTOR="$SKILL_DIR/../html-overflow-detector/run.sh"

if [ "$SKIP_VERIFY" -eq 0 ] && [ -x "$DETECTOR" ]; then
  echo "Verifying layout with html-overflow-detector…"
  if ! "$DETECTOR" "$SRC"; then
    echo
    echo "✗ Verify gate FAILED. PDF not written. Apply remediation, then re-run." >&2
    echo "  (To bypass — e.g., for non-paginated HTML — re-run with --skip-verify)" >&2
    exit 1
  fi
  echo "✓ Layout verified."
fi

# --- RENDER ---------------------------------------------------------------
SRC_ABS="$(cd "$(dirname "$SRC")" && pwd)/$(basename "$SRC")"

"$CHROME" --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf="$OUT" \
  "file://$SRC_ABS" 2>/dev/null

if [ ! -s "$OUT" ]; then
  echo "ERROR: render produced empty/missing PDF at $OUT" >&2
  exit 4
fi

# Page-count sanity: report it for the caller's audit log.
PAGES=$(mdls -name kMDItemNumberOfPages "$OUT" 2>/dev/null | grep -oE '[0-9]+' | head -1)
SIZE=$(ls -lh "$OUT" | awk '{print $5}')
echo "✓ PDF written: $OUT  ($SIZE, $PAGES page(s))"
