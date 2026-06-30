<template>
  <section id="featured" class="featured">

    <div class="featured-inner">

      <!-- header -->
      <div class="section-header">
        <div class="section-eyebrow">
          <svg width="40" height="1" viewBox="0 0 40 1"><line x1="0" y1="0.5" x2="40" y2="0.5" stroke="#C9A84C" stroke-width="1"/></svg>
          Hand-picked reads
          <svg width="40" height="1" viewBox="0 0 40 1"><line x1="0" y1="0.5" x2="40" y2="0.5" stroke="#C9A84C" stroke-width="1"/></svg>
        </div>
        <h2 class="section-title">Featured Books</h2>
        <p class="section-sub">Titles our team pressed into readers' hands this month — and they all said thank you.</p>
      </div>

      <!-- filter tabs -->
      <div class="filter-tabs">
        <button
          v-for="tab in tabs"
          :key="tab"
          class="tab"
          :class="{ active: activeTab === tab }"
          @click="activeTab = tab"
        >
          {{ tab }}
        </button>
      </div>

      <!-- book grid -->
      <div class="books-grid">
        <div
          v-for="(book, i) in filteredBooks"
          :key="book.id"
          class="book-card"
          :class="{ visible: mounted }"
          :style="{ transitionDelay: i * 70 + 'ms' }"
        >
          <!-- cover -->
          <div class="book-cover" :style="{ background: book.coverBg }">
            <div class="cover-texture"></div>
            <div class="cover-content">
              <div class="cover-deco" :style="{ borderColor: book.accentColor }"></div>
              <span class="cover-genre-tag" :style="{ color: book.accentColor }">{{ book.genre }}</span>
              <div class="cover-title-block">
                <div class="cover-book-title">{{ book.title }}</div>
                <div class="cover-book-author">{{ book.author }}</div>
              </div>
            </div>
            <!-- badge -->
            <div v-if="book.badge" class="cover-badge" :style="{ background: book.badgeColor }">{{ book.badge }}</div>
            <!-- quick actions -->
            <div class="cover-overlay">
              <button class="overlay-btn">Quick View</button>
            </div>
          </div>

          <!-- info -->
          <div class="book-info">
            <div class="book-meta">
              <span class="book-genre">{{ book.genre }}</span>
              <div class="book-rating">
                <span class="stars">{{ '★'.repeat(Math.floor(book.rating)) }}{{ book.rating % 1 ? '½' : '' }}</span>
                <span class="rating-count">({{ book.reviews }})</span>
              </div>
            </div>
            <h3 class="book-title">{{ book.title }}</h3>
            <p class="book-author">{{ book.author }}</p>
            <p class="book-desc">{{ book.desc }}</p>
            <div class="book-footer">
              <span class="book-price">${{ book.price }}</span>
              <button
    class="add-btn"
    :class="{ 'in-cart': cartStore.isInCart(book.id) }"
    @click="cartStore.addToCart(book)"
  >
    {{ cartStore.isInCart(book.id) ? '✓ In cart' : '+ Add to cart' }}
  </button>
            </div>
          </div>

        </div>
      </div>

      <!-- view all -->
      <div class="view-all-wrap">
        <a href="#" class="view-all">
          View all books
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none">
            <path d="M3 8h10M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </a>
      </div>

    </div>

  </section>
</template>

