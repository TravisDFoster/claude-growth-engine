// html-overflow-detector — injected into a target HTML page to flag layout
// problems before a PDF is generated. Walks the .page divs, detects:
//   1. content extending past the bottom of its .page container
//   2. sibling elements that overlap vertically when they should stack
//   3. elements whose scrollHeight exceeds clientHeight (clipped content)
// Writes results to a hidden <pre id="__overflow_report__"> element. The
// wrapper script then dumps the DOM and extracts the report.

(function () {
  function cssPath(el) {
    const parts = [];
    let cur = el;
    while (cur && cur.tagName && cur.tagName !== 'HTML') {
      let part = cur.tagName.toLowerCase();
      if (cur.id) part += '#' + cur.id;
      if (cur.classList && cur.classList.length) {
        part += '.' + Array.from(cur.classList).join('.');
      }
      parts.unshift(part);
      cur = cur.parentElement;
    }
    return parts.join(' > ');
  }

  function snippet(el, max) {
    const txt = (el.textContent || '').replace(/\s+/g, ' ').trim();
    return txt.length > max ? txt.slice(0, max) + '…' : txt;
  }

  function runDetector() {
    const issues = [];
    const pages = document.querySelectorAll('.page');

    pages.forEach(function (page, idx) {
      const pageRect = page.getBoundingClientRect();
      const pageBottom = pageRect.bottom;
      const pageRight = pageRect.right;

      // 1. Content that escapes the page's bottom edge.
      //    Skip elements that are inside a parent already flagged, to avoid
      //    cascade noise — we want the offender, not its descendants.
      const offenders = [];
      page.querySelectorAll('*').forEach(function (el) {
        // Skip the detector report itself
        if (el.id === '__overflow_report__') return;
        // Skip elements with no rendered box (display:none, etc.)
        const elRect = el.getBoundingClientRect();
        if (elRect.width === 0 && elRect.height === 0) return;

        if (elRect.bottom > pageBottom + 1.5) {
          offenders.push({ el: el, rect: elRect });
        }
      });
      // Filter to outermost offenders (not nested under another offender)
      offenders.forEach(function (o) {
        const isNested = offenders.some(function (p) {
          return p.el !== o.el && p.el.contains(o.el);
        });
        if (!isNested) {
          issues.push({
            page: idx + 1,
            type: 'overflow-page-bottom',
            selector: cssPath(o.el),
            overrun_px: Math.round(o.rect.bottom - pageBottom),
            text: snippet(o.el, 80)
          });
        }
      });

      // 2. Sibling overlap within layout containers (stacking ones).
      //    A child whose bottom extends past the top of the next sibling
      //    is overlapping it. Excludes side-by-side flex/grid rows AND
      //    elements taken out of flow (position: absolute / fixed) — those
      //    are intentionally layered (e.g., decorative blobs, mockup overlays).
      const stackContainers = page.querySelectorAll(
        '.page-body, .feature-grid, .bullet-grid, .icon-row-list, .editorial-2col, .cta-strip, .hero-cover, .hero-cover .title-block'
      );
      stackContainers.forEach(function (container) {
        const children = Array.from(container.children).filter(function (c) {
          const r = c.getBoundingClientRect();
          if (r.width === 0 && r.height === 0) return false;
          const pos = window.getComputedStyle(c).position;
          if (pos === 'absolute' || pos === 'fixed') return false;
          return true;
        });
        for (let i = 0; i < children.length; i++) {
          const a = children[i].getBoundingClientRect();
          for (let j = i + 1; j < children.length; j++) {
            const b = children[j].getBoundingClientRect();
            // Are they meant to be vertically stacked? (Y axis differs more than X)
            const stackedVertically = b.top >= a.top - 4;
            if (!stackedVertically) continue;
            // Horizontal overlap?
            const hOverlap = Math.min(a.right, b.right) - Math.max(a.left, b.left);
            if (hOverlap <= 0) continue;
            // Vertical overlap (A bottom past B top)?
            const vOverlap = a.bottom - b.top;
            if (vOverlap > 1.5) {
              issues.push({
                page: idx + 1,
                type: 'sibling-overlap',
                container: cssPath(container),
                upper: cssPath(children[i]),
                lower: cssPath(children[j]),
                overlap_px: Math.round(vOverlap),
                text_upper: snippet(children[i], 60),
                text_lower: snippet(children[j], 60)
              });
            }
          }
        }
      });

      // 3. Clipped content: scrollHeight > clientHeight on overflow:hidden boxes.
      page.querySelectorAll('*').forEach(function (el) {
        if (el.id === '__overflow_report__') return;
        const style = window.getComputedStyle(el);
        const hidden = style.overflowY === 'hidden' || style.overflow === 'hidden';
        if (!hidden) return;
        if (el.scrollHeight - el.clientHeight > 2) {
          issues.push({
            page: idx + 1,
            type: 'content-clipped',
            selector: cssPath(el),
            clipped_px: el.scrollHeight - el.clientHeight,
            text: snippet(el, 80)
          });
        }
      });
    });

    // Dedupe issues that point to the same selector + type
    const seen = new Set();
    const deduped = issues.filter(function (iss) {
      const key = iss.page + '|' + iss.type + '|' + (iss.selector || iss.upper + '+' + iss.lower);
      if (seen.has(key)) return false;
      seen.add(key);
      return true;
    });

    const status = deduped.length === 0 ? 'PASS' : 'FAIL';
    const report = document.createElement('pre');
    report.id = '__overflow_report__';
    report.setAttribute('data-status', status);
    report.setAttribute('data-count', String(deduped.length));
    report.style.cssText = 'position:fixed;top:-99999px;left:-99999px;width:1px;height:1px;overflow:hidden;';
    report.textContent = JSON.stringify({ status: status, count: deduped.length, issues: deduped }, null, 2);
    document.body.appendChild(report);
  }

  if (document.readyState === 'complete') {
    setTimeout(runDetector, 50);
  } else {
    window.addEventListener('load', function () {
      setTimeout(runDetector, 50);
    });
  }
})();
