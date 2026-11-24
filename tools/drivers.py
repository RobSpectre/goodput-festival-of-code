#!/usr/bin/env python3
"""Draws the four driver pen-portraits as two-ink halftone plates.

Usage: drivers.py <out_dir>
Each plate is ink black plus one spot colour on buff stock: flat shapes,
a dot screen for the shadow tones, no gradients.
"""
import sys
from pathlib import Path

INK = "#1B1915"
PAPER = "#E9DDBF"
RED = "#B82B16"
GREEN = "#0F3D2C"
YELLOW = "#F6C02A"


def defs(spot):
    return f"""
  <defs>
    <pattern id="ht1" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
      <circle cx="2.5" cy="2.5" r="1.05" fill="{INK}"/>
    </pattern>
    <pattern id="ht2" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
      <circle cx="2.5" cy="2.5" r="1.7" fill="{INK}"/>
    </pattern>
    <pattern id="ht3" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">
      <rect width="5" height="5" fill="{INK}"/>
      <circle cx="2.5" cy="2.5" r="1.25" fill="{PAPER}"/>
    </pattern>
    <pattern id="sp1" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(15)">
      <circle cx="2.5" cy="2.5" r="1.5" fill="{spot}"/>
    </pattern>
    <pattern id="hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(-38)">
      <rect width="6" height="2.2" fill="{INK}"/>
    </pattern>
    <pattern id="tweed" width="10" height="10" patternUnits="userSpaceOnUse">
      <rect width="10" height="10" fill="{INK}"/>
      <path d="M0 5 L5 0 M5 10 L10 5 M0 10 L2.5 7.5 M7.5 2.5 L10 0" stroke="{PAPER}" stroke-width="1.3" fill="none"/>
      <path d="M0 0 L5 5 M5 5 L10 10" stroke="{PAPER}" stroke-width=".6" fill="none" opacity=".7"/>
    </pattern>
    <clipPath id="plate"><rect x="0" y="0" width="320" height="372"/></clipPath>
  </defs>"""


def disc(spot, cx=160, cy=186, r=150):
    # the roundel behind every driver, printed slightly out of register
    return f"""
  <circle cx="{cx + 3}" cy="{cy + 2}" r="{r}" fill="{spot}"/>
  <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{INK}" stroke-width="1.6"/>"""


def face(shade="ht1", jaw="M106,168 C106,214 114,240 136,258 C147,267 173,267 184,258 C206,240 214,214 214,168 L214,136 L106,136 Z"):
    # paper face, then the shadow side as a dot screen that follows the nose
    shadow = ("M166,136 L169,190 C170,202 177,208 178,214 C176,220 168,221 164,221 "
              "L166,236 C165,241 163,244 162,247 C163,254 166,260 168,265 "
              "C176,264 181,261 184,258 C206,240 214,214 214,168 L214,136 Z")
    return f"""
  <path d="{jaw}" fill="{PAPER}"/>
  <path d="{shadow}" fill="url(#{shade})"/>"""


def neck(shade="ht2"):
    return f"""
  <path d="M130,246 L130,312 L190,312 L190,246 Z" fill="{PAPER}"/>
  <path d="M130,256 C146,272 174,272 190,254 L190,312 L160,312 C158,296 146,282 130,276 Z" fill="url(#{shade})"/>"""


def eyes(brow_l, brow_r, lid=3.2, smile=False):
    crow = ""
    if smile:
        crow = (f'<path d="M116,190 l-7,-3 M116,194 l-7,2 M204,190 l7,-3 M204,194 l7,2" '
                f'stroke="{INK}" stroke-width="1.3" stroke-linecap="round" fill="none"/>')
    return f"""
  <path d="{brow_l}" stroke="{INK}" stroke-width="5" stroke-linecap="round" fill="none"/>
  <path d="{brow_r}" stroke="{INK}" stroke-width="5" stroke-linecap="round" fill="none"/>
  <path d="M122,188 Q135,178 149,187" stroke="{INK}" stroke-width="{lid}" stroke-linecap="round" fill="none"/>
  <path d="M172,187 Q186,178 199,188" stroke="{INK}" stroke-width="{lid}" stroke-linecap="round" fill="none"/>
  <circle cx="136" cy="188" r="4.6" fill="{INK}"/>
  <circle cx="185" cy="188" r="4.6" fill="{INK}"/>
  <circle cx="137.6" cy="186.4" r="1.3" fill="{PAPER}"/>
  <circle cx="186.6" cy="186.4" r="1.3" fill="{PAPER}"/>
  <path d="M126,194 Q136,198 146,194" stroke="{INK}" stroke-width="1.1" stroke-linecap="round" fill="none" opacity=".75"/>
  <path d="M175,194 Q185,198 196,194" stroke="{INK}" stroke-width="1.1" stroke-linecap="round" fill="none" opacity=".75"/>
  {crow}"""


