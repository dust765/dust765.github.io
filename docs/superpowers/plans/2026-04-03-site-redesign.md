# Dust765 Site — Senior UX Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Rewrite `index.html` with particles hero, glassmorphism cards, screenshot slider + lightbox, video placeholder, scroll-reveal, social SVG icons, hamburger mobile nav, and active nav highlight.

**Architecture:** Single-file static site. All styles in one `<style>` block, all JS in one `<script>` block at end of `<body>`. CSS custom properties palette unchanged. Zero new external dependencies.

**Tech Stack:** HTML5, CSS3 (custom properties, backdrop-filter, aspect-ratio, Grid, Flexbox), vanilla JS (requestAnimationFrame, IntersectionObserver, ES6).

**Spec:** `docs/superpowers/specs/2026-04-03-site-redesign-design.md`  
**File to modify:** `D:/workspace/2026/Dust765-Site/index.html`

---

## SVG Assets (reference — used across multiple tasks)

### GitHub SVG (20×20 for nav, 24×24 for footer — scale via width/height attrs)
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true">
  <path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/>
</svg>
```

### Discord SVG (20×20 for nav, 24×24 for footer)
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true">
  <path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057c.002.022.015.043.032.054a19.9 19.9 0 0 0 5.993 3.03.077.077 0 0 0 .084-.028 14.09 14.09 0 0 0 1.226-1.994.076.076 0 0 0-.041-.106 13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.928 1.793 8.18 1.793 12.062 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.892.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.03zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z"/>
</svg>
```

### Play Triangle SVG (for video button)
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="28" height="28" fill="currentColor" aria-hidden="true">
  <path d="M8 5v14l11-7z"/>
</svg>
```

---

## Task 1: CSS — Foundation (variables, reset, base, scrollbar, noise)

**Files:**
- Modify: `D:/workspace/2026/Dust765-Site/index.html`

Replace the entire `<style>` block. Start with:

- [ ] **Step 1: Open index.html and locate the opening `<style>` tag (line ~11)**

- [ ] **Step 2: Replace the complete `<style>` block** with the following (keep `</style>` at end):

```css
/* ── Reset & Base ─────────────────────────────────────────── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --red-900: #1a0303;
  --red-800: #2e0606;
  --red-700: #4a0909;
  --red-600: #6b0d0d;
  --red-500: #8c1515;
  --red-400: #b01e1e;
  --red-300: #d43030;
  --red-200: #e87070;
  --red-100: #f5b0b0;
  --gold:    #c8a96e;
  --gold-dim:#7a6235;
  --text:    #e8ddd0;
  --text-dim:#9a8f83;
  --bg:      #0e0808;
  --bg2:     #160c0c;
  --border:  rgba(180,30,30,0.25);
}

html { scroll-behavior: smooth; }

body {
  font-family: 'Crimson Text', Georgia, serif;
  background: var(--bg);
  color: var(--text);
  font-size: 18px;
  line-height: 1.7;
  overflow-x: hidden;
}

a { color: var(--red-300); text-decoration: none; transition: color .2s; }
a:hover { color: var(--red-200); }

::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--bg); }
::-webkit-scrollbar-thumb { background: var(--red-600); border-radius: 3px; }

body::before {
  content: '';
  position: fixed; inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.04'/%3E%3C/svg%3E");
  pointer-events: none; z-index: 0; opacity: .4;
}

/* ── Scroll Reveal ───────────────────────────────────────── */
.reveal {
  opacity: 0;
  transform: translateY(28px);
  transition: opacity .55s ease, transform .55s ease;
}
.reveal.visible {
  opacity: 1;
  transform: none;
}

/* ── Navbar ──────────────────────────────────────────────── */
nav {
  position: fixed; top: 0; left: 0; right: 0; z-index: 100;
  display: flex; align-items: center; justify-content: space-between;
  padding: 0 2rem;
  height: 60px;
  background: rgba(14,8,8,.92);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--border);
  transition: background .3s, border-color .3s;
}

.nav-logo {
  display: flex; align-items: center; gap: .75rem;
  text-decoration: none;
}
.nav-logo img { height: 32px; filter: brightness(1.1); }
.nav-logo span {
  font-family: 'Cinzel', serif;
  font-size: .95rem;
  color: var(--red-200);
  letter-spacing: .08em;
}

.nav-links {
  display: flex; gap: 2rem; list-style: none; align-items: center;
}
.nav-links a {
  font-family: 'Cinzel', serif;
  font-size: .72rem;
  letter-spacing: .12em;
  color: var(--text-dim);
  text-transform: uppercase;
  transition: color .2s;
}
.nav-links a:hover,
.nav-links a.nav-active { color: var(--red-300); }

.nav-right {
  display: flex; align-items: center; gap: 1rem;
}

.nav-icon {
  display: flex; align-items: center; justify-content: center;
  color: var(--text-dim);
  transition: color .2s;
  line-height: 0;
}
.nav-icon:hover { color: var(--red-200); }

.nav-cta {
  font-family: 'Cinzel', serif;
  font-size: .72rem;
  letter-spacing: .1em;
  text-transform: uppercase;
  padding: .45rem 1.2rem;
  border: 1px solid var(--red-500);
  color: var(--red-200) !important;
  border-radius: 2px;
  transition: background .2s, color .2s;
}
.nav-cta:hover { background: var(--red-700); color: var(--text) !important; }

/* Hamburger */
.nav-toggle-input {
  position: absolute; opacity: 0; pointer-events: none; width: 0; height: 0;
}
.nav-hamburger {
  display: none;
  flex-direction: column; justify-content: center; gap: .35rem;
  width: 32px; height: 32px;
  cursor: pointer;
  padding: 4px;
}
.nav-hamburger span {
  display: block;
  width: 20px; height: 2px;
  background: var(--text);
  border-radius: 2px;
  transition: transform .25s, opacity .25s;
  transform-origin: center;
}
#nav-toggle:checked ~ nav .nav-hamburger span:nth-child(1) { transform: translateY(6px) rotate(45deg); }
#nav-toggle:checked ~ nav .nav-hamburger span:nth-child(2) { opacity: 0; }
#nav-toggle:checked ~ nav .nav-hamburger span:nth-child(3) { transform: translateY(-6px) rotate(-45deg); }

.nav-drawer {
  position: fixed; top: 60px; right: 0;
  width: 260px; height: calc(100vh - 60px);
  background: rgba(14,8,8,.97);
  backdrop-filter: blur(12px);
  transform: translateX(100%);
  transition: transform .3s ease;
  z-index: 99;
  padding: 2rem;
  border-left: 1px solid var(--border);
}
#nav-toggle:checked ~ .nav-drawer { transform: translateX(0); }
.nav-drawer ul {
  list-style: none;
  display: flex; flex-direction: column; gap: 1.5rem;
}
.nav-drawer ul a {
  font-family: 'Cinzel', serif;
  font-size: .85rem;
  letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--text-dim);
}
.nav-drawer ul a:hover { color: var(--red-300); }
.nav-drawer .drawer-social {
  display: flex; gap: 1rem; margin-top: 2rem;
  padding-top: 2rem; border-top: 1px solid var(--border);
}

/* ── Hero ────────────────────────────────────────────────── */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(20px); }
  to   { opacity: 1; transform: none; }
}

.hero {
  position: relative;
  min-height: 100vh;
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  text-align: center;
  padding: 8rem 2rem 6rem;
  overflow: hidden;
}

#particles {
  position: absolute; inset: 0;
  z-index: 0;
  pointer-events: none;
}

.hero-bg {
  position: absolute; inset: 0;
  background:
    radial-gradient(ellipse 80% 60% at 50% 40%, rgba(80,10,10,.55) 0%, transparent 70%),
    linear-gradient(180deg, var(--bg) 0%, var(--bg2) 100%);
  z-index: 1;
}
.hero-bg::after {
  content: '';
  position: absolute; inset: 0;
  background-image:
    linear-gradient(rgba(140,21,21,.08) 1px, transparent 1px),
    linear-gradient(90deg, rgba(140,21,21,.08) 1px, transparent 1px);
  background-size: 60px 60px;
}

