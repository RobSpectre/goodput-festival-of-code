/* Goodput Festival of Code: the Timekeepers' Tower.
   No dependencies. The page reads in full without this file. All motion is CSS
   (tiles dropping onto their hooks), parked by the .still class and by
   prefers-reduced-motion; nothing is animated from script.

   Capture-only query states (used with ?still for screenshots):
     ?demo=forecast   the visitor's row hung with 4,200
     ?demo=long       the visitor's row hung with a seven-figure forecast
     ?demo=error      the slip showing its error message
     ?demo=open       the entries board as it reads once an invitation URL is set
     ?demo=menu       the Treatment menu open
     ?demo=focus      keyboard focus on the hero pit board (on phones, the one held along the foot)
     ?demo=focus-fascia  keyboard focus on the pit board in the running head
   None of them stores anything. */
(() => {
  'use strict';

  const INVITE_URL = (window.GOODPUT && window.GOODPUT.inviteUrl) || '';
  const params = new URLSearchParams(window.location.search);
  const demo = params.get('demo');

  /* ---------- invitation ---------- */

  const showOpen = (url) => {
    document.querySelectorAll('[data-invite]').forEach((link) => { link.href = url; });
    const closed = document.getElementById('entry-closed');
    const open = document.getElementById('entry-open');
    if (closed && open) {
      closed.hidden = true;
      open.hidden = false;
      const title = open.querySelector('h2');
      if (title) {
        closed.querySelector('h2').removeAttribute('id');
        title.id = 'entries-title';
      }
    }
  };

  if (INVITE_URL) showOpen(INVITE_URL);
  else if (demo === 'open') showOpen('#entries');

  if (demo === 'menu') {
    const menu = document.querySelector('details[data-treatments]');
    if (menu) menu.open = true;
  }

  if (demo === 'focus' || demo === 'focus-fascia') {
    const shown = (board) => board && board.getClientRects().length > 0;
    const hero = document.querySelector('.pit--hero');
    const follow = document.querySelector('.pit--follow');
    const target = demo === 'focus' && shown(hero) ? hero : follow;
    if (shown(target)) target.focus({ preventScroll: true, focusVisible: true });
  }

  /* ---------- hang your forecast ---------- */

  const form = document.getElementById('forecast');
  const row = document.getElementById('forecast-tiles');
  if (!form || !row) return;

  const input = document.getElementById('forecast-input');
  const out = document.getElementById('forecast-out');
  const posted = document.getElementById('forecast-posted');
  const down = document.getElementById('forecast-down');
  const STORE = 'goodput.forecast';   // shared with the other treatments
  const PLACES = 7;                    // the board has seven hooks
  const LIMIT = 9999999;
  const number = new Intl.NumberFormat('en-GB');

  const say = (message, state) => {
    out.textContent = message;
    if (state) out.dataset.state = state; else delete out.dataset.state;
  };

  const emptyRow = () => {
    row.textContent = '';
    for (let i = 0; i < PLACES; i += 1) {
      const slot = document.createElement('span');
      slot.className = 'slot';
      row.appendChild(slot);
    }
  };

  /* Tiles are hung right to left on the last hooks, as a scorer fills a board:
     unused hooks on the left stay bare. */
  const hang = (value) => {
    const digits = String(value).split('');
    row.textContent = '';
    const bare = PLACES - digits.length;
    for (let i = 0; i < PLACES; i += 1) {
      const place = document.createElement('span');
      if (i < bare) {
        place.className = 'slot';
      } else {
        place.className = 'tile tile--l';
        place.textContent = digits[i - bare];
        place.style.setProperty('--i', String(i - bare));
      }
      row.appendChild(place);
    }
    posted.textContent = `Your forecast: ${number.format(value)} t.p.s.`;
    say(`Hung on the board: ${number.format(value)} tokens per second. We shall see on the day.`);
    down.hidden = false;
  };

  const read = () => {
    try {
      const saved = parseInt(window.localStorage.getItem(STORE), 10);
      return Number.isFinite(saved) && saved > 0 && saved <= LIMIT ? saved : null;
    } catch (error) {
      return null;
    }
  };

  const write = (value) => {
    try {
      if (value === null) window.localStorage.removeItem(STORE);
      else window.localStorage.setItem(STORE, String(value));
    } catch (error) {
      /* a private window: the forecast lasts until the page closes */
    }
  };

  const refuse = (message) => {
    input.setAttribute('aria-invalid', 'true');
    say(message, 'error');
    input.focus();
  };

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const raw = input.value.replace(/[\s,._]/g, '');
    if (!/^\d+$/.test(raw)) return refuse('Figures only, please: a whole number of tokens per second.');
    const value = parseInt(raw, 10);
    if (value < 1) return refuse('A forecast of nought will not trouble the scorer. Try a figure above zero.');
    if (value > LIMIT) return refuse('The board has seven hooks. Keep the forecast under ten million t.p.s.');
    input.removeAttribute('aria-invalid');
    input.value = number.format(value);
    write(value);
    hang(value);
    return undefined;
  });

  input.addEventListener('input', () => {
    if (input.hasAttribute('aria-invalid')) {
      input.removeAttribute('aria-invalid');
      say('');
    }
  });

  down.addEventListener('click', () => {
    write(null);
    emptyRow();
    input.value = '';
    posted.textContent = 'Nothing hung yet';
    say('Taken down. The hooks are bare again.');
    down.hidden = true;
    input.focus();
  });

  /* capture-only states, then any forecast saved on an earlier visit */
  if (demo === 'forecast') {
    input.value = number.format(4200);
    hang(4200);
  } else if (demo === 'long') {
    input.value = number.format(1250000);
    hang(1250000);
  } else if (demo === 'error') {
    input.value = 'fast';
    input.setAttribute('aria-invalid', 'true');
    say('Figures only, please: a whole number of tokens per second.', 'error');
  } else {
    const saved = read();
    if (saved) {
      input.value = number.format(saved);
      hang(saved);
    }
  }
})();
