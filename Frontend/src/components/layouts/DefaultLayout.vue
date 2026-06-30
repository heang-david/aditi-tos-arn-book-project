<!-- layouts/DefaultLayout.vue -->
<template>
  <nav class="nav">
    <div class="nav-inner">
      <a href="#" class="logo">
        <span class="logo-icon">📖</span>
        <span class="logo-text">Tos arn<em>Books</em></span>
      </a>
      <ul class="nav-links">
        <router-link to="/">Home</router-link>
        <router-link to="/about">About</router-link>
        <router-link to="/products">Products</router-link>
        <router-link to="/contact">Contact</router-link>
      </ul>
      <router-link to="/cart" class="cart-icon">
        🛒
        <span v-if="cartStore.totalItems > 0" class="cart-badge">
          {{ cartStore.totalItems }}
        </span>
      </router-link>
    </div>
  </nav>

  <RouterView />

  <Footer />
</template>

<script setup>
import { useCartStore } from '@/stores/cart'
import Footer from '@/components/layouts/Footer.vue'

const cartStore = useCartStore()
</script>

<style scoped>
.nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  background: rgba(247, 240, 230, 0.92);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid var(--ash);
}
.nav-inner {
  max-width: 1160px;
  margin: 0 auto;
  padding: 0 32px;
  height: 64px;
  display: flex;
  align-items: center;
  gap: 40px;
}
.logo {
  display: flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
  color: var(--navy);
  font-family: var(--ff-disp);
  font-size: 1.2rem;
  font-weight: 600;
  letter-spacing: -0.02em;
}
.logo-icon {
  font-size: 1.3rem;
}
.logo-text em {
  font-style: italic;
  color: var(--gold);
  margin-left: 3px;
}
.nav-links {
  display: flex;
  list-style: none;
  gap: 28px;
  margin-left: auto;
}
.nav-links a {
  text-decoration: none;
  color: var(--muted);
  font-size: 0.875rem;
  font-weight: 500;
  letter-spacing: 0.01em;
  transition: color 0.2s;
}

.nav-links a:hover,
.nav-links a.active {
  color: var(--navy);
}
.nav-links a.active {
  font-weight: 600;
}
.nav-cta {
  text-decoration: none;
  background: var(--navy);
  color: var(--parch);
  padding: 9px 20px;
  border-radius: 4px;
  font-size: 0.8rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  transition: background 0.2s;
  white-space: nowrap;
}
.nav-cta:hover {
  background: var(--gold);
  color: var(--navy);
}

.cart-icon {
  position: relative;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  text-decoration: none;
  font-size: 1.3rem;
  padding: 8px;
  border-radius: 8px;
  transition: background 0.2s;
}

.cart-icon:hover {
  background: rgba(201, 168, 76, 0.1);
}

.cart-badge {
  position: absolute;
  top: 0px;
  right: 0px;
  background: #C9A84C;
  color: #1A2233;
  font-family: 'Inter', sans-serif;
  font-size: 0.6rem;
  font-weight: 700;
  letter-spacing: 0.03em;
  min-width: 18px;
  height: 18px;
  padding: 0 4px;
  border-radius: 999px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 2px 6px rgba(201, 168, 76, 0.45);
  animation: badgePop 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

@keyframes badgePop {
  from { transform: scale(0); opacity: 0; }
  to   { transform: scale(1); opacity: 1; }
}
</style>
