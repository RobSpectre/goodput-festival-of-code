---
name: Goodput Festival of Code
description: The official programme of a race meeting for inference, printed in four letterpress inks on buff stock.
colors:
  yellow: "#F6C02A"
  green: "#0F3D2C"
  red: "#B22812"
  ink: "#1B1915"
  stock: "#E8D6AA"
  salmon: "#DFA88F"
  ink-soft: "#3F3B31"
  stock-soft: "#CFC09A"
typography:
  display:
    fontFamily: "Rammetto One, ui-rounded, system-ui, sans-serif"
    fontSize: "15.1vw"
    fontWeight: 400
    lineHeight: 0.84
    letterSpacing: "-0.012em"
  headline:
    fontFamily: "Stint Ultra Condensed, Rockwell Condensed, Georgia, serif"
    fontSize: "clamp(4.5rem, 11.5vw, 10.5rem)"
    fontWeight: 400
    lineHeight: 0.9
    letterSpacing: "0.012em"
  title:
    fontFamily: "Stint Ultra Condensed, Rockwell Condensed, Georgia, serif"
    fontSize: "clamp(3rem, 5.4vw, 5rem)"
    fontWeight: 400
    lineHeight: 0.9
    letterSpacing: "0.012em"
  script:
    fontFamily: "Yesteryear, Brush Script MT, cursive"
    fontSize: "clamp(2.75rem, 6.1vw, 7.5rem)"
    fontWeight: 400
    lineHeight: 1
  figure:
    fontFamily: "Old Standard TT, Century Schoolbook, Georgia, serif"
    fontSize: "2rem"
    fontWeight: 400
    lineHeight: 1
  stamp:
    fontFamily: "Hammersmith One, Gill Sans, Gill Sans MT, Trebuchet MS, sans-serif"
    fontSize: "1.5rem"
    fontWeight: 400
    lineHeight: 1
    letterSpacing: "0.16em"
  lede-l:
    fontFamily: "Old Standard TT, Century Schoolbook, Georgia, serif"
    fontSize: "1.5rem"
    fontWeight: 400
    lineHeight: 1.4
  lede:
    fontFamily: "Old Standard TT, Century Schoolbook, Georgia, serif"
    fontSize: "1.3125rem"
    fontWeight: 400
    lineHeight: 1.4
  body:
    fontFamily: "Old Standard TT, Century Schoolbook, Georgia, serif"
    fontSize: "1.1875rem"
    fontWeight: 400
    lineHeight: 1.55
  small:
    fontFamily: "Old Standard TT, Century Schoolbook, Georgia, serif"
    fontSize: "1.125rem"
    fontWeight: 400
    lineHeight: 1.3
  caption:
    fontFamily: "Old Standard TT, Century Schoolbook, Georgia, serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.45
  label-l:
    fontFamily: "Hammersmith One, Gill Sans, Gill Sans MT, Trebuchet MS, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: "0.16em"
  label:
    fontFamily: "Hammersmith One, Gill Sans, Gill Sans MT, Trebuchet MS, sans-serif"
    fontSize: "0.8125rem"
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: "0.16em"
  label-s:
    fontFamily: "Hammersmith One, Gill Sans, Gill Sans MT, Trebuchet MS, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: "0.2em"
rounded:
  none: "0"
  roundel: "50%"
spacing:
  gutter: "clamp(20px, 4vw, 64px)"
  pad-y: "clamp(72px, 9vw, 136px)"
  column-gap: "clamp(20px, 2.4vw, 40px)"
  mast-h: "56px"
  sheet: "1320px"
components:
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.yellow}"
    typography: "{typography.label-l}"
    rounded: "{rounded.none}"
    padding: "0 26px"
    height: "60px"
  button-primary-hover:
    backgroundColor: "{colors.red}"
    textColor: "{colors.stock}"
  button-on-green:
    backgroundColor: "{colors.yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.label-l}"
    rounded: "{rounded.none}"
    padding: "0 26px"
    height: "56px"
  button-on-green-hover:
    backgroundColor: "{colors.stock}"
    textColor: "{colors.ink}"
  masthead:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.stock}"
    typography: "{typography.label}"
    height: "{spacing.mast-h}"
  masthead-cta:
    backgroundColor: "{colors.yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "0 16px"
    height: "40px"
  masthead-cta-hover:
    backgroundColor: "{colors.stock}"
    textColor: "{colors.ink}"
  treatment-toggle:
    textColor: "{colors.stock}"
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "0 12px"
    height: "40px"
  treatment-toggle-hover:
    backgroundColor: "{colors.yellow}"
    textColor: "{colors.ink}"
  treatment-menu:
    backgroundColor: "{colors.stock}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "2px 16px 4px"
  race-card:
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    padding: "11px 0"
  forecast-input:
    textColor: "{colors.stock}"
    rounded: "{rounded.none}"
    padding: "0 2px"
    height: "56px"
  stamp:
    textColor: "{colors.red}"
    typography: "{typography.stamp}"
    rounded: "{rounded.none}"
    padding: "11px 16px 9px"
  roundel:
    backgroundColor: "{colors.stock}"
    textColor: "{colors.ink}"
    rounded: "{rounded.roundel}"
    size: "clamp(76px, 7.2vw, 108px)"
  notice:
    textColor: "{colors.red}"
    rounded: "{rounded.none}"
    padding: "clamp(20px, 2.6vw, 36px) clamp(20px, 3vw, 44px)"
---

# Design System: Goodput Festival of Code

