<template>
  <section id="categories" class="categories">

    <div class="categories-inner">

      <!-- header -->
      <div class="section-header">
        <div class="section-eyebrow">
          <svg width="40" height="1" viewBox="0 0 40 1"><line x1="0" y1="0.5" x2="40" y2="0.5" stroke="#C9A84C" stroke-width="1"/></svg>
          Browse by interest
          <svg width="40" height="1" viewBox="0 0 40 1"><line x1="0" y1="0.5" x2="40" y2="0.5" stroke="#C9A84C" stroke-width="1"/></svg>
        </div>
        <h2 class="section-title">Find Your World</h2>
        <p class="section-sub">
          Every shelf tells a different story. Explore by what draws you in today.
        </p>
      </div>

      <!-- large feature categories -->
      <div class="cat-feature">
        <div
          v-for="(cat, i) in featureCategories"
          :key="cat.id"
          class="cat-feature-card"
          :class="{ visible: mounted, wide: i === 0 }"
          :style="{ transitionDelay: i * 80 + 'ms', background: cat.bg }"
          @mouseenter="hoveredCat = cat.id"
          @mouseleave="hoveredCat = null"
        >
          <div class="cat-feature-inner">
            <div class="cat-mark" :style="{ color: cat.accent }">{{ cat.mark }}</div>
            <div class="cat-count" :style="{ color: cat.accent }">{{ cat.count }} titles</div>
            <h3 class="cat-name">{{ cat.name }}</h3>
            <p class="cat-blurb">{{ cat.blurb }}</p>
            <a href="#" class="cat-link" :style="{ color: cat.accent }">
              Explore
              <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
                <path d="M2 7h10M8 3l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </a>
          </div>
          <!-- decorative lines -->
          <div class="cat-deco-lines">
            <div v-for="n in 4" :key="n" class="deco-line" :style="{ opacity: 0.04 + n * 0.02, background: cat.accent }"></div>
          </div>
          <!-- hover shimmer -->
          <div class="cat-shimmer" :class="{ active: hoveredCat === cat.id }"></div>
        </div>
      </div>

      <!-- secondary grid -->
      <div class="cat-grid">
        <a
          v-for="(cat, i) in secondaryCategories"
          :key="cat.id"
          href="#"
          class="cat-tile"
          :class="{ visible: mounted }"
          :style="{ transitionDelay: (featureCategories.length * 80 + i * 60) + 'ms' }"
        >
          <span class="cat-tile-icon">{{ cat.icon }}</span>
          <div class="cat-tile-body">
            <strong>{{ cat.name }}</strong>
            <span>{{ cat.count }} titles</span>
          </div>
          <svg class="cat-tile-arrow" width="14" height="14" viewBox="0 0 14 14" fill="none">
            <path d="M2 7h10M8 3l4 4-4 4" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </a>
      </div>

    </div>

    <!-- book divider -->
    <div class="book-divider">
      <svg viewBox="0 0 800 60" preserveAspectRatio="xMidYMid meet">
        <line x1="0" y1="30" x2="310" y2="30" stroke="#C9A84C" stroke-width="0.8" opacity="0.35"/>
        <g transform="translate(360, 5)">
          <path d="M40 10 C30 8 10 12 0 18 L0 42 C10 36 30 32 40 34 C50 32 70 36 80 42 L80 18 C70 12 50 8 40 10Z" fill="none" stroke="#C9A84C" stroke-width="1.2"/>
          <line x1="40" y1="10" x2="40" y2="34" stroke="#C9A84C" stroke-width="1.2"/>
        </g>
        <line x1="490" y1="30" x2="800" y2="30" stroke="#C9A84C" stroke-width="0.8" opacity="0.35"/>
      </svg>
    </div>

  </section>
</template>

<script>
export default {
  name: 'CategoriesSection',
  data() {
    return {
      mounted: false,
      hoveredCat: null,
      featureCategories: [
        {
          id: 'fiction',
          name: 'Fiction',
          mark: '◈',
          count: '12,400+',
          blurb: 'Stories that pull you out of your world and deposit you somewhere more interesting. Literary, genre, translated — every kind of made-up truth.',
          bg: '#1A2233',
          accent: '#C9A84C',
        },
        {
          id: 'nonfiction',
          name: 'Non-Fiction',
          mark: '◉',
          count: '9,200+',
          blurb: 'The real world is stranger than any novel. Memoirs, histories, sciences, and biographies that make you see the familiar differently.',
          bg: '#2C4770',
          accent: '#E8C96A',
        },
        {
          id: 'essays',
          name: 'Essays & Criticism',
          mark: '✦',
          count: '4,100+',
          blurb: 'Ideas that deserve more than a tweet. The finest minds stretching their thinking across long-form prose.',
          bg: '#5C3D2E',
          accent: '#F7F0E6',
        },
      ],
      secondaryCategories: [
        { id: 's1', name: 'Classics',         icon: '📜', count: '3,800+' },
        { id: 's2', name: 'Poetry',           icon: '🖊',  count: '2,100+' },
        { id: 's3', name: 'Science & Nature', icon: '🔭', count: '3,400+' },
        { id: 's4', name: 'History',          icon: '🏛',  count: '5,200+' },
        { id: 's5', name: 'Art & Design',     icon: '🎨', count: '1,900+' },
        { id: 's6', name: 'Travel',           icon: '🗺',  count: '1,400+' },
        { id: 's7', name: 'Philosophy',       icon: '◇',  count: '2,600+' },
        { id: 's8', name: 'Children\'s',      icon: '🌱', count: '4,800+' },
      ],
    }
  },
  mounted() {
    this.$nextTick(() => { this.mounted = true })
  },
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@300;400;500;600&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

.categories {
  background: #1A2233;
  padding: 100px 0 0;
}
.categories-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 40px 80px;
}