.hero-content {
  position: relative; z-index: 2;
  display: flex; flex-direction: column;
  align-items: center;
}

.hero-badge {
  display: inline-block;
  font-family: 'Cinzel', serif;
  font-size: .7rem;
  letter-spacing: .25em;
  text-transform: uppercase;
  color: var(--red-300);
  border: 1px solid var(--red-700);
  padding: .3rem 1rem;
  border-radius: 2px;
  margin-bottom: 2rem;
  animation: fadeUp .7s ease both;
  animation-delay: 0s;
}

.hero-logo {
  width: min(340px, 70vw);
  margin-bottom: 2rem;
  filter: drop-shadow(0 0 40px rgba(180,30,30,.5));
  animation: fadeUp .7s ease both;
  animation-delay: .3s;
}

.hero-title {
  font-family: 'Cinzel', serif;
  font-size: clamp(2rem, 5vw, 3.6rem);
  font-weight: 400;
  color: var(--text);
  line-height: 1.15;
  margin-bottom: 1.25rem;
  text-shadow: 0 2px 20px rgba(200,50,50,.3);
  animation: fadeUp .7s ease both;
  animation-delay: .7s;
}
.hero-title em {
  font-style: normal;
  color: var(--red-300);
  display: block;
}

.hero-sub {
  max-width: 580px;
  font-size: 1.1rem;
  color: var(--text-dim);
  margin-bottom: 3rem;
  font-style: italic;
  animation: fadeUp .7s ease both;
  animation-delay: 1s;
}

.hero-actions {
  display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center;
  align-items: center;
  animation: fadeUp .7s ease both;
  animation-delay: 1.3s;
}

.btn-primary {
  font-family: 'Cinzel', serif;
  font-size: .8rem;
  letter-spacing: .15em;
  text-transform: uppercase;
  padding: .85rem 2.5rem;
  background: var(--red-600);
  color: var(--text);
  border: 1px solid var(--red-400);
  border-radius: 2px;
  cursor: pointer;
  transition: background .2s, transform .15s, box-shadow .2s;
  box-shadow: 0 0 20px rgba(180,30,30,.3);
}
.btn-primary:hover {
  background: var(--red-500);
  transform: translateY(-2px);
  box-shadow: 0 4px 30px rgba(200,40,40,.45);
  color: var(--text);
}

.btn-outline {
  font-family: 'Cinzel', serif;
  font-size: .8rem;
  letter-spacing: .15em;
  text-transform: uppercase;
  padding: .85rem 2.5rem;
  background: transparent;
  color: var(--text-dim);
  border: 1px solid rgba(150,150,150,.25);
  border-radius: 2px;
  cursor: pointer;
  transition: border-color .2s, color .2s;
}
.btn-outline:hover { border-color: var(--red-500); color: var(--text); }

.btn-icon {
  display: flex; align-items: center; justify-content: center;
  width: 44px; height: 44px;
  border: 1px solid rgba(150,150,150,.2);
  border-radius: 2px;
  color: var(--text-dim);
  transition: border-color .2s, color .2s, background .2s;
  line-height: 0;
}
.btn-icon:hover {
  border-color: var(--red-500);
  color: var(--red-200);
  background: rgba(80,10,10,.2);
}

.hero-scroll {
  position: absolute; bottom: 2rem; z-index: 2;
  font-family: 'Cinzel', serif;
  font-size: .65rem;
  letter-spacing: .2em;
  color: var(--red-700);
  text-transform: uppercase;
  animation: pulse 2.5s ease-in-out infinite;
}
@keyframes pulse { 0%,100%{opacity:.4} 50%{opacity:1} }

/* ── Section base ─────────────────────────────────────────── */
section { position: relative; padding: 6rem 2rem; }

.container { max-width: 1100px; margin: 0 auto; }

.section-label {
  font-family: 'Cinzel', serif;
  font-size: .65rem;
  letter-spacing: .3em;
  text-transform: uppercase;
  color: var(--red-400);
  margin-bottom: .75rem;
}

.section-title {
  font-family: 'Cinzel', serif;
  font-size: clamp(1.4rem, 3vw, 2.2rem);
  font-weight: 400;
  color: var(--text);
  margin-bottom: 1.25rem;
  line-height: 1.2;
}

.section-body {
  font-size: 1.05rem;
  color: var(--text-dim);
  max-width: 680px;
  line-height: 1.85;
}

/* ── About ───────────────────────────────────────────────── */
#about {
  background: var(--bg2);
  border-top: 1px solid var(--border);
  border-bottom: 1px solid var(--border);
}
.about-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 5rem;
  align-items: center;
}
.about-quote {
  position: relative;
  padding: 2rem 2rem 2rem 2.5rem;
  border-left: 3px solid var(--red-600);
  background: rgba(80,10,10,.15);
  border-radius: 0 4px 4px 0;
  margin-top: 2rem;
}
.about-quote p { font-size: 1rem; color: var(--text-dim); font-style: italic; }
.about-quote cite {
  display: block; margin-top: .75rem;
  font-size: .85rem; color: var(--gold-dim);
  font-style: normal; letter-spacing: .05em;
}
.about-stats { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; }
.stat-card {
  background: rgba(80,10,10,.12);
  border: 1px solid var(--border);
  border-radius: 4px;
  padding: 1.5rem;
  text-align: center;
  transition: border-color .2s, background .2s;
}
.stat-card:hover { border-color: var(--red-500); background: rgba(100,15,15,.22); }
.stat-card .num { font-family: 'Cinzel', serif; font-size: 2rem; color: var(--red-300); display: block; }
.stat-card .lbl { font-size: .85rem; color: var(--text-dim); margin-top: .25rem; }

/* ── Features ────────────────────────────────────────────── */
#features { background: var(--bg); }
.features-header { text-align: center; margin-bottom: 4rem; }
.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 1.5rem;
}
.feat-card {
  background: rgba(30, 8, 8, 0.55);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(180, 30, 30, 0.2);
  border-radius: 4px;
  padding: 1.75rem;
  box-shadow: 0 4px 24px rgba(0,0,0,.4), inset 0 1px 0 rgba(255,80,80,.06);
  transition: transform .2s, border-color .2s, box-shadow .2s;
}
.feat-card:hover {
  transform: translateY(-4px);
  border-color: var(--red-500);
  box-shadow: 0 12px 40px rgba(150,20,20,.3);
}
.feat-icon { font-size: 1.6rem; margin-bottom: 1rem; display: block; }
.feat-title {
  font-family: 'Cinzel', serif;
  font-size: 1rem; font-weight: 600;
  color: var(--text); margin-bottom: .5rem;
}
.feat-desc { font-size: .95rem; color: var(--text-dim); line-height: 1.75; }

/* ── Screenshots Slider ───────────────────────────────────── */
#screenshots {
  background: var(--bg2);
  border-top: 1px solid var(--border);
  border-bottom: 1px solid var(--border);
}
.screenshots-header { text-align: center; margin-bottom: 3rem; }

.slider { position: relative; user-select: none; }

.slider-track {
  position: relative;
  aspect-ratio: 16 / 9;
  overflow: hidden;
  border-radius: 4px;
  border: 1px solid var(--border);
  background: var(--bg);
}

.slide {
  position: absolute; inset: 0;
  opacity: 0;
  transition: opacity .5s ease;
  pointer-events: none;
}
.slide.active { opacity: 1; pointer-events: auto; }

.slide img {
  width: 100%; height: 100%;
  object-fit: cover; object-position: top;
  display: block;
  cursor: zoom-in;
}

.slide-caption {
  position: absolute; bottom: 0; left: 0; right: 0;
  background: linear-gradient(transparent, rgba(0,0,0,.75));
  padding: 2rem 1.5rem .75rem;
  font-family: 'Cinzel', serif;
  font-size: .75rem; letter-spacing: .12em;
  text-transform: uppercase;
  color: var(--text-dim);
}

