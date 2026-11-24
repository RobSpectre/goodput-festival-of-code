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
  caption:
    fontFamily: "Old Standard TT, Century Schoolbook, Georgia, serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.45
  label:
    fontFamily: "Hammersmith One, Gill Sans, Gill Sans MT, Trebuchet MS, sans-serif"
    fontSize: "0.875rem"
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: "0.16em"
  script:
    fontFamily: "Yesteryear, Brush Script MT, cursive"
    fontSize: "clamp(2.75rem, 6.1vw, 7.5rem)"
    fontWeight: 400
    lineHeight: 1
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
    typography: "{typography.label}"
    rounded: "{rounded.none}"
    padding: "0 26px"
    height: "60px"
  button-primary-hover:
    backgroundColor: "{colors.red}"
    textColor: "{colors.stock}"
  button-on-green:
    backgroundColor: "{colors.yellow}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
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
    typography: "{typography.label}"
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
- **Display** (400, 15.1vw fitted to the measure, line-height .84, uppercase): the cover title in vermilion, multiplied over the plate. The same face at smaller sizes sets racing numerals (roundels, the car's number), the entrant names on the insert (fitted, capped at 150px), the fat event line, the defined word (1.75rem) and the notice heading (clamp 1.75rem to 3.25rem).
- **Headline** (400, clamp 4.5rem / 11.5vw / 10.5rem, line-height .9, uppercase, balanced): the bill line that opens every page. The coupon's runs larger (clamp 6rem / 12.4vw / 11.75rem); the cover date and event names use the same face at clamp 4rem / 7vw / 6.75rem.
- **Title** (400, clamp 3rem / 5.4vw / 5rem, line-height .9, uppercase): driver names on the grid.
- **Lede** (400, 1.3125rem to 1.4375rem, line-height 1.4): the opening paragraph of a page and the notice text; columns are capped at 28rem to 36rem. The record page's lede is italic in yellow at clamp 1.625rem to 2.125rem.
- **Body** (400, 1.1875rem, line-height 1.55; 1.125rem under 700px): running text, capped at about 33rem to 34rem. Table values are 1.0625rem to 1.125rem.
- **Caption** (italic 400, 1rem to 1.0625rem, line-height 1.45): folios, figure captions, footnotes, in the soft screened colour of the page.
- **Label** (400, .8125rem to 1.0625rem, tracked .14em to .2em, uppercase): table terms, running head, buttons, stamps, seal and dial legends, form labels. The "Order of events" heading opens the tracking to .3em between two Oxford rules.
- **Script** (400, clamp 2.75rem / 6.1vw / 7.5rem, rotated -2 to -4 degrees): two overlines only, on the cover and the coupon, plus the maker's name on the dial and the price on the seal. It carries a stroke in the page colour (.1em to .16em, painted under the fill) so it reads where it crosses a headline.

### Named Rules
**The Five Voices Rule.** Each face has one job. Poster capitals for names and numbers, the slab for bill lines, label capitals for anything a clerk would stamp or rule, the Modern for anything read as a sentence, the script for a flourish across a headline. Do not set a sentence in the label face or a label in the text face.

**The Fitted Line Rule.** A bill line marked for fitting is sized by script to fill its column on one line (less 2px), after fonts load and on resize. Under 700px the fitted event names are released to wrap at a fixed clamp. Stars between names are drawn marks that ride the line's measure.

**The Whole Name Rule.** The script crosses a headline at its baseline only, so every letter of the headline stays legible.

## Layout

A stack of full-bleed pages. Each page pads itself (top `pad-y`, sides `gutter`, bottom 72% of `pad-y`) and holds one sheet capped at 1320px. Inside the sheet a twelve-column grid (`column-gap` between columns, clamp 28px to 72px between rows) places a full-width bill line first and then asymmetric blocks beneath it: 5/3/4 on the meeting page, 6/6 for dial and copy, 6/5 with a spare column for plan and glossary, 7/5 for coupon title and body. Text columns are narrow and capped in rem, so the wide sheet reads as print columns with air between them.

The cover is the exception: text and plate share one grid cell, the plate anchored to the foot and the lettering printed over it, with a minimum height of the viewport less the running head (or 118px + 40vw, whichever is greater). The driver grid is two columns split by a dashed centre line, with the even slots dropped by clamp 72px to 168px so the four stand staggered like a starting grid.

The running head is a sticky 56px black strip (52px under 700px); anchors land clear of it. Pages are closed by a centred italic folio. A checkered band (28px, 14px squares, ruled 3px above and below) opens the first text page; a dashed perforation with scissors and a "Detach here" tab sits astride the top edge of the coupon.

Responsive behaviour, as built:
- **1160 to 1359px:** the running head drops the long form of the name.
- **Under 1160px:** the contents links leave the running head; name and call to action remain.
- **1100 to 1239px:** the cover action moves under the date, clear of the rotunda, and the cover grows 72px taller.
- **Under 1100px:** the cover stops overlapping (text, then plate); every twelve-column block goes full width, except foreword and definition at 7/5; the price seal and the scrutineer's stamp are dropped; driver slots stack portrait over entry with the portrait capped at 320px.
- **Under 700px:** body drops to 1.125rem; the cover plate is cropped to 150vw and shifted so the car fills the sheet with the rotunda behind its nose, and the bunting string left of the rotunda is left out of that crop so it does not cross the driver; the venue line sets on two lines without its middle dot; the script sits in flow under the title, right-aligned; dot leaders are dropped and table values wrap under their terms, left-aligned; the driver grid is one column with odd and even slots inset 14% from opposite sides; buttons are 56px tall.
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

Every box is square-cornered (radius 0): buttons, inputs, frames, stamps, the notice. The circle is reserved for things that were round in the period object: number roundels, the price seal and scrutineer's stamp (an ellipse), the dial, wheels, portrait discs.

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
- **Primary:** ink black block, chrome yellow label capitals at 1rem tracked .15em. Used on yellow and buff pages.
- **On green:** chrome yellow block, ink label. Used on the green plate.
- **Hover:** primary turns vermilion with buff lettering; on-green turns buff. The arrow advances 6px (.25s). Colour changes take .18s on the system's one easing curve.
- **Active:** the block drops 2px, like a pressed sort.
- **Focus:** a 3px outline offset 3px: ink on light pages, yellow on green, the running head and the colophon.
- **Running-head action:** a smaller yellow block (40px, 44px on phones, .8125rem), turning buff on hover.

### Race card (dot-leader table)
The system's table. A definition list of rows ruled 1.5px top and bottom: the term in label capitals (.8125rem, tracked .15em) at the left, a dotted leader that takes the slack, the value in the text face (1.125rem) ranged right. On the green plate the rules are soft stock. Under 700px the leader is dropped and the value sets beneath the term. A result not yet known is a ruled blank, not a placeholder figure.

### Bill line and event listing
A page opens with one bill line. The order of events is a numbered list of whole-row links: a fitted bill-face name, then a row of label capitals with a leader and "Page three" plus an arrow. Hover turns the name vermilion and advances the arrow.

### Forecast field and dial
- **Field:** no box. A transparent input with a 2px dotted buff baseline, italic text face at 2rem with tabular lining figures, yellow caret; label capitals above. It sits inside a 2px yellow frame with a yellow label heading and a soft-stock hint.
- **Focus:** 3px yellow outline, offset 4px.
- **Error:** the baseline turns solid yellow and the status line beneath turns yellow with a plain instruction. Messages keep the programme's voice and say what to enter.
- **Dial:** a black face on a buff bezel with a screened outer ring, buff scale and numerals (0 to 12, times 1,000), a vermilion limit band over the last sixth, a seven-drum odometer and a vermilion needle keylined in buff. The needle steps to its value every 95ms with a little shake, easing out; it never sweeps. A forecast past the scale parks the needle just beyond the end and stamps "Off the clock" (a yellow-keylined black label that lands from 1.5 scale in .22s). On first view the dial runs up the scale and back; a saved forecast is shown instead. The forecast is kept in the visitor's own browser, and a text link in italic ("Rub it out") clears it.

### Roundel
A racing number on a buff disc: 3px ink ring with a 1.5px keyline 4px outside, poster face numerals (a tighter, smaller setting for five characters). It overlaps the top-left of a portrait plate. The numbers are NVIDIA cluster names.

### Stamps and seal
- **Rubber stamp:** a 4px vermilion frame with vermilion label capitals at 1.5rem, tilted -4 degrees, no fill. It keeps its size on phones and sets on two lines.
- **Scrutineer's stamp:** a double vermilion ellipse with lettering on its curves and one poster-face word, tilted -9 degrees at 90% strength. Decorative; dropped under 1100px.
- **Price seal:** a buff disc with two ink rings, lettering around the ring, and the price in vermilion script, tilted 9 degrees in the cover's bottom corner over the far colonnade. It is sized and placed in viewport units (9vw wide, .55vw from the right edge, 1.2vw from the foot) so it scales with the plate and always clears the rotunda. It lands last on load (.3s at 1.25s). Dropped under 1100px.

### Notice
A warning board: 6px ink frame with an inner keyline, a vermilion poster-face heading beside a short text in the lede size. One per page at most.

### Coupon
The closing page as a tear-off: yellow stock, a dashed perforation with scissors astride its top edge, a very large bill line crossed by a vermilion script, one paragraph, the button, and a ruled line of particulars in label capitals. When the entry office is closed the button saves the date and a rubber stamp says so; when it is open the stamp gives way to the invitation button and "Save the date" becomes a tracked text link.

### Navigation
A sticky black running head: the event name in yellow label capitals with "Official Programme" in buff after a centred dot, four contents links in buff (.8125rem, tracked .14em) and the yellow action block. Links turn yellow with a 2px underline set 7px below on hover. There is no menu on small sheets; the links simply leave and the name stacks on two lines.

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
- **Do** keep every box square and every rule in the page's text colour, at 1.5px, 2px, 3px, 5px or 6px.
- **Do** use the yellow focus ring on green and black grounds and the ink ring on yellow, buff and salmon.
- **Do** let a programme device carry a real fact (a roundel is a cluster name, the dial reads tokens per second), and leave an unknown result as a ruled blank.
- **Do** give every looping or entrance animation a still end state and honour reduced motion.

### Don't:
- **Don't** use gradients, box shadows, text shadows, glows or blur. The build has none.
- **Don't** introduce a colour outside the four inks and two stocks, or tint one with transparency to make a panel.
- **Don't** round the corners of buttons, inputs, frames or images. Circles belong to roundels, seals, dials and wheels.
- **Don't** set a fifth weight or a sixth face; four of the five faces have one weight, and emphasis is a change of voice.
- **Don't** let the script or a stamp cover the letters of a headline; it crosses the baseline and carries a ground-colour stroke.
- **Don't** place yellow, green or salmon as a card inside a buff page; an ink takes the whole page or stays inside a plate.
- **Don't** sweep the needle or ease anything with bounce; the instrument steps and the press slides home once.
- **Don't** use photographs, raster textures or icon fonts; marks and plates are drawn in the inks.
