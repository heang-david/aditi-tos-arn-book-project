<template>
  <div class="product-view">
    <Product_Sidebar v-model="selectedCategory" />

    <section class="product-section">

      <!-- section header -->
      <div class="section-header">
        <div>
          <div class="section-eyebrow">
            <svg width="28" height="1" viewBox="0 0 28 1"><line x1="0" y1="0.5" x2="28" y2="0.5" stroke="#C9A84C" stroke-width="1"/></svg>
            Our collection
            <svg width="28" height="1" viewBox="0 0 28 1"><line x1="0" y1="0.5" x2="28" y2="0.5" stroke="#C9A84C" stroke-width="1"/></svg>
          </div>
          <h1 class="section-title">{{ selectedCategory || 'All Books' }}</h1>
        </div>
        <span class="book-count" v-if="bookStore.books.length > 0">
          {{ filteredBooks.length }} titles
        </span>
      </div>

      <!-- search + filter row -->
      <div class="search-filter-row">
        <SearchBar
          v-model="searchQuery"
          placeholder="Search by title or author…"
          class="product-search"
        />
        <select v-model="sortBy" class="filter-select">
          <option value="">Sort by</option>
          <option value="price_asc">Price: Low → High</option>
          <option value="price_desc">Price: High → Low</option>
          <option value="stock_asc">Stock: Low → High</option>
          <option value="stock_desc">Stock: High → Low</option>
        </select>
      </div>

      <!-- loading state -->
      <div v-if="bookStore.books.length === 0 && !searchQuery" class="loading-state">
        <div class="loading-book">
          <div class="loading-spine"></div>
          <div class="loading-cover"></div>
        </div>
        <p>Fetching your books…</p>
      </div>

      <!-- no results -->
      <div v-if="bookStore.books.length > 0 && filteredBooks.length === 0" class="no-results">
        No books found for "{{ searchQuery }}"
      </div>

      <!-- grid -->
      <div v-else class="product-list">
        <div
          v-for="book in filteredBooks"
          :key="book.id"
          class="product-card"
        >
          <!-- cover -->
          <div class="card-cover-wrap">
            <img :src="book.image_url" :alt="book.title" class="product-image" />

            <!-- genre badge -->
            <div class="cover-badge">Fiction</div>

            <!-- stock badge -->
            <div
              class="stock-badge"
              :class="{
                low: book.stock > 0 && book.stock <= 5,
                out: book.stock === 0
              }"
            >
              {{ book.stock === 0 ? 'Out of stock' : book.stock <= 5 ? `Only ${book.stock} left` : 'In stock' }}
            </div>

            <!-- hover overlay -->
            <div class="cover-overlay">
              <button class="overlay-quick" @click="goToDetail(book.id)">Quick View</button>
            </div>
          </div>

          <!-- info -->
          <div class="card-body">
            <div class="card-meta">
              <div class="card-rating">
                <span class="stars">★★★★★</span>
                <span class="rating-num">(248)</span>
              </div>
            </div>

            <h2 class="card-title">{{ book.title }}</h2>
            <p class="card-author">{{ book.author }}</p>

            <div class="card-footer">
              <span class="card-price">${{ book.price }}</span>
              <button
                class="cta-btn"
                :class="{ 'in-cart': cartStore.isInCart(book.id) }"
                :disabled="book.stock === 0"
                @click="cartStore.addToCart(book)"
              >
                {{ book.stock === 0 ? 'Sold out' : cartStore.isInCart(book.id) ? '✓ In cart' : '+ Add to cart' }}
              </button>
            </div>
          </div>
        </div>
      </div>

    </section>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue"
import { useRouter } from "vue-router"
import { useBookStore } from "../stores/book"
import Product_Sidebar from "../components/layouts/Product_Sidebar.vue"
import { useCartStore } from '@/stores/cart'
import SearchBar from '@/components/ui/SearchBar.vue'

