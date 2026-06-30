<script setup>
import { useCartStore } from '@/stores/cart'
import { useRouter, } from 'vue-router';

const router = useRouter()
const cart = useCartStore()

function goToCheckOut() {
  router.push(`/Checkout`)
}
</script>

<template>
  <div class="cart-page">

    <!-- empty state -->
    <div v-if="cart.isEmpty" class="cart-empty">
      <div class="empty-icon">
        <svg width="56" height="56" viewBox="0 0 56 56" fill="none">
          <rect x="8" y="16" width="40" height="32" rx="4" stroke="#C9A84C" stroke-width="1.5" opacity="0.4"/>
          <path d="M18 16v-4a10 10 0 0 1 20 0v4" stroke="#C9A84C" stroke-width="1.5" stroke-linecap="round" opacity="0.4"/>
          <circle cx="22" cy="30" r="2" fill="#C9A84C" opacity="0.5"/>
          <circle cx="34" cy="30" r="2" fill="#C9A84C" opacity="0.5"/>
        </svg>
      </div>
      <h2 class="empty-title">Your cart is empty</h2>
      <p class="empty-sub">Looks like you haven't added any books yet.</p>
      <router-link to="/products" class="empty-cta">
        Browse Books
        <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
          <path d="M2 7h10M7 3l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </router-link>
    </div>

    <!-- cart content -->
    <div v-else class="cart-layout">

      <!-- left — items -->
      <div class="cart-items-col">

        <div class="cart-header">
          <div class="section-eyebrow">
            <svg width="28" height="1" viewBox="0 0 28 1"><line x1="0" y1="0.5" x2="28" y2="0.5" stroke="#C9A84C" stroke-width="1"/></svg>
            Your selection
            <svg width="28" height="1" viewBox="0 0 28 1"><line x1="0" y1="0.5" x2="28" y2="0.5" stroke="#C9A84C" stroke-width="1"/></svg>
          </div>
          <h1 class="cart-title">Shopping Cart</h1>
        </div>

        <div class="cart-items">
          <div
            v-for="item in cart.items"
            :key="item.id"
            class="cart-item"
          >
            <!-- book cover -->
            <div class="item-cover-wrap">
              <img :src="item.image_url" :alt="item.title" class="item-cover" />
            </div>

            <!-- info -->
            <div class="item-info">
              <span class="item-genre">{{ item.genre }}</span>
              <h3 class="item-title">{{ item.title }}</h3>
              <p class="item-author">{{ item.author }}</p>
              <span class="item-unit-price">${{ Number(item.price).toFixed(2) }} each</span>
            </div>

            <!-- controls + price -->
            <div class="item-right">
              <div class="qty-controls">
                <button class="qty-btn" @click="cart.updateQuantity(item.id, item.quantity - 1)">−</button>
                <span class="qty-value">{{ item.quantity }}</span>
                <button class="qty-btn" @click="cart.updateQuantity(item.id, item.quantity + 1)">+</button>
              </div>
              <span class="item-price">${{ (item.price * item.quantity).toFixed(2) }}</span>
              <button class="remove-btn" @click="cart.removeFromCart(item.id)" aria-label="Remove item">
                <svg width="13" height="13" viewBox="0 0 13 13" fill="none">
                  <path d="M2 2l9 9M11 2l-9 9" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/>
                </svg>
              </button>
            </div>
          </div>
        </div>

        <!-- clear cart -->
        <div class="cart-actions">
          <router-link to="/products" class="continue-link">
            <svg width="13" height="13" viewBox="0 0 13 13" fill="none">
              <path d="M11 6.5H2M5.5 3L2 6.5l3.5 3.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
            Continue browsing
          </router-link>
          <button class="clear-btn" @click="cart.clearCart()">Clear cart</button>
        </div>

      </div>

      <!-- right — summary -->
      <div class="cart-summary-col">
        <div class="summary-card">
          <h2 class="summary-title">Order Summary</h2>
          <div class="summary-rows">
            <div class="summary-row">
              <span>{{ cart.totalItems }} {{ cart.totalItems === 1 ? 'item' : 'items' }}</span>
              <span>${{ cart.totalPrice.toFixed(2) }}</span>
            </div>
            <div class="summary-row">
              <span>Shipping</span>
              <span class="free-tag">Free</span>
            </div>
            <div class="summary-row">
              <span>Tax (10%)</span>
              <span>${{ (cart.totalPrice * 0.1).toFixed(2) }}</span>
            </div>
          </div>

          <!-- divider -->
          <div class="summary-divider">
            <svg viewBox="0 0 260 24" xmlns="http://www.w3.org/2000/svg">
              <line x1="0" y1="12" x2="98" y2="12" stroke="#C9A84C" stroke-width="0.7" opacity="0.3"/>
              <g transform="translate(111, 2)">
                <path d="M19 4 C15 3 5 5 0 9 L0 17 C5 14 15 12 19 13 C23 12 33 14 38 17 L38 9 C33 5 23 3 19 4Z" fill="none" stroke="#C9A84C" stroke-width="1"/>
                <line x1="19" y1="4" x2="19" y2="13" stroke="#C9A84C" stroke-width="1"/>
              </g>
              <line x1="162" y1="12" x2="260" y2="12" stroke="#C9A84C" stroke-width="0.7" opacity="0.3"/>
            </svg>
          </div>

          <div class="summary-total">
            <span>Total</span>
            <strong>${{ (cart.totalPrice * 1.1).toFixed(2) }}</strong>
          </div>

          <button class="checkout-btn" @click="goToCheckOut">
            Proceed to Checkout
            <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
              <path d="M2 7h10M7 3l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
            </svg>
          </button>

          <p class="summary-note">
            Free shipping on all orders. Returns accepted within 30 days.
          </p>

        </div>
      </div>

    </div>
  </div>
