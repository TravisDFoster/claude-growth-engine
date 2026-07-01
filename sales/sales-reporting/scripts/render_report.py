# /// script
# requires-python = ">=3.9"
# ///
"""
render_report.py — deterministic HTML renderer for the Sales Pipeline Report.

Takes the aggregated JSON produced by pull_pipeline.py and emits the locked
dashboard HTML — no LLM, no sub-agent, byte-identical every run. The CSS is read
straight from reference-weekly-sales-report.html so that file stays the single
styling source of truth; this module only generates the <body>.

Standalone (re-render from a saved JSON without re-pulling):
    uv run render_report.py ../tmp/pipeline-2026-W21.json

Normally invoked in-process by pull_pipeline.py after it writes the JSON.
"""

import html
import json
import os
import re
import sys

SALES_REPORTING = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REFERENCE = os.path.join(SALES_REPORTING, "reference-weekly-sales-report.html")


def esc(x):
    return html.escape(str(x), quote=False)


def money(x):
    try:
        return f"${float(x):,.0f}"
    except (TypeError, ValueError):
        return "$0"


def plural(n, word):
    if n == 1:
        return word
    if word.endswith("y"):
        return word[:-1] + "ies"
    return word + "s"


def extract_style(reference_path=REFERENCE):
    """Return the verbatim <style>…</style> block from the locked reference.

    Strip HTML comments first — the reference's header comment mentions the literal
    string "<style>", which would otherwise match before the real tag.
    """
    txt = open(reference_path, encoding="utf-8").read()
    txt = re.sub(r"<!--.*?-->", "", txt, flags=re.DOTALL)
    i = txt.index("<style>")
    j = txt.index("</style>") + len("</style>")
    return txt[i:j]


def bar_chart(rows):
    """rows: iterable of (label, count, amount). Bars sorted desc; width relative to max."""
    rows = [(l, c, a) for (l, c, a) in rows if c > 0]
    rows.sort(key=lambda r: r[1], reverse=True)
    if not rows:
        return ""
    mx = rows[0][1]
    out = ['<div class="bar-chart">']
    for label, count, amount in rows:
        pct = round(count / mx * 100, 1)
        pstr = f"{pct:g}"
        dealword = f"{count} {plural(count, 'deal')}"
        if pct < 18:
            fill = (f'<div class="bar-fill thin" data-label="{esc(dealword)}" '
                    f'style="width: {pstr}%; --bar-w: {pstr}%;"></div>')
        else:
            fill = f'<div class="bar-fill" style="width: {pstr}%;">{esc(dealword)}</div>'
        out.append(
            f'<div class="bar-row"><div class="bar-label">{esc(label)}</div>'
            f'<div class="bar-track">{fill}</div>'
            f'<div class="bar-meta">{money(amount)}</div></div>'
        )
    out.append("</div>")
    return "\n".join(out)


def stat_cards(s):
    stats = [
        ("New pipeline created", s["new_deals"]["total"]["count"], money(s["new_deals"]["total"]["amount"])),
        ("Closed-won", s["closed_won"]["total"]["count"], money(s["closed_won"]["total"]["amount"])),
        ("Closed-lost", s["closed_lost"]["total"]["count"], money(s["closed_lost"]["total"]["amount"])),
        ("Active open pipeline", s["open_snapshot"]["total"]["count"], money(s["open_snapshot"]["total"]["amount"])),
        ("Demos requested", s.get("demos", {}).get("total", 0), "form submissions"),
        ("Foundations entries", s["foundations"]["new_in_period"], "new free-funnel"),
    ]
    cards = []
    for lbl, num, sub in stats:
        zero = " zero" if num == 0 else ""
        cards.append(
            f'<div class="h-stat{zero}"><div class="h-num">{num}</div>'
            f'<div class="h-sub">{sub}</div><div class="h-lbl">{lbl}</div></div>'
        )
    return "\n".join(cards)


