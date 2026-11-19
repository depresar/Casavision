/* CASAVISION — site behaviour. No libraries: easy to port into Tilda Zero Block / T123. */
(function () {
  var doc = document.documentElement;
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if ('IntersectionObserver' in window) doc.classList.add('js');

  function $(s, c) { return (c || document).querySelector(s); }
  function $$(s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); }
  function clamp(v, a, b) { return Math.max(a, Math.min(b, v)); }
  function store(k, v) { try { if (v === undefined) return localStorage.getItem(k); localStorage.setItem(k, v); } catch (e) { return null; } }

  /* ---------- preloader (full once per session, a quick wipe after that) ---------- */
  var pre = $('.preloader');
  var ready = false;
  var onReady = [];
  function whenReady(fn) { if (ready) fn(); else onReady.push(fn); }
  function finish() {
    if (ready) return; ready = true;
    doc.classList.add('ready');
    if (pre) { pre.classList.add('is-done'); setTimeout(function () { pre.hidden = true; }, 1300); }
    onReady.forEach(function (fn) { fn(); });
  }
  if (pre) {
    var seen = false;
    try { seen = sessionStorage.getItem('cv-pl') === '1'; sessionStorage.setItem('cv-pl', '1'); } catch (e) {}
    if (seen || reduce) {
      pre.classList.add('is-quick');
      var quick = function () { requestAnimationFrame(function () { setTimeout(finish, 120); }); };
      if (document.readyState !== 'loading') quick(); else document.addEventListener('DOMContentLoaded', quick);
    } else {
      var bar = $('.pl-bar', pre), num = $('.pl-num', pre);
      var t0 = performance.now(), MIN = 1500, MAX = 3200, shown = 0, loaded = document.readyState === 'complete';
      window.addEventListener('load', function () { loaded = true; });
      var tick = function (now) {
        var el = now - t0;
        var target = loaded ? 1 : Math.min(0.9, el / 1800);
        if (el > MAX) target = 1;
        shown += (target - shown) * 0.12;
        if (target === 1 && shown > 0.995) shown = 1;
        bar.style.setProperty('--p', shown.toFixed(3));
        num.textContent = Math.round(shown * 100);
        if (shown >= 1 && el >= MIN) { setTimeout(finish, 180); return; }
        requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    }
  } else finish();
  setTimeout(finish, 4000); // never keep the page covered

  /* ---------- page curtain on internal navigation ---------- */
  var curtain = $('.curtain');
  window.addEventListener('pageshow', function (e) { if (e.persisted && curtain) curtain.classList.remove('is-cover'); });
  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[data-go]');
    if (!a || !curtain || reduce || e.metaKey || e.ctrlKey || e.shiftKey) return;
    var href = a.getAttribute('href');
    if (!href || href.charAt(0) === '#') return;
    e.preventDefault();
    curtain.classList.add('is-cover');
    setTimeout(function () { window.location.href = href; }, 850);
  });

  /* ---------- fit giant words to their box ---------- */
  function fit() {
    $$('[data-fit]').forEach(function (el) {
      var box = el.parentElement.getBoundingClientRect().width * (parseFloat(el.getAttribute('data-fit')) || 1);
      el.style.fontSize = '100px';
      var rg = document.createRange(); rg.selectNodeContents(el);
      var w = rg.getBoundingClientRect().width;
      var fs = w ? 100 * box / w : 100;
      var capH = parseFloat(el.getAttribute('data-fit-h'));
      if (capH) fs = Math.min(fs, window.innerHeight * capH);
      el.style.fontSize = fs.toFixed(2) + 'px';
      if (el._sync) el._sync();
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
    $$('[data-r]').forEach(function (el) {
      if (el.closest('.hero')) whenReady(function () { setTimeout(function () { io.observe(el); }, 250); });
      else io.observe(el);
    });
  }

  /* ---------- haze text: split into words ---------- */
  var hazes = $$('[data-haze]');
  hazes.forEach(function (el) {
    (function walk(node) {
      Array.prototype.slice.call(node.childNodes).forEach(function (n) {
        if (n.nodeType === 3) {
          var frag = document.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach(function (w) {
            if (!w) return;
            if (/^\s+$/.test(w)) { frag.appendChild(document.createTextNode(w)); return; }
            var sp = document.createElement('span'); sp.className = 'hz'; sp.textContent = w; frag.appendChild(sp);
          });
          node.replaceChild(frag, n);
        } else if (n.nodeType === 1) walk(n);
      });
    })(el);
    el._w = $$('.hz', el);
  });

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

  /* ---------- hero name's shadow follows the scroll through About ---------- */
  var shadow = $('[data-shadow]');
  var mast = $('.masthead .mh-word');
  if (shadow && mast) {
    shadow._sync = function () { shadow.style.fontSize = mast.style.fontSize; };
    mast._sync = shadow._sync;
    shadow._sync();
  }

  /* ---------- approach: a square hops from step to step ---------- */
  var steps = $('.steps');
  if (steps && !reduce && 'IntersectionObserver' in window) {
    var items = $$('.step', steps);
    var cube = document.createElement('span'); cube.className = 'step-cube'; cube.setAttribute('aria-hidden', 'true');
    steps.appendChild(cube);
    var cur = -1, timer = null, running = false;
    var pos = function (i) { var a = steps.getBoundingClientRect(), b = items[i].getBoundingClientRect(); return [b.left - a.left, b.top - a.top - 6]; };
    var place = function (i) { var q = pos(i); cube.style.transform = 'translate(' + q[0] + 'px,' + q[1] + 'px)'; };
    var hop = function () {
      var next = (cur + 1) % items.length;
      if (next === 0) {
        items.forEach(function (it) { it.classList.remove('is-on', 'is-now'); });
        cube.style.opacity = '0';
        setTimeout(function () { place(0); cube.style.opacity = '1'; cur = 0; items[0].classList.add('is-on', 'is-now'); timer = setTimeout(hop, 1500); }, 500);
        return;
      }
      var a = pos(cur), b = pos(next);
      var lift = Math.max(40, Math.abs(b[0] - a[0]) * 0.35);
      var anim = cube.animate([
        { transform: 'translate(' + a[0] + 'px,' + a[1] + 'px) rotate(0deg)' },
        { transform: 'translate(' + ((a[0] + b[0]) / 2) + 'px,' + (Math.min(a[1], b[1]) - lift) + 'px) rotate(90deg)', offset: .5 },
        { transform: 'translate(' + b[0] + 'px,' + b[1] + 'px) rotate(180deg)' }
      ], { duration: 950, easing: 'cubic-bezier(.45,0,.3,1)' });
      items[cur].classList.remove('is-now');
      anim.onfinish = function () {
        place(next); cur = next;
        items[next].classList.add('is-on', 'is-now');
        cube.animate([{ transform: cube.style.transform + ' scale(1.25,.7)' }, { transform: cube.style.transform }], { duration: 260, easing: 'ease-out' });
        timer = setTimeout(hop, 1300);
      };
    };
    new IntersectionObserver(function (en) {
      en.forEach(function (x) {
        if (x.isIntersecting && !running) {
          running = true;
          if (cur < 0) { cur = 0; place(0); items[0].classList.add('is-on', 'is-now'); timer = setTimeout(hop, 1100); }
          else timer = setTimeout(hop, 600);
        } else if (!x.isIntersecting && running) { running = false; clearTimeout(timer); }
      });
    }, { threshold: 0.35 }).observe(steps);
    window.addEventListener('resize', function () { if (cur >= 0) place(cur); });
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
        var host = el.getBoundingClientRect();
        var max = parseFloat(el.getAttribute('data-focus')) || 0.12;
        var end = parseFloat(el.getAttribute('data-focus-min') || 0);
        var p = clamp((vh - host.top) / (host.height + vh * 0.04), 0, 1);
        el.style.setProperty('--blur', (max - (max - end) * p).toFixed(3) + 'em');
      });
      hazes.forEach(function (el) {
        var r = el.getBoundingClientRect();
        if (r.top > vh * 1.1 || r.bottom < -vh * 0.2) return;
        var p = clamp((vh * 0.92 - r.top) / (vh * 0.5), 0, 1);
        var n = el._w.length;
        el._w.forEach(function (w, i) {
          var local = clamp(p * 1.7 - (i / Math.max(1, n)) * 0.7, 0, 1);
          w.style.setProperty('--h', (1 - local).toFixed(3));
        });
      });
    }
    if (shadow && !reduce) {
      var host = shadow.parentElement.getBoundingClientRect();
      var sh = shadow.getBoundingClientRect().height;
      var sp = clamp((vh - host.top) / host.height, 0, 1);
      shadow.style.transform = 'translate3d(0,' + (sp * Math.max(0, host.height - sh)).toFixed(1) + 'px,0)';
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