</template>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@300;400;500;600&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

/* PAGE */
.cart-page {
  min-height: 100vh;
  background: #F7F0E6;
  padding: 56px 40px 100px;
  font-family: 'Inter', system-ui, sans-serif;
}

/* ── EMPTY STATE ── */
.cart-empty {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 60vh;
  text-align: center;
  gap: 16px;
}
.empty-icon {
  width: 96px;
  height: 96px;
  background: rgba(26, 34, 51, 0.05);
  border: 1.5px solid rgba(201, 168, 76, 0.2);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 8px;
}
.empty-title {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 2rem;
  font-weight: 700;
  color: #1A2233;
  letter-spacing: -0.03em;
}
.empty-sub {
  font-size: 0.95rem;
  color: #9B9590;
  font-weight: 300;
}
.empty-cta {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  text-decoration: none;
  background: #1A2233;
  color: #F7F0E6;
  padding: 13px 28px;
  border-radius: 4px;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.07em;
  text-transform: uppercase;
  margin-top: 8px;
  transition: background 0.2s, transform 0.15s;
}
.empty-cta:hover { background: #C9A84C; color: #1A2233; transform: translateY(-1px); }

/* ── LAYOUT ── */
.cart-layout {
  max-width: 1100px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr 360px;
  gap: 40px;
  align-items: start;
}

/* ── HEADER ── */
.cart-header { margin-bottom: 28px; }
.section-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 0.65rem;
  font-weight: 600;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #C9A84C;
  margin-bottom: 8px;
}
.cart-title {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(2rem, 3.5vw, 2.8rem);
  font-weight: 700;
  color: #1A2233;
  letter-spacing: -0.03em;
}

/* ── ITEMS ── */
.cart-items {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-bottom: 24px;
}

.cart-item {
  display: flex;
  align-items: center;
  gap: 20px;
  background: #fff;
  border-radius: 8px;
  padding: 18px 20px;
  box-shadow: 0 4px 16px rgba(26, 34, 51, 0.06);
  transition: box-shadow 0.2s;
}
.cart-item:hover { box-shadow: 0 8px 28px rgba(26, 34, 51, 0.1); }