def tldr(s):
    nw = s.get("num_weeks", 1)
    lead = (f'Week of {s["start"]} &rarr; {s["end"]}' if nw <= 1
            else f'{nw}-week lookback {s["start"]} &rarr; {s["end"]}')
    nd = s["new_deals"]["total"]
    new_clause = (f'<b>{nd["count"]} new {plural(nd["count"], "deal")} worth {money(nd["amount"])}</b> '
                  f'created across Sales Pipeline and RFP Process')
    wc, lc = s["closed_won"]["total"], s["closed_lost"]["total"]
    if wc["count"] == 0 and lc["count"] == 0:
        closed_clause = "<b>No deals closed-won or closed-lost</b>"
    else:
        closed_clause = (f'<b>{wc["count"]} {plural(wc["count"], "deal")} closed-won ({money(wc["amount"])})</b> '
                         f'and <b>{lc["count"]} {plural(lc["count"], "deal")} closed-lost ({money(lc["amount"])})</b>')
    f = s["foundations"]["new_in_period"]
    if f == 0:
        found_clause = "and <b>no new Foundations free-funnel entries</b>"
    else:
        found_clause = f'plus <b>{f} new Foundations free-funnel {plural(f, "entry")}</b>'
    dm = s.get("demos", {}).get("total", 0)
    demo_clause = (f' <b>{dm} {plural(dm, "demo")} requested</b> top-of-funnel.' if dm
                   else " <b>No demos requested</b> top-of-funnel.")
    o = s["open_snapshot"]["total"]
    open_clause = f'Active open pipeline holds at <b>{o["count"]} deals · {money(o["amount"])}</b>.'
    return f"{lead}: {new_clause}. {closed_clause}, {found_clause}.{demo_clause} {open_clause}"


def hero(s):
    return (
        '<header class="hero">'
        '<div class="breadcrumb">sales · pipeline report</div>'
        f'<h1>{esc("Sales Pipeline Report — " + s["period_label"])}</h1>'
        '<div class="meta-row">'
        f'<span><b>Range:</b> {s["start"]} &rarr; {s["end"]}</span>'
        '<span><b>Scope:</b> Sales Pipeline · RFP Process · Email Foundations</span>'
        '<span><b>Reps:</b> Josh · Marc · Tarek</span>'
        f'<span><b>Generated:</b> {s["generated_at"]}</span>'
        '</div>'
        f'<div class="hero-stats">{stat_cards(s)}</div>'
        f'<p class="tldr-strip">{tldr(s)}</p>'
        '</header>'
    )


def section_new(nd):
    tc = nd["total"]["count"]
    if tc == 0:
        return ('<section><h2><span class="num">01</span>New deals created'
                '<span class="lead">No activity</span></h2>'
                '<div class="empty-card"><div class="e-num">0<small> · $0</small></div>'
                '<div class="e-body"><span class="e-status">No activity</span>'
                '<p class="note-italic">No new deals in this period.</p></div></div></section>')
    owner_chart = bar_chart((n, d["count"], d["amount"]) for n, d in nd["by_owner"].items())
    pipe_rows = "".join(
        f'<tr><td>{esc(n)}</td><td class="num">{d["count"]}</td>'
        f'<td class="num">{money(d["amount"]) if d["amount"] else "&mdash;"}</td></tr>'
        for n, d in nd["by_pipeline"].items() if d["count"] > 0
    )
    pipe_table = (
        '<table class="data"><thead><tr><th>Pipeline</th>'
        '<th class="num">Deals</th><th class="num">Amount</th></tr></thead>'
        f'<tbody>{pipe_rows}</tbody></table>'
    )
    lead = f'{tc} {plural(tc, "deal")} · {money(nd["total"]["amount"])}'
    return (
        f'<section><h2><span class="num">01</span>New deals created<span class="lead">{lead}</span></h2>'
        '<div class="cols-2">'
        f'<div><h3>By owner</h3>{owner_chart}</div>'
        f'<div><h3>By pipeline</h3>{pipe_table}</div>'
        '</div></section>'
    )


def _closed_block(side, deals, totals, reason_col):
    title = side  # "Closed-won" / "Closed-lost"
    if totals["count"] == 0:
        verb = "closed-won" if side == "Closed-won" else "closed-lost"
        return (f'<div><h3>{title}</h3><div class="empty-card">'
                '<div class="e-num">0<small> · $0</small></div>'
                '<div class="e-body"><span class="e-status">No activity</span>'
                f'<p class="note-italic">No deals {verb} in this period.</p></div></div></div>')
    head_last = "Reason" if reason_col else "Pipeline"
    rows = []
    for d in deals:
        last = esc(d["reason"]) if (reason_col and d.get("reason")) else ("&mdash;" if reason_col else esc(d["pipeline"]))
        rows.append(
            f'<tr><td>{esc(d["name"])}</td><td class="num">{money(d["amount"])}</td>'
            f'<td class="owner">{esc(d["owner"])}</td><td>{last}</td></tr>'
        )
    h3 = f'{title} — {totals["count"]} {plural(totals["count"], "deal")} · {money(totals["amount"])}'
    table = (
        f'<table class="data"><thead><tr><th>Deal</th><th class="num">Amount</th>'
        f'<th>Owner</th><th>{head_last}</th></tr></thead>'
        f'<tbody>{"".join(rows)}</tbody></table>'
    )
    return f'<div><h3>{h3}</h3>{table}</div>'


