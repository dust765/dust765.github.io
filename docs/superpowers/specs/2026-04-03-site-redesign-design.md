# Spec: Dust765 Site — Senior UX Redesign

**Date:** 2026-04-03  
**File to modify:** `index.html` (single-file site, vanilla HTML/CSS/JS)  
**External deps:** Google Fonts CDN (already present, retained). Zero new JS/CSS libraries introduced.

---

## Context

The current site is functional but lacks visual impact. The goal is a senior-level UX overhaul that reflects the identity of Dust765: a PvP-focused, FNA-powered, cross-platform Ultima Online client. The redesign adds animations, a screenshot slider with lightbox, a video section, proper social icons, and scroll-reveal effects — all without introducing any new JS or CSS libraries.

---

## Section Order

```
NAV (fixed)
Hero
About
Features
Client Graphics (slider)
Video
Install
Download
Contribute
Footer
```

---

## 1. Navbar

**Layout:**
```
[Logo + "Dust765"]   About · Screenshots · Features · Install   [GitHub SVG] [Discord SVG] [Download btn]
```

**Scroll opacity:** `background` transitions from `rgba(14,8,8,.85)` to `rgba(14,8,8,.97)` when `scrollY > 40` (JS event listener on `scroll`, already partially present).

**Active nav link:**
- Each `<section>` with an `id` is observed by a shared `IntersectionObserver` (threshold: 0.4).
- On intersection, the corresponding `<a href="#id">` in the navbar gets class `.nav-active`; the previously active link has `.nav-active` removed.
- Initial state on page load: the link for `#home` (Hero) gets `.nav-active` by default via HTML `class`.
- CSS: `nav a.nav-active { color: var(--red-300); }`

**Social icons (SVG inline):**
- GitHub octicon SVG, 20×20, `aria-label="GitHub"`, links to `https://github.com/dust765/ClassicUO`
- Discord SVG logo, 20×20, `aria-label="Discord"`, links to `https://discord.gg/9Vh7aqqX`
- Both styled: `color: var(--text-dim); transition: color .2s;` → hover `color: var(--red-200)`

**Mobile (<860px) — hamburger:**

Markup pattern:
```html
<input type="checkbox" id="nav-toggle" class="nav-toggle-input" />
<label for="nav-toggle" class="nav-hamburger" aria-label="Menu">
  <span></span><span></span><span></span>
</label>
<div class="nav-drawer">
  <ul>...links...</ul>
</div>
```

- `.nav-toggle-input` is `position:absolute; opacity:0; pointer-events:none`
- `.nav-drawer`: `position:fixed; top:60px; right:0; width:260px; height:calc(100vh - 60px); background:rgba(14,8,8,.97); transform:translateX(100%); transition:transform .3s ease; z-index:99; padding:2rem`
- `#nav-toggle:checked ~ .nav-drawer { transform: translateX(0); }`
- Clicking any link inside drawer: JS adds `document.getElementById('nav-toggle').checked = false` to close drawer
- `.nav-hamburger` 3 spans: 2px height, 20px width, `background:var(--text)`, gap `.35rem`, transitions to X when checked (CSS `transform`)

---

## 2. Hero

**Z-index stack (bottom → top):**
| Layer | z-index |
|-------|---------|
| `<canvas id="particles">` | -2 |
| `.hero-bg` (radial + grid) | -1 |
| Hero content | 0 (flow) |

**Canvas particles (`<canvas id="particles" style="position:absolute;inset:0;z-index:-2">`):**
- Sized to `canvas.width = hero.offsetWidth`, `canvas.height = hero.offsetHeight`; resized on `window.resize`
- 80 particles, each: `x`, `y` (random), `vx` (±0.3), `vy` (-0.1 to -0.4), `r` (1–3px), `alpha` (0.15–0.4)
- Each frame: update position, wrap at edges, draw `arc` with `rgba(180,30,30,alpha)`
- Loop via `requestAnimationFrame`; stopped with `cancelAnimationFrame` if section not visible (performance)

