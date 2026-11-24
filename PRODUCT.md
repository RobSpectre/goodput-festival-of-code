# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Stack

Static HTML/CSS/JS. No build step and no dependencies; the site lives in `docs/`, which GitHub Pages serves from the `main` branch of `RobSpectre/goodput-festival-of-code` (public). Working files (PRODUCT.md, DESIGN.md, `.impeccable/`) stay outside `docs/` so they are never served. Chosen by the user.

## Users

Both audiences, engineers first.

- **Primary: AI engineers and builders.** People who train, serve and ship models and agents. They come for the technical spectacle: the record attempt, the talks, the hardware.
- **Secondary: technical leaders and buyers.** CTOs, founders and heads of infrastructure weighing Nebius as a platform. They come for proof and for who else is in the paddock.

## Product Purpose

The landing page for the **Goodput Festival of Code**, a two-day event on 27-28 April 2027 at the Palace of Fine Arts, San Francisco. The page exists to make a visitor want to be there and to request an invitation. Success is a visitor who knows what the festival is, when and where it runs, what happens at it, and who presses "Request an invitation".

## Positioning

A software and AI-infrastructure event staged as a motor-racing festival. The name plays on "goodput" (useful throughput: the work that actually arrives) and on the Goodwood Festival of Speed, which is the event's stated visual reference. The headline act is a live world record attempt for inference speed, not a keynote.

## Operating Context

- The visitor arrives from a link, an invitation or word of mouth, usually on a laptop, often on a phone.
- The page is a single landing page; there are no other routes yet.
- The primary action is "Request an invitation". The destination URL does not exist yet: it is one constant (`INVITE_URL` in `docs/assets/js/main.js`) that the user will set to the real form. Until then the page says entries open shortly and offers a save-the-date calendar file.

## Capabilities and Constraints

Confirmed programme content, as given by the user:

- **Speakers:** Arkady Volozh, Roman Chernin, Yann LeCun, and Teknium of Nous Research. Each gets an illustrated avatar in a vintage racing suit.
- **Nebius Token Factory:** a world record attempt for inference speed on NVIDIA Vera Rubin.
- **New frontiers of performance** with Nebius AI Cloud customers Cursor, Higgsfield and Cognition.

Terminology the page uses on purpose: goodput, tokens per second, NVIDIA cluster and platform names (B300, Vera Rubin) used as racing numbers and machine names.

Undecided, and not to be invented:

- The registration URL.
- Session titles, talk abstracts, a timed agenda, ticket prices and capacity.
- Speaker job titles beyond what the user stated ("Teknium from Nous Research").
- Any record figure, target speed or benchmark number. The record is an *attempt*.

## Brand Commitments

- Event name: **Goodput Festival of Code**.
- A thorough vintage motor-racing aesthetic, pushed hard, drawing on the visual vocabulary of the Goodwood Festival of Speed. Binding, in the user's words: "commit to a thorough vintage racing aesthetic peppered with language and NVIDIA cluster names throughout like B300 for a racing number or tokens per second on the speedometer."
- Inspiration only: no Goodwood marks, logos or assets are reproduced.

## Evidence on Hand

- The facts above, from the user's brief.
- No photography, no official logo files for Nebius, NVIDIA or the customers, and no speaker portraits. Company names are set in type; avatars are original illustrations and are not likenesses from reference photos.
- No testimonials, attendance numbers or past-event material exist. None may be fabricated.

## Product Principles

1. **The record attempt is the main event.** Everything else on the card supports it.
2. **The racing world carries real meaning.** A racing number is a cluster name; a speedometer reads tokens per second. Period dress never replaces a fact.
3. **Claims stay true.** An attempt is an attempt. Illustrative figures are labelled as such.
4. **One action.** Every route through the page ends at "Request an invitation".
5. **Engineers first.** The page respects the reader's fluency in the subject and never explains it down.
