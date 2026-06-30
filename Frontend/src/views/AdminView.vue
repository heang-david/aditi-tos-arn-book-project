<!-- views/AdminView.vue -->
<template>
  <div class="admin-page">

    <div class="admin-header">
      <div class="section-eyebrow">
        <svg width="28" height="1" viewBox="0 0 28 1"><line x1="0" y1="0.5" x2="28" y2="0.5" stroke="#C9A84C" stroke-width="1"/></svg>
        Dashboard
      </div>
      <h1 class="admin-title">Admin Panel</h1>
    </div>

    <div class="admin-actions">
        <button @click="addNewBook">
            Add New Book
        </button>
        <button @click="updateStock">
            Update Stock to book
        </button>
    </div>

    <!-- tabs -->
    <div class="admin-tabs">
      <button :class="{ active: tab === 'books' }" @click="tab = 'books'">
        Books ({{ bookStore.books.length }})
      </button>
      <button :class="{ active: tab === 'orders' }" @click="tab = 'orders'">
        Orders ({{ orderStore.orders.length }})
      </button>
    </div>

    <!-- BOOKS TABLE -->
    <div v-if="tab === 'books'" class="admin-table-wrap">
      <table class="admin-table">
        <thead>
          <tr>
            <th>Cover</th>
            <th>Title</th>
            <th>Author</th>
            <th>Genre</th>
            <th>Price</th>
            <th>Stock</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="book in bookStore.books" :key="book.id">
            <td><img :src="book.image_url" class="table-cover" /></td>
            <td>{{ book.title }}</td>
            <td>{{ book.author }}</td>
            <td>{{ book.genre }}</td>
            <td>${{ book.price }}</td>
            <td>
              <span class="stock-pill" :class="{ low: book.stock <= 5, out: book.stock === 0 }">
                {{ book.stock }}
              </span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- ORDERS TABLE -->
    <div v-if="tab === 'orders'" class="admin-table-wrap">
      <table class="admin-table">
        <thead>
          <tr>
            <th>Order #</th>
            <th>Customer</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Items</th>
            <th>Total</th>
            <th>Status</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="order in orderStore.orders" :key="order.id">
            <td>#{{ order.id }}</td>
            <td>{{ order.customer_name }}</td>
            <td>{{ order.email }}</td>
            <td>{{ order.phone }}</td>
            <td>{{ order.items.length }} items</td>
            <td>${{ order.total_price.toFixed(2) }}</td>
            <td>
              <select :value="order.status" @change="updateStatus(order.id, $event.target.value)">
                <option value="pending">Pending</option>
                <option value="confirmed">Confirmed</option>
                <option value="shipped">Shipped</option>
                <option value="delivered">Delivered</option>
                <option value="cancelled">Cancelled</option>
              </select>
            </td>
            <td>{{ new Date(order.created_at).toLocaleDateString() }}</td>
          </tr>
        </tbody>
      </table>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from "vue"
import { useBookStore } from "@/stores/book"
import { useOrderStore } from "@/stores/order"

const bookStore  = useBookStore()
const orderStore = useOrderStore()
const tab = ref("books")

onMounted(() => {
  bookStore.fetchBooks()
  orderStore.fetchOrders()
})

function updateStatus(orderId, status) {
  orderStore.updateOrderStatus(orderId, status)
}
</script>

<style scoped>
.admin-page { padding: 40px; background: #F7F0E6; min-height: 100vh; font-family: 'Inter', sans-serif; }

.section-eyebrow {
  font-size: 0.65rem; font-weight: 600; letter-spacing: 0.18em;
  text-transform: uppercase; color: #C9A84C; margin-bottom: 8px;
}
.admin-title {
  font-family: 'Playfair Display', serif; font-size: 2rem; font-weight: 700;
  color: #1A2233; letter-spacing: -0.02em; margin-bottom: 24px;
}

.admin-actions { display: flex; gap: 8px; margin-bottom: 24px; }
.admin-actions button {
  padding: 10px 20px; border-radius: 20px; border: 1.5px solid #E8E1D9;
  background: transparent; color: black; font-size: 1rem; font-weight: 800;
  cursor: pointer; transition: all 0.2s;
}

.admin-tabs { display: flex; gap: 8px; margin-bottom: 24px; }
.admin-tabs button {
  padding: 10px 20px; border-radius: 20px; border: 1.5px solid #E8E1D9;
  background: transparent; color: #6B6560; font-size: 0.85rem; font-weight: 600;
  cursor: pointer; transition: all 0.2s;
}
.admin-tabs button.active { background: #1A2233; border-color: #1A2233; color: #F7F0E6; }

.admin-table-wrap { background: #fff; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 16px rgba(26,34,51,0.06); }
.admin-table { width: 100%; border-collapse: collapse; }
.admin-table th {
  text-align: left; padding: 14px 16px; font-size: 0.7rem; font-weight: 700;
  letter-spacing: 0.08em; text-transform: uppercase; color: #9B9590;
  border-bottom: 1.5px solid #E8E1D9;
}
.admin-table td { padding: 14px 16px; font-size: 0.85rem; color: #1A2233; border-bottom: 1px solid #F0EAE0; }
.table-cover { width: 32px; height: 44px; object-fit: cover; border-radius: 3px; }

.stock-pill { padding: 3px 10px; border-radius: 12px; background: rgba(122,158,126,0.15); color: #5A7E5E; font-weight: 600; font-size: 0.78rem; }
.stock-pill.low { background: rgba(201,168,76,0.15); color: #A88830; }
.stock-pill.out { background: rgba(192,69,74,0.15); color: #C0454A; }

select { padding: 6px 10px; border-radius: 5px; border: 1px solid #E8E1D9; font-size: 0.8rem; }
</style>