> **Three treatments.** The site is one landing page drawn three ways, switchable from a "Treatment" menu in every header. Each is a complete, separate visual world.
>
> | Treatment | Files |
> |---|---|
> | The Official Programme | `docs/index.html`, `docs/assets/css/programme.css`, `docs/assets/js/main.js`, `docs/assets/fonts/`, `docs/assets/img/` |
> | The Timekeepers' Tower | `docs/tower/` |
> | The Hand-Inked Lap Chart | `docs/lap-chart/` |
>
> **The frontmatter tokens and the eight sections that follow describe the Official Programme only.** The other two treatments are recorded in their own parts after "Shared Across Treatments", and their tokens are kept out of the frontmatter on purpose.

## Overview

**Creative North Star: "The Official Programme"**

The site is the souvenir programme of a 1930s-50s race meeting, read page by page. Each section is a printed page in one stock or one ink: a chrome-yellow cover, buff text pages, a racing-green plate, a salmon insert, a yellow tear-off coupon, a black colophon. Nothing is a card floating on a background; the page itself is the object, edge to edge, and it changes colour when you turn it.

Everything on it is made the way a jobbing printer would have made it. Four inks, flat. Tone comes from dot screens and hatching, never from blends. The passes sit slightly out of register and the vermilion overprints what lies beneath it. Five typefaces each have one job and are never swapped. The furniture is the furniture of a programme: dot-leader entry tables, Oxford rules, number roundels, rubber stamps, a price seal, a perforation line with scissors. Every piece of that furniture carries a real fact about the event.

The density is that of print: very large bill lines set to fill their measure, then quiet book-weight text in narrow columns beside them. Motion belongs to the press and the instrument: plates slide into register once, a chronometric needle steps rather than sweeps, wheels turn and then settle into print.

**Key Characteristics:**
- Four inks (chrome yellow, racing green, vermilion, ink black) on buff stock, plus one salmon insert stock. No other colour exists.
- Flat shapes only: no gradients, no shadows, no blur. Depth is overprint, knockout and misregistration.
- Square corners on every box; circles only where the period object is round (roundels, seals, dials).
- Five single-weight voices: fat poster capitals, tracked label capitals, a tall condensed slab, a Modern text face, one brush script.
- Full-bleed pages that change stock, each closed by an italic folio ("Page three").
- Bill lines are fitted to the column width by script; they wrap on phones.
- Paper tooth: a fine noise grain over buff, yellow and green pages.

## Colors

A letterpress job in four inks and two paper stocks; every surface is one of them printed solid.

### Primary
- **Chrome Yellow** (`yellow`): the cover and the entry coupon, whole pages of it. Off the yellow pages it is the signal on dark grounds: the running-head name and call to action, the button on the green plate, the forecast frame and focus rings on green and black.
- **Ink Black** (`ink`): the key plate. All text on light stock, every rule, the running head, the colophon, the primary button, the dial face, all line work and halftone screens in the illustrations.

### Secondary
- **Racing Green** (`green`): owns the record-attempt page outright. Elsewhere it is an ink in the plates (the car, the trees, the exhibition hall on the plan) and the colour of the entrant names on the salmon insert.

### Tertiary
- **Vermilion** (`red`): titling and marks. The cover title, the brush-script overline on the coupon, rubber stamps, the defined word, the warning notice heading, the dial needle and its limit band, bunting, and the hover state of the black button and of event names. Also the selection highlight and caret.

