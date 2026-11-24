# Goodput Festival of Code

The landing page for the Goodput Festival of Code, 27 & 28 April 2027, Palace of Fine Arts, San Francisco. It is built as the official programme of a 1930s-50s race meeting: a litho cover, an entry list, a record page and a tear-off entry form.

Live: https://robspectre.github.io/goodput-festival-of-code/

## Three treatments

The same event is set three ways. A "Treatment" dropdown in every page's header switches between them.

| Treatment | Address | What it is |
|---|---|---|
| The Official Programme | `/` | A letterpress race-day programme, 1930s to 50s. The default. |
| The Timekeepers' Tower | `/tower/` | Painted scoreboards, slot-in number tiles and a pit board. |
| The Hand-Inked Lap Chart | `/lap-chart/` | The meeting drawn as hand-inked charts. |

Each treatment is its own page with its own stylesheet, script, typefaces and drawings. They share only the files in `docs/assets/js/` and the calendar file.

The Lap Chart page is generated, because its chart geometry is computed. Edit `tools/lap-chart/template.html` (or `build.py`) and rebuild; do not edit `docs/lap-chart/index.html` by hand:

```bash
python3 tools/lap-chart/build.py docs/lap-chart/index.html
```

## Layout of the repo

```
docs/                  the site, served by GitHub Pages from the main branch
  index.html           the Official Programme, with its plates as inline SVG
  tower/               the Timekeepers' Tower treatment (self-contained)
  lap-chart/           the Hand-Inked Lap Chart treatment (self-contained)
  assets/css/          programme.css: inks, the type ramp, layout, motion
  assets/js/config.js  the invitation URL, shared by all three treatments
  assets/js/treatments.js  the Treatment dropdown and the ?still switch, shared
  assets/js/main.js    the Programme's own behaviour: fitted lines, the forecast dial
  assets/img/          the Programme's four driver portraits
  assets/fonts/        the Programme's self-hosted faces (latin subsets)
  assets/*.ics         the save-the-date calendar file
tools/                 scripts that draw the driver portraits for each treatment
  lap-chart/           build.py and template.html, which generate docs/lap-chart/index.html
PRODUCT.md             what the page is for and what it may claim
DESIGN.md              the Official Programme's design system as built
.impeccable/           design working files (never served)
```

There is no build step. Edit the files in `docs/` and push.

Type sizes on the Programme come from one ramp, declared as `--t-*` custom properties at the top of `programme.css` and recorded in `DESIGN.md`. Use a ramp step, or a fluid range between two steps, rather than a new size. Lettering inside the drawings is sized on the SVG text itself, in the drawing's own units.

## Run it locally

```bash
python3 -m http.server 4173 --bind 127.0.0.1 --directory docs
```

Then open http://127.0.0.1:4173/. Add `?still` to the address to park every animation at its end state, which is useful for screenshots.

## Set the invitation link

Every "Request an invitation" button, on all three treatments, reads one value in `docs/assets/js/config.js`:

```js
window.GOODPUT = {
  inviteUrl: ''
};
```

While it is empty, each page's invitation buttons lead to its closing section, which says that entries open shortly and makes "Save the date" (a calendar file) its working button. Paste the real form's URL between the quotes and every "Request an invitation" button goes straight to it.

## What is illustrative

- The racing numbers are NVIDIA cluster names and the "machines" on the entry list are a figure of speech.
- The dial is a forecasting toy with a made-up scale. The page states no record figure, because the record is an attempt.
- The driver portraits are original drawings in period dress, not likenesses.

## Credits

Typefaces, all under the SIL Open Font License: Rammetto One, Hammersmith One, Stint Ultra Condensed, Yesteryear and Old Standard TT.

The page is an homage to the old race-day programmes and takes its cue from the Goodwood Festival of Speed. It is not affiliated with Goodwood. NVIDIA and Vera Rubin are trademarks of NVIDIA Corporation; all other names belong to their owners.
