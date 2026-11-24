/* Goodput Festival of Code: the Hand-Inked Lap Chart.
   No dependencies. The page reads in full without this file; it inks the forecast. */
(() => {
  'use strict';

  /* The invitation URL is set once, in ../assets/js/config.js, for all three treatments. */
  const params = new URLSearchParams(window.location.search);
  const demo = params.get('demo');   // capture-only states, see the foot of this file
  const INVITE_URL = (window.GOODPUT && window.GOODPUT.inviteUrl) || (demo === 'invite' ? '#invitation' : '');

  const root = document.documentElement;
  const motionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
  const quiet = () => root.classList.contains('still') || motionQuery.matches;

  /* ---------- invitation ---------- */

  if (INVITE_URL) {
    document.querySelectorAll('[data-invite]').forEach((link) => { link.href = INVITE_URL; });
    const closed = document.getElementById('entry-closed');
    const open = document.getElementById('entry-open');
    if (closed && open) {
      closed.hidden = true;
      open.hidden = false;
    }
  }

  /* capture-only: ?demo=menu shows the Treatment menu open */
  if (demo === 'menu') {
    const menu = document.querySelector('details[data-treatments]');
    if (menu) menu.open = true;
  }

  /* ---------- the forecast: one line, coiled or laid straight ---------- */

  const form = document.getElementById('forecast');
  const coil = document.getElementById('fc-coil');
  const rows = Array.from(document.querySelectorAll('.fc-row'));
  if (!form || !coil || !rows.length) return;

  const input = document.getElementById('fc-input');
  const out = document.getElementById('fc-out');
  const read = document.getElementById('fc-read');
  const tools = document.getElementById('fc-tools');
  const toggle = document.getElementById('fc-toggle');
  const rub = document.getElementById('fc-rub');
  const off = document.getElementById('fc-off');

  const STORE = 'goodput.forecast';   // shared with the other treatments, so a forecast follows you
  const ROW = 460;                    // drawing units in one row of the sheet
  const PER_ROW = 1000;               // tokens per second in one row
  const SHEET = ROW * rows.length;    // the whole sheet: twelve rows
  const X0 = 40;
  const X1 = X0 + ROW;
  const LIMIT = 9999999;

  const number = new Intl.NumberFormat('en-GB');
  const words = ['no', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve'];

  let value = 0;        // the forecast, in tokens per second
  let length = 0;       // the same thing as a length of line, capped at the sheet
  let straight = 0;     // how much of that line is laid straight; the rest is coiled
  let frame = 0;

  /* The one drawing rule: the ink on the coil plus the ink on the rows is always `inked`. */
  const draw = (inked, laid) => {
    coil.style.strokeDasharray = `${Math.max(inked - laid, 0)} ${SHEET * 2}`;
    rows.forEach((row, i) => {
      const part = Math.min(Math.max(laid - i * ROW, 0), ROW);
      const from = i % 2 === 0 ? X0 : X1;
      row.setAttribute('x2', i % 2 === 0 ? from + part : from - part);
    });
  };

  const run = (from, to, ms, step, done) => {
    cancelAnimationFrame(frame);
    if (quiet() || ms <= 0) {
      step(to);
      if (done) done();
      return;
    }
    const t0 = performance.now();
    const tick = (now) => {
      const t = Math.min((now - t0) / ms, 1);
      const eased = t < .5 ? 2 * t * t : 1 - Math.pow(-2 * t + 2, 2) / 2;
      step(from + (to - from) * eased);
      if (t < 1) frame = requestAnimationFrame(tick);
      else if (done) done();
    };
    frame = requestAnimationFrame(tick);
  };

  const say = (message, state) => {
    out.textContent = message;
    if (state) out.dataset.state = state; else delete out.dataset.state;
  };

  const rowsText = () => {
    if (value > PER_ROW * rows.length) return 'all twelve rows, and runs off the sheet';
    const whole = Math.floor(value / PER_ROW);
    const rest = value - whole * PER_ROW;
    if (!whole) return 'part of the first row';
    const base = `${words[whole]} ${whole === 1 ? 'row' : 'rows'}`;
    return rest ? `${base} and part of the next` : `${base} exactly`;
  };

  const describe = () => {
    const figure = `${number.format(value)} tokens per second`;
    const over = value > PER_ROW * rows.length;
    if (straight > 0) {
      read.textContent = `Your line, laid straight: ${figure} fills ${rowsText()}.` + (over ? ' The sheet stops at 12,000; your nerve evidently does not.' : '');
      say(`Laid straight: ${rowsText()}. Same ink, same length.`);
      toggle.textContent = 'Coil it again';
    } else {
      read.textContent = `Your line, coiled: ${figure}.` + (over ? ' It is longer than the sheet, so only the first twelve thousand are drawn.' : '');
      say(`Inked: ${figure}, coiled. Unroll it to read it off the rows.`);
      toggle.textContent = 'Unroll it';
    }
    off.setAttribute('visibility', over && straight > 0 ? 'visible' : 'hidden');
    tools.hidden = false;
  };

  const duration = () => 700 + Math.min(length / 4, 1300);

  const ink = (next, animate) => {
    value = next;
    length = Math.min(value * (ROW / PER_ROW), SHEET);
    straight = 0;
    off.setAttribute('visibility', 'hidden');
    run(0, length, animate ? duration() : 0, (now) => draw(now, 0), describe);
  };

  const lay = (target, animate) => {
    const from = straight;
    straight = target;
    off.setAttribute('visibility', 'hidden');
    run(from, target, animate ? duration() : 0, (now) => draw(length, now), describe);
  };

  const fail = (message) => {
    input.setAttribute('aria-invalid', 'true');
    say(message, 'error');
    input.focus();
  };

  const store = (next) => {
    try {
      if (next === null) window.localStorage.removeItem(STORE);
      else window.localStorage.setItem(STORE, String(next));
    } catch (error) {
      /* a private window: the forecast lasts until the page closes */
    }
  };

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const raw = input.value.replace(/[\s,._]/g, '');
    if (!/^\d+$/.test(raw)) return fail('Figures only, please: a whole number of tokens per second.');
    const next = parseInt(raw, 10);
    if (next < 1) return fail('A forecast of nought leaves the sheet as it is. Try a figure above zero.');
    if (next > LIMIT) return fail('That is more ink than we keep. Stay under ten million tokens per second.');
    input.removeAttribute('aria-invalid');
    input.value = number.format(next);
    store(next);
    ink(next, true);
  });

  input.addEventListener('input', () => {
    if (input.hasAttribute('aria-invalid')) {
      input.removeAttribute('aria-invalid');
      say('');
    }
  });

  toggle.addEventListener('click', () => lay(straight > 0 ? 0 : length, true));

  rub.addEventListener('click', () => {
    cancelAnimationFrame(frame);
    store(null);
    value = 0; length = 0; straight = 0;
    draw(0, 0);
    off.setAttribute('visibility', 'hidden');
    tools.hidden = true;
    toggle.textContent = 'Unroll it';
    input.value = '';
    read.textContent = 'Both are empty until you ink them.';
    say('Rubbed out. The sheet is empty again.');
    input.focus();
  });

  /* A saved forecast is shown as it was left: coiled. */
  let saved = null;
  try {
    const kept = parseInt(window.localStorage.getItem(STORE), 10);
    if (Number.isFinite(kept) && kept > 0 && kept <= LIMIT) saved = kept;
  } catch (error) {
    saved = null;
  }

  /* Capture-only states, reached with ?demo=…, never stored:
     coiled    a forecast of 4,200, coiled
     unrolled  the same, laid straight
     off       250,000: all twelve rows and off the sheet
     error     the form after a forecast that is not a number
     invite    the page as it reads once an invitation URL is set
     menu      the Treatment menu, open */
  if (demo === 'coiled' || demo === 'unrolled' || demo === 'off') {
    const figure = demo === 'off' ? 250000 : 4200;
    input.value = number.format(figure);
    ink(figure, false);
    if (demo !== 'coiled') lay(length, false);
  } else if (demo === 'error') {
    input.value = 'fast';
    input.setAttribute('aria-invalid', 'true');
    say('Figures only, please: a whole number of tokens per second.', 'error');
  } else if (saved) {
    input.value = number.format(saved);
    ink(saved, false);
  }
})();