.item-cover-wrap {
  flex-shrink: 0;
  width: 72px;
  height: 100px;
  border-radius: 4px;
  overflow: hidden;
  box-shadow: 3px 4px 12px rgba(26, 34, 51, 0.18);
}
.item-cover {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.item-info {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.item-genre {
  font-size: 0.62rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #C9A84C;
}
.item-title {
  font-family: 'Playfair Display', serif;
  font-size: 1.05rem;
  font-weight: 700;
  color: #1A2233;
  letter-spacing: -0.01em;
  line-height: 1.3;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.item-author {
  font-size: 0.8rem;
  color: #9B9590;
  margin-bottom: 4px;
}
.item-unit-price {
  font-size: 0.72rem;
  font-weight: 500;
  color: #B0ABA5;
  letter-spacing: 0.03em;
}

.item-right {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 10px;
  flex-shrink: 0;
}

.qty-controls {
  display: flex;
  align-items: center;
  gap: 0;
  border: 1.5px solid #E8E1D9;
  border-radius: 5px;
  overflow: hidden;
}
.qty-btn {
  width: 32px;
  height: 32px;
  background: transparent;
  border: none;
  font-size: 1rem;
  font-weight: 500;
  color: #1A2233;
  cursor: pointer;
  transition: background 0.15s;
  display: flex;
  align-items: center;
  justify-content: center;
}
.qty-btn:hover { background: rgba(201, 168, 76, 0.12); }
.qty-value {
  min-width: 32px;
  text-align: center;
  font-size: 0.875rem;
  font-weight: 600;
  color: #1A2233;
  border-left: 1.5px solid #E8E1D9;
  border-right: 1.5px solid #E8E1D9;
  padding: 0 4px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.item-price {
  font-family: 'Playfair Display', serif;
  font-size: 1.1rem;
  font-weight: 700;
  color: #1A2233;
  letter-spacing: -0.02em;
}

.remove-btn {
  background: transparent;
  border: 1.5px solid #E8E1D9;
  border-radius: 4px;
  width: 28px;
  height: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #B0ABA5;
  cursor: pointer;
  transition: border-color 0.2s, color 0.2s, background 0.2s;
}
.remove-btn:hover { border-color: #C0454A; color: #C0454A; background: rgba(192, 69, 74, 0.06); }

/* ── CART ACTIONS ── */
.cart-actions {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.continue-link {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  text-decoration: none;
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #6B6560;
  transition: color 0.2s;
}
.continue-link:hover { color: #1A2233; }
.clear-btn {
  background: transparent;
  border: 1.5px solid #E8E1D9;
  color: #9B9590;
  font-family: 'Inter', sans-serif;
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
  transition: border-color 0.2s, color 0.2s;
}
.clear-btn:hover { border-color: #C0454A; color: #C0454A; }

/* ── SUMMARY CARD ── */
.cart-summary-col { position: sticky; top: 100px; }

.summary-card {
  background: #1A2233;
  border-radius: 10px;
  padding: 32px 28px;
  box-shadow: 0 12px 40px rgba(26, 34, 51, 0.2);
  border: 1px solid rgba(201, 168, 76, 0.12);
}
.summary-title {
  font-family: 'Playfair Display', serif;
  font-size: 1.3rem;
  font-weight: 700;
  color: #F7F0E6;
  letter-spacing: -0.02em;
  margin-bottom: 24px;
}
.summary-rows {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 20px;
}
.summary-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.875rem;
  color: rgba(247, 240, 230, 0.55);
}
.free-tag {
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #7A9E7E;
  background: rgba(122, 158, 126, 0.12);
  padding: 2px 8px;
  border-radius: 3px;
}

.summary-divider { margin: 4px 0 20px; opacity: 0.8; }

.summary-total {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  margin-bottom: 24px;
}
.summary-total span {
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: rgba(247, 240, 230, 0.5);
}
.summary-total strong {
  font-family: 'Playfair Display', serif;
  font-size: 1.8rem;
  font-weight: 700;
  color: #F7F0E6;
  letter-spacing: -0.03em;
}

.checkout-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  width: 100%;
  background: #C9A84C;
  color: #1A2233;
  border: none;
  padding: 15px 20px;
  border-radius: 5px;
  font-family: 'Inter', sans-serif;
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0.07em;
  text-transform: uppercase;
  cursor: pointer;
  transition: background 0.2s, transform 0.15s;
  margin-bottom: 16px;
}
.checkout-btn:hover { background: #E8C96A; transform: translateY(-1px); }

.summary-note {
  font-size: 0.72rem;
  font-weight: 300;
  line-height: 1.6;
  color: rgba(247, 240, 230, 0.3);
  text-align: center;
}

/* ── RESPONSIVE ── */
@media (max-width: 860px) {
  .cart-layout { grid-template-columns: 1fr; }
  .cart-summary-col { position: static; }
  .cart-page { padding: 40px 20px 80px; }
}
@media (max-width: 540px) {
  .cart-item { flex-wrap: wrap; }
  .item-right { flex-direction: row; align-items: center; width: 100%; justify-content: space-between; }
}
</style>