def nose():
    return f"""
  <path d="M151,214 C147,217 148,223 154,224" stroke="{INK}" stroke-width="2" stroke-linecap="round" fill="none"/>
  <path d="M154,224 C160,229 170,228 177,221 C172,231 160,233 154,224 Z" fill="{INK}"/>"""


def mouth(kind="level"):
    if kind == "smile":
        return f"""
  <path d="M137,238 C148,250 172,250 184,237" stroke="{INK}" stroke-width="3.2" stroke-linecap="round" fill="none"/>
  <path d="M133,235 l5,4 M188,234 l-5,4" stroke="{INK}" stroke-width="2" stroke-linecap="round" fill="none"/>
  <path d="M150,254 Q160,258 171,254" stroke="{INK}" stroke-width="1.6" stroke-linecap="round" fill="none" opacity=".8"/>"""
    if kind == "wry":
        return f"""
  <path d="M140,242 C150,246 170,246 183,239" stroke="{INK}" stroke-width="3.2" stroke-linecap="round" fill="none"/>
  <path d="M151,253 Q160,256 170,252" stroke="{INK}" stroke-width="1.6" stroke-linecap="round" fill="none" opacity=".8"/>"""
    return f"""
  <path d="M140,241 C150,245 170,245 181,241" stroke="{INK}" stroke-width="3.2" stroke-linecap="round" fill="none"/>
  <path d="M151,252 Q160,255 170,252" stroke="{INK}" stroke-width="1.6" stroke-linecap="round" fill="none" opacity=".8"/>"""


def goggles_up(spot, y=112, on_ink=True, glare=PAPER):
    frame = PAPER if on_ink else INK
    strap = PAPER if on_ink else INK
    return f"""
  <path d="M92,{y + 6} L112,{y} M208,{y} L228,{y + 6}" stroke="{strap}" stroke-width="9" stroke-linecap="butt" fill="none"/>
  <path d="M151,{y} Q160,{y - 6} 169,{y}" stroke="{frame}" stroke-width="4" fill="none"/>
  <ellipse cx="132" cy="{y}" rx="23" ry="16" fill="{spot}" stroke="{frame}" stroke-width="4.5"/>
  <ellipse cx="188" cy="{y}" rx="23" ry="16" fill="{spot}" stroke="{frame}" stroke-width="4.5"/>
  <path d="M118,{y - 4} L130,{y - 11} L136,{y - 11} L122,{y + 2} Z" fill="{glare}" opacity=".9"/>
  <path d="M174,{y - 4} L186,{y - 11} L192,{y - 11} L178,{y + 2} Z" fill="{glare}" opacity=".9"/>"""


def leather_helmet(seam=True):
    # 1930s flying-style helmet: skull cap, ear rolls, chin strap
    s = f"""
  <path d="M96,206 C88,118 122,74 160,74 C198,74 232,118 224,206 L219,240 L204,244
           C212,222 214,196 214,168 L212,140 C190,132 130,132 108,140 L106,168
           C106,196 108,222 116,244 L101,240 Z" fill="{INK}"/>
  <path d="M114,240 C124,290 196,290 206,240" stroke="{INK}" stroke-width="9" fill="none"/>
  <rect x="116" y="252" width="13" height="11" rx="2" fill="{PAPER}" stroke="{INK}" stroke-width="2" transform="rotate(62 122 258)"/>
  <ellipse cx="101" cy="196" rx="9" ry="20" fill="none" stroke="{PAPER}" stroke-width="2"/>
  <ellipse cx="219" cy="196" rx="9" ry="20" fill="none" stroke="{PAPER}" stroke-width="2"/>"""
    if seam:
        s += f"""
  <path d="M160,76 L160,134" stroke="{PAPER}" stroke-width="1.6" stroke-dasharray="5 4" fill="none"/>
  <path d="M112,104 C136,92 184,92 208,104" stroke="{PAPER}" stroke-width="1.2" fill="none" opacity=".7"/>"""
    return s


