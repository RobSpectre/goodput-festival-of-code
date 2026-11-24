#!/usr/bin/env python3
"""Draws the four driver portraits for the Hand-Inked Lap Chart treatment.

Usage: lap-chart-drivers.py <out_dir>

The drawings come from drivers.py; this script re-inks them for the chart
world: the halftone screens become pen hatching, the shapes take an ink
keyline, the roundel behind each head is dropped (each portrait stands on a
flat colour square in the page), and the inks are the chart's four.
"""
import importlib.util
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("drivers", HERE / "drivers.py")
d = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d)

# These mirror --ink, --board, --crimson, --emerald and --gold in docs/lap-chart/lap-chart.css
# (and the same constants in tools/lap-chart/build.py). Change all three places together.
INK = "#171512"
BOARD = "#EFE3C8"
CRIMSON = "#B8232A"
EMERALD = "#1E6B4A"
GOLD = "#E3A81C"

d.INK, d.PAPER, d.RED, d.GREEN, d.YELLOW = INK, BOARD, CRIMSON, EMERALD, GOLD
d.goggles_up.__defaults__ = (112, True, BOARD)


def defs(spot):
    # pen hatching in place of the halftone screens
    return f"""
  <defs>
    <pattern id="ht1" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(-42)">
      <rect width="7" height="1.3" fill="{INK}"/>
    </pattern>
    <pattern id="ht2" width="4.6" height="4.6" patternUnits="userSpaceOnUse" patternTransform="rotate(-42)">
      <rect width="4.6" height="1.5" fill="{INK}"/>
    </pattern>
    <pattern id="ht3" width="4.6" height="4.6" patternUnits="userSpaceOnUse" patternTransform="rotate(-42)">
      <rect width="4.6" height="4.6" fill="{INK}"/><rect width="4.6" height="1.2" fill="{BOARD}"/>
    </pattern>
    <pattern id="sp1" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(38)">
      <rect width="6" height="1.6" fill="{spot}"/>
    </pattern>
    <pattern id="hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(-38)">
      <rect width="6" height="2" fill="{INK}"/>
    </pattern>
    <pattern id="tweed" width="8" height="8" patternUnits="userSpaceOnUse">
      <rect width="8" height="8" fill="{INK}"/>
      <path d="M0 8 L8 0 M-2 2 L2 -2 M6 10 L10 6" stroke="{BOARD}" stroke-width="1.1" fill="none"/>
    </pattern>
    <clipPath id="plate"><rect x="0" y="0" width="320" height="372"/></clipPath>
  </defs>"""


KEY = f' stroke="{INK}" stroke-width="2.4" stroke-linejoin="round"'
_face, _neck, _torso = d.face, d.neck, d.torso


def face(*args, **kwargs):
    # the face takes a keyline, then its hatched shadow
    return re.sub(r'(<path d="M10[26],168[^"]*" fill="[^"]*")/>', r"\1" + KEY + "/>", _face(*args, **kwargs), count=1)


def neck(*args, **kwargs):
    return re.sub(r'(<path d="M130,246[^"]*" fill="[^"]*")/>', r"\1" + KEY + "/>", _neck(*args, **kwargs), count=1)


def torso(kind, spot):
    out = _torso(kind, spot)
    return re.sub(r'(<path d="M22,372 L22,356[^"]*" fill="[^"]*")/>', r"\1" + KEY + "/>", out, count=1)


def svg(title, spot, body):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 372" role="img" aria-labelledby="t">
  <title id="t">{title}</title>{defs(spot)}
  <g clip-path="url(#plate)">{body}
  </g>
</svg>
"""


d.defs, d.face, d.neck, d.torso, d.svg = defs, face, neck, torso, svg
d.disc = lambda *a, **k: ""
d.disc_tint = lambda *a, **k: ""
d.baseline = lambda: ""

if __name__ == "__main__":
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    for name, fn in (("volozh", d.volozh), ("chernin", d.chernin), ("lecun", d.lecun), ("teknium", d.teknium)):
        (out / f"driver-{name}.svg").write_text(fn())
        print("wrote", out / f"driver-{name}.svg")
