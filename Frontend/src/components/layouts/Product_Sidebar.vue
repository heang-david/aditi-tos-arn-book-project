<template>
  <div>
    <aside class="sidebar">

      <!-- header -->
      <div class="sidebar-header">
        <div class="sidebar-eyebrow">
          <svg width="20" height="1" viewBox="0 0 20 1"><line x1="0" y1="0.5" x2="20" y2="0.5" stroke="#C9A84C" stroke-width="1"/></svg>
          Browse
          <svg width="20" height="1" viewBox="0 0 20 1"><line x1="0" y1="0.5" x2="20" y2="0.5" stroke="#C9A84C" stroke-width="1"/></svg>
        </div>
        <h2>Categories</h2>
      </div>

      <!-- category list -->
      <ul class="category-list">
        <li
          v-for="category in categories"
          :key="category.name"
          class="category-item"
          :class="{ active: selected === category.name }"
          @click="selected = category.name"
        >
          <span class="cat-icon">{{ category.icon }}</span>
          <span class="cat-name">{{ category.name }}</span>
          <svg class="cat-arrow" width="12" height="12" viewBox="0 0 12 12" fill="none">
            <path d="M2 6h8M6 2.5l3.5 3.5L6 9.5" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </li>
      </ul>

      <!-- divider -->
      <div class="sidebar-divider">
        <svg viewBox="0 0 220 30" xmlns="http://www.w3.org/2000/svg">
          <line x1="0" y1="15" x2="82" y2="15" stroke="#C9A84C" stroke-width="0.7" opacity="0.4"/>
          <g transform="translate(93, 3)">
            <path d="M17 4 C13 3 4 5 0 8 L0 18 C4 15 13 13 17 14 C21 13 30 15 34 18 L34 8 C30 5 21 3 17 4Z"
              fill="none" stroke="#C9A84C" stroke-width="1"/>
            <line x1="17" y1="4" x2="17" y2="14" stroke="#C9A84C" stroke-width="1"/>
          </g>
          <line x1="138" y1="15" x2="220" y2="15" stroke="#C9A84C" stroke-width="0.7" opacity="0.4"/>
        </svg>
      </div>

      <!-- stats block -->
      <div class="sidebar-stats">
        <div class="stat-row">
          <span class="stat-label">Total titles</span>
          <span class="stat-value">40,000+</span>
        </div>
        <div class="stat-row">
          <span class="stat-label">New this week</span>
          <span class="stat-value">124</span>
        </div>
      </div>

      <!-- CTA -->
      <a href="#" class="sidebar-cta">
        View all books
        <svg width="13" height="13" viewBox="0 0 13 13" fill="none">
          <path d="M2 6.5h9M7 2.5l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </a>

    </aside>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const selected = ref('Fiction')

const categories = ref([
  { name: 'Fiction', },
  { name: 'Fantasy',          },
  { name: 'Mystery',          },
  { name: 'Romance',          },
  { name: 'Thriller',         },
  { name: 'History',          },
  { name: 'Biography',        },
  { name: 'Programming',        },
  { name: 'Business',         },
  { name: 'Poetry',  },
  { name: 'Travel',           },
])
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,600;0,700;1,400&family=Inter:wght@300;400;500;600&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

.sidebar {
  width: 260px;
  background: #1A2233;
  border-radius: 12px;
  padding: 28px 22px;
  box-shadow: 0 12px 40px rgba(26, 34, 51, 0.25);
  align-self: flex-start;
  position: sticky;        /* ← was: fixed */
  top: 24px;               /* ← sticks 24px from the top of the viewport */
  max-height: calc(100vh - 48px);  /* ← prevents it from growing taller than the screen */
  overflow-y: auto;        /* ← lets the sidebar scroll internally if needed */
  scrollbar-width: none;   /* ← hides the scrollbar in Firefox */
  font-family: 'Inter', system-ui, sans-serif;
  border: 1px solid rgba(201, 168, 76, 0.12);
}
.sidebar::-webkit-scrollbar { display: none; } /* ← hides scrollbar in Chrome/Safari */

/* HEADER */
.sidebar-header { margin-bottom: 22px; }

.sidebar-eyebrow {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.6rem;
  font-weight: 600;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #C9A84C;
  margin-top: 32px;
  margin-bottom: 8px;
  opacity: 0.8;
}

.sidebar-header h2 {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 1.3rem;
  font-weight: 700;
  color: #F7F0E6;
  letter-spacing: -0.02em;
}

/* LIST */
.category-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 2px;
  margin-bottom: 20px;
}

.category-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 9px 12px;
  border-radius: 6px;
  cursor: pointer;
  border: 1px solid transparent;
  transition: background 0.18s, border-color 0.18s;
}

.category-item:hover {
  background: rgba(201, 168, 76, 0.08);
  border-color: rgba(201, 168, 76, 0.18);
}

.category-item.active {
  background: rgba(201, 168, 76, 0.13);
  border-color: rgba(201, 168, 76, 0.35);
}

.category-item.active .cat-name { color: #F7F0E6; font-weight: 600; }
.category-item.active .cat-arrow { color: #C9A84C; opacity: 1; transform: translateX(2px); }

.cat-icon {
  font-size: 0.95rem;
  flex-shrink: 0;
  width: 18px;
  text-align: center;
}

.cat-name {
  flex: 1;
  font-size: 0.845rem;
  font-weight: 400;
  color: rgba(247, 240, 230, 0.6);
  transition: color 0.18s;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.category-item:hover .cat-name { color: rgba(247, 240, 230, 0.9); }

.cat-count {
  font-size: 0.65rem;
  font-weight: 600;
  color: rgba(201, 168, 76, 0.55);
  letter-spacing: 0.04em;
  flex-shrink: 0;
}

.cat-arrow {
  color: rgba(247, 240, 230, 0.2);
  flex-shrink: 0;
  opacity: 0;
  transition: opacity 0.18s, transform 0.18s, color 0.18s;
}
.category-item:hover .cat-arrow { opacity: 1; transform: translateX(2px); }

/* DIVIDER */
.sidebar-divider {
  margin: 4px 0 18px;
  opacity: 0.7;
}

/* STATS */
.sidebar-stats {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 20px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(247, 240, 230, 0.06);
  border-radius: 6px;
  padding: 14px 14px;
}
.stat-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.stat-label {
  font-size: 0.72rem;
  font-weight: 400;
  color: rgba(247, 240, 230, 0.35);
  letter-spacing: 0.04em;
}
.stat-value {
  font-family: 'Playfair Display', serif;
  font-size: 0.9rem;
  font-weight: 700;
  color: #C9A84C;
  letter-spacing: -0.01em;
}

/* CTA */
.sidebar-cta {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  text-decoration: none;
  font-size: 0.75rem;
  font-weight: 700;
  letter-spacing: 0.07em;
  text-transform: uppercase;
  color: #1A2233;
  background: #C9A84C;
  padding: 11px 16px;
  border-radius: 5px;
  transition: background 0.2s, transform 0.15s;
}
.sidebar-cta:hover { background: #E8C96A; transform: translateY(-1px); }
</style>