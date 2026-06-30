<template>
  <div class="detail-page">

    <!-- loading state -->
    <div v-if="bookStore.loading" class="loading-state">
      <div class="loading-book">
        <div class="loading-spine"></div>
        <div class="loading-cover"></div>
      </div>
      <p>Fetching book details…</p>
    </div>

    <!-- error state -->
    <div v-else-if="bookStore.error" class="error-state">
      <p>{{ bookStore.error }}</p>
      <button class="back-link" @click="router.back()">
        <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
          <path d="M11 7H2M5.5 3L2 7l3.5 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        Back to books
      </button>
    </div>

    <!-- content -->
    <div v-else-if="bookStore.currentBook" class="detail-content">

      <!-- back link -->
      <button class="back-link" @click="router.back()">
        <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
          <path d="M11 7H2M5.5 3L2 7l3.5 4" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        Back to books
      </button>

      <div class="detail-grid">

        <!-- cover -->
        <div class="detail-cover-wrap">
          <img :src="bookStore.currentBook.image_url" :alt="bookStore.currentBook.title" class="detail-cover" />
          <div
            class="detail-stock-badge"
            :class="{
              low: bookStore.currentBook.stock > 0 && bookStore.currentBook.stock <= 5,
              out: bookStore.currentBook.stock === 0
            }"
          >
            {{
              bookStore.currentBook.stock === 0
                ? 'Out of stock'
                : bookStore.currentBook.stock <= 5
                  ? `Only ${bookStore.currentBook.stock} left`
                  : 'In stock'
            }}
          </div>
        </div>

        <!-- info -->
        <div class="detail-info">

          <div class="detail-genre-tag">{{ bookStore.currentBook.genre || 'Fiction' }}</div>

          <h1 class="detail-title">{{ bookStore.currentBook.title }}</h1>
          <p class="detail-author">by {{ bookStore.currentBook.author }}</p>

          <div class="detail-rating">
            <span class="stars">★★★★★</span>
            <span class="rating-num">(248 reviews)</span>
          </div>

          <div class="detail-price-row">
            <span class="detail-price">${{ bookStore.currentBook.price }}</span>
            <span class="detail-stock-text">{{ bookStore.currentBook.stock }} copies available</span>
          </div>

          <!-- book divider -->
          <div class="book-divider">
            <svg viewBox="0 0 320 30" xmlns="http://www.w3.org/2000/svg">
              <line x1="0" y1="15" x2="118" y2="15" stroke="#C9A84C" stroke-width="0.7" opacity="0.4"/>
              <g transform="translate(133, 3)">
                <path d="M17 4 C13 3 4 5 0 8 L0 18 C4 15 13 13 17 14 C21 13 30 15 34 18 L34 8 C30 5 21 3 17 4Z"
                  fill="none" stroke="#C9A84C" stroke-width="1"/>
                <line x1="17" y1="4" x2="17" y2="14" stroke="#C9A84C" stroke-width="1"/>
              </g>
              <line x1="202" y1="15" x2="320" y2="15" stroke="#C9A84C" stroke-width="0.7" opacity="0.4"/>
            </svg>
          </div>

          <p class="detail-desc">{{ bookStore.currentBook.description }}</p>

          <!-- quantity + cart -->
          <div class="detail-actions">
            <div class="qty-controls">
              <button class="qty-btn" @click="quantity = Math.max(1, quantity - 1)">−</button>
              <span class="qty-value">{{ quantity }}</span>
              <button class="qty-btn" @click="quantity = Math.min(bookStore.currentBook.stock, quantity + 1)">+</button>
            </div>

            <button
              class="add-to-cart-btn"
              :disabled="bookStore.currentBook.stock === 0"
              @click="handleAddToCart"
            >
              <svg width="15" height="15" viewBox="0 0 15 15" fill="none">
                <path d="M7.5 1v13M1 7.5h13" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>
              </svg>
              {{ bookStore.currentBook.stock === 0 ? 'Sold out' : 'Add to cart' }}
            </button>
          </div>

          <p v-if="added" class="added-confirmation">✓ Added to your cart</p>

        </div>
      </div>

    </div>

  </div>
</template>

<script setup>
import { ref, watch, onMounted } from "vue"
import { useRoute, useRouter } from "vue-router"
import { useBookStore } from "../stores/book"
import { useCartStore } from "@/stores/cart"

const route  = useRoute()
const router = useRouter()
const bookStore = useBookStore()
const cartStore  = useCartStore()

const quantity = ref(1)
const added    = ref(false)

async function loadBook() {
  added.value = false
  quantity.value = 1
  const id = Number(route.params.id)
  await bookStore.fetchBookById(id)
}

onMounted(loadBook)
watch(() => route.params.id, loadBook)