.slider-btn {
  position: absolute; top: 50%; transform: translateY(-50%);
  width: 44px; height: 44px;
  background: rgba(14,8,8,.75);
  border: 1px solid var(--border);
  border-radius: 2px;
  color: var(--text-dim);
  font-size: 1.6rem; line-height: 1;
  cursor: pointer;
  transition: background .2s, border-color .2s, color .2s;
  z-index: 2;
  display: flex; align-items: center; justify-content: center;
}
.slider-btn:hover { background: var(--red-700); border-color: var(--red-500); color: var(--text); }
.slider-prev { left: .75rem; }
.slider-next { right: .75rem; }

.slider-dots {
  display: flex; justify-content: center; gap: .6rem;
  margin-top: 1.25rem;
}
.dot {
  position: relative;
  width: 32px; height: 3px;
  background: rgba(180,30,30,.2);
  border: none;
  border-radius: 2px;
  cursor: pointer;
  overflow: hidden;
  padding: 0;
}
.dot::after {
  content: '';
  position: absolute; inset: 0;
  background: var(--red-400);
  transform: scaleX(0);
  transform-origin: left;
}
.dot.active::after {
  animation: dotFill 4s linear forwards;
}
@keyframes dotFill { to { transform: scaleX(1); } }

/* ── Lightbox ─────────────────────────────────────────────── */
.lightbox {
  position: fixed; inset: 0;
  z-index: 200;
  display: flex; align-items: center; justify-content: center;
  opacity: 0; pointer-events: none;
  transition: opacity .25s;
}
.lightbox.open { opacity: 1; pointer-events: auto; }

.lightbox-backdrop {
  position: absolute; inset: 0;
  background: rgba(0,0,0,.9);
}

.lightbox-img {
  position: relative; z-index: 1;
  max-width: 90vw; max-height: 85vh;
  border: 1px solid var(--red-700);
  border-radius: 4px;
  display: block;
}

.lightbox-close {
  position: absolute; top: 1.5rem; right: 1.5rem; z-index: 2;
  width: 40px; height: 40px;
  background: rgba(14,8,8,.8);
  border: 1px solid var(--border);
  border-radius: 2px;
  color: var(--text-dim);
  font-size: 1.1rem;
  cursor: pointer;
  transition: color .2s, background .2s;
  display: flex; align-items: center; justify-content: center;
}
.lightbox-close:hover { color: var(--text); background: var(--red-700); }

.lightbox-prev,
.lightbox-next {
  position: absolute; top: 50%; transform: translateY(-50%); z-index: 2;
  width: 44px; height: 44px;
  background: rgba(14,8,8,.8);
  border: 1px solid var(--border);
  border-radius: 2px;
  color: var(--text-dim);
  font-size: 1.8rem; line-height: 1;
  cursor: pointer;
  transition: background .2s, border-color .2s, color .2s;
  display: flex; align-items: center; justify-content: center;
}
.lightbox-prev:hover,
.lightbox-next:hover { background: var(--red-700); border-color: var(--red-500); color: var(--text); }
.lightbox-prev { left: 1.5rem; }
.lightbox-next { right: 1.5rem; }

/* ── Video ────────────────────────────────────────────────── */
#video {
  background: var(--bg);
  border-top: 1px solid var(--border);
}
.video-header { margin-bottom: 2.5rem; text-align: center; }
.video-wrapper { max-width: 900px; margin: 0 auto; }
.video-placeholder {
  position: relative;
  aspect-ratio: 16 / 9;
  background: var(--bg2);
  border: 1px solid var(--border);
  border-radius: 4px;
  display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  cursor: pointer;
  overflow: hidden;
  transition: border-color .2s, box-shadow .2s;
}
.video-placeholder:hover {
  border-color: var(--red-500);
  box-shadow: 0 0 50px rgba(150,20,20,.35);
}
.video-bg {
  position: absolute; inset: 0;
  background: url('logodust.png') center/25% no-repeat;
  opacity: .05;
  filter: grayscale(1);
}
.video-bg::after {
  content: '';
  position: absolute; inset: 0;
  background:
    radial-gradient(ellipse 70% 70% at 50% 50%, rgba(80,10,10,.4) 0%, transparent 70%);
}
.video-play-btn {
  width: 72px; height: 72px;
  border-radius: 50%;
  background: var(--red-600);
  border: 2px solid var(--red-400);
  display: flex; align-items: center; justify-content: center;
  cursor: pointer;
  transition: transform .2s, background .2s, box-shadow .2s;
  margin-bottom: 1.25rem;
  position: relative; z-index: 1;
  box-shadow: 0 0 30px rgba(180,30,30,.4);
}
.video-play-btn:hover { transform: scale(1.1); background: var(--red-500); box-shadow: 0 0 50px rgba(200,40,40,.6); }
.video-label {
  font-family: 'Cinzel', serif;
  font-size: 1rem; letter-spacing: .15em;
  text-transform: uppercase;
  color: var(--text);
  position: relative; z-index: 1;
}
.video-sub {
  font-size: .9rem; color: var(--text-dim);
  font-style: italic; margin-top: .4rem;
  position: relative; z-index: 1;
}