def basin_helmet(spot):
    # 1950s hard helmet: white dome, centre stripe, short peak, leather flaps
    return f"""
  <path d="M100,202 L98,150 L110,150 L108,170 C106,196 108,222 116,246 L103,240 Z" fill="{INK}"/>
  <path d="M220,202 L222,150 L210,150 L212,170 C214,196 212,222 204,246 L217,240 Z" fill="{INK}"/>
  <path d="M114,242 C124,290 196,290 206,242" stroke="{INK}" stroke-width="8" fill="none"/>
  <path d="M94,150 C90,98 124,66 160,66 C196,66 230,98 226,150 Z" fill="{PAPER}" stroke="{INK}" stroke-width="2.4"/>
  <path d="M176,68 C210,78 228,108 226,150 L196,150 C198,118 192,88 176,68 Z" fill="url(#ht1)"/>
  <path d="M148,67 C150,92 150,122 148,150 L172,150 C170,122 170,92 172,67 C166,65.5 154,65.5 148,67 Z" fill="{spot}"/>
  <path d="M90,150 L230,150 L236,160 C200,150 120,150 84,160 Z" fill="{INK}"/>
  <path d="M100,160 C130,152 190,152 220,160 L214,144 L106,144 Z" fill="{INK}"/>"""


def flat_cap(spot):
    # cloth cap worn peak-backwards, the 1920s way
    return f"""
  <path d="M96,146 C84,96 124,70 164,72 C206,74 236,100 224,146 C196,134 124,134 96,146 Z" fill="url(#tweed)"/>
  <path d="M96,146 C124,134 196,134 224,146 L223,154 C196,142 124,142 97,154 Z" fill="{INK}"/>
  <circle cx="162" cy="76" r="5" fill="{INK}"/>"""


def side_hair():
    # grey wavy hair escaping at the temples, and ears, for the cap wearer
    return f"""
  <path d="M98,150 C84,160 82,186 92,210 C96,196 100,184 108,176 L108,152 Z" fill="url(#ht2)"/>
  <path d="M222,150 C236,160 238,186 228,210 C224,196 220,184 212,176 L212,152 Z" fill="url(#ht2)"/>
  <path d="M92,166 q6,-8 12,-4 M90,180 q6,-8 13,-3 M92,194 q6,-7 12,-3 M228,166 q-6,-8 -12,-4 M230,180 q-6,-8 -13,-3 M228,194 q-6,-7 -12,-3"
        stroke="{INK}" stroke-width="1.6" stroke-linecap="round" fill="none"/>
  <path d="M106,186 C96,184 94,206 106,214 Z" fill="{PAPER}" stroke="{INK}" stroke-width="1.6"/>
  <path d="M214,186 C224,184 226,206 214,214 Z" fill="{PAPER}" stroke="{INK}" stroke-width="1.6"/>"""


def spectacles():
    return f"""
  <rect x="113" y="174" width="43" height="30" rx="11" fill="none" stroke="{INK}" stroke-width="3.6"/>
  <rect x="165" y="174" width="43" height="30" rx="11" fill="none" stroke="{INK}" stroke-width="3.6"/>
  <path d="M156,186 Q160.500,181 165,186" stroke="{INK}" stroke-width="3" fill="none"/>
  <path d="M113,184 L104,181 M208,184 L216,181" stroke="{INK}" stroke-width="3" stroke-linecap="round" fill="none"/>
  <path d="M120,180 l9,-3 M172,180 l9,-3" stroke="{PAPER}" stroke-width="1.6" stroke-linecap="round"/>"""


