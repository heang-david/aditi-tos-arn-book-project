<template>
  <section class="hero">

    <!-- background blobs -->
    <div class="hero-blob blob-1"></div>
    <div class="hero-blob blob-2"></div>
    <div class="hero-blob blob-3"></div>

    <!-- left column -->
    <div class="hero-content">
      <div class="hero-eyebrow">
        <span class="eyebrow-dot"></span>
        Welcome to Tos arn Book Store
      </div>

      <h1 class="hero-title">
        The right book,<br />
        found at the<br />
        <em class="hero-title-accent">right moment.</em>
      </h1>

      <p class="hero-sub">
        Forty thousand titles curated by readers, for readers.
        Whether you know exactly what you want or haven't a clue —
        you'll leave with something you'll love.
      </p>

      <div class="hero-actions">
        <a href="/products" class="btn-primary">Browse Books</a>
        <a href="#categories" class="btn-ghost">Explore Categories</a>
      </div>

      <div class="hero-trust">
        <div class="trust-item">
          <strong>40,000+</strong>
          <span>Titles in stock</span>
        </div>
        <div class="trust-divider"></div>
        <div class="trust-item">
          <strong>98%</strong>
          <span>Happy readers</span>
        </div>
        <div class="trust-divider"></div>
        <div class="trust-item">
          <strong>Est. 2018</strong>
          <span>Phnom Penh</span>
        </div>
      </div>
    </div>

    <!-- right column — stacked book art -->
    <div class="hero-visual" aria-hidden="true">
      <div class="book-stack">
        <div
          v-for="(book, i) in stackBooks"
          :key="book.id"
          class="stack-book"
          :style="{
            background: book.color,
            transform: `rotate(${book.rotate}deg) translateX(${book.offsetX}px)`,
            height: book.height + 'px',
            animationDelay: i * 0.12 + 's'
          }"
        >
          <div class="stack-book-spine">
            <span class="stack-title">{{ book.title }}</span>
            <span class="stack-author">{{ book.author }}</span>
          </div>
          <div class="stack-book-cover" :style="{ background: book.coverColor }">
            <div class="cover-pattern"></div>
          </div>
        </div>

        <!-- shadow -->
        <div class="stack-shadow"></div>
      </div>

      <!-- floating badge -->
      <div class="hero-badge">
        <div class="badge-inner">
          <span class="badge-icon">✦</span>
          <span class="badge-text">New arrivals<br/>every week</span>
        </div>
      </div>
    </div>

    <!-- scroll cue -->
    <div class="hero-scroll">
      <span>Scroll</span>
      <div class="scroll-track">
        <div class="scroll-thumb"></div>
      </div>
    </div>

  </section>
</template>