def section_closed(won, lost):
    wc, lc = won["total"]["count"], lost["total"]["count"]
    lead = ("No activity" if wc == 0 and lc == 0
            else f'Won {money(won["total"]["amount"])} · Lost {money(lost["total"]["amount"])}')
    return (
        f'<section><h2><span class="num">02</span>Closed in period<span class="lead">{lead}</span></h2>'
        '<div class="cols-2">'
        f'{_closed_block("Closed-won", won["deals"], won["total"], reason_col=False)}'
        f'{_closed_block("Closed-lost", lost["deals"], lost["total"], reason_col=True)}'
        '</div></section>'
    )


def section_open(o):
    stage_rows = "".join(
        f'<tr><td>{esc(s["pipeline"])}</td><td>{esc(s["stage"])}</td>'
        f'<td class="num">{s["count"]}</td><td class="num">{money(s["amount"])}</td></tr>'
        for s in o["by_stage"]
    )
    stage_table = (
        '<table class="data"><thead><tr><th>Pipeline</th><th>Stage</th>'
        '<th class="num">Deals</th><th class="num">Amount</th></tr></thead>'
        f'<tbody>{stage_rows}</tbody>'
        f'<tfoot><tr><td colspan="2">Total active</td>'
        f'<td class="num">{o["total"]["count"]}</td><td class="num">{money(o["total"]["amount"])}</td></tr></tfoot>'
        '</table>'
    )
    owner_chart = bar_chart((n, d["count"], d["amount"]) for n, d in o["by_owner"].items())
    nurture = ""
    h = o.get("holding_nurture", {"count": 0, "amount": 0})
    if h["count"] > 0:
        nurture = (
            '<h3 style="margin-top: 22px;">Nurture (holding) — excluded from active</h3>'
            '<div class="nurture"><span class="n-label">Nurture (holding)</span>'
            f'<span class="n-num">{h["count"]} deals</span><span class="n-num">{money(h["amount"])}</span>'
            '<span class="n-ctx">Parked in Nurture &mdash; excluded from the active pipeline above.</span></div>'
        )
    lead = f'{o["total"]["count"]} active deals · {money(o["total"]["amount"])}'
    return (
        f'<section><h2><span class="num">03</span>Open pipeline snapshot — active<span class="lead">{lead}</span></h2>'
        f'<h3>By pipeline &amp; stage</h3>{stage_table}'
        f'<h3 style="margin-top: 22px;">By owner</h3>{owner_chart}{nurture}</section>'
    )


def _email_block(em):
    """Email engagement sub-block for section 04 — handles three states:
    pending_scope (token still lacks email-read), no_engagement (counts but no open/click
    props on the portal), ok (full sent/received + open/click)."""
    if not em or em.get("status") == "pending_scope":
        return ('<p class="note-italic">Emails — pending HubSpot scope grant '
                '(<code>sales-email-read</code> / <code>crm.objects.emails.read</code>). '
                'Sent/received counts and open/click engagement will appear here automatically once granted.</p>')
    by_owner = em.get("by_owner") or {}
    tot = em.get("totals") or {}
    engagement = em.get("status") == "ok"
    cols = [("sent", "Sent"), ("received", "Received")]
    if engagement:
        cols += [("opens", "Opens"), ("clicks", "Clicks")]
    head = "".join(f'<th class="num">{lbl}</th>' for _, lbl in cols)
    rows = "".join(
        f'<tr><td class="owner">{esc(name)}</td>'
        + "".join(f'<td class="num">{d.get(k, 0)}</td>' for k, _ in cols)
        + "</tr>"
        for name, d in by_owner.items()
    )
    foot = "".join(f'<td class="num">{tot.get(k, 0)}</td>' for k, _ in cols)
    note = ('Sent/received from logged email engagements; opens/clicks from tracked sends.'
            if engagement else
            'Sent/received from logged email engagements. Open/click tracking not available on this portal.')
    note += ' Opens are total opens (a single email opened multiple times counts each time).' if engagement else ''
    return (
        '<h3 style="margin-top: 22px;">Email engagement</h3>'
        f'<table class="data"><thead><tr><th>Owner</th>{head}</tr></thead>'
        f'<tbody>{rows}</tbody>'
        f'<tfoot><tr><td>Team</td>{foot}</tr></tfoot></table>'
        f'<p class="note-italic">{note}</p>'
    )


