/* Shared by all three treatments.
   1. ?still parks every animation at its end state (for captures and print).
   2. The Treatment menu in the header closes on Escape, on a click outside it,
      and when focus leaves it. Without this file it still opens and closes. */
(() => {
  'use strict';

  if (new URLSearchParams(window.location.search).has('still')) {
    document.documentElement.classList.add('still');
  }

  const start = () => {
    document.querySelectorAll('details[data-treatments]').forEach((menu) => {
      const summary = menu.querySelector('summary');

      document.addEventListener('click', (event) => {
        if (menu.open && !menu.contains(event.target)) menu.open = false;
      });

      menu.addEventListener('keydown', (event) => {
        if (event.key === 'Escape' && menu.open) {
          menu.open = false;
          if (summary) summary.focus();
        }
      });

      menu.addEventListener('focusout', (event) => {
        if (menu.open && event.relatedTarget && !menu.contains(event.relatedTarget)) menu.open = false;
      });
    });
  };

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();
