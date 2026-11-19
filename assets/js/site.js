/* CASAVISION — site behaviour. No libraries: easy to port into Tilda Zero Block / T123. */
(function () {
  var doc = document.documentElement;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if ('IntersectionObserver' in window) doc.classList.add('js');

  function $(s, c) { return (c || document).querySelector(s); }
  function $$(s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); }
  function clamp(v, a, b) { return Math.max(a, Math.min(b, v)); }
  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }

  /* ---------- page curtain ---------- */
  var curtain = $('.curtain');
  function lift() { if (curtain) requestAnimationFrame(function () { curtain.classList.add('is-up'); }); }
  if (document.readyState === 'complete') lift(); else window.addEventListener('load', lift);
  setTimeout(lift, 1800); // never keep the page covered
  window.addEventListener('pageshow', function (e) { if (e.persisted && curtain) { curtain.classList.remove('is-cover', 'is-in'); curtain.classList.add('is-up'); } });
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[data-go]');
    if (!a || !curtain || reduce || e.metaKey || e.ctrlKey || e.shiftKey) return;
    var href = a.getAttribute('href');
    if (!href) return;
    e.preventDefault();
    curtain.classList.remove('is-up'); curtain.classList.add('is-in');
    void curtain.offsetWidth;
    curtain.classList.remove('is-in'); curtain.classList.add('is-cover');
    setTimeout(function () { window.location.href = href; }, 900);
  });

  /* ---------- fit giant words to their box ---------- */
  function fit() {
    $$('[data-fit]').forEach(function (el) {
      var box = el.parentElement.getBoundingClientRect().width * (parseFloat(el.getAttribute('data-fit')) || 1);
      el.style.fontSize = '100px';
      var rg = document.createRange(); rg.selectNodeContents(el);
      var w = rg.getBoundingClientRect().width;
      if (w) el.style.fontSize = (100 * box / w).toFixed(2) + 'px';
    });
  }
  fit();
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(fit);
  window.addEventListener('resize', fit);

  /* ---------- reveal ---------- */
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (ents) {
      ents.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
    $$('[data-r]').forEach(function (el) { io.observe(el); });
  }

  /* ---------- header: tone + hide on scroll down ---------- */
  var hdr = $('.hdr');
  var lastY = window.scrollY;
  function headerTone() {
    if (!hdr) return;
    var y = hdr.getBoundingClientRect().height / 2;
    var light = false;
    $$('[data-tone]').some(function (s) {
      var r = s.getBoundingClientRect();
      if (r.top <= y && r.bottom > y) { light = s.getAttribute('data-tone') === 'light'; return true; }
      return false;
    });
    hdr.classList.toggle('is-light', light);
    var sy = window.scrollY;
    hdr.classList.toggle('is-scrolled', sy > 40);
    if (!document.body.classList.contains('is-locked')) hdr.classList.toggle('is-hidden', sy > lastY && sy > 400);
    lastY = sy;
  }

  /* ---------- menu ---------- */
  var menu = $('#menu');
  var opener = null;
  function openMenu() {
    if (!menu) return;
    opener = document.activeElement;
    menu.classList.add('is-open'); menu.setAttribute('aria-hidden', 'false');
    document.body.classList.add('is-locked');
    $$('[data-menu-open]').forEach(function (b) { b.setAttribute('aria-expanded', 'true'); });
    setTimeout(function () { var f = $('.mn-link', menu); if (f) f.focus({ preventScroll: true }); }, 400);
  }
  function closeMenu() {
    if (!menu) return;
    menu.classList.remove('is-open'); menu.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('is-locked');
    $$('[data-menu-open]').forEach(function (b) { b.setAttribute('aria-expanded', 'false'); });
    if (opener && opener.focus) opener.focus({ preventScroll: true });
  }
  $$('[data-menu-open]').forEach(function (b) { b.addEventListener('click', openMenu); });
  $$('[data-menu-close]').forEach(function (b) { b.addEventListener('click', closeMenu); });
  if (menu) {
    $$('a', menu).forEach(function (a) { a.addEventListener('click', function () { if (!a.hasAttribute('data-go')) closeMenu(); }); });
    var nav = $('.menu-nav', menu);
    var imgs = $$('.menu-preview img', menu);
    var cap = $('.menu-preview figcaption', menu);
    $$('.mn-item', menu).forEach(function (it, i) {
      function on() {
        nav.classList.add('mn-nav-dim');
        $$('.mn-item', menu).forEach(function (o) { o.classList.toggle('is-hover', o === it); });
        imgs.forEach(function (im, j) { im.classList.toggle('is-on', j === i); });
        if (cap) cap.textContent = it.getAttribute('data-cap') || '';
      }
      it.addEventListener('mouseenter', on);
      it.addEventListener('focusin', on);
    });
    nav && nav.addEventListener('mouseleave', function () { nav.classList.remove('mn-nav-dim'); });
  }
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && menu && menu.classList.contains('is-open')) closeMenu(); });

  /* ---------- services accordion ---------- */
  $$('.svc-row').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var svc = btn.closest('.svc');
      var open = !svc.classList.contains('is-open');
      svc.classList.toggle('is-open', open);
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  });

  /* ---------- service preselect for the form ---------- */
  function pick(val) {
    var r = $$('input[name="service"]').filter(function (i) { return i.value === val; })[0];
    if (r) r.checked = true;
  }
  $$('[data-service]').forEach(function (a) {
    a.addEventListener('click', function () { store('cv-service', a.getAttribute('data-service')); pick(a.getAttribute('data-service')); });
  });
  var saved = store('cv-service');
  if (saved) pick(saved);

  var form = $('#brief');
  if (form) form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!form.reportValidity || form.reportValidity()) { form.classList.add('is-sent'); store('cv-service', ''); }
  });

  /* ---------- hero video: play only when visible ---------- */
  var vid = $('.hero video');
  if (vid) {
    if (reduce) { vid.removeAttribute('autoplay'); vid.pause(); }
    else if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (en) { en.forEach(function (x) { if (x.isIntersecting) { var p = vid.play(); if (p && p.catch) p.catch(function () {}); } else vid.pause(); }); }).observe(vid);
    }
  }

  /* ---------- scroll-linked effects ---------- */
  var par = $$('[data-par]');
  var marks = $$('[data-focus]');
  var words = $('.p-words');
  var wordEls = words ? $$('.pw-word', words) : [];
  var wordCount = words ? $('.pw-count', words) : null;
  var mood = $('.p-mood');
  var moodItems = mood ? $$('.pm-item, .pm-word', mood) : [];
  if (mood) moodItems.forEach(function (el, i) {
    // where each piece flies in from
    var a = (i * 137.5) * Math.PI / 180;
    el._fx = Math.cos(a) * (60 + (i % 3) * 30);
    el._fy = Math.sin(a) * (50 + (i % 4) * 20) + 40;
    el._fr = ((i % 2 ? 1 : -1) * (6 + (i % 5) * 3));
    el._t0 = (i / Math.max(1, moodItems.length)) * 0.55;
  });

  var ticking = false;
  function frame() {
    ticking = false;
    var vh = window.innerHeight;
    headerTone();
    if (!reduce) {
      par.forEach(function (el) {
        var r = el.getBoundingClientRect();
        if (r.bottom < -200 || r.top > vh + 200) return;
        var k = parseFloat(el.getAttribute('data-par')) || 0.1;
        var c = (r.top + r.height / 2 - vh / 2);
        el.style.transform = 'translate3d(0,' + (-c * k).toFixed(1) + 'px,0)';
      });
      marks.forEach(function (el) {
        // the wordmark comes into focus as its block reaches the middle of the screen
        var host = el.parentElement.getBoundingClientRect();
        var max = parseFloat(el.getAttribute('data-focus')) || 22;
        var end = parseFloat(el.getAttribute('data-focus-min') || 0);
        var p = clamp((vh - host.top) / (vh * 0.9), 0, 1);
        el.style.setProperty('--blur', (max - (max - end) * p).toFixed(1) + 'px');
      });
    }
    if (words && wordEls.length && !reduce) {
      var r = words.getBoundingClientRect();
      var p = clamp(-r.top / (r.height - vh), 0, 0.999);
      var idx = Math.floor(p * wordEls.length);
      wordEls.forEach(function (w, i) { w.classList.toggle('is-on', i === idx); w.classList.toggle('is-past', i < idx); });
      if (wordCount) wordCount.textContent = (idx + 1) + ' / ' + wordEls.length;
    }
    if (mood && !reduce) {
      var mr = mood.getBoundingClientRect();
      var mp = clamp((-mr.top + vh * 0.35) / (mr.height - vh * 0.65), 0, 1);
      moodItems.forEach(function (el) {
        var t = clamp((mp - el._t0) / 0.4, 0, 1);
        var e = 1 - Math.pow(1 - t, 3);
        var k = 1 - e;
        el.style.opacity = (0.08 + e * 0.92).toFixed(3);
        el.style.transform = 'translate3d(' + (el._fx * k).toFixed(1) + 'vw,' + (el._fy * k).toFixed(1) + 'vh,0) rotate(' + (el._fr * k).toFixed(2) + 'deg) scale(' + (0.86 + 0.14 * e).toFixed(3) + ')';
      });
    }
  }
  function onScroll() { if (!ticking) { ticking = true; requestAnimationFrame(frame); } }
  window.addEventListener('scroll', onScroll, { passive: true });
  window.addEventListener('resize', onScroll);
  frame();

  /* ---------- year ---------- */
  $$('[data-year]').forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
