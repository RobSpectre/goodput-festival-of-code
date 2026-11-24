/* Goodput Festival of Code: programme behaviour.
   No dependencies. Everything on the page reads without this file. */
(() => {
  'use strict';

  /* The one thing to change when the invitation form exists: paste its URL
     here. Every "Request an invitation" button will then lead to it, and the
     entry form swaps its "Entries open shortly" stamp for the button. While
     it is empty, the buttons lead to the entry form at the foot of the page,
     which says that entries open shortly and offers the calendar file. */
  const INVITE_URL = '';

  /* ?still parks every animation at its end state, for captures and print. */
  const still = new URLSearchParams(window.location.search).has('still');
  if (still) document.documentElement.classList.add('still');
  const motionQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
  const reduceMotion = { get matches() { return still || motionQuery.matches; } };

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

  /* ---------- bill lines: each line is set to fill its measure ---------- */

  const fitted = Array.from(document.querySelectorAll('[data-fit]'));

  const fit = () => {
    for (const line of fitted) {
      const inner = line.firstElementChild;
      if (!inner) continue;
      const max = parseFloat(line.dataset.fitMax) || Infinity;
      line.style.fontSize = '';
      if (window.getComputedStyle(line).whiteSpace !== 'nowrap') continue; // wraps on narrow sheets
      inner.style.display = 'inline-block';
      line.style.fontSize = '100px';
      const natural = inner.getBoundingClientRect().width;
      const measure = line.clientWidth;
      if (natural > 0 && measure > 0) {
        line.style.fontSize = Math.min(max, (100 * (measure - 2)) / natural).toFixed(2) + 'px';
      }
    }
  };

  if (fitted.length) {
    document.documentElement.classList.add('fits');
    let queued = 0;
    const refit = () => {
      cancelAnimationFrame(queued);
      queued = requestAnimationFrame(fit);
    };
    fit();
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(fit);
    window.addEventListener('resize', refit);
    window.addEventListener('load', fit);
  }

  /* ---------- the forecast dial ---------- */

  const dial = document.querySelector('.dial');
  const form = document.getElementById('forecast');
  if (!dial || !form) return;

  const input = document.getElementById('forecast-input');
  const out = document.getElementById('forecast-out');
  const digits = Array.from(dial.querySelectorAll('.dial__digit'));
  const STORE = 'goodput.forecast';
  const SCALE_MAX = 12000;      // the dial reads to twelve thousand t.p.s.
  const ODOMETER_MAX = 9999999; // seven drums
  const A_MIN = -135;
  const A_MAX = 135;

  let angle = A_MIN;
  let ticker = 0;

  const number = new Intl.NumberFormat('en-GB');

  const setAngle = (value) => {
    angle = value;
    dial.style.setProperty('--needle', value.toFixed(2) + 'deg');
  };

  /* A chronometric instrument does not sweep: it steps. */
  const tickTo = (target, done) => {
    window.clearInterval(ticker);
    if (reduceMotion.matches) {
      setAngle(target);
      if (done) done();
      return;
    }
    const from = angle;
    const steps = Math.max(5, Math.round(Math.abs(target - from) / 10));
    let step = 0;
    ticker = window.setInterval(() => {
      step += 1;
      const t = step / steps;
      const eased = 1 - Math.pow(1 - t, 3);
      const shake = step < steps ? (Math.random() - 0.5) * 1.6 : 0;
      setAngle(from + (target - from) * eased + shake);
      if (step >= steps) {
        window.clearInterval(ticker);
        if (done) done();
      }
    }, 95);
  };

  const setDigits = (value) => {
    const text = String(Math.min(value, ODOMETER_MAX)).padStart(digits.length, '0');
    digits.forEach((digit, index) => { digit.textContent = text[index]; });
  };

  const say = (message, state) => {
    out.textContent = message;
    if (state) out.dataset.state = state; else delete out.dataset.state;
  };

  const rub = document.createElement('button');
  rub.type = 'button';
  rub.className = 'forecast__rub';
  rub.textContent = 'Rub it out';
  rub.hidden = true;
  out.after(rub);

  const show = (value) => {
    const off = value > SCALE_MAX;
    setDigits(value);
    if (off) dial.setAttribute('data-off', ''); else dial.removeAttribute('data-off');
    tickTo(off ? A_MAX + 5 : A_MIN + (value / SCALE_MAX) * (A_MAX - A_MIN));
    say(
      off
        ? `Pencilled in: ${number.format(value)} t.p.s. That is off the clock. The dial stops at twelve thousand; your nerve evidently does not.`
        : `Pencilled in: ${number.format(value)} t.p.s. We shall see on the day.`
    );
    rub.hidden = false;
  };

  const read = () => {
    try {
      const saved = parseInt(window.localStorage.getItem(STORE), 10);
      return Number.isFinite(saved) && saved > 0 ? saved : null;
    } catch (error) {
      return null;
    }
  };

  const write = (value) => {
    try {
      if (value === null) window.localStorage.removeItem(STORE);
      else window.localStorage.setItem(STORE, String(value));
    } catch (error) {
      /* a private window: the forecast simply lasts until the page closes */
    }
  };

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const raw = input.value.replace(/[\s,._]/g, '');
    if (!/^\d+$/.test(raw)) {
      input.setAttribute('aria-invalid', 'true');
      say('Figures only, please: a whole number of tokens per second, such as 4200.', 'error');
      input.focus();
      return;
    }
    const value = parseInt(raw, 10);
    if (value < 1) {
      input.setAttribute('aria-invalid', 'true');
      say('A forecast of nought will not trouble the timekeepers. Try a figure above zero.', 'error');
      input.focus();
      return;
    }
    if (value > ODOMETER_MAX) {
      input.setAttribute('aria-invalid', 'true');
      say('The odometer has seven drums. Keep the forecast under ten million t.p.s.', 'error');
      input.focus();
      return;
    }
    input.removeAttribute('aria-invalid');
    input.value = number.format(value);
    write(value);
    show(value);
  });

  input.addEventListener('input', () => {
    if (input.hasAttribute('aria-invalid')) {
      input.removeAttribute('aria-invalid');
      say('');
    }
  });

  rub.addEventListener('click', () => {
    write(null);
    input.value = '';
    dial.removeAttribute('data-off');
    setDigits(0);
    tickTo(A_MIN);
    say('Rubbed out. The line is blank again.');
    input.focus();
  });

  /* When the dial first comes into view it checks itself, as an instrument
     does at switch-on: up the scale and back. A saved forecast is shown instead. */
  const wake = () => {
    const saved = read();
    if (saved) {
      input.value = number.format(saved);
      show(saved);
    } else if (!reduceMotion.matches) {
      tickTo(A_MAX, () => window.setTimeout(() => tickTo(A_MIN), 260));
    }
  };

  if ('IntersectionObserver' in window) {
    const watcher = new IntersectionObserver((entries) => {
      if (entries.some((entry) => entry.isIntersecting)) {
        watcher.disconnect();
        wake();
      }
    }, { threshold: 0.45 });
    watcher.observe(dial);
  } else {
    wake();
  }
})();
