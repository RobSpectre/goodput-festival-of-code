---
version: 1
slug: "docs-index-html"
primary_target: "docs/index.html"
related_targets: []
---

# Surface brief: landing page (docs/index.html)

## Scope and mode

The single landing page of the Goodput Festival of Code. Mode: **Persuade**.

## Audience, job, action

- Audience: AI engineers and builders first; technical leaders and buyers second.
- Job: decide whether this is a real technical event worth two days in San Francisco.
- Action: **Request an invitation**. The destination URL is not decided. Until it is set (one constant, `INVITE_URL`, in `docs/assets/js/main.js`), the entry form shows an "Entries open shortly" stamp and makes "Save the date" (a calendar file) its working action; the cover and running-head buttons lead there. Setting the URL swaps the stamp for the invitation button.
- Proof and content: the user's programme facts only (four speakers, the Nebius Token Factory record attempt on NVIDIA Vera Rubin, Cursor / Higgsfield / Cognition on Nebius AI Cloud, dates, venue). No agenda times, talk titles, record figures or testimonials exist; none are invented.
- Constraints: static HTML/CSS/JS in `docs/`; no logos or photos on hand, so names are set in type and portraits are original illustrations; inspiration from Goodwood, no Goodwood marks.

## Direction contract

**THESIS.** The page is the souvenir race-day programme of a 1930s-50s meeting, read page by page, and every piece of programme furniture carries a real fact: the entry list is the speakers, the record page is the Vera Rubin attempt, the tear-off entry form is the invitation. It refuses the tech-conference template (dark gradient hero, headshot grid, logo wall, agenda accordion) and equally the soft "vintage" rendition of cream paper under a serif.

**OWN-WORLD.** Four letterpress inks on programme stock, each owning whole pages: chrome yellow (cover, entry form), racing green (the record plate), vermilion (titling, stamps; screened to salmon for the insert), ink black; buff text pages between them. Flat litho shapes, halftone dot screens, visible misregistration; no gradients, no soft shadows, no rounded cards. Type: fat Granby-style poster capitals for titling and racing numerals, Johnston-style tracked capitals for labels, a tall condensed slab for bill headlines, a Modern text face with italics, one brush script. Components: ruled entry tables with dot leaders, Oxford rules, number roundels, rubber stamps, a price seal, a perforated coupon.

**STORY.** In one screen the visitor understands: a two-day festival of AI inference staged as a race meeting, 27-28 April 2027, Palace of Fine Arts, San Francisco. They come to believe the main event is real engineering (a world record attempt for inference speed on Vera Rubin), with drivers worth hearing and customers running at the limit. They act by requesting an invitation: from the cover, from the running head that follows the scroll, and from the entry form at the close.

**FIRST VIEWPORT.** The programme cover, full-bleed chrome yellow. A masthead strip across the top carries "Official Programme" and the contents links. "GOODPUT" in vermilion fat capitals spans the page, "Festival of Code" in brush script crossing its baseline at the left, every letter of the name left whole. The lower half is one litho plate: a single-seater with B300 on its roundel at speed past the Palace of Fine Arts rotunda, in green, vermilion and black overprint. Beside the title: 27 & 28 April 2027, the venue, one sentence of offer, and the primary action, "Request an invitation", as a solid black letterpress block. On load the ink plates slide into register.

**FORM.** The Official Programme: position 1 on my ordered list (my own top-ranked candidate), chosen by the user on the decision page in place of the roll's assignment. seed:d325287fd91e4f3e. Signature interaction: the forecast dial. The visitor pencils a tokens-per-second forecast into the record table and a chronometric needle ticks round to it; past the scale it reads "off the clock". Motion grammar: plates sliding into register, chronometric ticking, wheels turning.

**FINISH.** unreviewed and undocumented is unfinished; this build ends with the finish review, the verdict, DESIGN.md, and every shipping raster carrying its provenance

## Memorable moment

The record page: a racing-green plate with one enormous period dial reading tokens per second, and a results table whose record line is still blank.

## Unresolved

- Invitation URL (placeholder constant).
- Agenda times, talk subjects, speaker titles beyond what the user gave.
- Whether real logos or photographs will replace the set names and drawn portraits.
