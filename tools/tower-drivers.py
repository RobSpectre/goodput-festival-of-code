#!/usr/bin/env python3
"""Draws the four driver portraits for the Timekeepers' Tower treatment.

Usage: tower-drivers.py <out_dir>

Each portrait is an enamel plate for the scoreboard: a cream plate with two
hanging holes, flat colour, and tone carried by one coarse ruled hatch (the
same pitch as the scorer on the tower, so it still reads as hatching at the
size the plate is hung).

The heads are the drawings from drivers.py, set smaller and higher on the
plate. The busts are drawn here, down to the chest, so the racing suit reads:
a buttoned or zipped front, a breast pocket, sleeve seams and a belt.
"""
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("drivers", HERE / "drivers.py")
d = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d)

INK = "#151412"
PLATE = "#F3E9CF"
RED = "#C4271B"
GREEN = "#114232"
YELLOW = "#F4C20D"

# the head drawings read these at call time
d.INK, d.PAPER, d.RED, d.GREEN, d.YELLOW = INK, PLATE, RED, GREEN, YELLOW

# the head is drawn at this scale, with the crown of the helmet near the top of the plate
HEAD = 'transform="translate(160 44) scale(.74) translate(-160 -66)"'


def defs(spot):
    # Patterns named ht*/sp1/tweed are used inside the scaled head, so they are
    # drawn at a pitch of 12 (about 9 once scaled); tt* are used on the bust at 9.
    return f"""
  <defs>
    <pattern id="ht1" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(-52)">
      <rect width="12" height="3" fill="{INK}"/>
    </pattern>
    <pattern id="ht2" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(-52)">
      <rect width="12" height="5.6" fill="{INK}"/>
    </pattern>
    <pattern id="ht3" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(-52)">
      <rect width="12" height="12" fill="{INK}"/>
      <rect width="12" height="2.6" fill="{PLATE}"/>
    </pattern>
    <pattern id="sp1" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(38)">
      <rect width="12" height="5.4" fill="{spot}"/>
    </pattern>
    <pattern id="tweed" width="16" height="16" patternUnits="userSpaceOnUse">
      <rect width="16" height="16" fill="{INK}"/>
      <path d="M0 8 L8 0 M8 16 L16 8 M0 16 L4 12 M12 4 L16 0" stroke="{PLATE}" stroke-width="2.6" fill="none"/>
    </pattern>
    <pattern id="tt1" width="9" height="9" patternUnits="userSpaceOnUse" patternTransform="rotate(-52)">
      <rect width="9" height="2.3" fill="{INK}"/>
    </pattern>
    <clipPath id="plate"><rect x="10" y="10" width="300" height="360"/></clipPath>
  </defs>"""


def disc(spot, tint=False):
    fill = "url(#sp1)" if tint else spot
    return f"""
  <g {HEAD}>
    <circle cx="160" cy="188" r="138" fill="{fill}"/>
    <circle cx="160" cy="188" r="138" fill="none" stroke="{INK}" stroke-width="3"/>
  </g>"""


def head(*parts):
    return f"""
  <g {HEAD}>{''.join(parts)}
  </g>"""


BUST = ("M14,372 L14,304 C18,268 62,250 114,234 C126,230 132,224 136,214 L184,214 "
        "C188,224 194,230 206,234 C258,250 302,268 306,304 L306,372 Z")
BUST_SHADE = "M212,236 C260,252 302,268 306,304 L306,372 L234,372 C242,330 238,280 212,236 Z"
COLLAR = "M136,214 L110,238 L146,258 L160,240 L174,258 L210,238 L184,214 L160,240 Z"


def overalls(front="buttons", collar=PLATE, extra=""):
    """White racing overalls, to the chest."""
    s = f"""
  <path d="{BUST}" fill="{PLATE}" stroke="{INK}" stroke-width="3.2" stroke-linejoin="round"/>
  <path d="{BUST_SHADE}" fill="url(#tt1)"/>
  <path d="M60,290 C54,316 52,344 52,372 M260,290 C266,316 268,344 268,372" stroke="{INK}" stroke-width="3" fill="none" stroke-linecap="round"/>
  <path d="{COLLAR}" fill="{collar}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>"""
    if front == "zip":
        s += f"""
  <path d="M160,248 L160,344" stroke="{INK}" stroke-width="8"/>
  <path d="M160,266 L160,344" stroke="{PLATE}" stroke-width="3.4" stroke-dasharray="3 6"/>
  <path d="M152,244 h16 v18 h-16 z" fill="{INK}"/>
  <path d="M160,262 v10" stroke="{INK}" stroke-width="3"/>
  <circle cx="160" cy="276" r="5" fill="{PLATE}" stroke="{INK}" stroke-width="3"/>"""
    else:
        s += f"""
  <path d="M150,258 L150,344 M170,258 L170,344" stroke="{INK}" stroke-width="2.8" fill="none"/>
  <circle cx="160" cy="276" r="5.8" fill="{INK}"/><circle cx="160" cy="304" r="5.8" fill="{INK}"/><circle cx="160" cy="330" r="5.8" fill="{INK}"/>"""
    # breast pocket with a buttoned flap
    s += f"""
  <path d="M74,286 h50 v46 h-50 z" fill="{PLATE}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>
  <path d="M74,300 h50" stroke="{INK}" stroke-width="3"/>
  <circle cx="99" cy="293" r="3.6" fill="{INK}"/>"""
    # belt and buckle
    s += f"""
  <path d="M52,344 H268 V364 H52 Z" fill="{INK}"/>
  <path d="M142,339 h36 v30 h-36 z" fill="{PLATE}" stroke="{INK}" stroke-width="3.6" stroke-linejoin="round"/>
  <path d="M160,339 v30" stroke="{INK}" stroke-width="3.2"/>"""
    return s + extra