<script>
export default {
  name: 'HeroSection',
  data() {
    return {
      stackBooks: [
        { id: 1, title: 'Pachinko',         author: 'Min Jin Lee',   color: '#2C4770', coverColor: '#1A2F50', height: 220, rotate: -6,  offsetX: -24 },
        { id: 2, title: 'Circe',            author: 'M. Miller',     color: '#7A9E7E', coverColor: '#5A7E5E', height: 200, rotate:  3,  offsetX:  8  },
        { id: 3, title: 'Educated',         author: 'T. Westover',   color: '#C9A84C', coverColor: '#A88830', height: 210, rotate: -2,  offsetX: -4  },
        { id: 4, title: 'The Master',       author: 'Bulgakov',      color: '#8B4B62', coverColor: '#6B2B42', height: 230, rotate:  7,  offsetX:  18 },
        { id: 5, title: 'Invisible Cities', author: 'Calvino',       color: '#4A7C8E', coverColor: '#2A5C6E', height: 195, rotate: -4,  offsetX: -12 },
      ],
    }
  },
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Inter:wght@300;400;500;600&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

.hero {
  position: relative;
  min-height: 100vh;
  background: #1A2233;
  display: grid;
  grid-template-columns: 1fr 1fr;
  align-items: center;
  padding: 100px 8vw 80px;
  gap: 60px;
  overflow: hidden;
}

/* BLOBS */
.hero-blob {
  position: absolute;
  border-radius: 50%;
  filter: blur(90px);
  pointer-events: none;
}
.blob-1 { width: 500px; height: 500px; background: #C9A84C; opacity: 0.1;  top: -120px;  right: 10%; }
.blob-2 { width: 360px; height: 360px; background: #7A9E7E; opacity: 0.12; bottom: -60px; left: 5%;  }
.blob-3 { width: 280px; height: 280px; background: #8B4B62; opacity: 0.08; top: 40%;     right: 30%; }

/* CONTENT */
.hero-content {
  position: relative;
  z-index: 2;
  display: flex;
  flex-direction: column;
  gap: 0;
}

.hero-eyebrow {
  display: flex;
  align-items: center;
  gap: 10px;
  font-family: 'Inter', sans-serif;
  font-size: 0.7rem;
  font-weight: 600;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #C9A84C;
  margin-bottom: 28px;
  opacity: 0;
  animation: fadeUp 0.6s ease 0.1s forwards;
}
.eyebrow-dot {
  width: 6px; height: 6px;
  border-radius: 50%;
  background: #C9A84C;
  flex-shrink: 0;
}

.hero-title {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(2.8rem, 5.5vw, 5.2rem);
  font-weight: 700;
  color: #F7F0E6;
  line-height: 1.06;
  letter-spacing: -0.03em;
  margin-bottom: 28px;
  opacity: 0;
  animation: fadeUp 0.6s ease 0.2s forwards;
}
.hero-title-accent {
  color: #C9A84C;
  font-style: italic;
}

.hero-sub {
  font-family: 'Inter', sans-serif;
  font-size: 1rem;
  font-weight: 300;
  line-height: 1.8;
  color: rgba(247,240,230,0.6);
  max-width: 460px;
  margin-bottom: 40px;
  opacity: 0;
  animation: fadeUp 0.6s ease 0.3s forwards;
}

.hero-actions {
  display: flex;
  gap: 14px;
  flex-wrap: wrap;
  margin-bottom: 52px;
  opacity: 0;
  animation: fadeUp 0.6s ease 0.4s forwards;
}
.btn-primary {
  text-decoration: none;
  background: #C9A84C;
  color: #1A2233;
  padding: 14px 28px;
  border-radius: 4px;
  font-family: 'Inter', sans-serif;
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  transition: background 0.2s, transform 0.15s;
}
.btn-primary:hover { background: #E8C96A; transform: translateY(-1px); }
.btn-ghost {
  text-decoration: none;
  border: 1.5px solid rgba(247,240,230,0.25);
  color: rgba(247,240,230,0.75);
  padding: 14px 28px;
  border-radius: 4px;
  font-family: 'Inter', sans-serif;
  font-size: 0.82rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  transition: border-color 0.2s, color 0.2s;
}
.btn-ghost:hover { border-color: #C9A84C; color: #C9A84C; }

.hero-trust {
  display: flex;
  align-items: center;
  gap: 24px;
  opacity: 0;
  animation: fadeUp 0.6s ease 0.5s forwards;
}
.trust-item { display: flex; flex-direction: column; gap: 3px; }
.trust-item strong {
  font-family: 'Playfair Display', serif;
  font-size: 1.2rem;
  font-weight: 700;
  color: #F7F0E6;
  letter-spacing: -0.02em;
}
.trust-item span {
  font-family: 'Inter', sans-serif;
  font-size: 0.7rem;
  font-weight: 500;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: rgba(247,240,230,0.4);
}
.trust-divider {
  width: 1px;
  height: 36px;
  background: rgba(247,240,230,0.12);
}

/* VISUAL */
.hero-visual {
  position: relative;
  z-index: 2;
  display: flex;
  justify-content: center;
  align-items: flex-end;
  height: 420px;
  opacity: 0;
  animation: fadeIn 0.8s ease 0.5s forwards;
}

.book-stack {
  position: relative;
  width: 320px;
  height: 380px;
  display: flex;
  align-items: flex-end;
  justify-content: center;
}

.stack-book {
  position: absolute;
  bottom: 20px;
  width: 64px;
  border-radius: 2px 4px 4px 2px;
  display: flex;
  box-shadow: 4px 8px 24px rgba(0,0,0,0.45);
  animation: floatBook 4s ease-in-out infinite alternate;
  transform-origin: bottom center;
}
.stack-book:nth-child(1) { left: 20px;  animation-duration: 3.8s; }
.stack-book:nth-child(2) { left: 80px;  animation-duration: 4.2s; }
.stack-book:nth-child(3) { left: 140px; animation-duration: 3.6s; }
.stack-book:nth-child(4) { left: 200px; animation-duration: 4.5s; }
.stack-book:nth-child(5) { left: 255px; animation-duration: 3.9s; }

@keyframes floatBook {
  from { transform: var(--base-transform, rotate(0deg)) translateY(0px); }
  to   { transform: var(--base-transform, rotate(0deg)) translateY(-8px); }
}

.stack-book-spine {
  width: 18px;
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 4px;
  padding: 10px 0;
  background: rgba(0,0,0,0.2);
}
.stack-title {
  font-family: 'Playfair Display', serif;
  font-size: 0.42rem;
  font-weight: 700;
  color: rgba(255,255,255,0.8);
  writing-mode: vertical-rl;
  transform: rotate(180deg);
  letter-spacing: 0.04em;
}
.stack-author {
  font-family: 'Inter', sans-serif;
  font-size: 0.36rem;
  color: rgba(255,255,255,0.45);
  writing-mode: vertical-rl;
  transform: rotate(180deg);
}
.stack-book-cover {
  flex: 1;
  position: relative;
  overflow: hidden;
}
.cover-pattern {
  position: absolute;
  inset: 8px;
  border: 1px solid rgba(255,255,255,0.08);
  border-radius: 1px;
}

.stack-shadow {
  position: absolute;
  bottom: 0;
  left: 10px; right: 10px;
  height: 24px;
  background: radial-gradient(ellipse at center, rgba(0,0,0,0.4) 0%, transparent 70%);
  filter: blur(6px);
}

.hero-badge {
  position: absolute;
  top: 20px;
  right: -20px;
  z-index: 3;
}
.badge-inner {
  background: #C9A84C;
  border-radius: 50%;
  width: 88px;
  height: 88px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 4px;
  box-shadow: 0 8px 24px rgba(201,168,76,0.4);
  animation: rotateBadge 12s linear infinite;
}
@keyframes rotateBadge {
  from { transform: rotate(0deg); }
  to   { transform: rotate(360deg); }
}
.badge-icon {
  font-size: 0.9rem;
  color: #1A2233;
  animation: rotateBadge 12s linear infinite reverse;
}
.badge-text {
  font-family: 'Inter', sans-serif;
  font-size: 0.52rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #1A2233;
  text-align: center;
  line-height: 1.3;
  animation: rotateBadge 12s linear infinite reverse;
}

/* SCROLL CUE */
.hero-scroll {
  position: absolute;
  bottom: 36px;
  left: 8vw;
  display: flex;
  align-items: center;
  gap: 12px;
  z-index: 3;
}
.hero-scroll span {
  font-family: 'Inter', sans-serif;
  font-size: 0.65rem;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: rgba(247,240,230,0.3);
}
.scroll-track {
  width: 36px;
  height: 2px;
  background: rgba(247,240,230,0.12);
  border-radius: 2px;
  overflow: hidden;
}
.scroll-thumb {
  height: 100%;
  width: 40%;
  background: #C9A84C;
  border-radius: 2px;
  animation: scrollPulse 2s ease-in-out infinite;
}
@keyframes scrollPulse {
  0%   { transform: translateX(-100%); }
  100% { transform: translateX(250%); }
}

/* FADE ANIMATIONS */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(20px); }
  to   { opacity: 1; transform: translateY(0); }
}
@keyframes fadeIn {
  from { opacity: 0; }
  to   { opacity: 1; }
}

/* RESPONSIVE */
@media (max-width: 900px) {
  .hero {
    grid-template-columns: 1fr;
    padding: 100px 6vw 60px;
    text-align: center;
    gap: 40px;
  }
  .hero-eyebrow { justify-content: center; }
  .hero-sub { margin-left: auto; margin-right: auto; }
  .hero-actions { justify-content: center; }
  .hero-trust { justify-content: center; }
  .hero-visual { height: 320px; }
  .hero-badge { right: 0; }
  .hero-scroll { display: none; }
}
@media (prefers-reduced-motion: reduce) {
  .stack-book, .badge-inner, .badge-icon, .badge-text, .scroll-thumb { animation: none; }
  .hero-content > *, .hero-visual { opacity: 1; animation: none; }
}
</style>
