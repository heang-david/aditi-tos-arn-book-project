import { defineStore } from 'pinia'
import { ref, computed } from 'vue'

export const useCartStore = defineStore('cart', () => {

  // --- STATE ---
  const items = ref(JSON.parse(localStorage.getItem('tosarn-cart') || '[]'))

  // --- PERSIST to localStorage on every change ---
  function persist() {
    localStorage.setItem('tosarn-cart', JSON.stringify(items.value))
  }

  // --- GETTERS ---
  const totalItems = computed(() =>
    items.value.reduce((sum, item) => sum + item.quantity, 0)
  )

  const totalPrice = computed(() =>
    items.value.reduce((sum, item) => sum + item.price * item.quantity, 0)
  )

  const isEmpty = computed(() => items.value.length === 0)

  // --- ACTIONS ---
  function addToCart(book) {
    const existing = items.value.find(i => i.id === book.id)
    if (existing) {
      existing.quantity++
    } else {
      items.value.push({ ...book, quantity: 1 })
    }
    persist()
  }

  function removeFromCart(bookId) {
    items.value = items.value.filter(i => i.id !== bookId)
    persist()
  }

  function updateQuantity(bookId, quantity) {
    if (quantity < 1) return removeFromCart(bookId)
    const item = items.value.find(i => i.id === bookId)
    if (item) item.quantity = quantity
    persist()
  }

  function clearCart() {
    items.value = []
    persist()
  }

  function isInCart(bookId) {
    return items.value.some(i => i.id === bookId)
  }

  return {
    items, totalItems, totalPrice, isEmpty,
    addToCart, removeFromCart, updateQuantity, clearCart, isInCart
  }
})