### Neutral
- **Buff Stock** (`stock`): the paper of the text pages, and the "unprinted" colour inside plates (knockouts, the marshal's coat, the roundel ground). On green and black it is the text colour.
- **Salmon Insert** (`salmon`): one page only, the customers' insert. Read as vermilion screened back onto stock; it carries no grain.
- **Soft Ink** (`ink-soft`): ink screened back on buff, for folios, captions and footnotes in italic.
- **Soft Stock** (`stock-soft`): buff screened back on green and black, for captions, hints and table rules on the dark pages.

### Named Rules
**The Four Inks Rule.** Every colour on a page is one of the four inks or one of the two stocks. A lighter tone is made with a dot screen, a hatch, or the two "soft" screened values, never with a new colour, an alpha wash over a photograph, or a gradient.

**The Whole Page Rule.** An ink that owns a page owns it edge to edge. Yellow, green and salmon are never used as tinted panels inside a buff page.

**The Vermilion Size Rule.** Vermilion on chrome yellow measures about 3.9:1, so it is set only at display sizes (24px and up): the title, the script, the stamp. Small text on yellow is ink black. Vermilion on buff (about 4.6:1) may go down to heading sizes.

## Typography

**Display Font:** Rammetto One (with ui-rounded, system-ui, sans-serif)
**Bill Font:** Stint Ultra Condensed (with Rockwell Condensed, Georgia, serif)
**Body Font:** Old Standard TT, regular, italic and bold (with Century Schoolbook, Georgia, serif)
**Label Font:** Hammersmith One (with Gill Sans, Trebuchet MS, sans-serif)
**Script Font:** Yesteryear (with Brush Script MT, cursive)

**Character:** A printer's type case from between the wars: one fat poster face, one tall slab for bills, one sans for labels, one bookish Modern for reading, one sign-writer's script. All are self-hosted latin subsets and all but the text face exist in a single weight, so emphasis comes from changing voice and size, not weight.

### Hierarchy
The page has one ramp. Ten static steps are named tokens; four fluid roles are written out where they are used; every other fluid size runs between two values of the ramp.

- **Display** (400, 15.1vw fitted to the measure, line-height .84, uppercase): the cover title in vermilion, multiplied over the plate. The same face sets racing numerals on the roundels (clamp 1rem to 1.5rem; five characters clamp .8125rem to 1.1875rem), the entrant names on the insert (clamp 3rem / 12vw / 10.5rem, fitted, capped at 120px), the fat event line and the notice heading (both clamp 1.5rem to 3rem).
- **Headline** (400, clamp 4.5rem / 11.5vw / 10.5rem, line-height .9, uppercase, balanced): the bill line that opens every page. The coupon's keeps the same endpoints on a steeper slope (12.4vw; 23vw on phones); the cover date runs clamp 4.5rem / 7vw / 7.5rem.
- **Title** (400, clamp 3rem / 5.4vw / 5rem, line-height .9, uppercase): driver names on the grid and the event names in the order of events. On phones the same endpoints take a steeper slope (14.5vw to 16vw).
- **Script** (400, clamp 2.75rem / 6.1vw / 7.5rem, rotated -2 to -4 degrees): two overlines only, on the cover and the coupon (the coupon's stops at 5rem). It carries a stroke in the page colour (.1em to .16em, painted under the fill) so it reads where it crosses a headline.
- **Figure** (2rem): the forecast figure in italic text face with tabular lining numerals, and the defined word in the poster face. The record page's italic yellow lede climbs to it (clamp 1.5rem to 2rem).
- **Stamp** (1.5rem, label capitals, tracked .16em): the rubber stamp. This is the 24px floor for vermilion on yellow.
- **Large lede** (1.5rem, line-height 1.35 to 1.4): the foreword's first paragraph, the address, the notice text. The "Order of events" heading is set at this step in label capitals tracked .3em between two Oxford rules, so a page-level heading outranks the block titles.
- **Lede** (1.3125rem, line-height 1.4): the opening paragraph of a page; columns are capped at 28rem to 36rem.
- **Body** (1.1875rem, line-height 1.55): running text, capped at about 33rem to 34rem. Under 700px body drops to the small step.
- **Small** (1.125rem, line-height 1.3 to 1.5): table values and the definition.
- **Caption** (1rem, usually italic, line-height 1.4 to 1.5): folios, figure captions, footnotes, hints, the colophon, in the soft screened colour of the page.
- **Large label** (1rem, label capitals, tracked .14em to .16em): buttons, block titles, the venue line, the tracked text link.
- **Label** (.8125rem, label capitals, tracked .13em to .16em): table terms, running head, form labels, colophon. Two labels grow from this step with the sheet: the event row (to 1rem) and the entrant trades (to 1.125rem, tracked .2em).
- **Small label** (.75rem, label capitals): the "Detach here" tab and the running-head name on phones.

### Named Rules
**The Five Voices Rule.** Each face has one job. Poster capitals for names and numbers, the slab for bill lines, label capitals for anything a clerk would stamp or rule, the Modern for anything read as a sentence, the script for a flourish across a headline. Do not set a sentence in the label face or a label in the text face.

**The Fitted Line Rule.** A bill line marked for fitting is sized by script to fill its column on one line (less 2px), after fonts load and on resize. Under 700px the fitted event names are released to wrap at a fixed clamp. Stars between names are drawn marks that ride the line's measure.

**The One Ramp Rule.** A static size is one of the ten ramp steps. A fluid size is one of the four fluid roles, or a clamp whose two ends are both values on the ramp. A new size is a new step added to the ramp on purpose, never a one-off.

**The Drawn Lettering Rule.** Lettering inside a plate (seal, scrutineer's stamp, the car's number, dial, plan) is part of the drawing: it is sized as an attribute on the drawn text in the drawing's own units and scales with the plate, at one size for every width. It is not on the page ramp and is never sized from the stylesheet.

**The Whole Name Rule.** The script crosses a headline at its baseline only, so every letter of the headline stays legible.

## Layout

A stack of full-bleed pages. Each page pads itself (top `pad-y`, sides `gutter`, bottom 72% of `pad-y`) and holds one sheet capped at 1320px. Inside the sheet a twelve-column grid (`column-gap` between columns, clamp 28px to 72px between rows) places a full-width bill line first and then asymmetric blocks beneath it: 5/3/4 on the meeting page, 6/6 for dial and copy, 6/5 with a spare column for plan and glossary, 7/5 for coupon title and body. Text columns are narrow and capped in rem, so the wide sheet reads as print columns with air between them.

The cover is the exception: text and plate share one grid cell, the plate anchored to the foot and the lettering printed over it, with a minimum height of the viewport less the running head (or 118px + 40vw, whichever is greater). The driver grid is two columns split by a dashed centre line, with the even slots dropped by clamp 72px to 168px so the four stand staggered like a starting grid.

The running head is a sticky 56px black strip (two rows, 100px in all, under 700px); anchors land clear of it. Pages are closed by a centred italic folio. A checkered band (28px, 14px squares, ruled 3px above and below) opens the first text page; a dashed perforation with scissors and a "Detach here" tab sits astride the top edge of the coupon.

Responsive behaviour, as built:
- **The running head sheds in order:** the long form of the name under 1500px, the contents links under 1280px, the word "Treatment" under 860px. Name, Treatment menu and call to action always remain.
- **1100 to 1239px:** the cover action moves under the date, clear of the rotunda, and the cover grows 72px taller.
- **Under 1100px:** the cover stops overlapping (text, then plate); every twelve-column block goes full width, except foreword and definition at 7/5; the price seal and the scrutineer's stamp are dropped; driver slots stack portrait over entry with the portrait capped at 320px.
- **Under 700px:** the running head is two rows, name and action above, the Treatment menu full width beneath a yellow hairline; body drops to 1.125rem; the cover plate is cropped to 150vw and shifted so the car fills the sheet with the rotunda behind its nose, and the bunting string left of the rotunda is left out of that crop so it does not cross the driver; the venue line sets on two lines without its middle dot; the script sits in flow under the title, right-aligned; dot leaders are dropped and table values wrap under their terms, left-aligned; the driver grid is one column with odd and even slots inset 14% from opposite sides; buttons are 56px tall.
- **Print:** running head, seal, forecast form and coupon actions are removed, and paper grain is switched off.

## Elevation & Depth

Flat. There are no box shadows, text shadows, blurs or gradients anywhere in the build. Depth is a printing effect, made three ways:

- **Overprint.** The vermilion pass and the cover title use multiply blending, so red darkens where it crosses green or black, as transparent ink does.
- **Misregistration.** At rest the vermilion pass sits at translate(-1.6px, 1.2px) and the green pass at translate(1.2px, -.9px). Portrait discs are printed 3px right and 2px down of their keyline.
- **Knockout and screen.** Shapes are "left unprinted" in buff inside a plate; shadow tones are 5px dot screens at 45 degrees (dot radius 1.05 light, 1.7 dark), a 6px hatch at -38 degrees, or a reversed screen of buff dots on ink.

Paper tooth is a 240px tiled fractal-noise image (base frequency .85, two octaves): dark flecks on buff and yellow, light flecks on green. The salmon insert, the running head and the colophon carry none.

### Named Rules
**The Flat Ink Rule.** If a surface needs to look lifted, darker or lit, it is drawn that way with a screen, a hatch, a keyline or a second pass out of register. Shadows and gradients are not in this system.

**The Keyline Rule.** Where one ink would be lost against another (the vermilion needle on the black dial, the script over a headline), it gets a thin stroke in the ground colour painted beneath the fill, not a glow.

## Shapes

Every box is square-cornered (radius 0): buttons, inputs, frames, stamps, the notice. The circle is reserved for things that were round in the period object: number roundels, the price seal and scrutineer's stamp (an ellipse), the dial, wheels, portrait discs, and the small ring that marks the current treatment in the menu.

Rules do the structural work, in a small set of weights, always in the text colour of the page:
- **Hairline (1.5px):** table rows, list dividers, glossary rows, the outer keyline of double frames.
- **Leader (2px dotted, 60 to 70% strength):** dot leaders between a term and its value; the forecast input's baseline (full strength).
- **Oxford rule (5px over 1.5px, 9px overall):** section breaks and the flanks of the "Order of events" heading. A lone 5px rule heads the definition, the glossary, the entrant list and the coupon particulars.
- **Frame:** 2px for the forecast box and the plan (the plan with a 1px keyline 5px outside); 4px for the stamp; 6px for the notice with a 1.5px keyline 12px inside; 6px three-sided for the painted grid box above each driver.
- **Dashed (3px):** the perforation and the grid's centre line.

Marks are tilted by hand, a few degrees only: stamps -4, the scrutineer's stamp -9, the seal +9, the scripts -2 to -4.

## Components

### Buttons
One button, cut like a letterpress sort: a solid block with label capitals and a drawn arrow.
- **Shape:** square (0), 60px tall (56px under 700px and inside the forecast form), 26px side padding, 14px gap to a 30 by 14px line arrow.
- **Primary:** ink black block, chrome yellow label capitals at the large-label step tracked .15em. Used on yellow and buff pages.
- **On green:** chrome yellow block, ink label. Used on the green plate.
- **Hover:** primary turns vermilion with buff lettering; on-green turns buff. The arrow advances 6px (.25s). Colour changes take .18s on the system's one easing curve.
- **Active:** the block drops 2px, like a pressed sort.
- **Focus:** a 3px outline offset 3px: ink on light pages, yellow on green, the running head and the colophon.
- **Running-head action:** a smaller yellow block (40px, 44px on phones, label step), turning buff on hover.

### Race card (dot-leader table)
The system's table. A definition list of rows ruled 1.5px top and bottom: the term in label capitals (label step, tracked .15em) at the left, a dotted leader that takes the slack, the value in the text face (small step) ranged right. On the green plate the rules are soft stock. Under 700px the leader is dropped and the value sets beneath the term. A result not yet known is a ruled blank, not a placeholder figure.

### Bill line and event listing
A page opens with one bill line. The order of events is a numbered list of whole-row links: a fitted bill-face name, then a row of label capitals with a leader and "Page three" plus an arrow. Hover turns the name vermilion and advances the arrow.

### Forecast field and dial
- **Field:** no box. A transparent input with a 2px dotted buff baseline, italic text face at the figure step with tabular lining figures, yellow caret; label capitals above. The placeholder asks for a whole number and suggests no figure. It sits inside a 2px yellow frame with a yellow label heading and a soft-stock hint.
- **Focus:** 3px yellow outline, offset 4px.
- **Error:** the baseline turns solid yellow and the status line beneath turns yellow with a plain instruction. Messages keep the programme's voice and say what to enter.
- **Dial:** a black face on a buff bezel with a screened outer ring, buff scale and numerals (0 to 12, times 1,000), a vermilion limit band over the last sixth, a seven-drum odometer and a vermilion needle keylined in buff. Its legends are drawn lettering, one size at every width. The needle steps to its value every 95ms with a little shake, easing out; it never sweeps. A forecast past the scale parks the needle just beyond the end and stamps "Off the clock" (a yellow-keylined black label that lands from 1.5 scale in .22s). On first view the dial runs up the scale and back; a saved forecast is shown instead. The forecast is kept in the visitor's own browser, and a text link in italic ("Rub it out") clears it.

### Roundel
A racing number on a buff disc: 3px ink ring with a 1.5px keyline 4px outside, poster face numerals (a tighter, smaller setting for five characters). It overlaps the top-left of a portrait plate. The numbers are NVIDIA cluster names.

### Stamps and seal
- **Rubber stamp:** a 4px vermilion frame with vermilion label capitals at the stamp step, tilted -4 degrees, no fill. It keeps its size on phones and sets on two lines.
- **Scrutineer's stamp:** a double vermilion ellipse with lettering on its curves and one poster-face word, tilted -9 degrees at 90% strength. Decorative; dropped under 1100px.
- **Price seal:** a buff disc with two ink rings, lettering around the ring, and the price in vermilion script, tilted 9 degrees in the cover's bottom corner over the far colonnade. It is sized and placed in viewport units (9vw wide, .55vw from the right edge, 1.2vw from the foot) so it scales with the plate and always clears the rotunda. It lands last on load (.3s at 1.25s). Dropped under 1100px.

### Notice
A warning board: 6px ink frame with an inner keyline, a vermilion poster-face heading beside a short text in the lede size. One per page at most.

### Coupon
The closing page as a tear-off: yellow stock, a dashed perforation with scissors astride its top edge, a very large bill line crossed by a vermilion script, one paragraph, the button, and a ruled line of particulars in label capitals. When the entry office is closed the button saves the date and a rubber stamp says so; when it is open the stamp gives way to the invitation button and "Save the date" becomes a tracked text link.

### Navigation
A sticky black running head: the event name in yellow label capitals (buff on hover), the Treatment menu beside it, four contents links in buff (label step, tracked .14em) and the yellow action block. Links turn yellow with a 2px underline set 7px below on hover. There is no hamburger on small sheets; the head sheds its parts by width and becomes two rows on phones.

### Treatment menu
A ruled box in the running head that opens a printed slip.
- **Closed:** a 1.5px yellow box, 40px tall, in label capitals: "Treatment:" in yellow, then "Official Programme" in buff, then a small drawn chevron. Hover and open fill the box yellow with ink lettering; the chevron turns over.
- **Open:** a buff slip with a 2px ink border and a 6px ink head rule, set 8px below the box. Three entries ruled 1.5px apart: the name in large label capitals over a one-line description in italic caption; a 12px ring at the left, filled vermilion for the current page. Hover underlines the name.
- **Under 700px:** the box loses its frame and becomes a full-width row (46px) under a yellow hairline, chevron at the far right; the slip opens full width beneath it.
- **Focus:** yellow ring on the box, ink ring inside the slip.

### Text links
Inherit the text colour, underlined at 1.5px with a .2em offset, thickening to 3px on hover.

### Plates (illustration)
All illustration is drawn as vector line work in the page's inks; there are no photographs or raster images.
- **The cover plate** is built as a printer would: a stock layer of knockouts, then vermilion, green and the black key plate as separate groups, each sliding into register on load from up to 26px away (1.15s, staggered .15s). While it "prints" the wheels spin, the car jolts, the road streaks, the scarf flutters and dust trails off, each for a fixed count, then all settle into a still print. A pointer over the plate starts them again.
- **Driver portraits** are generated by a script as two-ink plates on a 320 by 380 sheet: ink black plus one spot ink (green, vermilion or yellow) on buff, a 150-radius disc behind the head printed slightly out of register (or laid as a dot tint), dot screens for shadow, period headgear and overalls. They are figures in period dress, not likenesses.
- **The plan** is a ruled map in ink, green and vermilion with a wave pattern for water, label capitals for buildings and italic text face for places, inside a double frame.
- Small marks (arrow, five-point star, scissors) are drawn inline in the current text colour.

### Motion
One easing curve, an exponential ease-out (cubic-bezier(.16, 1, .3, 1)), for every state change (.12s to .25s). Entrance motion is the cover's registration and nothing else; no section animates on scroll except the dial's self-check. With reduced motion set, plates are in register from the first frame, nothing spins, and the needle jumps straight to its value. Adding `?still` to the address parks every animation, for captures.

## Do's and Don'ts

### Do:
- **Do** give each new page one stock or ink, full bleed, with the paper grain on buff, yellow and green, and close it with an italic folio.
- **Do** open a page with a single bill line in the condensed slab, then set the facts beneath it in narrow columns on the twelve-column sheet (1320px cap).
- **Do** put tabular facts in a race card: label capitals, dot leader, value ranged right, 1.5px rules.
- **Do** make tone with dot screens (5px grid at 45 degrees), hatching and knockouts, and let passes sit a pixel or two out of register.
- **Do** keep vermilion on yellow to 24px and larger; use ink black for anything smaller on yellow.
- **Do** take every type size from the ramp, and size lettering inside a plate in the drawing itself.
- **Do** keep every box square and every rule in the page's text colour, at 1.5px, 2px, 3px, 5px or 6px.
- **Do** use the yellow focus ring on green and black grounds and the ink ring on yellow, buff and salmon.
- **Do** let a programme device carry a real fact (a roundel is a cluster name, the dial reads tokens per second), and leave an unknown result as a ruled blank.
- **Do** give every looping or entrance animation a still end state and honour reduced motion.

### Don't:
- **Don't** use gradients, box shadows, text shadows, glows or blur. The build has none.
- **Don't** introduce a colour outside the four inks and two stocks, or tint one with transparency to make a panel.
- **Don't** round the corners of buttons, inputs, frames or images. Circles belong to roundels, seals, dials, wheels and the menu's marker ring.
- **Don't** set a fifth weight or a sixth face; four of the five faces have one weight, and emphasis is a change of voice.
- **Don't** let the script or a stamp cover the letters of a headline; it crosses the baseline and carries a ground-colour stroke.
- **Don't** place yellow, green or salmon as a card inside a buff page; an ink takes the whole page or stays inside a plate.
- **Don't** sweep the needle or ease anything with bounce; the instrument steps and the press slides home once.
- **Don't** use photographs, raster textures or icon fonts; marks and plates are drawn in the inks.

## Shared Across Treatments

The three treatments are three complete pages for one event. They share facts and behaviour, never appearance.

**What is shared**
- **The one setting.** `docs/assets/js/config.js` holds `window.GOODPUT.inviteUrl`. While it is empty, every treatment's closing section says entries open shortly and its working action is "Save the date"; once set, every invitation button on all three leads to it and each closing section swaps to its open state.
- **The Treatment menu's markup and behaviour.** A native disclosure, `details.treatments[data-treatments]`, with a summary holding `.treatments__label` ("Treatment"), `.treatments__current` (this page's name) and `.treatments__chev`, and a `.treatments__menu` list of three links, each a name in `strong` over a one-line description, the current one marked `aria-current="page"`. `docs/assets/js/treatments.js` closes it on Escape (returning focus to the summary), on a click outside, and when focus leaves; without the script it still opens and closes. Every treatment marks the current entry with a filled marker in its own red.
- **Still mode.** `treatments.js` adds the class `still` to the root for `?still`; each stylesheet parks its own animations and transitions under that class.
- **The forecast.** One browser storage key, `goodput.forecast`, so a forecast entered on one treatment is shown on the others. Every treatment accepts a whole number from 1 to 9,999,999, keeps it on the visitor's own device, offers a way to remove it, and suggests no figure (the placeholder is "a whole number").
- **The calendar file** (`docs/assets/goodput-festival-of-code.ics`) and the favicon.
- **Portrait heads.** `tools/drivers.py` draws the four heads; the other two portrait scripts import it and re-ink the drawings in their own inks and shading.

### Named Rules
**The Separate Worlds Rule.** A treatment owns its folder, its stylesheet, its script, its fonts folder and its portraits. No typeface, colour token or component style crosses from one treatment to another; a face used by one is not available to the other two.

**The Behaviour Only Rule.** Files under `docs/assets/js/` that all three load carry behaviour and settings only. They set no styles, inject no markup and name no colours, so each treatment draws the shared menu and states in its own vocabulary.

**The Same Facts Rule.** All three say the same things: the same dates, venue, four drivers and racing numbers, three customers, the record left unposted, the same closed and open states. A fact changed on one is changed on all three.

## Treatment: The Timekeepers' Tower

Files: `docs/tower/index.html`, `docs/tower/tower.css`, `docs/tower/tower.js`, fonts in `docs/tower/fonts/`, portraits in `docs/tower/img/` drawn by `tools/tower-drivers.py`.

A trackside scoreboard tower. Racing-green gloss boards are bolted to a black timber frame whose two posts show at the sides; plank seams and bolt heads are drawn on every board. Facts are hung, not typeset: cream enamel tiles with black numerals on hooks that show through two holes, a little out of true. A chrome-yellow pit board carries the action. Anything typed or pencilled is on paper pinned to the tower. A place with nothing to post is shown as bare hooks.

### Tower palette
- **Board Green** (#114232): the boards. **Deep Green** (#0A2B20): recesses for unposted tiles, plank seams, the ground behind the ledger sheet.
- **Frame Black** (#151412): the page ground, the fascia, tile numerals, keylines, the black board for the customers. **Post** (#2A2823): the timber posts where they show.
- **Pit Yellow** (#F4C20D): the pit boards, column heads on green, the fascia's rule, the visitor's own number tile, board titles on black.
- **Enamel Cream** (#F3E9CF): tiles, paper, painted lettering on green and black, the finger board.
- **Signal Red** (#C4271B): on cream only (the defined word, the finger board's title, drawing pins, the ledger's margin line, the current-treatment marker, the button's hover on paper), or as the whole warning board with cream lettering.
- **Thinned Cream** (#C3D2BA) and **Dim Cream** (#CFC6AE): second-rank painted lettering and row rules on green and on black respectively. **Soft Ink** (#45423A): second-rank type on paper. **Ledger Rule** (#9DB3B0): the ruling of the sheet.

### Tower type
Five faces, split by material.
- **Signwriter's block** (Bungee 400): painted names and board titles. **Inline block** (Bungee Inline): the name board only.
- **Tall gothic** (Big Shoulders Display, variable, used at 700, 800 and 900): tile numerals, column heads, and painted sentences in upper and lower case. It is the page's default voice.
- **Typewriter** (Special Elite): typed matter, on paper only. **Pencil** (Kalam 400 and 700): written entries, on paper only.

Static ramp for anything set as text: label .8125rem (painted column heads, tracked .16em, uppercase), small .9375rem, note 1rem (slips, small print), body 1.125rem (the sheet), lede 1.375rem (painted sentences, pencilled entries), small signwriting 1.75rem.

Lettering painted at board scale is sized in modules with a rem floor: board title max(1.75rem, 6 modules); entrant max(1.375rem, 3.4 modules); customer names max(1.75rem, 5.2 modules); warning title max(1.75rem, 4 modules); the big pit board max(2.75rem, 11 modules); the name 14.6 modules with "Festival of Code" at 5.2; the month 6. The sheet's typed heading runs clamp(1.75rem, 3.4vw, 3rem).

### Tower layout
One module sizes the tower: `--m` is clamp(5.8px, the lesser of .8333vw and (viewport height less 64px) / 62, 16px). 120 modules make the tower's width, so it fills a wide window and narrows, posts showing, when the window is short enough that the three hero boards would not fit one screen. Boards stack with one module between them and are padded 3 by 4 modules; bolts are 1.5 modules, planks 6 modules deep. Tiles are 10 by 14 modules (date), 13 by 8.5 (racing number) and 6 by 8.5 (figures), each tilted by under two degrees and hung with slightly uneven gaps.

The fascia is a sticky 64px black strip with a 3px yellow rule under it. The ledger sheet is capped at 1240px with every line of type on a 32px rule and a red margin line; the paddock is a twelve-column stage (finger board 7, glossary 5, warning board full width).

- **Under 1240px:** the board links leave the fascia. **Under 1000px:** "Festival of Code" leaves the fascia; boards restack to one column; the record list drops its head row and puts the time beneath; the second scorer is dropped. **Under 860px:** the venue takes two lines.
- **Under 700px:** the module becomes 1/62 of the width, so the five date tiles fill the board exactly; the posts and bolts are dropped; the fascia is 56px; list rows become stacked cells with their column head painted above each; the hero pit board is dropped and the fascia's pit board is fixed along the foot of the screen (68px), with the page padded to clear it. **Under 380px:** the word "Treatment" is dropped.
- **Print:** fascia, forecast slip, hero pit board and second scorer are removed.

### Tower components
- **Board:** green (or black with a yellow keyline half a module inside), four bolts, plank seams. Titles in the block face, cream on green, yellow on black.
- **Tile:** cream enamel, black gothic numeral at weight 900, a 2px black keyline inside the edge, two hook holes near the top. The visitor's number tile is yellow.
- **Recess and hook pair:** an empty place on the record board is a deep-green recess with two bare hooks; everywhere else an unposted value is a drawn pair of hooks over "To be posted".
- **Pit board (the action):** yellow, black lettering, a 3px black keyline 5px inside, a drawn arrow. Hover turns it cream and advances the arrow 6px; pressed, it drops 2px. Three sizes: in the fascia (two lines: when and where, then the action), on the hero board (block face at 3.3 modules), and the closing board across the tower's foot.
- **Button on paper:** a black block with yellow gothic capitals (56px tall, 3px border). Hover is red with cream lettering on cream paper, and cream with black lettering on the yellow board.
- **Paper:** cream, 3px black border, a red drawing pin at the top centre. Three kinds: a typed note pinned to a board at a slight angle; the ruled ledger sheet; the forecast slip.
- **List board:** a four-column table (No. / Entrant / Machine / Time) with yellow column heads over a 4px cream rule, rows ruled 2px. Number tile, optional portrait plate, name in the block face, machine in gothic capitals.
- **Forecast slip (signature interaction):** a pinned slip with a typed heading, a field whose 3px writing line belongs to the field and whose figure is pencilled (Kalam 700, 1.75rem), and the button. The figure is hung tile by tile on the visitor's row, right to left on the last of seven hooks, under the official row whose hooks stay empty. Errors turn the writing line and the message red. "Take it down" clears it.
- **Finger board and warning board:** the address on a cream board with a red title and a drawn pointing hand; the warning as a red board with a cream keyline 10px inside.
- **Treatment menu:** a cream enamel plate with a black keyline inside; yellow on hover and when open; the list is a cream plate with a 4px black border and a 3px yellow outline, entries ruled 2px, a round marker filled red for the current page.
- **Focus:** a 3px cream ring on paint, a black ring on paper and on the yellow boards.

### Tower motion and illustration
Tiles are hung, they do not fade: each drops from above, overshoots and settles with one small swing (.62s for the date tiles, staggered up to .78s; .5s for forecast tiles, 90ms apart) on cubic-bezier(.2, .9, .3, 1). State changes take .15s; the arrow .22s. Nothing loops and nothing is animated from script.

Illustration is flat colour with one coarse ruled hatch (6-unit pitch at -52 degrees). The scorer on his ladder appears twice, hanging the last date tile and reaching up to the visitor's row. Portraits are cream enamel plates with two hanging holes, hung as wide as a number tile, with the bust drawn to the chest so the racing suit reads.

### Tower rules
**The Painted or Paper Rule.** What is painted on a board is set in the signwriter's faces. What is typed or pencilled is always on paper: the ledger sheet or a slip pinned to a board. The typewriter and the pencil never appear directly on paint.

**The One Module Rule.** Boards, tiles, gaps and lettering painted at board scale are sized in modules, so the tower keeps its proportions at every width.

**The Bare Hooks Rule.** A value that does not exist yet is shown as empty hooks and the words "to be posted". No figure, dash or zero stands in for it.

**The Red on Cream Rule.** Red appears on cream, or as the whole warning board. It is never laid on yellow or green.

### Tower don'ts
- Don't set small tiles in a grid of metrics; tiles are few and large.
- Don't fade, slide or loop anything; a tile drops onto its hooks once.
- Don't put typed or pencilled text straight onto a board.
- Don't use gradients, shadows or gloss highlights; the paint is flat and tone is one hatch.
- Don't borrow the Programme's or the Lap Chart's faces, inks or furniture.

## Treatment: The Hand-Inked Lap Chart

Files: `docs/lap-chart/index.html` (generated by `tools/lap-chart/build.py` from `tools/lap-chart/template.html`; never edited by hand), `docs/lap-chart/lap-chart.css`, `docs/lap-chart/lap-chart.js`, fonts in `docs/lap-chart/fonts/`, portraits in `docs/lap-chart/img/` drawn by `tools/lap-chart-drivers.py`.

The meeting argued in hand-inked charts, after the data portraits W. E. B. Du Bois and his students made for the 1900 Paris Exposition (credited in the colophon). Every section is a plate titled by a question and answered by one chart whose form was invented for it. What was counted is drawn to scale; what is not yet known is drawn as a gap or as a form with no scale, and says so on the drawing.

### Lap Chart palette
- **Board** (#EFE3C8): the aged cream sheet; the header; text on the dark plates.
- **Ink** (#171512): all text and every keyline; the record plate and the colophon.
- **Crimson** (#B8232A): the unknown (the spiral and its question mark), the two inked days, the closing plate, the button's hover, the current-treatment swatch.
- **Gold** (#E3A81C): the "What is goodput?" plate, the visitor's forecast line, emphasis and focus on the ink plate, hover fills.
- **Emerald** (#1E6B4A): the customers' plate and one driver's square.
- **Soft Ink** (#4A4337): ink thinned, for second-rank text on the board.

Each ink owns whole plates and whole fields. Shapes carry an ink keyline with the colour laid flat inside.

### Lap Chart type
Three hands.
- **Fat hand-cut capitals** (Londrina Solid 900; 400 for figures on a ruled sheet): titles, questions, names, racing numbers.
- **Drafting hand** (Dekko, always in capitals, tracked .05em to .09em): every caption, label, button and note on a drawing.
- **Ink-soft serif** (Averia Serif Libre 400, italic, 700): prose.

Static ramp: small capitals .875rem; small 1rem; drafting hand 1.125rem; body 1.1875rem; lede 1.5rem; names and numbers 2rem. Fluid roles: question clamp(2.5rem, 5.2vw, 4.5rem); title clamp(3.5rem, 6.9vw, 6.5rem). Lettering inside a chart is sized on the drawing in its own units (22 to 50), never from the stylesheet.

### Lap Chart layout
Full-bleed plates separated by a 2.5px ink rule, padded clamp(64px, 8vw, 116px) by clamp(20px, 4.4vw, 64px), each holding a sheet capped at 1240px. A plate is a centred question (at most 16 characters to the line), then a two-column pairing of chart and text (5/7, 4/7 or 7/5), or a row of four squares. Board, ink, emerald and crimson plates carry a paper tooth; the tooth is dark on light grounds and light on dark ones.

The first plate is one screen: the title across the top, then three columns with the chart in the middle sized to the viewport height (at least 430px, at most 800px), the date, place, offer and action at the left, and the blank lap-chart form with a reading note at the right. The header is a sticky 62px board-coloured bar with an ink rule beneath.

- **Under 1180px:** the long name leaves the header; the first plate becomes two columns with the chart spanning both rows at the right. **Under 1060px:** the chart links leave the header.
- **Under 960px:** everything is one column, centred on the first plate; the driver squares go two to a row.
- **Under 700px:** the header is two rows, the Treatment menu on top (which scrolls away) and the name and action beneath (which stay); the first plate runs title, date, place, action, chart, offer, lap chart, so the question mark is on the first screen; charts run at full bleed; the forecast's coil and rows stack, still to one scale; squares go one to a row.
- **Print:** header, forecast form and closing actions are removed, and the tooth is switched off.

### Lap Chart components
- **Plate question:** fat capitals, centred, balanced.
- **Legend:** a term in the drafting hand at the left, its value in prose at the right, a 1.5px rule under each row; on phones the value wraps beneath.
- **Button:** an inked block, 56px tall, drafting-hand capitals, a drawn arrow. Ink on board (hover crimson); gold on the ink plate (hover board); board on the crimson plate (hover gold); a board-coloured outline for secondary actions on ink. Pressed, it drops 2px.
- **The meeting in one line (first plate):** a single ribbon with mitred corners runs as four straight bars to one scale (4 drivers, 3 customers, 2 days, 1 machine), then turns crimson and coils into a spiral with a question mark at its centre: tokens per second, drawn to no scale and labelled so.
- **Lap-chart form:** a ruled timekeeper's form with the four racing numbers entered and every lap blank.
- **Idea bar:** throughput as one bar, split beneath into goodput and wheelspin, marked illustrative and not to scale.
- **Forecast (signature interaction):** a field on the ink plate inside a 2px gold frame (dotted board-coloured baseline, tabular figures at 2rem, gold focus ring and gold error state). The figure is inked as a gold coil; "Unroll it" moves the same ink from the coil onto twelve ruled rows that run back and forth, a thousand tokens per second to the row, and "Coil it again" returns it. The ink on the coil plus the ink on the rows is always the same length. Past twelve thousand an arrow marks the line running off the sheet. A saved forecast is shown coiled. "Rub it out" clears it.
- **Driver squares:** four flat squares (gold, emerald, crimson, and one left open for the driver entered under a nom de course), each with the racing number in the corner and a pen-and-ink portrait standing on its foot, a name and a two-row legend beneath.
- **Fan:** three equal wedges for the three customers, drawn equal on purpose and captioned so.
- **Calendar:** the thirty days of April 2027 as ruled squares with two inked crimson.
- **Tag:** a 2px outlined label in the drafting hand for a status that is not an action.
- **Treatment menu:** a chart key. A 2px ink box, gold on hover and when open; the list gives each treatment a square swatch, filled crimson for the current page.
- **Focus:** a 3px ink ring on board and gold; gold on ink and the colophon; board on emerald and crimson.

### Lap Chart motion and illustration
Ink is drawn, never faded. On load the first plate's line is revealed in one continuous stroke along its middle (3.4s after a .35s pause), bars first, then the coil. The forecast inks and unrolls over 700ms to 2s depending on its length, easing in and out. State changes take .16s on cubic-bezier(.16, 1, .3, 1). Reduced motion and still mode show every drawing complete.

The charts are plain vector drawings set into the page by the build script; nothing is computed in the browser except how much of the forecast line is inked. Every "ruled" edge carries a slow waver that is part of the geometry, so edges stay crisp and shared corners stay shared; nothing is filtered. The forecast sheet alone is drawn true, because its lengths are measured. Portraits are the shared heads re-inked: pen hatching in place of dot screens, an ink keyline, no disc behind the head.

### Lap Chart rules
**The One Question, One Chart Rule.** Each plate asks one question and answers it with one drawing whose form belongs to that question. No chart form is reused as a template.

**The Counted or Blank Rule.** A length drawn to scale was counted. Anything not yet known is drawn blank, or to no scale and labelled so. No figure appears that was not counted or entered by the visitor.

**The Drawn Waver Rule.** The hand is in the geometry, produced by the build script. No blur, displacement or roughening filter is applied, and measured drawings are ruled true.

**The Generated Page Rule.** The page is built from the template and the build script. A change is made there and rebuilt, never in the generated file.

### Lap Chart don'ts
- Don't draw axes-and-cards analytics, gauges or dashboards.
- Don't rank the customers or size anything by a number nobody measured.
- Don't use gradients, shadows or filters; inks are flat and saturated inside an ink keyline.
- Don't set the drafting hand in lower case, or prose in it.
- Don't borrow the Programme's or the Tower's faces, inks or furniture.
