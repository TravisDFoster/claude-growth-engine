#!/usr/bin/env bash
# html-overflow-detector — scan an HTML file for layout overflow + overlap
# before generating a PDF. Returns 0 if PASS, 1 if FAIL.
#
# Usage:
#   run.sh <path-to-html>
#
# How it works:
#   1. Copies the source HTML to a temp file with detector.js injected before </body>
#   2. Runs Chrome headless with --dump-dom on the temp file (renders + executes JS)
#   3. Extracts the <pre id="__overflow_report__" data-status=> contents (JSON) from the DOM dump
#   4. Pretty-prints the report; sets exit code by status

set -uo pipefail

if [ $# -lt 1 ]; then
  echo "usage: $0 <path-to-html>" >&2
  exit 2
fi

SRC="$1"
if [ ! -f "$SRC" ]; then
  echo "ERROR: file not found: $SRC" >&2
  exit 2
fi

SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DETECTOR_JS="$SKILL_DIR/detector.js"
if [ ! -f "$DETECTOR_JS" ]; then
  echo "ERROR: detector.js missing at $DETECTOR_JS" >&2
  exit 2
fi

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
if [ ! -x "$CHROME" ]; then
  echo "ERROR: Chrome not found at $CHROME" >&2
  exit 2
fi

# Build instrumented HTML in a temp dir alongside the source (so relative paths resolve)
SRC_DIR="$(cd "$(dirname "$SRC")" && pwd)"
SRC_NAME="$(basename "$SRC")"
TMP_NAME=".__overflow_probe_${SRC_NAME}"
TMP_PATH="$SRC_DIR/$TMP_NAME"
trap 'rm -f "$TMP_PATH"' EXIT

# Inject the detector script before </body>. Use a marker that's unlikely to collide.
awk -v js_path="$DETECTOR_JS" '
  /<\/body>/ && !injected {
    print "<script>"
    while ((getline line < js_path) > 0) print line
    print "</script>"
    injected = 1
  }
  { print }
' "$SRC" > "$TMP_PATH"

# Render and dump the post-JS DOM. --virtual-time-budget gives the detector a moment to run.
DOM_DUMP=$("$CHROME" --headless --disable-gpu --hide-scrollbars \
  --virtual-time-budget=4000 \
  --run-all-compositor-stages-before-draw \
  --dump-dom "file://$TMP_PATH" 2>/dev/null)

# Extract the report. The detector writes <pre id="__overflow_report__" data-status="…" data-count="…">.
# Match strictly on the rendered <pre> tag (data-status attr is unique to the element —
# stray "__overflow_report__" references inside <script> blocks don't have it).
STATUS=$(printf '%s' "$DOM_DUMP" | grep -oE '<pre id="__overflow_report__" data-status="[A-Z]+"' | grep -oE 'data-status="[A-Z]+"' | head -1 | sed -E 's/data-status="([A-Z]+)"/\1/')
COUNT=$(printf '%s' "$DOM_DUMP" | grep -oE '<pre id="__overflow_report__" data-status="[A-Z]+" data-count="[0-9]+"' | grep -oE 'data-count="[0-9]+"' | head -1 | sed -E 's/data-count="([0-9]+)"/\1/')
# Pull the JSON content between the rendered <pre id="__overflow_report__" data-status=...> and </pre>.
# The opening <pre ...> tag and the JSON's first "{" usually share a line, so
# strip everything up through the closing ">" of the pre tag on the opening line.
REPORT_JSON=$(printf '%s' "$DOM_DUMP" | awk '
  !capture && /<pre id="__overflow_report__" data-status=/ {
    capture = 1
    sub(/^.*<pre id="__overflow_report__" data-status=[^>]*>/, "", $0)
    if (/<\/pre>/) {
      sub(/<\/pre>.*$/, "", $0)
      print $0
      exit
    }
    buf = $0 "\n"
    next
  }
  capture && /<\/pre>/ {
    sub(/<\/pre>.*$/, "", $0)
    buf = buf $0
    print buf
    exit
  }
  capture { buf = buf $0 "\n" }
')

if [ -z "$STATUS" ]; then
  echo "ERROR: detector report not found in DOM dump — JS may not have run." >&2
  echo "(rendered HTML may be at $TMP_PATH)" >&2
  exit 3
fi

echo "Overflow detector: $STATUS ($COUNT issue(s)) — $SRC"
if [ "$STATUS" = "FAIL" ]; then
  # Decode HTML entities (&quot; &amp; &lt; &gt;) so JSON is readable
  printf '%s' "$REPORT_JSON" \
    | sed -e 's/&quot;/"/g' -e 's/&amp;/\&/g' -e 's/&lt;/</g' -e 's/&gt;/>/g'
  echo
  exit 1
fi

exit 0