def section_activity(a):
    if not a:
        return ""
    types = [("meetings", "Meetings"), ("notes", "Notes"), ("tasks", "Tasks")]
    head = "".join(f'<th class="num">{lbl}</th>' for _, lbl in types)
    rows = "".join(
        f'<tr><td class="owner">{esc(name)}</td>'
        + "".join(f'<td class="num">{d[t]}</td>' for t, _ in types)
        + "</tr>"
        for name, d in a["by_owner"].items()
    )
    tot = a["totals"]
    foot = "".join(f'<td class="num">{tot[t]}</td>' for t, _ in types)
    lead = f'{sum(tot.values())} logged'
    return (
        f'<section><h2><span class="num">04</span>Activity (logged)<span class="lead">{lead}</span></h2>'
        f'<table class="data"><thead><tr><th>Owner</th>{head}</tr></thead>'
        f'<tbody>{rows}</tbody>'
        f'<tfoot><tr><td>Team</td>{foot}</tr></tfoot></table>'
        f'{_email_block(a.get("emails"))}'
        '</section>'
    )


def _gap_rows(rows):
    out = []
    for r in rows:
        cap = r.get("mapped_gap", "")
        if cap.lower().startswith("novel:"):
            cap = cap.split(":", 1)[1].strip() + " (new)"
        src = esc(r.get("source", ""))
        if r.get("competitor"):
            src += " — vs " + esc(r["competitor"])
        out.append(
            f'<tr><td>{esc(cap)}</td><td>{src}</td>'
            f'<td class="owner">{esc(r.get("owner", ""))}</td>'
            f'<td>{esc(r.get("quote", ""))}</td></tr>'
        )
    return "".join(out)


def section_feature(s, feature_requests):
    rollup = s.get("feature_gaps_rollup") or {"by_option": {}, "deal_count": 0}
    reqs = feature_requests or []
    if not reqs and not rollup["by_option"]:
        return ""
    gaps = [r for r in reqs if r.get("already_ships") is not True]   # false / unsure = real gaps
    sought = [r for r in reqs if r.get("already_ships") is True]      # capabilities we ship — recorded, not gaps

    def gap_table(rows):
        return ('<table class="data"><thead><tr><th>Capability</th><th>Source</th>'
                '<th>Owner</th><th>Signal</th></tr></thead>'
                f'<tbody>{_gap_rows(rows)}</tbody></table>')

    gaps_block = ('<h3>Gaps surfaced in notes — roadmap signal</h3>' + gap_table(gaps)) if gaps else \
                 '<h3>Gaps surfaced in notes — roadmap signal</h3><p class="note-italic">No real product gaps surfaced in notes this period.</p>'
    roll = ""
    if rollup["by_option"]:
        rr = "".join(f'<tr><td>{esc(k)}</td><td class="num">{v}</td></tr>' for k, v in rollup["by_option"].items())
        roll = (f'<h3>Flagged in HubSpot — structured <code>feature_gaps</code> ({rollup["deal_count"]} AE deals)</h3>'
                '<table class="data"><thead><tr><th>Feature gap</th><th class="num">Deals</th></tr></thead>'
                f'<tbody>{rr}</tbody></table>')
    sought_note = ""
    if sought:
        sought_note = (f'<p class="note-italic">{len(sought)} note mention(s) of capabilities Cerkl already ships '
                       '(prospect priorities, not gaps) were recorded — reserved for the planned most-requested-capabilities view.</p>')

    lead = f'{len(gaps)} from notes · {rollup["deal_count"]} flagged in HubSpot'
    return (
        f'<section><h2><span class="num">05</span>Feature gaps<span class="lead">{lead}</span></h2>'
        f'{gaps_block}{roll}{sought_note}'
        '<p class="note-italic">Real gaps only (capabilities Cerkl lacks), from AE notes + the structured feature_gaps property. '
        'Signal is sparse — best read over a multi-week window.</p></section>'
    )


