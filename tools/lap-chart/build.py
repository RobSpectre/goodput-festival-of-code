#!/usr/bin/env python3
"""Assembles docs/lap-chart/index.html: draws the chart geometry and sets it into the page.

Usage: python3 tools/lap-chart/build.py docs/lap-chart/index.html

The figures are plain SVG in the page; nothing is computed in the browser except
how much of the forecast line is inked. Edit this file and template.html, then
rebuild; never edit the generated page by hand.

The hand: nothing is filtered. Every "ruled" edge is drawn with a slight waver
that is part of the geometry (see `field`), so edges stay crisp. The forecast
sheet is the exception: it is drawn true, because its lengths are measured.
"""
import math
import sys
from pathlib import Path

# The inks. These mirror --ink, --board, --crimson, --gold and --emerald in
# docs/lap-chart/lap-chart.css (and the same constants in tools/lap-chart-drivers.py).
# The drawings carry them as literals; change all three places together.
INK = "#171512"
BOARD = "#EFE3C8"
CRIMSON = "#B8232A"
GOLD = "#E3A81C"
EMERALD = "#1E6B4A"


def n(x):
    s = f"{x:.1f}"
    return s[:-2] if s.endswith(".0") else s


def field(p, k=1.0):
    """A slow waver, the same for every point of a drawing, so shared corners stay shared."""
    x, y = p
    dx = 1.5 * math.sin(.021 * x + .013 * y + 1.3) + 1.0 * math.sin(.008 * x - .017 * y + 4.1)
    dy = 1.5 * math.sin(.017 * x - .011 * y + 2.2) + 1.0 * math.sin(.006 * x + .019 * y + .7)
    return (x + k * dx, y + k * dy)


