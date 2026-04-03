# Spec: Dust765 Site — Senior UX Redesign

**Date:** 2026-04-03  
**File to modify:** `index.html` (single-file site, vanilla HTML/CSS/JS, zero external dependencies)

---

## Context

The current site is functional but lacks visual impact. The goal is a senior-level UX overhaul that reflects the identity of Dust765: a PvP-focused, FNA-powered, cross-platform Ultima Online client. The redesign adds animations, a screenshot slider with lightbox, a video section, proper social icons, and scroll-reveal effects — all without introducing any external JS or CSS libraries.

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

**Behavior:**
- Background blur increases opacity on scroll: `rgba(14,8,8,.85)` → `rgba(14,8,8,.97)`
- Active nav link: `IntersectionObserver` on each `<section>` sets `data-active` on the matching `<a>`, styled with `color: var(--red-300)`
- GitHub icon: links to `https://github.com/dust765/ClassicUO` (SVG octicon, 20×20)
- Discord icon: links to `https://discord.gg/9Vh7aqqX` (SVG Discord logo, 20×20)
- Mobile (<860px): hamburger toggle (CSS checkbox trick), drawer slides in from right

---

## 2. Hero

**Layers (bottom → top):**
1. `<canvas id="particles">` — ~80 circular particles, `rgba(180,30,30,0.15–0.4)`, random position/velocity/size, looped `requestAnimationFrame`
2. Radial gradient `rgba(80,10,10,.55)` + linear gradient (existing)
3. Decorative grid (existing `::after`)
4. Content

**Entry animation sequence (CSS `@keyframes fadeUp`):**
| Element | Delay |
|---------|-------|
| Badge | 0.0s |
| Logo | 0.3s |
| Title | 0.7s |
| Subtitle | 1.0s |
| Buttons | 1.3s |

**Headline:**
```
Built for PvP.
Powered by FNA.
```

**Subtitle:**
```
Dust765 is a ClassicUO fork built for serious Ultima Online players —
fast, cross-platform, and packed with PvP features. No drama. Just UO.
```

**Buttons:**
- `[Download Now]` — primary red
- `[View on GitHub]` — outline
- GitHub SVG icon button
- Discord SVG icon button

---

## 3. About

No structural change. Adds `.reveal` class to text blocks and stat-cards for scroll-reveal cascade.

---

## 4. Features

Cards get glassmorphism treatment:
```css
background: rgba(30, 8, 8, 0.55);
backdrop-filter: blur(12px);
border: 1px solid rgba(180, 30, 30, 0.2);
box-shadow: 0 4px 24px rgba(0,0,0,.4), inset 0 1px 0 rgba(255,80,80,.06);
```

Each card gets `.reveal` + incremental `transition-delay` (0, 0.08s, 0.16s…).

---

## 5. Client Graphics — Slider

**Markup:**
```html
<div class="slider">
  <div class="slides-track">
    <div class="slide active"><img ...><div class="slide-caption">Login Screen</div></div>
    <div class="slide"><img ...><div class="slide-caption">Character Selection</div></div>
    <div class="slide"><img ...><div class="slide-caption">Character Creation</div></div>
    <div class="slide"><img ...><div class="slide-caption">Options Menu</div></div>
  </div>
  <button class="slider-prev">‹</button>
  <button class="slider-next">›</button>
  <div class="slider-dots">...</div>
</div>
```

**Image source:** GitHub raw
- `https://raw.githubusercontent.com/dust765/ClassicUO/developer/docs/login.png`
- `https://raw.githubusercontent.com/dust765/ClassicUO/developer/docs/selectcharacter.png`
- `https://raw.githubusercontent.com/dust765/ClassicUO/developer/docs/create.png`
- `https://raw.githubusercontent.com/dust765/ClassicUO/developer/docs/options.png`

**Behavior:**
- Slides use `opacity` + `position: absolute` for cross-fade transition (no layout shift)
- Autoplay: 4s interval, `clearInterval` on `mouseenter`, restart on `mouseleave`
- Active dot has a CSS progress bar animation (`@keyframes dotProgress`) that fills over 4s
- Click on image → open lightbox (`<div id="lightbox">`) with `<img>`, prev/next buttons, close button
- Lightbox: close on `Esc` keydown or click on overlay backdrop
- `loading="lazy"` on all images

---

## 6. Video

**Markup:**
```html
<div class="video-placeholder" id="videoPlaceholder" onclick="loadVideo()">
  <div class="video-bg-overlay"></div>
  <div class="play-btn"><svg ...play icon...></svg></div>
  <p class="video-label">Watch Gameplay</p>
  <p class="video-sub">See Dust765 in action — PvP showcase</p>
</div>
```

**Behavior:**
- `loadVideo()` replaces the div with:
  `<iframe src="https://www.youtube.com/embed/VIDEO_ID?autoplay=1" ...>`
- Placeholder uses `aspect-ratio: 16/9`, `max-width: 900px`, centered
- Background: dark gradient + subtle logo watermark (low-opacity logodust.png)
- Border: `1px solid var(--border)` with red glow on hover

---

## 7. Scroll-Reveal System

```css
.reveal { opacity: 0; transform: translateY(28px); transition: opacity .55s ease, transform .55s ease; }
.reveal.visible { opacity: 1; transform: none; }
```

```js
const io = new IntersectionObserver(entries => {
  entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); io.unobserve(e.target); } });
}, { threshold: 0.12 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));
```

Applied to: `.feat-card`, `.stat-card`, `.c-step`, `.dl-card`, `.section-title`, `.section-body`, `.about-quote`.

---

## 8. Footer

```
[Logo]
[GitHub SVG]  [Discord SVG]

About · Screenshots · Features · Install · Contribute · GitHub · Discord · Wiki

© Dust765 — MIT License
Built on ClassicUO by andreakarasho · FNA · 7 Link · 6 Gaechti · 5 Syrupz · jsebold666
```

Social icons: 24×24, `color: var(--text-dim)`, hover `color: var(--red-300)`.

---

## 9. Mobile / Responsive

| Breakpoint | Change |
|-----------|--------|
| ≤860px | Nav links hidden, hamburger shown; grids → 1 col |
| ≤660px | Slider maintains aspect ratio; video full-width |
| ≤560px | Features grid → 1 col |

---

## Verification

1. Open `index.html` in browser (no server needed)
2. Hero: particles animate, headline fades in sequentially
3. Scroll down: `.reveal` elements fade up as they enter viewport
4. Slider: auto-advances every 4s, pauses on hover, arrows/dots work, lightbox opens/closes
5. Video: click play → iframe loads with `autoplay=1`
6. Nav: active section link is highlighted as you scroll
7. GitHub/Discord icons in nav and footer are clickable
8. Mobile: hamburger opens drawer, slider is touch-friendly (swipe not required but layout holds)