def section_foundations(f):
    n = f["new_in_period"]
    if n == 0:
        return ('<section><h2><span class="num">06</span>Foundations funnel — new in period'
                '<span class="lead">Count-only · No activity</span></h2>'
                '<div class="empty-card"><div class="e-num">0</div>'
                '<div class="e-body"><span class="e-status">No activity</span>'
                '<p class="note-italic">No new Foundations deals in this period.</p></div></div></section>')
    rows = "".join(
        f'<tr><td>{esc(stage)}</td><td class="num">{c}</td></tr>'
        for stage, c in f["by_stage"].items()
    )
    lead = f'Count-only · {n} new free-funnel {plural(n, "deal")}'
    return (
        f'<section><h2><span class="num">06</span>Foundations funnel — new in period<span class="lead">{lead}</span></h2>'
        '<table class="data"><thead><tr><th>Stage</th><th class="num">New deals</th></tr></thead>'
        f'<tbody>{rows}</tbody></table></section>'
    )


def section_demos(d):
    if not d:
        return ""
    n = d["total"]
    if n == 0:
        return ('<section><h2><span class="num">07</span>Demos requested'
                '<span class="lead">No activity</span></h2>'
                '<div class="empty-card"><div class="e-num">0</div>'
                '<div class="e-body"><span class="e-status">No activity</span>'
                '<p class="note-italic">No demo-request form submissions in this period.</p></div></div></section>')
    rows = []
    for s in d["submissions"]:
        name = (s.get("first_name", "") + " " + s.get("last_name", "")).strip() or "—"
        if s.get("contact_url") and name != "—":
            name_cell = (f'<a href="{esc(s["contact_url"])}" target="_blank" '
                         f'rel="noopener noreferrer">{esc(name)}</a>')
        else:
            name_cell = esc(name)
        rows.append(
            f'<tr><td>{esc(s["submitted_at"][:10])}</td>'
            f'<td>{name_cell}</td>'
            f'<td>{esc(s.get("company", "") or "—")}</td>'
            f'<td>{esc(s.get("company_size", "") or "—")}</td>'
            f'<td class="owner">{esc(s.get("owner", "Unassigned"))}</td></tr>'
        )
    table = (
        '<table class="data"><thead><tr><th>Date</th><th>Name</th>'
        '<th>Company</th><th>Company size</th><th>Owner</th></tr></thead>'
        f'<tbody>{"".join(rows)}</tbody></table>'
    )
    lead = f'{n} {plural(n, "request")}'
    return (
        f'<section><h2><span class="num">07</span>Demos requested<span class="lead">{lead}</span></h2>'
        f'{table}'
        '<p class="note-italic">Source: HubSpot form submissions on the configured demo form(s). All submissions in the window, regardless of owner.</p>'
        '</section>'
    )


def footer(s):
    return (
        '<footer>Source: HubSpot — Sales Pipeline, RFP Process, Email Foundations. '
        'Pulled by <code>scripts/pull_pipeline.py</code>. AE metrics cover Sales Pipeline + RFP Process '
        '(owner-filtered); Foundations is the full free funnel (no owner filter). '
        'Open snapshot reflects live state at generation time.<br>'
        f'Generated {s["generated_at"]} from <code>tmp/pipeline-{s["label"]}.json</code></footer>'
    )


def render_html(s, style_block=None, feature_requests=None):
    if style_block is None:
        style_block = extract_style()
    title = esc("Sales Pipeline Report — " + s["period_label"])
    body = "\n".join([
        hero(s), section_new(s["new_deals"]), section_closed(s["closed_won"], s["closed_lost"]),
        section_open(s["open_snapshot"]), section_activity(s.get("activity")),
        section_feature(s, feature_requests), section_foundations(s["foundations"]),
        section_demos(s.get("demos")), footer(s),
    ])
    return (
        '<!doctype html>\n<html lang="en">\n<head>\n'
        '<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f'<title>{title}</title>\n'
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Work+Sans:wght@400;500;600;700&display=swap">\n'
        f'{style_block}\n</head>\n<body>\n<div class="wrap">\n{body}\n</div>\n</body>\n</html>\n'
    )


def render_to_file(summary):
    # Merge the classifier output (feature requests) if it has been produced for this label.
    fr_path = os.path.join(SALES_REPORTING, "tmp", f'feature-requests-{summary["label"]}.json')
    feature_requests = None
    if os.path.exists(fr_path):
        feature_requests = json.load(open(fr_path, encoding="utf-8")).get("feature_requests")
    out = os.path.join(SALES_REPORTING, "reports", f'{summary["label"]}.html')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(render_html(summary, feature_requests=feature_requests))
    return out


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("usage: render_report.py <path-to-pipeline-json>")
    summary = json.load(open(sys.argv[1], encoding="utf-8"))
    print(render_to_file(summary))