const cartStore = useCartStore()
const bookStore = useBookStore()
const router = useRouter()
const searchQuery      = ref("")
const sortBy           = ref("")
const selectedCategory = ref("")

const filteredBooks = computed(() => {
  const q   = searchQuery.value.toLowerCase()
  const cat = selectedCategory.value.toLowerCase()

  let list = bookStore.books.filter(b => {
    const matchesSearch = !q || b.title.toLowerCase().includes(q) || b.author.toLowerCase().includes(q)
    const matchesCategory = !cat || b.genre?.toLowerCase() === cat
    return matchesSearch && matchesCategory
  })

  if (sortBy.value === "price_asc")  list.sort((a, b) => a.price - b.price)
  if (sortBy.value === "price_desc") list.sort((a, b) => b.price - a.price)
  if (sortBy.value === "stock_asc")  list.sort((a, b) => a.stock - b.stock)
  if (sortBy.value === "stock_desc") list.sort((a, b) => b.stock - a.stock)

  return list
})

onMounted(() => {
  bookStore.fetchBooks()
})

function goToDetail(bookId) {
  router.push(`/Products/${bookId}`)
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@300;400;500;600&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

/* LAYOUT */
.product-view {
  display: flex;
  gap: 24px;
  align-items: flex-start;
  padding: 32px 0;
  background: #F7F0E6;
  min-height: 100vh;
  font-family: 'Inter', system-ui, sans-serif;
}

.product-section {
  flex: 1;
  
}

/* PAGE ENTER ANIMATIONS */
@keyframes fadeUp {
  from { opacity: 0; transform: translateY(20px); }
  to   { opacity: 1; transform: translateY(0); }
}

.section-header {
  opacity: 0;
  animation: fadeUp 0.55s ease 0.05s forwards;
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  margin-top: 40px;
  margin-bottom: 32px;
}
.product-list {
  opacity: 0;
  animation: fadeUp 0.6s ease 0.25s forwards;
}
.loading-state {
  opacity: 0;
  animation: fadeUp 0.5s ease 0.15s forwards;
}
.no-results {
  opacity: 0;
  animation: fadeUp 0.4s ease 0.1s forwards;
}

.section-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 0.65rem;
  font-weight: 600;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #C9A84C;
  margin-bottom: 6px;
}

.section-title {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(1.8rem, 3vw, 2.6rem);
  font-weight: 700;
  color: #1A2233;
  letter-spacing: -0.03em;
  line-height: 1.1;
}

.book-count {
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #9B9590;
  padding-bottom: 6px;
}

.search-filter-row {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 28px;
  opacity: 0;
  animation: fadeUp 0.55s ease 0.15s forwards;
}
.product-search { flex: 1; max-width: 420px; margin-bottom: 0; }

.filter-select {
  padding: 9px 14px;
  border: 1.5px solid #E8E1D9;
  border-radius: 24px;
  background: #fff;
  font-family: 'Inter', sans-serif;
  font-size: 0.82rem;
  color: #1A2233;
  cursor: pointer;
  outline: none;
  transition: border-color 0.2s;
  white-space: nowrap;
}
.filter-select:focus { border-color: #C9A84C; }

.no-results {
  text-align: center; padding: 60px 20px; color: #9B9590;
  font-size: 0.9rem; letter-spacing: 0.03em;
}

/* LOADING */
.loading-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 20px;
  padding: 80px 20px;
  color: #9B9590;
  font-size: 0.9rem;
  letter-spacing: 0.04em;
}

.loading-book {
  display: flex;
  height: 72px;
  animation: loadingPulse 1.4s ease-in-out infinite;
}
.loading-spine {
  width: 14px;
  background: #C9A84C;
  border-radius: 2px 0 0 2px;
  opacity: 0.6;
}
.loading-cover {
  width: 52px;
  background: #1A2233;
  border-radius: 0 3px 3px 0;
  opacity: 0.15;
}
@keyframes loadingPulse {
  0%, 100% { opacity: 0.5; transform: scale(1); }
  50%       { opacity: 1;   transform: scale(1.04); }
}