**Entry animation — CSS `@keyframes fadeUp`:**
```css
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(20px); }
  to   { opacity: 1; transform: none; }
}
```
Applied with `animation: fadeUp .7s ease both`:

| Element | `animation-delay` |
|---------|------------------|
| `.hero-badge` | 0s |
| `.hero-logo` | 0.3s |
| `.hero-title` | 0.7s |
| `.hero-sub` | 1.0s |
| `.hero-actions` | 1.3s |

**Headline:**
```
Built for PvP.
Powered by FNA.
```

**Subtitle:**
```
Dust765 is a ClassicUO fork built for serious Ultima Online players —
fast, cross-platform, and packed with combat features. No drama. Just UO.
```

**Buttons row:**
```html
<a class="btn-primary" href="#download">Download Now</a>
<a class="btn-outline" href="https://github.com/dust765/ClassicUO">View on GitHub</a>
<a class="btn-icon" href="https://github.com/dust765/ClassicUO" aria-label="GitHub">[GH SVG]</a>
<a class="btn-icon" href="https://discord.gg/9Vh7aqqX" aria-label="Discord">[Discord SVG]</a>
```

---

## 3. About

No structural change to existing markup. Add class `.reveal` to:
- `.section-label` (first child of the left column `<div>`)
- `.section-title`
- `.section-body` (both paragraphs, each independently)
- `.about-quote`
- Each `.stat-card` individually

---

## 4. Features

**Glassmorphism card style (replaces existing `.feat-card` background/border):**
```css
.feat-card {
  background: rgba(30, 8, 8, 0.55);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(180, 30, 30, 0.2);
  box-shadow: 0 4px 24px rgba(0,0,0,.4), inset 0 1px 0 rgba(255,80,80,.06);
}
```

Hover (keep existing `translateY(-4px)` + red border), add: `box-shadow: 0 12px 40px rgba(150,20,20,.3)`.

Each `.feat-card` gets class `.reveal` + inline `style="transition-delay: Xs"` where X = 0, 0.08, 0.16, 0.24, 0.32, 0.40, 0.48, 0.56, 0.64 for 9 cards.

---

## 5. Client Graphics — Slider

**HTML structure:**
```html
<section id="screenshots">
  <div class="container">
    <div class="screenshots-header reveal">...</div>
    <div class="slider" id="mainSlider">
      <div class="slider-track">
        <div class="slide active">
          <img src="...login.png" alt="Login Screen" loading="eager" />
          <div class="slide-caption">Login Screen</div>
        </div>
        <div class="slide">
          <img src="...selectcharacter.png" alt="Character Selection" loading="lazy" />
          <div class="slide-caption">Character Selection</div>
        </div>
        <div class="slide">
          <img src="...create.png" alt="Character Creation" loading="lazy" />
          <div class="slide-caption">Character Creation</div>
        </div>
        <div class="slide">
          <img src="...options.png" alt="Options Menu" loading="lazy" />
          <div class="slide-caption">Options Menu</div>
        </div>
      </div>
      <button class="slider-btn slider-prev" aria-label="Previous">&#8249;</button>
      <button class="slider-btn slider-next" aria-label="Next">&#8250;</button>
      <div class="slider-dots" id="sliderDots"></div>
    </div>
  </div>
</section>
```

**CSS — cross-fade (no height collapse):**
```css
.slider { position: relative; }
.slider-track {
  position: relative;
  aspect-ratio: 16 / 9;   /* fixes height — track is always 16:9 */
  overflow: hidden;
  border-radius: 4px;
  border: 1px solid var(--border);
}
.slide {
  position: absolute; inset: 0;
  opacity: 0;
  transition: opacity .5s ease;
  pointer-events: none;
}
.slide.active {
  opacity: 1;
  pointer-events: auto;
}
.slide img {
  width: 100%; height: 100%;
  object-fit: cover; object-position: top;
  display: block;
  cursor: zoom-in;
}
.slide-caption {
  position: absolute; bottom: 0; left: 0; right: 0;
  background: linear-gradient(transparent, rgba(0,0,0,.7));
  padding: 1.5rem 1rem .75rem;
  font-family: 'Cinzel', serif;
  font-size: .75rem; letter-spacing: .12em; text-transform: uppercase;
  color: var(--text-dim);
}
```