/* ── Install ─────────────────────────────────────────────── */
#install {
  background: var(--bg2);
  border-top: 1px solid var(--border);
  border-bottom: 1px solid var(--border);
}
.install-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: start; }
.platform-tabs { display: flex; gap: .5rem; margin-bottom: 1.5rem; flex-wrap: wrap; }
.tab-btn {
  font-family: 'Cinzel', serif; font-size: .7rem; letter-spacing: .12em;
  text-transform: uppercase; padding: .4rem 1rem;
  background: transparent; border: 1px solid var(--border);
  color: var(--text-dim); border-radius: 2px; cursor: pointer; transition: all .2s;
}
.tab-btn.active, .tab-btn:hover { background: var(--red-700); border-color: var(--red-500); color: var(--text); }
.tab-content { display: none; }
.tab-content.active { display: block; }
.steps { list-style: none; counter-reset: step-counter; }
.steps li {
  counter-increment: step-counter;
  display: flex; gap: 1rem; margin-bottom: 1.25rem; align-items: flex-start;
}
.steps li::before {
  content: counter(step-counter, decimal-leading-zero);
  font-family: 'Cinzel', serif; font-size: .75rem; color: var(--red-400);
  background: rgba(80,10,10,.3); border: 1px solid var(--red-700);
  border-radius: 2px; padding: .2rem .5rem;
  min-width: 2.4rem; text-align: center; margin-top: .2rem; flex-shrink: 0;
}
.steps li span { font-size: 1rem; color: var(--text-dim); }
.steps li strong { color: var(--text); }
.code-block {
  background: #0a0606; border: 1px solid var(--border);
  border-left: 3px solid var(--red-600); border-radius: 0 4px 4px 0;
  padding: 1.25rem 1.5rem; font-family: 'Courier New', monospace;
  font-size: .85rem; color: #ccc; margin-top: 1.25rem; overflow-x: auto; line-height: 1.8;
}
.code-block .cmd-comment { color: var(--red-700); }
.code-block .cmd-main    { color: #e8d5b0; }
.prereq-list { list-style: none; }
.prereq-list li {
  display: flex; align-items: center; gap: .75rem; padding: .6rem 0;
  border-bottom: 1px solid rgba(150,30,30,.1); font-size: .95rem; color: var(--text-dim);
}
.prereq-list li:last-child { border-bottom: none; }
.prereq-list li::before { content: '▸'; color: var(--red-400); font-size: .8rem; flex-shrink: 0; }
.prereq-list a { color: var(--red-300); }

/* ── Contribute ──────────────────────────────────────────── */
#contribute { background: var(--bg); }
.contribute-grid { display: grid; grid-template-columns: 2fr 1fr; gap: 4rem; align-items: start; }
.contribute-steps { margin-top: 2rem; }
.c-step { display: flex; gap: 1.25rem; margin-bottom: 1.75rem; }
.c-step-num {
  font-family: 'Cinzel', serif; font-size: .8rem; color: var(--red-300);
  background: rgba(80,10,10,.35); border: 1px solid var(--red-700); border-radius: 50%;
  width: 2.2rem; height: 2.2rem; display: flex; align-items: center; justify-content: center;
  flex-shrink: 0; margin-top: .15rem;
}
.c-step-body strong { font-family: 'Cinzel', serif; font-size: .9rem; color: var(--text); display: block; margin-bottom: .25rem; }
.c-step-body p { font-size: .95rem; color: var(--text-dim); }
.links-panel { background: rgba(80,10,10,.1); border: 1px solid var(--border); border-radius: 4px; padding: 2rem; }
.links-panel h3 { font-family: 'Cinzel', serif; font-size: .9rem; color: var(--text); margin-bottom: 1.25rem; letter-spacing: .08em; }
.link-item {
  display: flex; align-items: center; gap: .75rem; padding: .75rem 0;
  border-bottom: 1px solid rgba(150,30,30,.1); font-size: .95rem; color: var(--text-dim); transition: color .2s;
}
.link-item:last-child { border-bottom: none; }
.link-item:hover { color: var(--text); }
.link-item .li-icon { font-size: 1.1rem; }
.link-item a { color: inherit; }

/* ── Download ────────────────────────────────────────────── */
#download {
  background: linear-gradient(135deg, var(--red-900) 0%, #1e0808 50%, var(--red-900) 100%);
  border-top: 1px solid var(--red-700); border-bottom: 1px solid var(--red-700);
  text-align: center; padding: 5rem 2rem;
}
#download .section-title { margin-bottom: .5rem; }
#download .section-body { margin: 0 auto 2.5rem; text-align: center; }
.download-grid {
  display: flex; flex-wrap: wrap; gap: 1.5rem; justify-content: center; margin-top: 2rem;
}
.dl-card {
  background: rgba(0,0,0,.35); border: 1px solid var(--border);
  border-radius: 4px; padding: 1.5rem 2rem; min-width: 180px; text-align: center;
  transition: border-color .2s, background .2s;
}
.dl-card:hover { border-color: var(--red-400); background: rgba(80,10,10,.25); }
.dl-card .dl-icon { font-size: 2rem; display: block; margin-bottom: .5rem; }
.dl-card .dl-name { font-family: 'Cinzel', serif; font-size: .85rem; color: var(--text); }
.dl-card .dl-sub { font-size: .8rem; color: var(--text-dim); margin-top: .25rem; }

/* ── Footer ──────────────────────────────────────────────── */
footer {
  background: #080404;
  border-top: 1px solid var(--border);
  padding: 3rem 2rem;
  text-align: center;
}
footer > img { height: 36px; margin-bottom: 1.25rem; opacity: .7; filter: grayscale(.3); display: block; margin-left: auto; margin-right: auto; }
.footer-social { display: flex; justify-content: center; gap: 1.25rem; margin-bottom: 1.5rem; }
.footer-social a { color: var(--text-dim); transition: color .2s; line-height: 0; }
.footer-social a:hover { color: var(--red-300); }
.footer-links {
  display: flex; flex-wrap: wrap; gap: 2rem; justify-content: center; margin-bottom: 1.5rem;
}
.footer-links a {
  font-family: 'Cinzel', serif; font-size: .65rem; letter-spacing: .15em;
  text-transform: uppercase; color: var(--text-dim);
}
.footer-links a:hover { color: var(--red-300); }
.footer-copy { font-size: .85rem; color: var(--red-700); }
.footer-credits { margin-top: .5rem; font-size: .82rem; color: rgba(120,80,80,.6); }

/* ── Misc ────────────────────────────────────────────────── */
.text-accent { color: var(--red-300); }
.mt-2 { margin-top: 2rem; }
.badge-row { display: flex; flex-wrap: wrap; gap: .6rem; margin-top: 1.5rem; }
.badge {
  font-family: 'Cinzel', serif; font-size: .62rem; letter-spacing: .12em;
  text-transform: uppercase; padding: .28rem .75rem; border-radius: 2px;
  background: rgba(80,10,10,.3); border: 1px solid var(--red-700); color: var(--red-200);
}
.about-quote.mt-2 { margin-top: 2rem; }

hr.divider { border: none; border-top: 1px solid var(--border); margin: 0; }

/* ── Responsive ──────────────────────────────────────────── */
@media (max-width: 860px) {
  .about-grid, .install-grid, .contribute-grid { grid-template-columns: 1fr; gap: 2.5rem; }
  .nav-links { display: none; }
  .nav-right .nav-icon { display: none; }
  .nav-hamburger { display: flex; }
}

@media (max-width: 660px) {
  .slider-btn { width: 36px; height: 36px; font-size: 1.3rem; }
  .lightbox-prev, .lightbox-next { display: none; }
}

@media (max-width: 560px) {
  .about-stats { grid-template-columns: 1fr 1fr; }
  .features-grid { grid-template-columns: 1fr; }
}
```

- [ ] **Step 3: Verify in browser** — open `index.html`. Page should load with correct colors (dark red theme). No layout visible yet until HTML tasks below.

- [ ] **Step 4: Commit**
```bash
cd "D:/workspace/2026/Dust765-Site"
git add index.html
git commit -m "feat: complete CSS rewrite — particles, slider, glassmorphism, hamburger, scroll-reveal"
```

---

## Task 2: HTML — Complete page structure

**Files:**
- Modify: `D:/workspace/2026/Dust765-Site/index.html`

Replace everything inside `<body>...</body>` (keep `<head>` and `</html>` tags).

- [ ] **Step 1: Replace the entire `<body>` content** with:

```html
<body>

<!-- ── NAV ───────────────────────────────────────────────────── -->
<input type="checkbox" id="nav-toggle" class="nav-toggle-input" />
<nav>
  <a href="https://dust765.github.io/" class="nav-logo">
    <img src="logodust.png" alt="Dust765" />
    <span>Dust765</span>
  </a>

  <ul class="nav-links">
    <li><a href="#about" class="nav-link">About</a></li>
    <li><a href="#features" class="nav-link">Features</a></li>
    <li><a href="#screenshots" class="nav-link">Screenshots</a></li>
    <li><a href="#video" class="nav-link">Video</a></li>
    <li><a href="#install" class="nav-link">Install</a></li>
    <li><a href="https://github.com/dust765/ClassicUO/wiki" target="_blank">Wiki</a></li>
  </ul>

  <div class="nav-right">
    <a class="nav-icon" href="https://github.com/dust765/ClassicUO" target="_blank" rel="noopener" aria-label="GitHub">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/></svg>
    </a>
    <a class="nav-icon" href="https://discord.gg/9Vh7aqqX" target="_blank" rel="noopener" aria-label="Discord">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="20" height="20" fill="currentColor" aria-hidden="true"><path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057c.002.022.015.043.032.054a19.9 19.9 0 0 0 5.993 3.03.077.077 0 0 0 .084-.028 14.09 14.09 0 0 0 1.226-1.994.076.076 0 0 0-.041-.106 13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.928 1.793 8.18 1.793 12.062 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.892.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.03zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z"/></svg>
    </a>
    <a class="nav-cta" href="https://discord.gg/9Vh7aqqX" target="_blank" rel="noopener">Discord</a>
    <a class="nav-cta" href="#download">Download</a>
    <label for="nav-toggle" class="nav-hamburger" aria-label="Menu">
      <span></span><span></span><span></span>
    </label>
  </div>
</nav>

<div class="nav-drawer">
  <ul>
    <li><a href="#about" class="nav-drawer-link">About</a></li>
    <li><a href="#features" class="nav-drawer-link">Features</a></li>
    <li><a href="#screenshots" class="nav-drawer-link">Screenshots</a></li>
    <li><a href="#video" class="nav-drawer-link">Video</a></li>
    <li><a href="#install" class="nav-drawer-link">Install</a></li>
    <li><a href="#download" class="nav-drawer-link">Download</a></li>
    <li><a href="https://github.com/dust765/ClassicUO/wiki" target="_blank">Wiki</a></li>
  </ul>
  <div class="drawer-social">
    <a class="nav-icon" href="https://github.com/dust765/ClassicUO" target="_blank" rel="noopener" aria-label="GitHub">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" aria-hidden="true"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/></svg>
    </a>
    <a class="nav-icon" href="https://discord.gg/9Vh7aqqX" target="_blank" rel="noopener" aria-label="Discord">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" aria-hidden="true"><path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057c.002.022.015.043.032.054a19.9 19.9 0 0 0 5.993 3.03.077.077 0 0 0 .084-.028 14.09 14.09 0 0 0 1.226-1.994.076.076 0 0 0-.041-.106 13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.928 1.793 8.18 1.793 12.062 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.892.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.03zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z"/></svg>
    </a>
  </div>
</div>

<!-- ── HERO ──────────────────────────────────────────────────── -->
<section class="hero" id="home">
  <canvas id="particles"></canvas>
  <div class="hero-bg"></div>
  <div class="hero-content">
    <div class="hero-badge">Ultima Online Enhanced Client</div>
    <img class="hero-logo" src="logodust.png" alt="Dust765 Logo" />
    <h1 class="hero-title">
      Built for PvP.<em>Powered by FNA.</em>
    </h1>
    <p class="hero-sub">
      Dust765 is a ClassicUO fork built for serious Ultima Online players —
      fast, cross-platform, and packed with combat features. No drama. Just UO.
    </p>
    <div class="hero-actions">
      <a class="btn-primary" href="#download">Download Now</a>
      <a class="btn-outline" href="https://github.com/dust765/ClassicUO" target="_blank" rel="noopener">View on GitHub</a>
      <a class="btn-icon" href="https://github.com/dust765/ClassicUO" target="_blank" rel="noopener" aria-label="GitHub">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="22" height="22" fill="currentColor" aria-hidden="true"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/></svg>
      </a>
      <a class="btn-icon" href="https://discord.gg/9Vh7aqqX" target="_blank" rel="noopener" aria-label="Discord">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="22" height="22" fill="currentColor" aria-hidden="true"><path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057c.002.022.015.043.032.054a19.9 19.9 0 0 0 5.993 3.03.077.077 0 0 0 .084-.028 14.09 14.09 0 0 0 1.226-1.994.076.076 0 0 0-.041-.106 13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.928 1.793 8.18 1.793 12.062 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.892.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.03zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z"/></svg>
      </a>
    </div>
  </div>
  <span class="hero-scroll">↓ Scroll to explore</span>
</section>

<!-- ── ABOUT ─────────────────────────────────────────────────── -->
<section id="about">
  <div class="container">
    <div class="about-grid">
      <div>
        <p class="section-label reveal">The Project</p>
        <h2 class="section-title reveal">Why Dust765 Exists</h2>
        <p class="section-body reveal">
          Dust765 was born from frustration — not with Ultima Online itself,
          but with the drama, gatekeeping, and clique culture that had crept
          into its open-source tooling ecosystem.
        </p>
        <p class="section-body mt-2 reveal">
          We took ClassicUO, stripped the politics out, and focused on what
          actually matters: a fast, stable, cross-platform client that
          respects every player regardless of what OS they run or who they know.
        </p>
        <div class="about-quote reveal">
          <p>"This project was created to show the community that open source
          isn't meant for cliques and high school drama — it's meant for the
          expansion of something greater: innovation."</p>
          <cite>— A penny for your thoughts, the adder that prays beneath the rose.</cite>
        </div>
      </div>
      <div class="about-stats">
        <div class="stat-card reveal">
          <span class="num">3</span>
          <span class="lbl">Platforms<br>Windows · Linux · macOS</span>
        </div>
        <div class="stat-card reveal">
          <span class="num">.NET</span>
          <span class="lbl">Framework 4.8<br>Stable & Proven</span>
        </div>
        <div class="stat-card reveal">
          <span class="num">FNA</span>
          <span class="lbl">Cross-platform<br>Graphics Engine</span>
        </div>
        <div class="stat-card reveal">
          <span class="num">v3</span>
          <span class="lbl">Current Release<br>Series</span>
        </div>
        <div class="badge-row reveal" style="grid-column:1/-1">
          <span class="badge">Open Source</span>
          <span class="badge">MIT License</span>
          <span class="badge">No Drama</span>
          <span class="badge">Cross-Platform</span>
          <span class="badge">PvP Focused</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ── FEATURES ──────────────────────────────────────────────── -->
<section id="features">
  <div class="container">
    <div class="features-header reveal">
      <p class="section-label">What We Built</p>
      <h2 class="section-title">Features</h2>
      <p class="section-body" style="margin:0 auto;text-align:center">
        Every feature below was added because players asked for it — not
        because someone in a Discord inner-circle approved it.
      </p>
    </div>
    <div class="features-grid">
      <div class="feat-card reveal" style="transition-delay:0s">
        <span class="feat-icon">⚔️</span>
        <div class="feat-title">Combat Enhancements</div>
        <p class="feat-desc">Last target tracking, self-cast support, stun/mortal highlight, swing line indicators for ranged weapons, sync position on attack, and UO Classic Combat integration.</p>
      </div>
      <div class="feat-card reveal" style="transition-delay:.08s">
        <span class="feat-icon">🧿</span>
        <div class="feat-title">Visual Helpers</div>
        <p class="feat-desc">Glowing weapons, highlight friends and guild members, gargoyle fly state override, custom gargoyle walk animation while flying, and health indicator overlay.</p>
      </div>
      <div class="feat-card reveal" style="transition-delay:.16s">
        <span class="feat-icon">🪄</span>
        <div class="feat-title">Casting & Spells</div>
        <p class="feat-desc">Active spell icon on cursor, OnCasting gump, self-cast last target highlight, and fast rotation support for fluid spellcasting.</p>
      </div>
      <div class="feat-card reveal" style="transition-delay:.24s">
        <span class="feat-icon">🖥️</span>
        <div class="feat-title">Modern UI</div>
        <p class="feat-desc">Custom window title bar with HP/Mana/Stamina bars (UOS/Orion-style), borderless window mode with resize edges, and a redesigned login screen.</p>
      </div>
      <div class="feat-card reveal" style="transition-delay:.32s">
        <span class="feat-icon">🌍</span>
        <div class="feat-title">Cross-Platform</div>
        <p class="feat-desc">Native builds for Windows x64, Linux x64, and macOS. All platforms are treated equally — first-class support, not an afterthought.</p>
      </div>
      <div class="feat-card reveal" style="transition-delay:.40s">
        <span class="feat-icon">🔌</span>
        <div class="feat-title">Plugin Compatibility</div>
        <p class="feat-desc">Razor Enhanced, UOStealth, UOAssist, ClassicAssist, and other popular plugins all work out of the box. No manual patching required.</p>
      </div>
      <div class="feat-card reveal" style="transition-delay:.48s">
        <span class="feat-icon">🗒️</span>
        <div class="feat-title">Auto Loot & Macros</div>
        <p class="feat-desc">Built-in auto-loot system, UO Classic Combat macro helpers, action bar, and scriptable macro support for repetitive tasks.</p>
      </div>
      <div class="feat-card reveal" style="transition-delay:.56s">
        <span class="feat-icon">📊</span>
        <div class="feat-title">Info & Nameplates</div>
        <p class="feat-desc">Configurable nameplates, health bars, info bars, cooldown bars, counters, and an in-game buff bar — all customizable per profile.</p>
      </div>
      <div class="feat-card reveal" style="transition-delay:.64s">
        <span class="feat-icon">🔄</span>
        <div class="feat-title">Auto Updater</div>
        <p class="feat-desc">Integrated update manager checks for new releases and applies them automatically so you never miss a patch or have to hunt down downloads.</p>
      </div>
    </div>
  </div>
</section>

<!-- ── SCREENSHOTS ──────────────────────────────────────────── -->
<section id="screenshots">
  <div class="container">
    <div class="screenshots-header reveal">
      <p class="section-label">Visual</p>
      <h2 class="section-title">Client Graphics</h2>
      <p class="section-body" style="margin:0 auto;text-align:center">
        A look at the Dust765 client interface — redesigned for clarity and performance.
      </p>
    </div>
    <div class="slider" id="mainSlider">
      <div class="slider-track">
        <div class="slide active">
          <img src="https://raw.githubusercontent.com/dust765/ClassicUO/developer/docs/login.png"
               alt="Login Screen" loading="eager" />
          <div class="slide-caption">Login Screen</div>
        </div>
        <div class="slide">
          <img src="https://raw.githubusercontent.com/dust765/ClassicUO/developer/docs/selectcharacter.png"
               alt="Character Selection" loading="lazy" />
          <div class="slide-caption">Character Selection</div>
        </div>
        <div class="slide">
          <img src="https://raw.githubusercontent.com/dust765/ClassicUO/developer/docs/create.png"
               alt="Character Creation" loading="lazy" />
          <div class="slide-caption">Character Creation</div>
        </div>
        <div class="slide">
          <img src="https://raw.githubusercontent.com/dust765/ClassicUO/developer/docs/options.png"
               alt="Options Menu" loading="lazy" />
          <div class="slide-caption">Options Menu</div>
        </div>
      </div>
      <button class="slider-btn slider-prev" aria-label="Previous">&#8249;</button>
      <button class="slider-btn slider-next" aria-label="Next">&#8250;</button>
      <div class="slider-dots" id="sliderDots"></div>
    </div>
  </div>
</section>

<!-- ── VIDEO ─────────────────────────────────────────────────── -->
<section id="video">
  <div class="container">
    <div class="video-header reveal">
      <p class="section-label">Gameplay</p>
      <h2 class="section-title">See It in Action</h2>
    </div>
    <div class="video-wrapper reveal">
      <div class="video-placeholder" id="videoPlaceholder">
        <div class="video-bg"></div>
        <button class="video-play-btn" onclick="loadVideo()" aria-label="Play video">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="28" height="28" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>
        </button>
        <p class="video-label">Watch Gameplay</p>
        <p class="video-sub">See Dust765 in action — PvP showcase</p>
      </div>
    </div>
  </div>
</section>

<!-- ── INSTALL ────────────────────────────────────────────────── -->
<section id="install">
  <div class="container">
    <div class="install-grid">
      <div>
        <p class="section-label reveal">Getting Started</p>
        <h2 class="section-title reveal">Installation</h2>
        <p class="section-body reveal">
          Dust765 is a standalone client. No source code required — just
          download, extract, and point it at your UO installation.
        </p>
        <div class="platform-tabs mt-2">
          <button class="tab-btn active" onclick="showTab('win')">Windows</button>
          <button class="tab-btn" onclick="showTab('linux')">Linux</button>
          <button class="tab-btn" onclick="showTab('mac')">macOS</button>
          <button class="tab-btn" onclick="showTab('src')">From Source</button>
        </div>
        <div id="tab-win" class="tab-content active">
          <ol class="steps">
            <li><span>Download <strong>Dust765-Windows-x64.zip</strong> from the <a href="https://github.com/dust765/ClassicUO/releases" target="_blank">Releases page</a>.</span></li>
            <li><span>Extract the archive to a folder of your choice (e.g. <code>C:\Games\Dust765</code>).</span></li>
            <li><span>Open <strong>settings.json</strong> and set <strong>uo_path</strong> to your Ultima Online client directory.</span></li>
            <li><span>Run <strong>ClassicUO.exe</strong> — no installation wizard needed.</span></li>
          </ol>
        </div>
        <div id="tab-linux" class="tab-content">
          <ol class="steps">
            <li><span>Download <strong>Dust765-linux.zip</strong> from the <a href="https://github.com/dust765/ClassicUO/releases" target="_blank">Releases page</a>.</span></li>
            <li><span>Extract: <code>unzip Dust765-linux.zip -d ~/Dust765</code></span></li>
            <li><span>Install Mono: <code>sudo apt install mono-complete</code></span></li>
            <li><span>Edit <strong>settings.json</strong> to point to your UO data files.</span></li>
            <li><span>Run: <code>mono ClassicUO.exe</code></span></li>
          </ol>
        </div>
        <div id="tab-mac" class="tab-content">
          <ol class="steps">
            <li><span>Download <strong>Dust765-mac.zip</strong> from the <a href="https://github.com/dust765/ClassicUO/releases" target="_blank">Releases page</a>.</span></li>
            <li><span>Install Mono via Homebrew: <code>brew install mono</code></span></li>
            <li><span>Edit <strong>settings.json</strong> to point to your UO data files.</span></li>
            <li><span>Run: <code>mono ClassicUO.exe</code></span></li>
          </ol>
        </div>
        <div id="tab-src" class="tab-content">
          <div class="code-block">
<span class="cmd-comment"># Clone with submodules</span>
<span class="cmd-main">git clone --recurse-submodules \
  https://github.com/dust765/ClassicUO.git
cd ClassicUO</span>

<span class="cmd-comment"># Restore &amp; build (.NET Framework 4.8)</span>
<span class="cmd-main">dotnet restore src/ClassicUO.Client/ClassicUO.Client.csproj
dotnet build src/ClassicUO.Client/ClassicUO.Client.csproj -c Release</span>
          </div>
        </div>
      </div>
      <div>
        <p class="section-label reveal">Requirements</p>
        <h3 class="section-title reveal" style="font-size:1.2rem">Prerequisites</h3>
        <ul class="prereq-list reveal">
          <li>Ultima Online client files (any licensed copy)</li>
          <li><a href="https://dotnet.microsoft.com/download/dotnet-framework/net48" target="_blank">.NET Framework 4.8</a> (Windows)</li>
          <li><a href="https://www.mono-project.com/download/stable/" target="_blank">Mono Runtime</a> (Linux / macOS)</li>
          <li>64-bit OS (x64 architecture)</li>
          <li>OpenGL 3.0+ capable GPU</li>
        </ul>
        <div class="about-quote mt-2 reveal">
          <p>Point <strong>uo_path</strong> in <code>settings.json</code> to your Ultima Online
          data directory. Everything else is optional — sensible defaults are provided.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ── DOWNLOAD ───────────────────────────────────────────────── -->
<section id="download">
  <div class="container">
    <p class="section-label reveal">Latest Release</p>
    <h2 class="section-title reveal">Download Dust765</h2>
    <p class="section-body reveal">
      Builds are produced automatically from every commit. Grab the
      version for your platform — no account needed, no strings attached.
    </p>
    <div class="download-grid">
      <a class="dl-card reveal" href="https://github.com/dust765/ClassicUO/releases" target="_blank" rel="noopener">
        <span class="dl-icon">🪟</span>
        <div class="dl-name">Windows</div>
        <div class="dl-sub">x64 · .exe</div>
      </a>
      <a class="dl-card reveal" href="https://github.com/dust765/ClassicUO/releases" target="_blank" rel="noopener" style="transition-delay:.08s">
        <span class="dl-icon">🐧</span>
        <div class="dl-name">Linux</div>
        <div class="dl-sub">x64 · Mono</div>
      </a>
      <a class="dl-card reveal" href="https://github.com/dust765/ClassicUO/releases" target="_blank" rel="noopener" style="transition-delay:.16s">
        <span class="dl-icon">🍎</span>
        <div class="dl-name">macOS</div>
        <div class="dl-sub">x64 · Mono</div>
      </a>
      <a class="dl-card reveal" href="https://github.com/dust765/ClassicUO" target="_blank" rel="noopener" style="transition-delay:.24s">
        <span class="dl-icon">📦</span>
        <div class="dl-name">Source</div>
        <div class="dl-sub">GitHub · MIT</div>
      </a>
    </div>
  </div>
</section>

<!-- ── CONTRIBUTE ────────────────────────────────────────────── -->
<section id="contribute">
  <div class="container">
    <div class="contribute-grid">
      <div>
        <p class="section-label reveal">Open Source</p>
        <h2 class="section-title reveal">Contribute</h2>
        <p class="section-body reveal">
          Dust765 is open to everyone. If you play UO and you have an idea
          that makes the game better — you're already qualified. No inner circle.
        </p>
        <div class="contribute-steps">
          <div class="c-step reveal">
            <div class="c-step-num">1</div>
            <div class="c-step-body">
              <strong>Fork the Repository</strong>
              <p>Click Fork on GitHub to create your own copy of the codebase.</p>
            </div>
          </div>
          <div class="c-step reveal">
            <div class="c-step-num">2</div>
            <div class="c-step-body">
              <strong>Create a Feature Branch</strong>
              <p><code>git checkout -b feature/YourIdea</code> — keep it focused.</p>
            </div>
          </div>
          <div class="c-step reveal">
            <div class="c-step-num">3</div>
            <div class="c-step-body">
              <strong>Build &amp; Test Locally</strong>
              <p>Run <code>dotnet build</code> and make sure nothing is broken before pushing.</p>
            </div>
          </div>
          <div class="c-step reveal">
            <div class="c-step-num">4</div>
            <div class="c-step-body">
              <strong>Open a Pull Request</strong>
              <p>Target the <code>developer</code> branch. Describe what you changed and why.</p>
            </div>
          </div>
          <div class="c-step reveal">
            <div class="c-step-num">5</div>
            <div class="c-step-body">
              <strong>Get Honest Feedback</strong>
              <p>Expect real technical review — not gatekeeping, not politics.</p>
            </div>
          </div>
        </div>
      </div>
      <div class="links-panel reveal">
        <h3>Community &amp; Links</h3>
        <a class="link-item" href="https://github.com/dust765/ClassicUO" target="_blank" rel="noopener">
          <span class="li-icon">📁</span><span>GitHub Repository</span>
        </a>
        <a class="link-item" href="https://github.com/dust765/ClassicUO/issues" target="_blank" rel="noopener">
          <span class="li-icon">🐛</span><span>Bug Reports &amp; Issues</span>
        </a>
        <a class="link-item" href="https://github.com/dust765/ClassicUO/discussions" target="_blank" rel="noopener">
          <span class="li-icon">💬</span><span>Discussions</span>
        </a>
        <a class="link-item" href="https://discord.gg/9Vh7aqqX" target="_blank" rel="noopener">
          <span class="li-icon">🎮</span><span>Discord Server</span>
        </a>
        <a class="link-item" href="https://github.com/dust765/ClassicUO/wiki" target="_blank" rel="noopener">
          <span class="li-icon">📖</span><span>Dust765 Wiki</span>
        </a>
        <a class="link-item" href="https://github.com/dust765/ClassicUO/releases" target="_blank" rel="noopener">
          <span class="li-icon">📦</span><span>Release Notes</span>
        </a>
        <div style="margin-top:1.5rem;padding-top:1.25rem;border-top:1px solid var(--border)">
          <p style="font-size:.85rem;color:var(--text-dim);font-style:italic">
            "Innovation doesn't come from cliques, but from true collaboration."
          </p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ── FOOTER ────────────────────────────────────────────────── -->
<footer>
  <img src="logodust.png" alt="Dust765" />
  <div class="footer-social">
    <a href="https://github.com/dust765/ClassicUO" target="_blank" rel="noopener" aria-label="GitHub">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" aria-hidden="true"><path d="M12 0C5.37 0 0 5.37 0 12c0 5.31 3.435 9.795 8.205 11.385.6.105.825-.255.825-.57 0-.285-.015-1.23-.015-2.235-3.015.555-3.795-.735-4.035-1.41-.135-.345-.72-1.41-1.23-1.695-.42-.225-1.02-.78-.015-.795.945-.015 1.62.87 1.845 1.23 1.08 1.815 2.805 1.305 3.495.99.105-.78.42-1.305.765-1.605-2.67-.3-5.46-1.335-5.46-5.925 0-1.305.465-2.385 1.23-3.225-.12-.3-.54-1.53.12-3.18 0 0 1.005-.315 3.3 1.23.96-.27 1.98-.405 3-.405s2.04.135 3 .405c2.295-1.56 3.3-1.23 3.3-1.23.66 1.65.24 2.88.12 3.18.765.84 1.23 1.905 1.23 3.225 0 4.605-2.805 5.625-5.475 5.925.435.375.81 1.095.81 2.22 0 1.605-.015 2.895-.015 3.3 0 .315.225.69.825.57A12.02 12.02 0 0 0 24 12c0-6.63-5.37-12-12-12z"/></svg>
    </a>
    <a href="https://discord.gg/9Vh7aqqX" target="_blank" rel="noopener" aria-label="Discord">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" aria-hidden="true"><path d="M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057c.002.022.015.043.032.054a19.9 19.9 0 0 0 5.993 3.03.077.077 0 0 0 .084-.028 14.09 14.09 0 0 0 1.226-1.994.076.076 0 0 0-.041-.106 13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.928 1.793 8.18 1.793 12.062 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.892.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.03zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z"/></svg>
    </a>
  </div>
  <div class="footer-links">
    <a href="#about">About</a>
    <a href="#features">Features</a>
    <a href="#screenshots">Screenshots</a>
    <a href="#install">Install</a>
    <a href="#contribute">Contribute</a>
    <a href="https://github.com/dust765/ClassicUO" target="_blank" rel="noopener">GitHub</a>
    <a href="https://discord.gg/9Vh7aqqX" target="_blank" rel="noopener">Discord</a>
    <a href="https://github.com/dust765/ClassicUO/wiki" target="_blank" rel="noopener">Wiki</a>
  </div>
  <p class="footer-copy">© Dust765 Project — MIT License</p>
  <p class="footer-credits">
    Built on <a href="https://github.com/andreakarasho/ClassicUO" target="_blank" rel="noopener" style="color:inherit">ClassicUO</a> by andreakarasho ·
    Powered by <a href="https://github.com/FNA-XNA/FNA" target="_blank" rel="noopener" style="color:inherit">FNA</a> ·
    7 Link · 6 Gaechti · 5 Syrupz · jsebold666
  </p>
</footer>

<!-- ── LIGHTBOX ───────────────────────────────────────────────── -->
<div id="lightbox" class="lightbox" role="dialog" aria-modal="true" aria-label="Screenshot viewer">
  <div class="lightbox-backdrop" id="lightboxBackdrop"></div>
  <button class="lightbox-close" id="lightboxClose" aria-label="Close">✕</button>
  <button class="lightbox-prev" id="lightboxPrev" aria-label="Previous">&#8249;</button>
  <img class="lightbox-img" id="lightboxImg" src="" alt="" />
  <button class="lightbox-next" id="lightboxNext" aria-label="Next">&#8250;</button>
</div>
```

- [ ] **Step 2: Verify page renders** — open `index.html` in browser. All sections visible, no console errors, layout correct.

- [ ] **Step 3: Commit**
```bash
cd "D:/workspace/2026/Dust765-Site"
git add index.html
git commit -m "feat: complete HTML rewrite — all sections, slider markup, video placeholder, lightbox"
```

---

## Task 3: JavaScript — All interactive behaviors

**Files:**
- Modify: `D:/workspace/2026/Dust765-Site/index.html`

Replace the existing `<script>` block (everything between `<script>` and `</script>` at the bottom of `<body>`) with:

- [ ] **Step 1: Replace the `<script>` block** with:

```js
/* ── Tab switching (install section) ─────────────────────── */
function showTab(id) {
  document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
  document.getElementById('tab-' + id).classList.add('active');
  event.currentTarget.classList.add('active');
}

/* ── Particle Canvas ─────────────────────────────────────── */
(function initParticles() {
  const canvas = document.getElementById('particles');
  const hero   = canvas.parentElement;
  const ctx    = canvas.getContext('2d');
  let W, H, particles, raf;

  function resize() {
    W = canvas.width  = hero.offsetWidth;
    H = canvas.height = hero.offsetHeight;
  }

  function makeParticle() {
    return {
      x:  Math.random() * W,
      y:  Math.random() * H,
      vx: (Math.random() - 0.5) * 0.6,
      vy: -(Math.random() * 0.3 + 0.1),
      r:  Math.random() * 2 + 1,
      a:  Math.random() * 0.25 + 0.15
    };
  }

  function init() {
    resize();
    particles = Array.from({ length: 80 }, makeParticle);
  }

  function draw() {
    ctx.clearRect(0, 0, W, H);
    particles.forEach(p => {
      p.x += p.vx;
      p.y += p.vy;
      if (p.x < 0) p.x = W;
      if (p.x > W) p.x = 0;
      if (p.y < -5) { p.y = H + 5; p.x = Math.random() * W; }
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(180,30,30,${p.a})`;
      ctx.fill();
    });
    raf = requestAnimationFrame(draw);
  }

  // Pause when hero not visible (perf)
  const heroObs = new IntersectionObserver(([e]) => {
    if (e.isIntersecting) { if (!raf) draw(); }
    else { cancelAnimationFrame(raf); raf = null; }
  });
  heroObs.observe(hero);

  window.addEventListener('resize', resize);
  init();
  draw();
})();

/* ── Scroll Reveal ────────────────────────────────────────── */
(function initReveal() {
  const observer = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('visible');
        observer.unobserve(e.target);
      }
    });
  }, { threshold: 0.12 });
  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
})();

/* ── Active Nav Link ──────────────────────────────────────── */
(function initActiveNav() {
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('nav .nav-link');

  function setActive(id) {
    navLinks.forEach(a => {
      a.classList.toggle('nav-active', a.getAttribute('href') === '#' + id);
    });
  }

  const observer = new IntersectionObserver(entries => {
    entries.forEach(e => { if (e.isIntersecting) setActive(e.target.id); });
  }, { threshold: 0.4 });

  sections.forEach(s => observer.observe(s));
  setActive('home'); // default on load
})();

/* ── Navbar scroll opacity ────────────────────────────────── */
(function initNavScroll() {
  const nav = document.querySelector('nav');
  window.addEventListener('scroll', () => {
    const scrolled = scrollY > 40;
    nav.style.background = scrolled ? 'rgba(14,8,8,.97)' : 'rgba(14,8,8,.92)';
    nav.style.borderBottomColor = scrolled ? 'rgba(180,30,30,.45)' : 'rgba(180,30,30,.25)';
  }, { passive: true });
})();

/* ── Hamburger drawer — close on link click ───────────────── */
(function initDrawer() {
  document.querySelectorAll('.nav-drawer-link').forEach(a => {
    a.addEventListener('click', () => {
      document.getElementById('nav-toggle').checked = false;
    });
  });
})();

/* ── Slider ──────────────────────────────────────────────── */
(function initSlider() {
  const slider    = document.getElementById('mainSlider');
  const slides    = slider.querySelectorAll('.slide');
  const dotsEl    = document.getElementById('sliderDots');
  const imgs      = slider.querySelectorAll('.slide img');
  let current     = 0;
  let autoplayId  = null;
  let dots        = [];

  // Build dots
  slides.forEach((_, i) => {
    const btn = document.createElement('button');
    btn.className = 'dot' + (i === 0 ? ' active' : '');
    btn.setAttribute('aria-label', 'Go to slide ' + (i + 1));
    btn.addEventListener('click', () => goTo(i));
    dotsEl.appendChild(btn);
    dots.push(btn);
  });

  function goTo(n) {
    slides[current].classList.remove('active');
    const prevDot = dots[current];
    prevDot.classList.remove('active');
    prevDot.offsetWidth; // force reflow to restart CSS animation
    current = ((n % slides.length) + slides.length) % slides.length;
    slides[current].classList.add('active');
    dots[current].classList.add('active');
    resetAutoplay();
  }

  function resetAutoplay() {
    clearInterval(autoplayId);
    autoplayId = setInterval(() => goTo(current + 1), 4000);
  }

  slider.querySelector('.slider-prev').addEventListener('click', () => goTo(current - 1));
  slider.querySelector('.slider-next').addEventListener('click', () => goTo(current + 1));

  slider.addEventListener('mouseenter', () => clearInterval(autoplayId));
  slider.addEventListener('mouseleave', () => resetAutoplay());

  // Open lightbox on image click
  imgs.forEach((img, i) => img.addEventListener('click', () => openLightbox(i)));

  resetAutoplay();

  // expose goTo for lightbox sync
  window._sliderGoTo = goTo;
  window._sliderCurrent = () => current;
})();

/* ── Lightbox ────────────────────────────────────────────── */
(function initLightbox() {
  const lightbox  = document.getElementById('lightbox');
  const lbImg     = document.getElementById('lightboxImg');
  const lbClose   = document.getElementById('lightboxClose');
  const lbPrev    = document.getElementById('lightboxPrev');
  const lbNext    = document.getElementById('lightboxNext');
  const backdrop  = document.getElementById('lightboxBackdrop');

  const allImgs = Array.from(
    document.querySelectorAll('#mainSlider .slide img')
  );
  let lbIndex = 0;

  function openLightbox(i) {
    lbIndex = i;
    lbImg.src = allImgs[i].src;
    lbImg.alt = allImgs[i].alt;
    lightbox.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  function closeLightbox() {
    lightbox.classList.remove('open');
    document.body.style.overflow = '';
  }

  function lbGoTo(n) {
    lbIndex = ((n % allImgs.length) + allImgs.length) % allImgs.length;
    lbImg.src = allImgs[lbIndex].src;
    lbImg.alt = allImgs[lbIndex].alt;
    // Sync main slider
    if (window._sliderGoTo) window._sliderGoTo(lbIndex);
  }

  lbClose.addEventListener('click', closeLightbox);
  backdrop.addEventListener('click', closeLightbox);
  lbPrev.addEventListener('click', () => lbGoTo(lbIndex - 1));
  lbNext.addEventListener('click', () => lbGoTo(lbIndex + 1));

  document.addEventListener('keydown', e => {
    if (!lightbox.classList.contains('open')) return;
    if (e.key === 'Escape')     closeLightbox();
    if (e.key === 'ArrowLeft')  lbGoTo(lbIndex - 1);
    if (e.key === 'ArrowRight') lbGoTo(lbIndex + 1);
  });

  // expose openLightbox so slider can call it
  window.openLightbox = openLightbox;
})();

/* ── Video placeholder ───────────────────────────────────── */
function loadVideo() {
  const placeholder = document.getElementById('videoPlaceholder');
  const wrapper = placeholder.parentElement;
  wrapper.innerHTML = `<iframe
    src="https://www.youtube.com/embed/YOUR_VIDEO_ID?autoplay=1&rel=0"
    allow="autoplay; fullscreen; picture-in-picture"
    allowfullscreen
    style="width:100%;aspect-ratio:16/9;border:1px solid var(--border);border-radius:4px;display:block;"
  ></iframe>`;
}
```

- [ ] **Step 2: Verify particles** — hero should show animated red particles floating upward.

- [ ] **Step 3: Verify slider** — auto-advances every 4s, arrows work, dots fill, hover pauses.

- [ ] **Step 4: Verify lightbox** — click a slide image → overlay opens, ESC closes, arrows navigate, syncs slider.

- [ ] **Step 5: Verify scroll-reveal** — scroll down slowly, elements fade-up as they enter viewport.

- [ ] **Step 6: Verify nav active** — scroll through sections, nav link for current section highlights red.

- [ ] **Step 7: Verify hamburger (resize to <860px)** — hamburger appears, click opens drawer, click link closes it.

- [ ] **Step 8: Verify video** — click play button → placeholder replaced by iframe (note: autoplay needs video ID to be set).

- [ ] **Step 9: Check console** — no errors in browser devtools.

- [ ] **Step 10: Commit**
```bash
cd "D:/workspace/2026/Dust765-Site"
git add index.html
git commit -m "feat: add all JS — particles, slider, lightbox, scroll-reveal, active nav, hamburger, video"
```

---

## Verification Checklist

- [ ] Hero: particles animate, headline fades in sequentially
- [ ] Nav: GitHub + Discord icons render, active section link highlights, scroll opacity changes
- [ ] Slider: 4s autoplay, pause on hover, arrows + dots work, dot progress restarts on manual nav
- [ ] Lightbox: opens on image click, closes on ESC/backdrop, prev/next syncs with slider
- [ ] Features: glassmorphism cards with blur visible in browser
- [ ] Scroll-reveal: all `.reveal` elements animate on scroll (once only)
- [ ] Video: placeholder renders, click loads iframe
- [ ] Mobile (<860px): hamburger works, drawer opens/closes, layout single-column
- [ ] Footer: GitHub + Discord SVG icons clickable
- [ ] No console errors
