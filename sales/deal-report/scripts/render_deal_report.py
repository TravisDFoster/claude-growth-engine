# /// script
# requires-python = ">=3.9"
# ///
"""
render_deal_report.py — deterministic HTML for the Deal Report.

Reuses the weekly Sales Pipeline Report's locked CSS verbatim (single styling
source of truth — no second stylesheet to drift) and adds a small block of
band-badge styles. Renders a team summary + one section per owner, deals sorted
worst-health-first, each row showing its metrics and the plain-English `reasons`
the score was built from (the audit trail).

Standalone re-render (no re-pull):  uv run render_deal_report.py ../tmp/deal-report.json
"""

import html
import os
import sys

DEAL_REPORT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_SALES = os.path.dirname(DEAL_REPORT)
sys.path.insert(0, os.path.join(_SALES, "sales-reporting", "scripts"))

import render_report as rr  # esc, money, extract_style — shared styling source

BAND_LABEL = {"at_risk": "At risk", "watch": "Watch", "healthy": "Healthy"}
# Extra styles layered on top of the weekly report's CSS (band badges + reason chips).
EXTRA_CSS = """<style>
.band{display:inline-block;padding:2px 9px;border-radius:11px;font-size:11px;font-weight:700;
 letter-spacing:.02em;text-transform:uppercase;white-space:nowrap}
.band.at_risk{background:#fde7e7;color:#b42318}
.band.watch{background:#fef3d7;color:#9a6700}
.band.healthy{background:#e3f5ea;color:#197048}
.reasons{color:#667085;font-size:12px}
.nurture-tag{display:inline-block;margin-left:6px;padding:1px 7px;border-radius:10px;
 background:#eef0f3;color:#475467;font-size:10px;font-weight:600}
.owner-head{display:flex;align-items:baseline;gap:12px;margin:26px 0 6px}
.owner-head h3{margin:0;font-size:17px}
.owner-head .o-meta{color:#667085;font-size:13px}
</style>"""


def esc(x):
    return rr.esc(x)


def money(x):
    return rr.money(x)


def num(v, suffix=""):
    return f"{v}{suffix}" if v is not None else "—"


def deal_row(d):
    name = esc(d["name"])
    link = f'<a href="{esc(d["url"])}" target="_blank" rel="noopener noreferrer">{name}</a>'
    nurture = '<span class="nurture-tag">nurture?</span>' if d.get("nurture_candidate") else ""
    reply = f'{d.get("email_sent", 0)}/{d.get("email_received", 0)}'
    tasks = f'{d.get("tasks_open", 0)}'
    if d.get("tasks_overdue"):
        tasks += f' ({d["tasks_overdue"]} overdue)'
    reasons = esc(" · ".join(d.get("reasons", []))) or "—"
    return (
        f'<tr><td>{link}{nurture}<div class="reasons">{reasons}</div></td>'
        f'<td><span class="band {d["band"]}">{BAND_LABEL.get(d["band"], d["band"])}</span></td>'
        f'<td>{esc(d["stage"])}</td>'
        f'<td class="num">{money(d["amount"])}</td>'
        f'<td class="num">{num(d.get("recency_days"), "d")}</td>'
        f'<td class="num">{num(d.get("stage_age_days"), "d")}</td>'
        f'<td class="num">{num(d.get("age_days"), "d")}</td>'
        f'<td class="num">{d.get("slippage_count", 0)}</td>'
        f'<td class="num">{reply}</td>'
        f'<td class="num">{tasks}</td>'
        f'<td class="num">{d.get("contacts", 0)}</td></tr>'
    )


def owner_section(owner, deals):
    bands = {b: sum(1 for d in deals if d["band"] == b) for b in ("at_risk", "watch", "healthy")}
    amt = sum(d["amount"] or 0 for d in deals)
    head = (f'<div class="owner-head"><h3>{esc(owner)}</h3>'
            f'<span class="o-meta">{len(deals)} deals · {money(amt)} · '
            f'{bands["at_risk"]} at risk · {bands["watch"]} watch · {bands["healthy"]} healthy</span></div>')
    rows = "".join(deal_row(d) for d in deals)
    table = (
        '<table class="data"><thead><tr><th>Deal</th><th>Health</th><th>Stage</th>'
        '<th class="num">Amount</th><th class="num">Last touch</th><th class="num">In stage</th>'
        '<th class="num">Age</th><th class="num">Slips</th><th class="num">Sent/Rcv</th>'
        '<th class="num">Tasks</th><th class="num">Contacts</th></tr></thead>'
        f'<tbody>{rows}</tbody></table>'
    )
    return head + table


def hero(s):
    b = s["bands"]
    stats = [
        ("Deals analyzed", s["deal_count"], "active open"),
        ("At risk", b["at_risk"], "need action"),
        ("Watch", b["watch"], "monitor"),
        ("Healthy", b["healthy"], "on track"),
        ("Nurture candidates", s["nurture_candidates"], "flagged"),
    ]
    cards = "".join(
        f'<div class="h-stat{" zero" if n == 0 else ""}"><div class="h-num">{n}</div>'
        f'<div class="h-sub">{sub}</div><div class="h-lbl">{lbl}</div></div>'
        for lbl, n, sub in stats
    )
    return (
        '<header class="hero"><div class="breadcrumb">sales · deal report</div>'
        '<h1>Deal Report — Health Drilldown</h1>'
        '<div class="meta-row">'
        f'<span><b>Scope:</b> {esc(s["scope"])}</span>'
        f'<span><b>Reps:</b> {esc(" · ".join(s["owners"]))}</span>'
        f'<span><b>Generated:</b> {esc(s["generated_at"])}</span></div>'
        f'<div class="hero-stats">{cards}</div>'
        '<p class="tldr-strip">Rules-based health over active open Sales + RFP deals, '
        'worst-first by owner. <b>Health</b> is a transparent score (see <code>score.py</code>); '
        'the chips under each deal are the exact signals that drove it. '
        'Deals banded <b>watch</b>/<b>at risk</b> are the queue for the Phase-2 inference pass.</p>'
        '</header>'
    )


def footer(s):
    return f'<footer>Generated {esc(s["generated_at"])}</footer>'


def render_html(s):
    style_block = rr.extract_style()  # weekly report's CSS, verbatim
    body_sections = [hero(s)]
    # Group by owner, preserving the worst-first sort within each owner.
    for owner in s["owners"]:
        od = [d for d in s["deals"] if d["owner"] == owner]
        if od:
            body_sections.append(f"<section>{owner_section(owner, od)}</section>")
    body_sections.append(footer(s))
    body = "\n".join(body_sections)
    return (
        '<!doctype html>\n<html lang="en">\n<head>\n'
        '<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<title>Deal Report — Health Drilldown</title>\n'
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Work+Sans:wght@400;500;600;700&display=swap">\n'
        f'{style_block}\n{EXTRA_CSS}\n</head>\n<body>\n<div class="wrap">\n{body}\n</div>\n</body>\n</html>\n'
    )


def render_to_file(summary):
    out = os.path.join(DEAL_REPORT, "reports", "deal-report.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(render_html(summary))
    return out


if __name__ == "__main__":
    import json
    if len(sys.argv) < 2:
        sys.exit("usage: render_deal_report.py <path-to-deal-report-json>")
    print(render_to_file(json.load(open(sys.argv[1], encoding="utf-8"))))