<script>
import { useCartStore } from '@/stores/cart';
export default {
  name: 'FeaturedBooks',
  data() {
    return {
      cartStore: useCartStore(),
      mounted: false,
      activeTab: 'All',
      tabs: ['All', 'Fiction', 'Non-Fiction', 'Essays', 'Classics'],
      books: [
        {
          id: 1,
          title: 'Pachinko',
          author: 'Min Jin Lee',
          genre: 'Fiction',
          desc: 'A multigenerational saga following a Korean family who immigrates to Japan — sweeping, devastating, and impossible to set down.',
          price: '16.99',
          rating: 5,
          reviews: 1842,
          badge: 'Staff Pick',
          badgeColor: '#7A9E7E',
          coverBg: 'linear-gradient(145deg, #2C4770, #1A2F50)',
          accentColor: '#C9A84C',
        },
        {
          id: 2,
          title: 'Educated',
          author: 'Tara Westover',
          genre: 'Non-Fiction',
          desc: 'A remarkable memoir of a young woman who grows up in a survivalist family and eventually earns a PhD from Cambridge.',
          price: '14.99',
          rating: 4.5,
          reviews: 2210,
          badge: 'Bestseller',
          badgeColor: '#C9A84C',
          coverBg: 'linear-gradient(145deg, #5C3D2E, #3A2010)',
          accentColor: '#E8C96A',
        },
        {
          id: 3,
          title: 'Circe',
          author: 'Madeline Miller',
          genre: 'Fiction',
          desc: 'The witch of Greek myth reimagined as a fully human figure — discovering her voice, her power, and what it means to be mortal.',
          price: '15.99',
          rating: 5,
          reviews: 3104,
          badge: null,
          badgeColor: null,
          coverBg: 'linear-gradient(145deg, #7A9E7E, #4A6E4E)',
          accentColor: '#F7F0E6',
        },
        {
          id: 4,
          title: 'Between the World and Me',
          author: 'Ta-Nehisi Coates',
          genre: 'Essays',
          desc: 'A letter from father to son — a visceral account of what it means to inhabit a Black body in America.',
          price: '13.99',
          rating: 5,
          reviews: 1567,
          badge: 'Award Winner',
          badgeColor: '#8B4B62',
          coverBg: 'linear-gradient(145deg, #1A2233, #0A1220)',
          accentColor: '#C9A84C',
        },
        {
          id: 5,
          title: 'Invisible Cities',
          author: 'Italo Calvino',
          genre: 'Classics',
          desc: 'Marco Polo describes cities to Kublai Khan — a fever-dream meditation on memory, desire, and what cities mean to those who build them.',
          price: '12.99',
          rating: 4.5,
          reviews: 987,
          badge: null,
          badgeColor: null,
          coverBg: 'linear-gradient(145deg, #4A7C8E, #2A5C6E)',
          accentColor: '#E8C96A',
        },
        {
          id: 6,
          title: 'The Buried Giant',
          author: 'Kazuo Ishiguro',
          genre: 'Fiction',
          desc: 'An elderly couple journey through an Arthurian England where all memory has been erased by a collective amnesia — haunting and tender.',
          price: '15.49',
          rating: 4.5,
          reviews: 741,
          badge: null,
          badgeColor: null,
          coverBg: 'linear-gradient(145deg, #8B4B62, #5B1B32)',
          accentColor: '#C9A84C',
        },
      ],
    }
  },
  computed: {
    filteredBooks() {
      if (this.activeTab === 'All') return this.books
      return this.books.filter(b => b.genre === this.activeTab)
    },
  },
  mounted() {
    this.$nextTick(() => { this.mounted = true })
  },
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@300;400;500;600&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

.featured {
  background: #F7F0E6;
  padding: 100px 0 110px;
}
.featured-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 40px;
}

/* HEADER */
.section-header { text-align: center; margin-bottom: 48px; }
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
}
.section-title {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(2rem, 4vw, 3.2rem);
  font-weight: 700;
  color: #1A2233;
  letter-spacing: -0.03em;
  margin-bottom: 14px;
}
.section-sub {
  font-family: 'Inter', sans-serif;
  font-size: 0.975rem;
  font-weight: 300;
  line-height: 1.75;
  color: #6B6560;
  max-width: 480px;
  margin: 0 auto;
}

