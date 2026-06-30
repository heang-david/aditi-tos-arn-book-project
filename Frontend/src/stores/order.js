// stores/order.js
import { defineStore } from "pinia"
import axios from "axios"
import { ref } from "vue"

export const useOrderStore = defineStore("orderStore", () => {
  const orders = ref([])
  const loading = ref(false)
  const error = ref(null)

  function fetchOrders() {
    loading.value = true
    error.value = null
    return axios.get("http://127.0.0.1:8000/api/orders/")
      .then(response => {
        orders.value = response.data
      })
      .catch(err => {
        error.value = err.message || "Failed to fetch orders."
      })
      .finally(() => {
        loading.value = false
      })
  }

  function updateOrderStatus(orderId, status) {
    return axios.patch(`http://127.0.0.1:8000/api/orders/${orderId}/status`, { status })
      .then(response => {
        const index = orders.value.findIndex(o => o.id === orderId)
        if (index !== -1) orders.value[index] = response.data
      })
  }

  return { orders, loading, error, fetchOrders, updateOrderStatus }
})