def bow_tie(spot):
    return f"""
  <path d="M160,243 L130,229 L132,262 Z M160,243 L190,229 L188,262 Z" fill="{spot}" stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>
  <circle cx="141" cy="245" r="2.8" fill="{INK}"/><circle cx="179" cy="245" r="2.8" fill="{INK}"/>
  <rect x="153" y="235" width="14" height="16" rx="2" fill="{spot}" stroke="{INK}" stroke-width="3"/>"""


def leathers():
    """Black racing leathers: collar turned up, double-breasted front, belt."""
    return f"""
  <path d="{BUST}" fill="{INK}" stroke="{INK}" stroke-width="3.2" stroke-linejoin="round"/>
  <path d="M60,290 C54,316 52,344 52,372 M260,290 C266,316 268,344 268,372" stroke="{PLATE}" stroke-width="2.8" fill="none" stroke-linecap="round"/>
  <path d="M136,214 L102,200 L108,252 L152,272 L160,246 Z" fill="{INK}" stroke="{PLATE}" stroke-width="2.8" stroke-linejoin="round"/>
  <path d="M184,214 L218,200 L212,252 L168,272 L160,246 Z" fill="{INK}" stroke="{PLATE}" stroke-width="2.8" stroke-linejoin="round"/>
  <path d="M168,272 L178,344" stroke="{PLATE}" stroke-width="2.8" fill="none"/>
  <circle cx="138" cy="294" r="5.6" fill="{PLATE}"/><circle cx="138" cy="322" r="5.6" fill="{PLATE}"/>
  <circle cx="200" cy="294" r="5.6" fill="{PLATE}"/><circle cx="200" cy="322" r="5.6" fill="{PLATE}"/>
  <path d="M78,300 L118,290" stroke="{PLATE}" stroke-width="2.8" stroke-linecap="round"/>
  <path d="M52,344 H268 V364 H52 Z" fill="{INK}" stroke="{PLATE}" stroke-width="2.8"/>
  <path d="M142,339 h36 v30 h-36 z" fill="{PLATE}" stroke="{INK}" stroke-width="3.6" stroke-linejoin="round"/>
  <path d="M160,339 v30" stroke="{INK}" stroke-width="3.2"/>"""


def svg(title, spot, body):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 380" role="img" aria-labelledby="t">
  <title id="t">{title}</title>{defs(spot)}
  <rect width="320" height="380" fill="{PLATE}"/>
  <g clip-path="url(#plate)">{body}
  </g>
  <rect x="6" y="6" width="308" height="368" fill="none" stroke="{INK}" stroke-width="4"/>
  <circle cx="104" cy="24" r="6.5" fill="{INK}"/><circle cx="216" cy="24" r="6.5" fill="{INK}"/>
</svg>
"""


def volozh():
    spot = GREEN
    body = (disc(spot) + overalls(front="zip", collar=spot)
            + head(d.neck(), d.face(), d.temples_grey(), d.lines_age(),
                   d.eyes("M120,176 Q135,170 150,175", "M171,175 Q186,170 200,176", lid=3),
                   d.nose(), d.mouth("level"), d.rimless(), d.basin_helmet(spot),
                   d.goggles_up("url(#ht1)", y=128, on_ink=False, glare=PLATE)))
    return svg("Portrait plate: a driver in a 1950s hard helmet, goggles raised, wearing wire spectacles and "
               "zip-fronted racing overalls with a breast pocket and belt.", spot, body)


def chernin():
    spot = RED
    body = (disc(spot) + overalls(front="buttons")
            + head(d.neck(), d.scarf_tucked(spot), d.face(), d.stubble(),
                   d.eyes("M119,174 Q135,165 151,173", "M170,173 Q186,165 201,174", lid=3.6),
                   d.nose(), d.mouth("wry"), d.leather_helmet(),
                   d.goggles_up(PLATE, y=112, on_ink=True, glare=INK)))
    return svg("Portrait plate: a bearded driver in a 1930s leather helmet, goggles raised, in white buttoned "
               "racing overalls with a spotted scarf, breast pocket and belt.", spot, body)


def lecun():
    spot = YELLOW
    jaw = "M102,168 C102,218 112,246 134,261 C146,270 174,270 186,261 C208,246 218,218 218,168 L218,136 L102,136 Z"
    body = (disc(spot) + overalls(front="buttons", extra=bow_tie(spot))
            + head(d.neck(), d.side_hair(), d.face(jaw=jaw),
                   d.eyes("M118,171 Q134,160 151,170", "M170,170 Q187,160 202,171", lid=3, smile=True),
                   d.nose(), d.mouth("smile"), d.spectacles(), d.flat_cap(spot),
                   d.goggles_up(spot, y=112, on_ink=True, glare=PLATE)))
    return svg("Portrait plate: a smiling driver in a reversed tweed cap and raised goggles, with round spectacles, "
               "in white buttoned racing overalls with a spotted bow tie, breast pocket and belt.", spot, body)


def teknium():
    spot = RED
    body = (disc(spot, tint=True) + leathers()
            + head(d.neck(), d.face(shade="ht2"), d.leather_helmet(), d.masked(spot)))
    return svg("Portrait plate: a masked driver in black racing leathers, leather helmet and goggles down, "
               "a scarf pulled up over the face and streaming in the wind.", spot, body)


if __name__ == "__main__":
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    for name, fn in (("volozh", volozh), ("chernin", chernin), ("lecun", lecun), ("teknium", teknium)):
        (out / f"driver-{name}.svg").write_text(fn())
        print("wrote", out / f"driver-{name}.svg")