def rimless():
    # light wire spectacles
    return f"""
  <rect x="116" y="177" width="38" height="24" rx="9" fill="none" stroke="{INK}" stroke-width="1.7"/>
  <rect x="167" y="177" width="38" height="24" rx="9" fill="none" stroke="{INK}" stroke-width="1.7"/>
  <path d="M154,187 Q160.500,183 167,187 M116,186 L106,183 M205,186 L214,183" stroke="{INK}" stroke-width="1.7" stroke-linecap="round" fill="none"/>"""


def stubble():
    return f"""
  <path d="M108,206 C112,236 122,250 136,258 C147,267 173,267 184,258 C198,250 208,236 212,206
           C204,226 194,236 184,232 C176,228 170,231 160,231 C150,231 144,228 136,232 C126,236 116,226 108,206 Z"
        fill="url(#ht2)"/>
  <path d="M138,232 C146,229 152,231 160,231 C168,231 174,229 182,232 C176,225 144,225 138,232 Z" fill="url(#ht2)"/>"""


def temples_grey():
    return f"""
  <path d="M108,152 L108,176 C112,172 114,164 114,152 Z" fill="url(#ht2)"/>
  <path d="M212,152 L212,176 C208,172 206,164 206,152 Z" fill="url(#ht2)"/>"""


def lines_age():
    # the lean, lined face of the veteran
    return f"""
  <path d="M146,226 C140,234 138,240 138,248 M176,226 C182,234 184,240 184,248" stroke="{INK}" stroke-width="1.5" stroke-linecap="round" fill="none"/>
  <path d="M124,214 C122,224 124,232 130,240" stroke="{INK}" stroke-width="1.2" stroke-linecap="round" fill="none" opacity=".8"/>
  <path d="M140,158 Q160,155 180,158" stroke="{INK}" stroke-width="1" stroke-linecap="round" fill="none" opacity=".55"/>"""


def torso(kind, spot):
    base = "M22,372 L22,356 C36,326 92,312 130,302 L190,302 C228,312 284,326 298,356 L298,372 Z"
    if kind == "overalls":
        # white linen overalls: screen tone, buttoned placket, soft collar
        return f"""
  <path d="{base}" fill="{PAPER}"/>
  <path d="{base}" fill="url(#ht1)"/>
  <path d="M190,302 C228,312 284,326 298,356 L298,372 L206,372 C210,346 204,322 190,302 Z" fill="url(#ht2)"/>
  <path d="M130,300 L112,318 L146,338 L160,316 L174,338 L208,318 L190,300 L160,316 Z" fill="{PAPER}" stroke="{INK}" stroke-width="2.2" stroke-linejoin="round"/>
  <path d="M160,330 L160,372" stroke="{INK}" stroke-width="2"/>
  <circle cx="160" cy="346" r="4" fill="{INK}"/><circle cx="160" cy="364" r="4" fill="{INK}"/>
  <path d="M60,340 C52,350 48,360 46,372 M260,340 C268,350 272,360 274,372" stroke="{INK}" stroke-width="1.6" fill="none"/>"""
    if kind == "polo":
        # short-sleeved sports shirt, the 1950s works driver
        return f"""
  <path d="{base}" fill="{PAPER}"/>
  <path d="{base}" fill="url(#ht1)"/>
  <path d="M190,302 C228,312 284,326 298,356 L298,372 L210,372 C214,346 206,322 190,302 Z" fill="url(#ht2)"/>
  <path d="M128,298 L104,322 L140,346 L160,318 L180,346 L216,322 L192,298 L160,318 Z" fill="{spot}" stroke="{INK}" stroke-width="2.2" stroke-linejoin="round"/>
  <path d="M160,320 L160,372" stroke="{INK}" stroke-width="2"/>
  <circle cx="160" cy="342" r="3.6" fill="{INK}"/><circle cx="160" cy="360" r="3.6" fill="{INK}"/>
  <path d="M58,340 C50,350 46,360 44,372 M262,340 C270,350 274,360 276,372" stroke="{INK}" stroke-width="1.6" fill="none"/>"""
    if kind == "tweed":
        # tweed jacket, soft collar and a spotted bow tie
        return f"""
  <path d="{base}" fill="url(#tweed)"/>
  <path d="M130,302 L160,372 L190,302 Z" fill="{PAPER}"/>
  <path d="M130,302 L112,330 L150,372 L160,372 Z" fill="{INK}"/>
  <path d="M190,302 L208,330 L170,372 L160,372 Z" fill="{INK}"/>
  <path d="M132,300 L146,322 L160,310 L174,322 L188,300 L160,310 Z" fill="{PAPER}" stroke="{INK}" stroke-width="2" stroke-linejoin="round"/>
  <path d="M160,322 L132,310 L134,340 Z M160,322 L188,310 L186,340 Z" fill="{spot}" stroke="{INK}" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="143" cy="324" r="2.2" fill="{INK}"/><circle cx="177" cy="324" r="2.2" fill="{INK}"/>
  <circle cx="150" cy="330" r="1.8" fill="{INK}"/><circle cx="170" cy="330" r="1.8" fill="{INK}"/>
  <rect x="154" y="316" width="12" height="13" rx="2" fill="{spot}" stroke="{INK}" stroke-width="2"/>"""
    if kind == "leather":
        # black leather coat with the collar turned up
        return f"""
  <path d="{base}" fill="{INK}"/>
  <path d="M118,300 L96,290 L104,336 L150,372 L160,372 L160,330 Z" fill="{INK}" stroke="{PAPER}" stroke-width="1.6" stroke-linejoin="round"/>
  <path d="M202,300 L224,290 L216,336 L170,372 L160,372 L160,330 Z" fill="{INK}" stroke="{PAPER}" stroke-width="1.6" stroke-linejoin="round"/>
  <path d="M52,346 C44,354 40,362 38,372 M268,346 C276,354 280,362 282,372" stroke="{PAPER}" stroke-width="1.4" fill="none" opacity=".8"/>
  <circle cx="160" cy="352" r="4" fill="{PAPER}"/>"""
    return ""