/* GRID */
.product-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 24px;
}

/* CARD */
.product-card {
  background: #fff;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 16px rgba(26, 34, 51, 0.07);
  display: flex;
  flex-direction: column;
  cursor: pointer;
  transition: box-shadow 0.25s, transform 0.25s;
}
.product-card:hover {
  box-shadow: 0 12px 40px rgba(26, 34, 51, 0.14);
  transform: translateY(-4px);
}

/* COVER */
.card-cover-wrap {
  position: relative;
  overflow: hidden;
}
.product-image {
  width: 100%;
  height: 260px;
  object-fit: cover;
  display: block;
  transition: transform 0.4s ease;
}
.product-card:hover .product-image { transform: scale(1.04); }

.cover-badge {
  position: absolute;
  top: 12px;
  left: 12px;
  background: #1A2233;
  color: #C9A84C;
  font-size: 0.58rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding: 4px 10px;
  border-radius: 3px;
}

/* STOCK BADGE */
.stock-badge {
  position: absolute;
  top: 12px;
  right: 12px;
  background: rgba(122, 158, 126, 0.95);
  color: #fff;
  font-size: 0.58rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 4px 10px;
  border-radius: 3px;
  white-space: nowrap;
}
.stock-badge.low {
  background: rgba(201, 168, 76, 0.95);
  color: #1A2233;
}
.stock-badge.out {
  background: rgba(192, 69, 74, 0.95);
  color: #fff;
}

.cover-overlay {
  position: absolute;
  inset: 0;
  background: rgba(26, 34, 51, 0.65);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.25s;
}
.product-card:hover .cover-overlay { opacity: 1; }

.overlay-quick {
  background: #C9A84C;
  color: #1A2233;
  border: none;
  padding: 10px 20px;
  border-radius: 4px;
  font-family: 'Inter', sans-serif;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  cursor: pointer;
  transition: background 0.2s;
}
.overlay-quick:hover { background: #E8C96A; }

/* CARD BODY */
.card-body {
  padding: 18px 18px 20px;
  display: flex;
  flex-direction: column;
  flex: 1;
}

.card-meta {
  margin-bottom: 8px;
}
.card-rating { display: flex; align-items: center; gap: 5px; }
.stars {
  font-size: 0.62rem;
  color: #C9A84C;
  letter-spacing: 1.5px;
}
.rating-num {
  font-size: 0.65rem;
  color: #B0ABA5;
}

.card-title {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 1.05rem;
  font-weight: 700;
  color: #1A2233;
  letter-spacing: -0.01em;
  line-height: 1.3;
  margin-bottom: 5px;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card-author {
  font-size: 0.8rem;
  font-weight: 400;
  color: #9B9590;
  margin-bottom: 16px;
}

.card-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: auto;
}

.card-price {
  font-family: 'Playfair Display', serif;
  font-size: 1.2rem;
  font-weight: 700;
  color: #1A2233;
  letter-spacing: -0.02em;
}

.cta-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  background: #1A2233;
  color: #F7F0E6;
  border: none;
  padding: 9px 14px;
  border-radius: 4px;
  font-family: 'Inter', sans-serif;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  cursor: pointer;
  transition: background 0.2s, transform 0.15s;
}
.cta-btn:hover { background: #C9A84C; color: #1A2233; transform: translateY(-1px); }
.cta-btn:disabled {
  background: #E8E1D9;
  color: #B0ABA5;
  cursor: not-allowed;
  transform: none;
}

/* RESPONSIVE */
@media (max-width: 900px) {
  .product-section { margin-left: 0; }
  .product-view { flex-direction: column; padding: 20px; }
}
@media (max-width: 540px) {
  .product-list { grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 16px; }
  .product-image { height: 200px; }
}
</style>