<template>
  <div style="align-self: stretch;">
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
          v-for="cat in categories"
          :key="cat"
          class="category-item"
          :class="{ active: modelValue === cat }"
          @click="select(cat)"
        >
          <span class="cat-name">{{ cat }}</span>
          <span class="cat-count" v-if="countFor(cat) > 0">{{ countFor(cat) }}</span>
          <svg class="cat-arrow" width="12" height="12" viewBox="0 0 12 12" fill="none">
            <path d="M2 6h8M6 2.5l3.5 3.5L6 9.5" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>
          </svg>
        </li>
      </ul>

    </aside>
  </div>
</template>

<script setup>
import { useBookStore } from '@/stores/book'

const props = defineProps({ modelValue: { type: String, default: '' } })
const emit  = defineEmits(['update:modelValue'])

const bookStore = useBookStore()

const categories = [
  'Fiction', 'Fantasy', 'Mystery', 'Romance', 'Thriller',
  'History', 'Biography', 'Programming', 'Business', 'Poetry', 'Travel',
]

function countFor(cat) {
  return bookStore.books.filter(b => b.genre?.toLowerCase() === cat.toLowerCase()).length
}

function select(cat) {
  emit('update:modelValue', props.modelValue === cat ? '' : cat)
}
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

</style>