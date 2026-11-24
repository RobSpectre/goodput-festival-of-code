# Goodput Festival of Code

The landing page for the Goodput Festival of Code, 27 & 28 April 2027, Palace of Fine Arts, San Francisco. It is built as the official programme of a 1930s-50s race meeting: a litho cover, an entry list, a record page and a tear-off entry form.

Live: https://robspectre.github.io/goodput-festival-of-code/

## Layout of the repo

```
docs/                  the site, served by GitHub Pages from the main branch
  index.html           the whole programme, with its plates as inline SVG
  assets/css/          programme.css: inks, type, layout, motion
  assets/js/main.js    invitation link, fitted bill lines, the forecast dial
  assets/img/          the four driver portraits
  assets/fonts/        self-hosted faces (latin subsets)
  assets/*.ics         the save-the-date calendar file
tools/drivers.py       draws the four portraits: python3 tools/drivers.py docs/assets/img
PRODUCT.md             what the page is for and what it may claim
DESIGN.md              the design system as built
.impeccable/           design working files (never served)
```

There is no build step. Edit the files in `docs/` and push.

## Run it locally

```bash
python3 -m http.server 4173 --bind 127.0.0.1 --directory docs
```

Then open http://127.0.0.1:4173/. Add `?still` to the address to park every animation at its end state, which is useful for screenshots.

## Set the invitation link

Every "Request an invitation" button reads one constant at the top of `docs/assets/js/main.js`:

```js
const INVITE_URL = '';
```

While it is empty, the cover and running-head buttons lead to the entry form at the foot of the page, which shows an "Entries open shortly" stamp and makes "Save the date" (a calendar file) its working button. Paste the real form's URL there and every "Request an invitation" button goes straight to it, and the entry form swaps its stamp for that button.

## What is illustrative

- The racing numbers are NVIDIA cluster names and the "machines" on the entry list are a figure of speech.
- The dial is a forecasting toy with a made-up scale. The page states no record figure, because the record is an attempt.
- The driver portraits are original drawings in period dress, not likenesses.

## Credits

Typefaces, all under the SIL Open Font License: Rammetto One, Hammersmith One, Stint Ultra Condensed, Yesteryear and Old Standard TT.

The page is an homage to the old race-day programmes and takes its cue from the Goodwood Festival of Speed. It is not affiliated with Goodwood. NVIDIA and Vera Rubin are trademarks of NVIDIA Corporation; all other names belong to their owners.