function handleAddToCart() {
  for (let i = 0; i < quantity.value; i++) {
    cartStore.addToCart(bookStore.currentBook)
  }
  added.value = true
  setTimeout(() => { added.value = false }, 2500)
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@300;400;500;600&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

.detail-page {
  min-height: 100vh;
  background: #F7F0E6;
  padding: 48px 40px 100px;
  font-family: 'Inter', system-ui, sans-serif;
}

/* LOADING */
.loading-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 20px;
  padding: 120px 20px;
  color: #9B9590;
  font-size: 0.9rem;
}
.loading-book {
  display: flex;
  height: 72px;
  animation: loadingPulse 1.4s ease-in-out infinite;
}
.loading-spine { width: 14px; background: #C9A84C; border-radius: 2px 0 0 2px; opacity: 0.6; }
.loading-cover { width: 52px; background: #1A2233; border-radius: 0 3px 3px 0; opacity: 0.15; }
@keyframes loadingPulse {
  0%, 100% { opacity: 0.5; transform: scale(1); }
  50%       { opacity: 1;   transform: scale(1.04); }
}

/* ERROR */
.error-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 20px;
  padding: 120px 20px;
  text-align: center;
}
.error-state p {
  font-size: 0.95rem;
  color: #C0454A;
  font-weight: 500;
}

/* CONTENT */
.detail-content {
  max-width: 1000px;
  margin: 0 auto;
}

.back-link {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: transparent;
  border: none;
  color: #6B6560;
  font-family: 'Inter', sans-serif;
  font-size: 0.8rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  cursor: pointer;
  margin-bottom: 32px;
  transition: color 0.2s;
}
.back-link:hover { color: #1A2233; }

.detail-grid {
  display: grid;
  grid-template-columns: 340px 1fr;
  gap: 56px;
  align-items: start;
}

/* COVER */
.detail-cover-wrap {
  position: relative;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(26, 34, 51, 0.18);
}
.detail-cover {
  width: 100%;
  height: 480px;
  object-fit: cover;
  display: block;
}
.detail-stock-badge {
  position: absolute;
  top: 16px;
  right: 16px;
  background: rgba(122, 158, 126, 0.95);
  color: #fff;
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 6px 12px;
  border-radius: 4px;
}
.detail-stock-badge.low { background: rgba(201, 168, 76, 0.95); color: #1A2233; }
.detail-stock-badge.out { background: rgba(192, 69, 74, 0.95); color: #fff; }

/* INFO */
.detail-info { display: flex; flex-direction: column; }

.detail-genre-tag {
  display: inline-block;
  align-self: flex-start;
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #C9A84C;
  background: rgba(201, 168, 76, 0.1);
  padding: 5px 12px;
  border-radius: 20px;
  margin-bottom: 16px;
}

.detail-title {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(1.8rem, 3.5vw, 2.6rem);
  font-weight: 700;
  color: #1A2233;
  letter-spacing: -0.03em;
  line-height: 1.15;
  margin-bottom: 8px;
}

.detail-author {
  font-size: 1rem;
  font-weight: 400;
  color: #9B9590;
  margin-bottom: 14px;
}

.detail-rating {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 22px;
}
.stars { font-size: 0.85rem; color: #C9A84C; letter-spacing: 2px; }
.rating-num { font-size: 0.78rem; color: #B0ABA5; }

.detail-price-row {
  display: flex;
  align-items: baseline;
  gap: 16px;
  margin-bottom: 20px;
}
.detail-price {
  font-family: 'Playfair Display', serif;
  font-size: 2rem;
  font-weight: 700;
  color: #1A2233;
  letter-spacing: -0.03em;
}
.detail-stock-text {
  font-size: 0.78rem;
  color: #9B9590;
  font-weight: 500;
}

.book-divider { margin-bottom: 20px; opacity: 0.7; }

.detail-desc {
  font-size: 0.95rem;
  line-height: 1.85;
  color: #6B6560;
  font-weight: 300;
  margin-bottom: 32px;
  max-width: 540px;
}

/* ACTIONS */
.detail-actions {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 14px;
}

.qty-controls {
  display: flex;
  align-items: center;
  border: 1.5px solid #E8E1D9;
  border-radius: 6px;
  overflow: hidden;
  flex-shrink: 0;
}
.qty-btn {
  width: 40px;
  height: 46px;
  background: transparent;
  border: none;
  font-size: 1.1rem;
  font-weight: 500;
  color: #1A2233;
  cursor: pointer;
  transition: background 0.15s;
}
.qty-btn:hover { background: rgba(201, 168, 76, 0.12); }
.qty-value {
  min-width: 44px;
  height: 46px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.95rem;
  font-weight: 600;
  color: #1A2233;
  border-left: 1.5px solid #E8E1D9;
  border-right: 1.5px solid #E8E1D9;
}

.add-to-cart-btn {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  background: #1A2233;
  color: #F7F0E6;
  border: none;
  padding: 0 28px;
  height: 46px;
  border-radius: 6px;
  font-family: 'Inter', sans-serif;
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  cursor: pointer;
  transition: background 0.2s, transform 0.15s;
}
.add-to-cart-btn:hover { background: #C9A84C; color: #1A2233; transform: translateY(-1px); }
.add-to-cart-btn:disabled {
  background: #E8E1D9;
  color: #B0ABA5;
  cursor: not-allowed;
  transform: none;
}

.added-confirmation {
  font-size: 0.82rem;
  font-weight: 600;
  color: #7A9E7E;
}

/* RESPONSIVE */
@media (max-width: 800px) {
  .detail-grid { grid-template-columns: 1fr; gap: 32px; }
  .detail-cover { height: 380px; }
}
@media (max-width: 480px) {
  .detail-page { padding: 32px 20px 80px; }
  .detail-actions { flex-direction: column; align-items: stretch; }
}
</style>