**Dots:**
- Generated by JS: one `<button>` per slide, `.dot`, `.dot.active`
- Active dot has `::after` pseudo with `@keyframes dotFill`: `width: 0% → 100%` over 4s
- On navigation: to restart animation, remove class `.active` from dot, force reflow (`dot.offsetWidth`), re-add `.active`

**JS slider logic (`sliderInit()`):**
```
currentIndex = 0
slides = querySelectorAll('.slide')
dots = []

function goTo(n):
  slides[currentIndex].classList.remove('active')
  dots[currentIndex].classList.remove('active')
  dots[currentIndex].offsetWidth  // reflow to restart CSS animation
  currentIndex = (n + slides.length) % slides.length
  slides[currentIndex].classList.add('active')
  dots[currentIndex].classList.add('active')
  resetAutoplay()

autoplay = setInterval(() => goTo(currentIndex + 1), 4000)
slider.addEventListener('mouseenter', () => clearInterval(autoplay))
slider.addEventListener('mouseleave', () => autoplay = setInterval(...))

prev btn → goTo(currentIndex - 1)
next btn → goTo(currentIndex + 1)
each img.click → openLightbox(currentIndex)
```

**Lightbox:**
```html
<div id="lightbox" class="lightbox" role="dialog" aria-modal="true">
  <div class="lightbox-backdrop"></div>
  <button class="lightbox-close" aria-label="Close">✕</button>
  <button class="lightbox-prev" aria-label="Previous">&#8249;</button>
  <img class="lightbox-img" src="" alt="" />
  <button class="lightbox-next" aria-label="Next">&#8250;</button>
</div>
```

```css
.lightbox {
  position: fixed; inset: 0;
  z-index: 200;  /* above nav z-index:100 */
  display: flex; align-items: center; justify-content: center;
  opacity: 0; pointer-events: none;
  transition: opacity .25s;
}
.lightbox.open { opacity: 1; pointer-events: auto; }
.lightbox-backdrop {
  position: absolute; inset: 0;
  background: rgba(0,0,0,.88);
}
.lightbox-img {
  position: relative; z-index: 1;
  max-width: 90vw; max-height: 85vh;
  border: 1px solid var(--red-700);
  border-radius: 4px;
}
```

- `openLightbox(index)`: sets `lightbox-img.src`, shares same index as slider, calls `lightbox.classList.add('open')`
- Lightbox prev/next: updates `lightboxIndex`, updates `lightbox-img.src` AND advances `mainSlider` to same index (shared state)
- Close: click backdrop or `.lightbox-close` or `Esc` keydown → `lightbox.classList.remove('open')`

---

## 6. Video Section

**HTML:**
```html
<section id="video">
  <div class="container">
    <div class="video-header reveal">
      <p class="section-label">Gameplay</p>
      <h2 class="section-title">See It in Action</h2>
    </div>
    <div class="video-wrapper reveal">
      <div class="video-placeholder" id="videoPlaceholder">
        <div class="video-bg">
          <!-- low-opacity logodust.png as watermark via CSS background-image -->
        </div>
        <button class="video-play-btn" onclick="loadVideo()" aria-label="Play video">
          <svg ...play triangle SVG...></svg>
        </button>
        <p class="video-label">Watch Gameplay</p>
        <p class="video-sub">See Dust765 in action — PvP showcase</p>
      </div>
    </div>
  </div>
</section>
```

**CSS:**
```css
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
  box-shadow: 0 0 40px rgba(150,20,20,.3);
}
.video-bg {
  position: absolute; inset: 0;
  background: url('logodust.png') center/30% no-repeat;
  opacity: .06;
  filter: grayscale(1);
}
.video-play-btn {
  width: 72px; height: 72px;
  border-radius: 50%;
  background: var(--red-600);
  border: 2px solid var(--red-400);
  display: flex; align-items: center; justify-content: center;
  cursor: pointer;
  transition: transform .2s, background .2s;
  margin-bottom: 1rem;
  position: relative; z-index: 1;
}
.video-play-btn:hover { transform: scale(1.1); background: var(--red-500); }
```