def scarf_tucked(spot):
    return f"""
  <path d="M126,286 C140,300 180,300 194,286 L198,306 C182,322 138,322 122,306 Z" fill="{spot}" stroke="{INK}" stroke-width="1.8" stroke-linejoin="round"/>
  <circle cx="140" cy="304" r="2.6" fill="{PAPER}"/><circle cx="156" cy="309" r="2.6" fill="{PAPER}"/>
  <circle cx="172" cy="307" r="2.6" fill="{PAPER}"/><circle cx="186" cy="300" r="2.6" fill="{PAPER}"/>
  <circle cx="148" cy="296" r="2.6" fill="{PAPER}"/><circle cx="166" cy="298" r="2.6" fill="{PAPER}"/>"""


def masked(spot):
    # goggles down and a scarf pulled up over nose and mouth: the nom de course
    return f"""
  <path d="M206,258 C236,246 262,262 308,236 L312,258 C274,280 240,266 210,282 Z" fill="{spot}" stroke="{INK}" stroke-width="1.8" stroke-linejoin="round"/>
  <path d="M208,278 C232,278 252,292 288,284 L284,304 C254,312 232,298 210,300 Z" fill="{spot}" stroke="{INK}" stroke-width="1.8" stroke-linejoin="round"/>
  <path d="M232,262 C252,262 272,262 296,250 M230,290 C248,294 264,298 280,296" stroke="{PAPER}" stroke-width="1.5" fill="none" opacity=".85"/>
  <path d="M104,214 C122,204 142,208 160,202 C178,208 198,204 216,214 C218,238 212,256 202,270
           C198,284 200,298 208,310 L112,310 C120,298 122,284 118,270 C108,256 102,238 104,214 Z"
        fill="{spot}" stroke="{INK}" stroke-width="1.8" stroke-linejoin="round"/>
  <path d="M116,232 C140,246 182,246 206,230 M120,254 C144,268 178,268 202,252 M122,284 C146,294 176,294 200,284"
        stroke="{PAPER}" stroke-width="1.6" fill="none" opacity=".85"/>
  <path d="M160,204 C167,212 169,220 165,228" stroke="{PAPER}" stroke-width="1.6" fill="none" opacity=".85"/>
  <path d="M92,184 L112,180 M208,180 L228,184" stroke="{PAPER}" stroke-width="10" stroke-linecap="butt" fill="none"/>
  <path d="M152,182 Q160,176 168,182" stroke="{PAPER}" stroke-width="4.5" fill="none"/>
  <path d="M106,172 C108,160 148,160 154,176 C156,194 146,204 130,204 C114,204 104,190 106,172 Z" fill="{INK}" stroke="{PAPER}" stroke-width="4.5"/>
  <path d="M214,172 C212,160 172,160 166,176 C164,194 174,204 190,204 C206,204 216,190 214,172 Z" fill="{INK}" stroke="{PAPER}" stroke-width="4.5"/>
  <path d="M114,176 L128,166 L138,166 L120,184 Z M174,176 L188,166 L198,166 L180,184 Z" fill="{PAPER}"/>
  <path d="M130,197 L142,185 L146,189 L136,199 Z M190,197 L202,185 L206,189 L196,199 Z" fill="{spot}"/>"""