def subdivide(pts, step=14, closed=True):
    out = []
    count = len(pts)
    for i in range(count if closed else count - 1):
        p, q = pts[i], pts[(i + 1) % count]
        parts = max(1, int(math.dist(p, q) // step))
        for j in range(parts):
            t = j / parts
            out.append((p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t))
    if not closed:
        out.append(pts[-1])
    return out


def to_d(pts, closed=False):
    return "M" + " L".join(f"{n(x)},{n(y)}" for x, y in pts) + (" Z" if closed else "")


def ruled(pts, closed=True, step=14, k=1.0):
    """A shape or line as a hand would rule it: subdivided, then wavered."""
    return to_d([field(p, k) for p in subdivide(pts, step, closed)], closed)


def box(x, y, w, h):
    return [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]


# ---------------------------------------------------------------- plate one

def hero_plate():
    u = 64          # one, on the scale of the bars
    w = 24          # the width of the line
    A0, A1 = (700, 46), (444, 46)                                          # 4 units, heading left
    B1 = (A1[0] + 3 * u * math.sqrt(.5), A1[1] + 3 * u * math.sqrt(.5))   # 3 units, down-right
    C1 = (B1[0] - 2 * u * math.sqrt(.5), B1[1] + 2 * u * math.sqrt(.5))   # 2 units, down-left
    D1 = (C1[0] - u, C1[1])                                               # 1 unit, heading left
    run = 118
    E = (D1[0] + run * math.sqrt(.5), D1[1] + run * math.sqrt(.5))
    R, pitch, r_end = 232, 37, 44
    phi0 = -math.pi / 4
    cx, cy = E[0] - R * math.cos(phi0), E[1] - R * math.sin(phi0)

    coil = []
    theta, step = 0.0, math.radians(4)
    while True:
        r = R - pitch * theta / (2 * math.pi)
        if r < r_end:
            break
        coil.append((cx + r * math.cos(phi0 + theta), cy + r * math.sin(phi0 + theta)))
        theta += step

    def unit(p, q):
        length = math.dist(p, q)
        return ((q[0] - p[0]) / length, (q[1] - p[1]) / length)

    def normal(d):
        return (-d[1], d[0])

    def mitre(p, d_in, d_out):
        """The two corners of a folded line at p: the line is cut along the bisector of the fold."""
        a, b = normal(d_in), normal(d_out)
        scale = (w / 2) / (1 + a[0] * b[0] + a[1] * b[1])
        m = ((a[0] + b[0]) * scale, (a[1] + b[1]) * scale)
        return (p[0] + m[0], p[1] + m[1]), (p[0] - m[0], p[1] - m[1])

    spine = [A0, A1, B1, C1, D1, E]
    dirs = [unit(spine[i], spine[i + 1]) for i in range(len(spine) - 1)]
    a = normal(dirs[0])
    corners = [((A0[0] + a[0] * w / 2, A0[1] + a[1] * w / 2), (A0[0] - a[0] * w / 2, A0[1] - a[1] * w / 2))]
    for i in range(1, 5):
        corners.append(mitre(spine[i], dirs[i - 1], dirs[i]))

    shapes = []
    for i, colour in enumerate((EMERALD, GOLD, INK, BOARD)):
        (l0, r0), (l1, r1) = corners[i], corners[i + 1]
        # each bar's run, along the middle of the line, is exactly (4 - i) units
        assert abs(math.dist(spine[i], spine[i + 1]) - (4 - i) * u) < 1e-6
        shapes.append(f'<path d="{ruled([l0, l1, r1, r0])}" fill="{colour}"/>')

    # the crimson: from the last fold, down the straight run and round the coil, as one shape
    path = coil   # its first point is E, the end of the straight run
    left, right = [corners[4][0]], [corners[4][1]]
    for i, p in enumerate(path):
        d = unit(path[i - 1], p) if i == len(path) - 1 else unit(p, path[i + 1])
        nx, ny = normal(d)
        left.append((p[0] + nx * w / 2, p[1] + ny * w / 2))
        right.append((p[0] - nx * w / 2, p[1] - ny * w / 2))
    outline = subdivide(left[:2], 14, False) + left[2:] + right[:1:-1] + subdivide([right[1], right[0]], 14, False)
    shapes.append(f'<path d="{to_d([field(p) for p in outline], True)}" fill="{CRIMSON}"/>')

    centre = to_d([field(p) for p in subdivide(spine, 14, False) + coil[1:]])
    kx, ky = 574, 640
    turns = theta / (2 * math.pi)
    svg = f'''<svg class="plate-one__chart" viewBox="0 0 760 770" role="img" aria-labelledby="p1-title p1-desc">
          <title id="p1-title">The meeting in one line.</title>
          <desc id="p1-desc">One line, folded like a ribbon, runs as four straight bars drawn to a single scale: four drivers, three customers, two days and one machine. It then turns crimson and coils into a large spiral: tokens per second, the one quantity not yet known, drawn to no scale.</desc>
          <mask id="ink-run" maskUnits="userSpaceOnUse" x="0" y="0" width="760" height="770">
            <path class="ink" pathLength="1" style="--d:.35s;--t:3.4s" d="{centre}" fill="none" stroke="#fff" stroke-width="{w + 14}" stroke-linejoin="miter" stroke-miterlimit="12"/>
          </mask>
          <g mask="url(#ink-run)" stroke="{INK}" stroke-width="2.6" stroke-linejoin="miter" stroke-miterlimit="12">
            {chr(10).join("            " + s for s in shapes).strip()}
          </g>
          <circle cx="{n(cx)}" cy="{n(cy)}" r="27" fill="{BOARD}" stroke="{INK}" stroke-width="2.6"/>
          <text class="num" x="{n(cx)}" y="{n(cy + 15)}" text-anchor="middle" font-size="42" fill="{CRIMSON}">?</text>
          <g class="cap" font-size="30">
            <text x="{n(A1[0] - 46)}" y="{n(A1[1] + 11)}" text-anchor="end"><tspan class="num" font-size="46">4</tspan> DRIVERS ENTERED</text>
            <text x="{n((A1[0] + B1[0]) / 2 - 36)}" y="{n((A1[1] + B1[1]) / 2 + 30)}" text-anchor="end"><tspan class="num" font-size="46">3</tspan> CUSTOMERS ON THE LINE</text>
            <text x="{n((B1[0] + C1[0]) / 2 + 34)}" y="{n((B1[1] + C1[1]) / 2 + 30)}"><tspan class="num" font-size="46">2</tspan> DAYS</text>
            <text x="{n(D1[0] - 50)}" y="{n(D1[1] - 9)}" text-anchor="end"><tspan class="num" font-size="46">1</tspan> MACHINE</text>
            <text x="{n(E[0] + 28)}" y="{n(E[1] - 36)}" fill="{CRIMSON}"><tspan class="num" font-size="46">?</tspan> TOKENS</text>
            <text x="{n(E[0] + 28)}" y="{n(E[1] - 4)}" fill="{CRIMSON}">PER SECOND</text>
          </g>
          <path d="{ruled(box(kx, ky - w / 2, u, w))}" fill="{INK}"/>
          <g class="cap" font-size="26">
            <text x="{kx}" y="{ky + 46}">= ONE.</text>
            <text x="{kx}" y="{ky + 76}">CRIMSON HAS</text>
            <text x="{kx}" y="{ky + 106}">NO SCALE.</text>
          </g>
        </svg>'''
    return svg, turns


# ---------------------------------------------------------------- the timekeeper's lap chart

def lapchart_figure():
    x0, x1, xn = 4, 296, 112
    y0, head, row = 52, 36, 42
    numbers = ("B300", "GB300", "H200", "H100")
    yb = y0 + head + row * len(numbers)
    laps = 5
    lw = (x1 - xn) / laps
    lines = [ruled(box(x0, y0, x1 - x0, yb - y0), True, 18, .7)]
    thin = [ruled([(x0, y0 + head), (x1, y0 + head)], False, 18, .7), ruled([(xn, y0), (xn, yb)], False, 18, .7)]
    for i in range(1, len(numbers)):
        y = y0 + head + row * i
        thin.append(ruled([(x0, y), (x1, y)], False, 18, .7))
    for i in range(1, laps):
        x = xn + lw * i
        thin.append(ruled([(x, y0 + head), (x, yb)], False, 18, .7))
    rows = "".join(
        f'<text class="num" x="{x0 + 10}" y="{y0 + head + row * i + 31}" font-size="30">{number}</text>'
        for i, number in enumerate(numbers))
    return f'''<svg class="lapchart__form" viewBox="0 0 300 {yb + 66}" role="img" aria-labelledby="lc-title lc-desc">
          <title id="lc-title">The timekeeper’s lap chart.</title>
          <desc id="lc-desc">A ruled lap-chart form. The four racing numbers are entered down the side: B300, GB300, H200 and H100. Every lap column is blank.</desc>
          <text class="num" x="{x0}" y="34" font-size="38" fill="{INK}">LAP CHART</text>
          <path d="{' '.join(lines)}" fill="none" stroke="{INK}" stroke-width="3"/>
          <path d="{' '.join(thin)}" fill="none" stroke="{INK}" stroke-width="1.7"/>
          <g class="cap" font-size="22" fill="{INK}">
            <text x="{x0 + 10}" y="{y0 + 25}">NO.</text>
            <text x="{xn + 10}" y="{y0 + 25}">LAPS</text>
            <text x="{x0}" y="{yb + 30}">FOUR NUMBERS ENTERED.</text>
            <text x="{x0}" y="{yb + 57}">LAPS BLANK UNTIL THE DAY.</text>
          </g>
          <g fill="{INK}">{rows}</g>
        </svg>'''


# ---------------------------------------------------------------- goodput, as a picture of an idea

def goodput_figure():
    return f'''<svg class="idea__chart" viewBox="0 0 720 322" role="img" aria-labelledby="p2-title p2-desc">
          <title id="p2-title">Goodput, as a picture of the idea.</title>
          <desc id="p2-desc">A long bar stands for throughput: every token sent. Beneath it the same length is split in two: goodput, the part that arrives whole and in time, and wheelspin, the rest. Illustrative; not to scale.</desc>
          <g class="cap" font-size="30" fill="{INK}">
            <text x="30" y="34">THROUGHPUT: EVERY TOKEN SENT</text>
            <text x="44" y="151">GOODPUT</text>
            <text x="676" y="151" text-anchor="end">WHEELSPIN</text>
            <text x="30" y="252">ARRIVES WHOLE, AND IN TIME</text>
            <text x="30" y="304">ILLUSTRATIVE. NOT TO SCALE.</text>
          </g>
          <path d="{ruled(box(30, 48, 660, 46))}" fill="{INK}"/>
          <path d="M30,96 V162 M690,96 V162 M508,96 V162" stroke="{INK}" stroke-width="1.8" stroke-dasharray="3 6" fill="none"/>
          <path d="{ruled(box(508, 164, 182, 46))}" fill="{BOARD}"/>
          <path d="{ruled(box(508, 164, 182, 46))}" fill="url(#hatch)" stroke="{INK}" stroke-width="2.6" stroke-linejoin="round"/>
          <path d="{ruled(box(30, 164, 478, 46))}" fill="{EMERALD}" stroke="{INK}" stroke-width="2.6" stroke-linejoin="round"/>
        </svg>'''


# ---------------------------------------------------------------- the forecast: coil and wrapped bars

ROW = 460          # one row of the sheet, in drawing units: 1,000 tokens per second
ROWS = 12


def forecast_figures():
    """Drawn true, with no waver: the coil and the rows must hold exactly the same length of line."""
    total = ROW * ROWS
    cx = cy = 220
    r0, pitch = 16, 24
    pts, theta, step, length = [], 0.0, math.radians(3), 0.0
    prev = None
    while True:
        r = r0 + pitch * theta / (2 * math.pi)
        p = (cx + r * math.cos(theta - math.pi / 2), cy + r * math.sin(theta - math.pi / 2))
        if prev is not None:
            seg = math.dist(prev, p)
            if length + seg >= total:
                k = (total - length) / seg
                pts.append((prev[0] + (p[0] - prev[0]) * k, prev[1] + (p[1] - prev[1]) * k))
                length = total
                break
            length += seg
        pts.append(p)
        prev = p
        theta += step
    d = to_d(pts)
    coil = f'''<svg class="forecast__coil" viewBox="0 0 440 440" aria-hidden="true" focusable="false">
              <path d="{d}" fill="none" stroke="{BOARD}" stroke-width="2.2" stroke-dasharray="1 8" stroke-linecap="round" opacity=".8"/>
              <path id="fc-coil" d="{d}" pathLength="{total}" fill="none" stroke="{GOLD}" stroke-width="14" stroke-dasharray="0 {total * 2}"/>
              <circle cx="{cx}" cy="{cy}" r="5" fill="{BOARD}"/>
            </svg>'''

    x0, x1, y0, gap = 40, 40 + ROW, 24, 24
    guides, inks, labels = [], [], []
    for i in range(ROWS):
        y = y0 + gap * i
        guides.append(f"M{x0},{y} H{x1}")
        if i < ROWS - 1:   # the return at the end of each row
            xe = x1 if i % 2 == 0 else x0
            sweep = 1 if i % 2 == 0 else 0
            guides.append(f"M{xe},{y} A{gap / 2:g},{gap / 2:g} 0 0 {sweep} {xe},{y + gap}")
        start = x0 if i % 2 == 0 else x1
        inks.append(f'<line class="fc-row" x1="{start}" y1="{y}" x2="{start}" y2="{y}"/>')
        if i % 2 == 0:
            labels.append(f'<text x="{x1 + 12}" y="{y + 8}">{i + 1}</text>')
        else:
            labels.append(f'<text x="{x0 - 12}" y="{y + 8}" text-anchor="end">{i + 1}</text>')
    yl = y0 + gap * (ROWS - 1)
    rows = f'''<svg class="forecast__rows" viewBox="0 0 540 312" aria-hidden="true" focusable="false">
              <path d="{' '.join(guides)}" fill="none" stroke="{BOARD}" stroke-width="2.2" stroke-dasharray="1 8" stroke-linecap="round" opacity=".8"/>
              <g stroke="{GOLD}" stroke-width="14">
                {chr(10).join("                " + s for s in inks).strip()}
              </g>
              <path id="fc-off" d="M{x0 - 2},{yl + 16} l-22,0 m0,0 l9,-8 m-9,8 l9,8" fill="none" stroke="{GOLD}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" visibility="hidden"/>
              <g class="fig" font-size="24" fill="{BOARD}">
                {chr(10).join("                " + s for s in labels).strip()}
              </g>
            </svg>'''
    return coil, rows, total


# ---------------------------------------------------------------- three customers, drawn equal

def fan_figure():
    ax, ay, R = 50, 310, 580
    half = 10.5
    wedges = [(-21, CRIMSON, BOARD, "CURSOR"), (0, GOLD, INK, "HIGGSFIELD"), (21, BOARD, INK, "COGNITION")]
    shapes, names = [], []
    for mid, fill, text, name in wedges:
        a0, a1 = math.radians(mid - half), math.radians(mid + half)
        arc = [(ax + R * math.cos(a0 + (a1 - a0) * i / 14), ay + R * math.sin(a0 + (a1 - a0) * i / 14)) for i in range(15)]
        edge = subdivide([(ax, ay), arc[0]], 16, False) + arc[1:] + subdivide([arc[-1], (ax, ay)], 16, False)[1:-1]
        shapes.append(f'<path d="{to_d([field(p) for p in edge], True)}" fill="{fill}" stroke="{INK}" stroke-width="2.6" stroke-linejoin="round"/>')
        names.append(f'<text class="num" x="{ax + 238}" y="{ay + 15}" font-size="44" fill="{text}" transform="rotate({mid} {ax} {ay})">{name}</text>')
    hub = field((ax, ay))
    return f'''<svg class="fan__chart" viewBox="0 0 660 620" role="img" aria-labelledby="p5-title p5-desc">
          <title id="p5-title">Three customers, drawn equal.</title>
          <desc id="p5-desc">A fan of three equal wedges, one each for Cursor, Higgsfield and Cognition. The wedges are the same size on purpose: no ranking is meant and nothing was measured.</desc>
          {chr(10).join("          " + s for s in shapes).strip()}
          {chr(10).join("          " + s for s in names).strip()}
          <circle cx="{n(hub[0])}" cy="{n(hub[1])}" r="9" fill="{INK}"/>
        </svg>'''


# ---------------------------------------------------------------- April 2027

def calendar_figure():
    cell, gap, x0, y0 = 88, 8, 28, 62
    days = "SMTWTFS"
    open_cells, inked, text = [], [], []
    heads = "".join(f'<text x="{x0 + (cell + gap) * i + cell / 2:g}" y="40" text-anchor="middle">{d}</text>' for i, d in enumerate(days))
    first = 4   # 1 April 2027 is a Thursday; the week is drawn from Sunday
    for day in range(1, 31):
        k = first + day - 1
        col, row = k % 7, k // 7
        x, y = x0 + (cell + gap) * col, y0 + (cell + gap) * row
        if day in (27, 28):
            inked.append(ruled(box(x, y, cell, cell), True, 22))
            text.append(f'<text class="num" x="{x + cell / 2:g}" y="{y + 60}" text-anchor="middle" font-size="50" fill="{BOARD}">{day}</text>')
        else:
            open_cells.append(ruled(box(x, y, cell, cell), True, 22))
            text.append(f'<text class="fig" x="{x + 10}" y="{y + 36}" font-size="30" fill="{INK}">{day}</text>')
    h = y0 + (cell + gap) * 5
    return f'''<svg class="when__chart" viewBox="0 0 720 {h}" role="img" aria-labelledby="p6-title p6-desc">
          <title id="p6-title">April 2027, with two days inked.</title>
          <desc id="p6-desc">The thirty days of April 2027 drawn as squares, a week to the row, starting on Sunday. Tuesday the 27th and Wednesday the 28th are inked in crimson.</desc>
          <g class="cap" font-size="27" fill="{INK}">{heads}</g>
          <path d="{' '.join(open_cells)}" fill="none" stroke="{INK}" stroke-width="1.8" stroke-linejoin="round"/>
          <path d="{' '.join(inked)}" fill="{CRIMSON}" stroke="{INK}" stroke-width="2.6" stroke-linejoin="round"/>
          {chr(10).join("          " + s for s in text).strip()}
        </svg>'''


TEMPLATE = Path(__file__).with_name("template.html")

if __name__ == "__main__":
    out = Path(sys.argv[1])
    hero, turns = hero_plate()
    coil, rows, total = forecast_figures()
    page = TEMPLATE.read_text()
    for key, value in {
        "{{HERO_PLATE}}": hero,
        "{{LAPCHART_FIGURE}}": lapchart_figure(),
        "{{GOODPUT_FIGURE}}": goodput_figure(),
        "{{FORECAST_COIL}}": coil,
        "{{FORECAST_ROWS}}": rows,
        "{{FAN_FIGURE}}": fan_figure(),
        "{{CALENDAR_FIGURE}}": calendar_figure(),
    }.items():
        assert key in page, key
        page = page.replace(key, value)
    assert "{{" not in page, page[page.index("{{"):][:60]
    out.write_text(page)
    print(f"wrote {out} ({len(page) // 1024} KB); hero coil {turns:.1f} turns; forecast line {total} units")