/* FILTER TABS */
.filter-tabs {
  display: flex;
  justify-content: center;
  gap: 8px;
  flex-wrap: wrap;
  margin-bottom: 48px;
}
.tab {
  font-family: 'Inter', sans-serif;
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  padding: 8px 20px;
  border-radius: 40px;
  border: 1.5px solid #E8E1D9;
  background: transparent;
  color: #6B6560;
  cursor: pointer;
  transition: all 0.2s;
}
.tab:hover { border-color: #C9A84C; color: #1A2233; }
.tab.active { background: #1A2233; border-color: #1A2233; color: #F7F0E6; }

/* GRID */
.books-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 28px;
}

/* CARD */
.book-card {
  background: #fff;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 16px rgba(26,34,51,0.07);
  transition: box-shadow 0.25s, transform 0.25s, opacity 0.5s, translateY 0.5s;
  opacity: 0;
  transform: translateY(24px);
}
.book-card.visible { opacity: 1; transform: translateY(0); }
.book-card:hover {
  box-shadow: 0 12px 40px rgba(26,34,51,0.14);
  transform: translateY(-4px);
}

/* COVER */
.book-cover {
  position: relative;
  height: 220px;
  overflow: hidden;
}
.cover-texture {
  position: absolute;
  inset: 0;
  background-image: repeating-linear-gradient(
    0deg,
    transparent,
    transparent 2px,
    rgba(255,255,255,0.02) 2px,
    rgba(255,255,255,0.02) 4px
  );
}
.cover-content {
  position: relative;
  z-index: 1;
  height: 100%;
  padding: 20px 20px 16px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.cover-deco {
  width: 28px;
  height: 28px;
  border: 1.5px solid;
  border-radius: 50%;
  opacity: 0.5;
}
.cover-genre-tag {
  font-family: 'Inter', sans-serif;
  font-size: 0.6rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  align-self: flex-start;
  background: rgba(255,255,255,0.1);
  padding: 4px 10px;
  border-radius: 20px;
}
.cover-title-block { margin-top: auto; }
.cover-book-title {
  font-family: 'Playfair Display', serif;
  font-size: 1.15rem;
  font-weight: 700;
  color: #F7F0E6;
  line-height: 1.2;
  letter-spacing: -0.01em;
  margin-bottom: 4px;
}
.cover-book-author {
  font-family: 'Inter', sans-serif;
  font-size: 0.72rem;
  font-weight: 400;
  color: rgba(247,240,230,0.55);
  letter-spacing: 0.04em;
}

.cover-badge {
  position: absolute;
  top: 12px;
  right: 12px;
  font-family: 'Inter', sans-serif;
  font-size: 0.58rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #fff;
  padding: 4px 10px;
  border-radius: 3px;
}

.cover-overlay {
  position: absolute;
  inset: 0;
  background: rgba(26,34,51,0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.25s;
}
.book-card:hover .cover-overlay { opacity: 1; }
.overlay-btn {
  font-family: 'Inter', sans-serif;
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #1A2233;
  background: #C9A84C;
  border: none;
  padding: 10px 22px;
  border-radius: 4px;
  cursor: pointer;
  transition: background 0.2s;
}
.overlay-btn:hover { background: #E8C96A; }

/* INFO */
.book-info {
  padding: 20px 22px 22px;
}
.book-meta {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 8px;
}
.book-genre {
  font-family: 'Inter', sans-serif;
  font-size: 0.65rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #C9A84C;
}
.book-rating {
  display: flex;
  align-items: center;
  gap: 5px;
}
.stars {
  font-size: 0.65rem;
  color: #C9A84C;
  letter-spacing: 1px;
}
.rating-count {
  font-family: 'Inter', sans-serif;
  font-size: 0.65rem;
  color: #9B9590;
}
.book-title {
  font-family: 'Playfair Display', serif;
  font-size: 1.1rem;
  font-weight: 700;
  color: #1A2233;
  letter-spacing: -0.01em;
  line-height: 1.25;
  margin-bottom: 4px;
}
.book-author {
  font-family: 'Inter', sans-serif;
  font-size: 0.78rem;
  font-weight: 400;
  color: #9B9590;
  margin-bottom: 10px;
}
.book-desc {
  font-family: 'Inter', sans-serif;
  font-size: 0.82rem;
  line-height: 1.65;
  color: #6B6560;
  margin-bottom: 18px;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
.book-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.book-price {
  font-family: 'Playfair Display', serif;
  font-size: 1.3rem;
  font-weight: 700;
  color: #1A2233;
  letter-spacing: -0.02em;
}
.add-btn {
  display: flex;
  align-items: center;
  gap: 7px;
  font-family: 'Inter', sans-serif;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #F7F0E6;
  background: #1A2233;
  border: none;
  padding: 9px 16px;
  border-radius: 4px;
  cursor: pointer;
  transition: background 0.2s;
}
.add-btn:hover { background: #C9A84C; color: #1A2233; }

/* VIEW ALL */
.view-all-wrap { text-align: center; margin-top: 56px; }
.view-all {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
  font-family: 'Inter', sans-serif;
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #1A2233;
  border-bottom: 1.5px solid #C9A84C;
  padding-bottom: 3px;
  transition: color 0.2s, gap 0.2s;
}
.view-all:hover { color: #C9A84C; gap: 16px; }

/* RESPONSIVE */
@media (max-width: 960px) {
  .books-grid { grid-template-columns: repeat(2, 1fr); }
}
@media (max-width: 600px) {
  .books-grid { grid-template-columns: 1fr; }
  .featured-inner { padding: 0 20px; }
}
</style>