**JS `loadVideo()`:**
```js
function loadVideo() {
  const placeholder = document.getElementById('videoPlaceholder');
  const wrapper = placeholder.parentElement;
  // Replace placeholder with iframe
  wrapper.innerHTML = `
    <iframe
      src="https://www.youtube.com/embed/YOUR_VIDEO_ID?autoplay=1&rel=0"
      allow="autoplay; fullscreen; picture-in-picture"
      allowfullscreen
      style="width:100%;aspect-ratio:16/9;border:1px solid var(--border);border-radius:4px;"
    ></iframe>`;
}
```

Note: `YOUR_VIDEO_ID` is a placeholder — replace with the actual YouTube video ID when available.

---

## 7. Scroll-Reveal System

```css
.reveal {
  opacity: 0;
  transform: translateY(28px);
  transition: opacity .55s ease, transform .55s ease;
}
.reveal.visible {
  opacity: 1;
  transform: none;
}
```

```js
const revealObserver = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('visible');
      revealObserver.unobserve(e.target);
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));
```

**Elements with `.reveal`** (exhaustive list):
- `#about`: `.section-label`, `.section-title`, `.section-body` (×2), `.about-quote`, each `.stat-card`
- `#features`: `.features-header`, each `.feat-card` (with `transition-delay`)
- `#screenshots`: `.screenshots-header`
- `#video`: `.video-header`, `.video-wrapper`
- `#install`: `.section-label`, `.section-title`, `.section-body`
- `#download`: `.section-label`, `.section-title`, `.section-body`, each `.dl-card`
- `#contribute`: `.section-label`, `.section-title`, `.section-body`, each `.c-step`

---

## 8. Footer

```html
<footer>
  <img src="logodust.png" alt="Dust765" />
  <div class="footer-social">
    <a href="https://github.com/dust765/ClassicUO" aria-label="GitHub">[GH SVG 24×24]</a>
    <a href="https://discord.gg/9Vh7aqqX" aria-label="Discord">[Discord SVG 24×24]</a>
  </div>
  <div class="footer-links">...</div>
  <p class="footer-copy">© Dust765 — MIT License</p>
  <p class="footer-credits">Built on ClassicUO by andreakarasho · FNA · ...</p>
</footer>
```

`.footer-social a`: `color: var(--text-dim)` → hover `color: var(--red-300)`, `transition: color .2s`.

---

## 9. Z-index Stack

| Element | z-index |
|---------|---------|
| `canvas#particles` | -2 (absolute within hero) |
| `.hero-bg` | -1 |
| `nav` | 100 |
| `.nav-drawer` | 99 |
| `#lightbox` | 200 |

---

## 10. Mobile / Responsive

| Breakpoint | Change |
|-----------|--------|
| ≤860px | Nav links hidden, hamburger shown; `.about-grid`, `.install-grid`, `.contribute-grid` → 1 col |
| ≤660px | `.slider-track` maintains `aspect-ratio: 16/9` naturally; video full-width |
| ≤560px | `.features-grid` → 1 col |

---

## Verification

1. Open `index.html` directly in browser (no server needed for static assets)
2. **Hero:** particles animate, elements fade-up sequentially on load
3. **Scroll:** `.reveal` elements animate in as they enter viewport (no repeat)
4. **Nav active:** scrolling highlights the current section's nav link
5. **Slider:** auto-advances every 4s, pauses on hover, setas and dots functional, dot progress bar restarts on navigation
6. **Lightbox:** click image → overlay opens; ESC / backdrop click closes; prev/next syncs with slider index
7. **Video:** click play button → iframe replaces placeholder with `autoplay=1`; `allow="autoplay"` attribute present
8. **Social icons:** GitHub and Discord SVGs render and link correctly in nav and footer
9. **Mobile:** hamburger opens drawer; clicking a nav link inside drawer closes it
10. **No console errors** in devtools