def disc_tint(spot, cx=160, cy=186, r=150):
    # a screened disc: the spot colour laid down as a dot tint
    return f"""
  <circle cx="{cx + 3}" cy="{cy + 2}" r="{r}" fill="url(#sp1)"/>
  <circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{INK}" stroke-width="1.6"/>"""


def baseline():
    # the plate is trimmed square at the foot, with a keyline
    return f"""
  <path d="M10,372 L310,372" stroke="{INK}" stroke-width="2.4"/>
  <path d="M10,377 L310,377" stroke="{INK}" stroke-width=".9"/>"""


def svg(title, spot, body):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 380" role="img" aria-labelledby="t">
  <title id="t">{title}</title>{defs(spot)}
  <g clip-path="url(#plate)">{body}
  </g>{baseline()}
</svg>
"""


def volozh():
    spot = GREEN
    body = (disc(spot) + torso("polo", spot) + neck() + face() + temples_grey() + lines_age()
            + eyes("M120,176 Q135,170 150,175", "M171,175 Q186,170 200,176", lid=3)
            + nose() + mouth("level") + rimless() + basin_helmet(spot)
            + goggles_up("url(#ht1)", y=128, on_ink=False))
    return svg("Illustrated portrait of a driver in a 1950s hard helmet, goggles raised, wearing wire spectacles and a sports shirt.", spot, body)


def chernin():
    spot = RED
    body = (disc(spot) + torso("overalls", spot) + neck() + scarf_tucked(spot) + face() + stubble()
            + eyes("M119,174 Q135,165 151,173", "M170,173 Q186,165 201,174", lid=3.6)
            + nose() + mouth("wry") + leather_helmet() + goggles_up(PAPER, y=112, glare=INK))
    return svg("Illustrated portrait of a bearded driver in a 1930s leather helmet, goggles raised, in white overalls and a spotted scarf.", spot, body)


def lecun():
    spot = YELLOW
    jaw = "M102,168 C102,218 112,246 134,261 C146,270 174,270 186,261 C208,246 218,218 218,168 L218,136 L102,136 Z"
    body = (disc(spot) + torso("tweed", spot) + neck() + side_hair() + face(jaw=jaw)
            + eyes("M118,171 Q134,160 151,170", "M170,170 Q187,160 202,171", lid=3, smile=True)
            + nose() + mouth("smile") + spectacles() + flat_cap(spot)
            + goggles_up(spot, y=112, on_ink=True))
    return svg("Illustrated portrait of a smiling driver in a reversed tweed cap and raised goggles, with round spectacles, a tweed jacket and a spotted bow tie.", spot, body)


def teknium():
    spot = RED
    body = (disc_tint(spot) + torso("leather", spot) + neck() + face(shade="ht2") + leather_helmet()
            + masked(spot))
    return svg("Illustrated portrait of a masked driver: leather helmet, goggles down, a scarf pulled up over the face and streaming in the wind.", spot, body)


if __name__ == "__main__":
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    for name, fn in (("volozh", volozh), ("chernin", chernin), ("lecun", lecun), ("teknium", teknium)):
        (out / f"driver-{name}.svg").write_text(fn())
        print("wrote", out / f"driver-{name}.svg")