/* HEADER */
.section-header { text-align: center; margin-bottom: 56px; }
.section-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  font-family: 'Inter', sans-serif;
  font-size: 0.7rem;
  font-weight: 600;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #C9A84C;
  margin-bottom: 16px;
  opacity: 0.8;
}
.section-title {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(2rem, 4vw, 3.2rem);
  font-weight: 700;
  color: #F7F0E6;
  letter-spacing: -0.03em;
  margin-bottom: 14px;
}
.section-sub {
  font-family: 'Inter', sans-serif;
  font-size: 0.975rem;
  font-weight: 300;
  line-height: 1.75;
  color: rgba(247,240,230,0.5);
  max-width: 440px;
  margin: 0 auto;
}

/* FEATURE ROW */
.cat-feature {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr;
  gap: 16px;
  margin-bottom: 16px;
}

.cat-feature-card {
  position: relative;
  border-radius: 8px;
  padding: 40px 36px;
  min-height: 280px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  cursor: pointer;
  opacity: 0;
  transform: translateY(24px);
  transition: opacity 0.5s ease, transform 0.5s ease, box-shadow 0.25s;
}
.cat-feature-card.visible { opacity: 1; transform: translateY(0); }
.cat-feature-card:hover { box-shadow: 0 20px 60px rgba(0,0,0,0.35); }

.cat-feature-inner { position: relative; z-index: 2; }

.cat-mark {
  font-size: 1.4rem;
  margin-bottom: 12px;
  display: block;
}
.cat-count {
  font-family: 'Inter', sans-serif;
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  margin-bottom: 8px;
  opacity: 0.75;
}
.cat-name {
  font-family: 'Playfair Display', serif;
  font-size: clamp(1.4rem, 2.5vw, 2rem);
  font-weight: 700;
  color: #F7F0E6;
  letter-spacing: -0.02em;
  margin-bottom: 12px;
  line-height: 1.15;
}
.cat-blurb {
  font-family: 'Inter', sans-serif;
  font-size: 0.84rem;
  line-height: 1.7;
  color: rgba(247,240,230,0.55);
  margin-bottom: 24px;
  max-width: 320px;
}
.cat-link {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  text-decoration: none;
  font-family: 'Inter', sans-serif;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  border-bottom: 1px solid currentColor;
  padding-bottom: 2px;
  transition: gap 0.2s;
}
.cat-feature-card:hover .cat-link { gap: 14px; }

/* deco lines */
.cat-deco-lines {
  position: absolute;
  top: 0; right: 0;
  width: 120px;
  height: 100%;
  display: flex;
  gap: 16px;
  pointer-events: none;
}
.deco-line {
  flex: 1;
  height: 100%;
}

/* shimmer */
.cat-shimmer {
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, rgba(255,255,255,0) 40%, rgba(255,255,255,0.04) 60%, rgba(255,255,255,0) 80%);
  opacity: 0;
  transition: opacity 0.4s;
  pointer-events: none;
}
.cat-shimmer.active { opacity: 1; }

/* SECONDARY GRID */
.cat-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
}

.cat-tile {
  display: flex;
  align-items: center;
  gap: 14px;
  text-decoration: none;
  background: rgba(255,255,255,0.04);
  border: 1px solid rgba(201,168,76,0.12);
  border-radius: 6px;
  padding: 18px 20px;
  transition: background 0.2s, border-color 0.2s, transform 0.2s;
  opacity: 0;
  transform: translateY(16px);
}
.cat-tile.visible { opacity: 1; transform: translateY(0); transition: opacity 0.4s ease, transform 0.4s ease, background 0.2s, border-color 0.2s; }
.cat-tile:hover {
  background: rgba(201,168,76,0.08);
  border-color: rgba(201,168,76,0.3);
  transform: translateY(-2px);
}
.cat-tile-icon { font-size: 1.3rem; flex-shrink: 0; }
.cat-tile-body {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 2px;
}
.cat-tile-body strong {
  font-family: 'Inter', sans-serif;
  font-size: 0.875rem;
  font-weight: 600;
  color: #F7F0E6;
}
.cat-tile-body span {
  font-family: 'Inter', sans-serif;
  font-size: 0.68rem;
  font-weight: 400;
  color: rgba(247,240,230,0.35);
  letter-spacing: 0.05em;
}
.cat-tile-arrow {
  color: rgba(201,168,76,0.4);
  flex-shrink: 0;
  transition: color 0.2s, transform 0.2s;
}
.cat-tile:hover .cat-tile-arrow { color: #C9A84C; transform: translateX(3px); }

/* BOOK DIVIDER */
.book-divider {
  padding: 0 40px;
  max-width: 960px;
  margin: 0 auto;
  opacity: 0.6;
}

/* RESPONSIVE */
@media (max-width: 960px) {
  .cat-feature { grid-template-columns: 1fr 1fr; }
  .cat-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 600px) {
  .cat-feature { grid-template-columns: 1fr; }
  .cat-grid { grid-template-columns: 1fr 1fr; }
  .categories-inner { padding: 0 20px 60px; }
  .cat-blurb { display: none; }
}
</style>
