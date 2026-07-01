<!-- views/AdminView.vue -->
<template>
  <div class="admin-page">

    <div class="admin-actions">
      <button @click="showAddModal = true">+ Add New Book</button>
    </div>

    <!-- search + filter row -->
    <div class="search-filter-row">
      <SearchBar
        v-model="searchQuery"
        :placeholder="tab === 'books' ? 'Search by title, author or genre…' : 'Search by customer name or email…'"
        class="admin-search"
      />
      <select v-if="tab === 'books'" v-model="sortBy" class="filter-select">
        <option value="">Sort by</option>
        <option value="price_asc">Price: Low → High</option>
        <option value="price_desc">Price: High → Low</option>
        <option value="stock_asc">Stock: Low → High</option>
        <option value="stock_desc">Stock: High → Low</option>
      </select>
    </div>

    <!-- tabs -->
    <div class="admin-tabs">
      <button :class="{ active: tab === 'books' }" @click="tab = 'books'">
        Books ({{ bookStore.books.length }})
      </button>
      <button :class="{ active: tab === 'orders' }" @click="tab = 'orders'">
        Orders ({{ orderStore.orders.length }})
      </button>
      <button :class="{ active: tab === 'users' }" @click="switchToUsers">
        Admins ({{ adminUsers.length }})
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
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="book in filteredBooks" :key="book.id">
            <td><img :src="book.image_url" class="table-cover" /></td>
            <td>{{ book.title }}</td>
            <td>{{ book.author }}</td>
            <td>{{ book.genre }}</td>
            <td>${{ book.price }}</td>
            <td>
              <span
                class="stock-pill"
                :class="{ low: book.stock <= 5, out: book.stock === 0 }"
              >
                {{ book.stock }}
              </span>
            </td>
            <td>
              <button class="view-btn" @click="openAddStock(book)">Add Stock</button>
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
            <th>Items</th>
            <th>Total</th>
            <th>Status</th>
            <th>Date</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="order in filteredOrders" :key="order.id">
            <td>#{{ order.id }}</td>
            <td>{{ order.customer_name }}</td>
            <td>{{ order.email }}</td>
            <td>{{ order.items.length }} item{{ order.items.length !== 1 ? 's' : '' }}</td>
            <td>${{ order.total_price.toFixed(2) }}</td>
            <td>
              <span class="status-pill" :class="order.status">{{ order.status }}</span>
            </td>
            <td>{{ new Date(order.created_at).toLocaleDateString() }}</td>
            <td>
              <button class="view-btn" @click="openOrderDetail(order)">View</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!-- ADMIN USERS TABLE -->
    <div v-if="tab === 'users'" class="admin-table-wrap">
      <div class="users-toolbar">
        <SearchBar v-model="userSearch" placeholder="Search admins…" class="user-search" />
        <button class="btn-add-admin" @click="showCreateAdminModal = true">+ New Admin</button>
      </div>
      <table class="admin-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Username</th>
            <th>Status</th>
            <th>Created</th>
          </tr>
        </thead>
        <tbody>
          <tr v-if="usersLoading">
            <td colspan="4" class="table-loading">Loading…</td>
          </tr>
          <tr v-else-if="filteredAdminUsers.length === 0">
            <td colspan="4" class="table-empty">No admins found.</td>
          </tr>
          <tr v-for="u in filteredAdminUsers" :key="u.id">
            <td>#{{ u.id }}</td>
            <td><strong>{{ u.username }}</strong></td>
            <td>
              <span class="status-pill" :class="u.is_active ? 'delivered' : 'cancelled'">
                {{ u.is_active ? 'Active' : 'Inactive' }}
              </span>
            </td>
            <td>{{ new Date(u.created_at).toLocaleDateString() }}</td>
          </tr>
        </tbody>
      </table>
    </div>

  </div>

  <!-- CREATE ADMIN MODAL -->
  <div v-if="showCreateAdminModal" class="modal-backdrop" @click.self="closeCreateAdminModal">
    <div class="modal modal-sm">
      <div class="modal-header">
        <h2 class="modal-title">New Admin</h2>
        <button class="modal-close" @click="closeCreateAdminModal">✕</button>
      </div>
      <form class="modal-form" @submit.prevent="submitCreateAdmin">
        <div class="form-row">
          <label>Username <span class="required">*</span></label>
          <input v-model="newAdmin.username" type="text" placeholder="username" required />
        </div>
        <div class="form-row">
          <label>Password <span class="required">*</span></label>
          <input v-model="newAdmin.password" type="password" placeholder="••••••••" required minlength="6" />
        </div>
        <p v-if="adminFormError" class="form-error">{{ adminFormError }}</p>
        <div class="modal-actions">
          <button type="button" class="btn-cancel" @click="closeCreateAdminModal">Cancel</button>
          <button type="submit" class="btn-primary" :disabled="adminSubmitting">
            {{ adminSubmitting ? 'Creating…' : 'Create Admin' }}
          </button>
        </div>
      </form>
    </div>
  </div>

  <!-- ORDER DETAIL MODAL -->
  <div v-if="showOrderModal && selectedOrder" class="modal-backdrop" @click.self="showOrderModal = false">
    <div class="modal modal-order">
      <div class="modal-header">
        <div>
          <h2 class="modal-title">Order #{{ selectedOrder.id }}</h2>
          <span class="order-date">{{ new Date(selectedOrder.created_at).toLocaleString() }}</span>
        </div>
        <button class="modal-close" @click="showOrderModal = false">✕</button>
      </div>

      <div class="order-body">

        <!-- Customer info -->
        <div class="order-section">
          <h3 class="order-section-title">Customer</h3>
          <div class="info-grid">
            <div class="info-item"><span class="info-label">Name</span><span>{{ selectedOrder.customer_name }}</span></div>
            <div class="info-item"><span class="info-label">Email</span><span>{{ selectedOrder.email }}</span></div>
            <div class="info-item"><span class="info-label">Phone</span><span>{{ selectedOrder.phone }}</span></div>
            <div class="info-item info-full"><span class="info-label">Address</span><span>{{ selectedOrder.address }}</span></div>
          </div>
        </div>

        <!-- Items -->
        <div class="order-section">
          <h3 class="order-section-title">Items</h3>
          <table class="order-items-table">
            <thead>
              <tr>
                <th>Book</th>
                <th>Unit Price</th>
                <th>Qty</th>
                <th>Subtotal</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in selectedOrder.items" :key="item.id">
                <td>{{ bookTitle(item.book_id) }}</td>
                <td>${{ item.unit_price.toFixed(2) }}</td>
                <td>{{ item.quantity }}</td>
                <td>${{ (item.unit_price * item.quantity).toFixed(2) }}</td>
              </tr>
            </tbody>
          </table>
          <div class="order-total">
            <span>Total</span>
            <span class="order-total-price">${{ selectedOrder.total_price.toFixed(2) }}</span>
          </div>
        </div>

        <!-- Status -->
        <div class="order-section">
          <h3 class="order-section-title">Status</h3>
          <div class="status-row">
            <span class="status-pill" :class="selectedOrder.status">{{ selectedOrder.status }}</span>
            <select :value="selectedOrder.status" @change="changeOrderStatus(selectedOrder.id, $event.target.value)">
              <option value="pending">Pending</option>
              <option value="confirmed">Confirmed</option>
              <option value="shipped">Shipped</option>
              <option value="delivered">Delivered</option>
              <option value="cancelled">Cancelled</option>
            </select>
          </div>
        </div>

      </div>
    </div>
  </div>

  <!-- ADD BOOK MODAL -->
  <div v-if="showAddModal" class="modal-backdrop" @click.self="closeAddModal">
    <div class="modal">
      <div class="modal-header">
        <h2 class="modal-title">Add New Book</h2>
        <button class="modal-close" @click="closeAddModal">✕</button>
      </div>
      <form class="modal-form" @submit.prevent="submitAddBook">
        <div class="form-row">
          <label>Title <span class="required">*</span></label>
          <input
            v-model="newBook.title"
            type="text"
            placeholder="Book title"
            required
          />
        </div>
        <div class="form-row">
          <label>Author</label>
          <input
            v-model="newBook.author"
            type="text"
            placeholder="Author name"
          />
        </div>
        <div class="form-row">
          <label>Genre</label>
          <input
            v-model="newBook.genre"
            type="text"
            placeholder="e.g. Fiction, Science"
          />
        </div>
        <div class="form-grid">
          <div class="form-row">
            <label>Price ($)</label>
            <input
              v-model.number="newBook.price"
              type="number"
              step="0.01"
              min="0"
              placeholder="0.00"
            />
          </div>
          <div class="form-row">
            <label>Stock</label>
            <input
              v-model.number="newBook.stock"
              type="number"
              min="0"
              placeholder="0"
            />
          </div>
        </div>
        <div class="form-row">
          <label>Cover Image URL</label>
          <input
            v-model="newBook.image_url"
            type="url"
            placeholder="https://..."
          />
        </div>
        <div class="form-row">
          <label>Description</label>
          <textarea
            v-model="newBook.description"
            rows="3"
            placeholder="Short description…"
          ></textarea>
        </div>
        <p v-if="formError" class="form-error">{{ formError }}</p>
        <div class="modal-actions">
          <button type="button" class="btn-cancel" @click="closeAddModal">
            Cancel
          </button>
          <button type="submit" class="btn-primary" :disabled="submitting">
            {{ submitting ? "Saving…" : "Add Book" }}
          </button>
        </div>
      </form>
    </div>
  </div>

  <!-- ADD STOCK MODAL (inline per-book) -->
  <div v-if="showAddStockModal && addStockTarget" class="modal-backdrop" @click.self="closeAddStock">
    <div class="modal modal-sm">
      <div class="modal-header">
        <h2 class="modal-title">Add Stock</h2>
        <button class="modal-close" @click="closeAddStock">✕</button>
      </div>
      <form class="modal-form" @submit.prevent="submitAddStock">
        <div class="add-stock-book">
          <img v-if="addStockTarget.image_url" :src="addStockTarget.image_url" class="add-stock-cover" />
          <div>
            <p class="add-stock-title">{{ addStockTarget.title }}</p>
            <p class="add-stock-current">Current stock: <strong>{{ addStockTarget.stock }}</strong></p>
          </div>
        </div>
        <div class="form-row">
          <label>Quantity to add <span class="required">*</span></label>
          <input
            v-model.number="addStockQty"
            type="number"
            min="1"
            placeholder="e.g. 10"
            required
            autofocus
          />
          <p v-if="addStockQty > 0" class="add-stock-preview">
            New stock will be <strong>{{ addStockTarget.stock + addStockQty }}</strong>
          </p>
        </div>
        <p v-if="addStockError" class="form-error">{{ addStockError }}</p>
        <div class="modal-actions">
          <button type="button" class="btn-cancel" @click="closeAddStock">Cancel</button>
          <button type="submit" class="btn-primary" :disabled="addStockSaving">
            {{ addStockSaving ? 'Saving…' : 'Add Stock' }}
          </button>
        </div>
      </form>
    </div>
  </div>

  <!-- UPDATE STOCK MODAL -->
  <div
    v-if="showStockModal"
    class="modal-backdrop"
    @click.self="closeStockModal"
  >
    <div class="modal modal-sm">
      <div class="modal-header">
        <h2 class="modal-title">Update Stock</h2>
        <button class="modal-close" @click="closeStockModal">✕</button>
      </div>
      <form class="modal-form" @submit.prevent="submitUpdateStock">
        <div class="form-row">
          <label>Book <span class="required">*</span></label>
          <select v-model="stockEdit.bookId" required>
            <option value="" disabled>Select a book…</option>
            <option
              v-for="book in bookStore.books"
              :key="book.id"
              :value="book.id"
            >
              {{ book.title }} (current: {{ book.stock }})
            </option>
          </select>
        </div>
        <div class="form-row">
          <label>New Stock <span class="required">*</span></label>
          <input
            v-model.number="stockEdit.stock"
            type="number"
            min="0"
            placeholder="0"
            required
          />
        </div>
        <p v-if="formError" class="form-error">{{ formError }}</p>
        <div class="modal-actions">
          <button type="button" class="btn-cancel" @click="closeStockModal">
            Cancel
          </button>
          <button type="submit" class="btn-primary" :disabled="submitting">
            {{ submitting ? "Saving…" : "Update Stock" }}
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import { useBookStore } from "@/stores/book";
import { useOrderStore } from "@/stores/order";
import { useAuthStore } from "@/stores/auth";
import SearchBar from "@/components/ui/SearchBar.vue";
import axios from "axios";

const bookStore  = useBookStore();
const orderStore = useOrderStore();
const authStore  = useAuthStore();
const tab = ref("books");
const searchQuery = ref("");

// ── Order detail modal ─────────────────────────────────────
const showOrderModal = ref(false)
const selectedOrder  = ref(null)

function openOrderDetail(order) {
  selectedOrder.value = order
  showOrderModal.value = true
}

// order details 
function bookTitle(bookId) {
  return bookStore.books.find(b => b.id === bookId)?.title ?? `Book #${bookId}`
}

function changeOrderStatus(orderId, status) {
  orderStore.updateOrderStatus(orderId, status)
  // keep selectedOrder in sync
  if (selectedOrder.value?.id === orderId) {
    selectedOrder.value = { ...selectedOrder.value, status }
  }
}

// ── Add Book modal ──────────────────────────────────────────
const showAddModal = ref(false);
const submitting = ref(false);
const formError = ref("");
const newBook = ref({
  title: "",
  author: "",
  genre: "",
  price: null,
  stock: 0,
  image_url: "",
  description: "",
});

function closeAddModal() {
  showAddModal.value = false;
  formError.value = "";
  newBook.value = {
    title: "",
    author: "",
    genre: "",
    price: null,
    stock: 0,
    image_url: "",
    description: "",
  };
}


async function submitAddBook() {
  formError.value = "";
  submitting.value = true;
  try {
    await bookStore.createBook(newBook.value);
    closeAddModal();
  } catch (e) {
    formError.value = e.response?.data?.detail || "Failed to add book.";
  } finally {
    submitting.value = false;
  }
}

// ── Add Stock modal (per-book inline) ──────────────────────
const showAddStockModal = ref(false)
const addStockTarget    = ref(null)
const addStockQty       = ref(1)
const addStockSaving    = ref(false)
const addStockError     = ref("")

function openAddStock(book) {
  addStockTarget.value = book
  addStockQty.value    = 1
  addStockError.value  = ""
  showAddStockModal.value = true
}

function closeAddStock() {
  showAddStockModal.value = false
  addStockTarget.value    = null
  addStockError.value     = ""
}

async function submitAddStock() {
  addStockError.value  = ""
  addStockSaving.value = true
  try {
    const newStock = addStockTarget.value.stock + addStockQty.value
    await bookStore.updateBookStock(addStockTarget.value.id, newStock)
    closeAddStock()
  } catch (e) {
    addStockError.value = e.response?.data?.detail || "Failed to update stock."
  } finally {
    addStockSaving.value = false
  }
}

// ── Update Stock modal ──────────────────────────────────────
const showStockModal = ref(false);
const stockEdit = ref({ bookId: "", stock: 0 });

function closeStockModal() {
  showStockModal.value = false;
  formError.value = "";
  stockEdit.value = { bookId: "", stock: 0 };
}

async function submitUpdateStock() {
  formError.value = "";
  submitting.value = true;
  try {
    await bookStore.updateBookStock(
      stockEdit.value.bookId,
      stockEdit.value.stock,
    );
    closeStockModal();
  } catch (e) {
    formError.value = e.response?.data?.detail || "Failed to update stock.";
  } finally {
    submitting.value = false;
  }
}

const sortBy = ref("")

const filteredBooks = computed(() => {
  const q = searchQuery.value.toLowerCase();
  let list = q
    ? bookStore.books.filter(
        (b) =>
          b.title.toLowerCase().includes(q) ||
          b.author.toLowerCase().includes(q) ||
          (b.genre && b.genre.toLowerCase().includes(q)),
      )
    : [...bookStore.books];

  if (sortBy.value === "price_asc")  list.sort((a, b) => a.price - b.price);
  if (sortBy.value === "price_desc") list.sort((a, b) => b.price - a.price);
  if (sortBy.value === "stock_asc")  list.sort((a, b) => a.stock - b.stock);
  if (sortBy.value === "stock_desc") list.sort((a, b) => b.stock - a.stock);

  return list;
});

const filteredOrders = computed(() => {
  const q = searchQuery.value.toLowerCase();
  if (!q) return orderStore.orders;
  return orderStore.orders.filter(
    (o) =>
      o.customer_name.toLowerCase().includes(q) ||
      o.email.toLowerCase().includes(q),
  );
});

onMounted(() => {
  bookStore.fetchBooks();
  orderStore.fetchOrders();
});

function updateStatus(orderId, status) {
  orderStore.updateOrderStatus(orderId, status);
}

// ── Admin Users tab ────────────────────────────────────────
const adminUsers   = ref([])
const usersLoading = ref(false)
const userSearch   = ref("")

const filteredAdminUsers = computed(() => {
  const q = userSearch.value.toLowerCase()
  if (!q) return adminUsers.value
  return adminUsers.value.filter(u => u.username.toLowerCase().includes(q))
})

async function fetchAdminUsers() {
  usersLoading.value = true
  try {
    const res = await axios.get("http://127.0.0.1:8000/api/admin/users", authStore.authHeaders())
    adminUsers.value = res.data
  } catch {
    adminUsers.value = []
  } finally {
    usersLoading.value = false
  }
}

function switchToUsers() {
  tab.value = "users"
  if (adminUsers.value.length === 0) fetchAdminUsers()
}

// ── Create Admin modal ─────────────────────────────────────
const showCreateAdminModal = ref(false)
const adminSubmitting      = ref(false)
const adminFormError       = ref("")
const newAdmin = ref({ username: "", password: "" })

function closeCreateAdminModal() {
  showCreateAdminModal.value = false
  adminFormError.value = ""
  newAdmin.value = { username: "", password: "" }
}

async function submitCreateAdmin() {
  adminFormError.value = ""
  adminSubmitting.value = true
  try {
    await axios.post("http://127.0.0.1:8000/api/admin/", newAdmin.value, authStore.authHeaders())
    await fetchAdminUsers()
    closeCreateAdminModal()
  } catch (e) {
    adminFormError.value = e.response?.data?.detail || "Failed to create admin."
  } finally {
    adminSubmitting.value = false
  }
}
</script>

<style scoped>
.admin-page {
  padding: 24px;
  background: #f7f0e6;
  min-height: 100vh;
  font-family: "Inter", sans-serif;
}

.admin-actions {
  display: flex;
  gap: 8px;
  margin-bottom: 24px;
}
.admin-actions button {
  padding: 10px 20px;
  border-radius: 20px;
  border: 1.5px solid #e8e1d9;
  background: transparent;
  color: black;
  font-size: 1rem;
  font-weight: 800;
  cursor: pointer;
  transition: all 0.2s;
}

.search-filter-row {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 16px;
}
.admin-search { max-width: 480px; }

.filter-select {
  padding: 8px 14px;
  border: 1.5px solid #E8E1D9;
  border-radius: 20px;
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

.admin-tabs {
  display: flex;
  gap: 8px;
  margin-bottom: 24px;
}
.admin-tabs button {
  padding: 10px 20px;
  border-radius: 20px;
  border: 1.5px solid #e8e1d9;
  background: transparent;
  color: #6b6560;
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
}
.admin-tabs button.active {
  background: #1a2233;
  border-color: #1a2233;
  color: #f7f0e6;
}

.admin-table-wrap {
  background: #fff;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 4px 16px rgba(26, 34, 51, 0.06);
}
.admin-table {
  width: 100%;
  border-collapse: collapse;
}
.admin-table th {
  text-align: left;
  padding: 14px 16px;
  font-size: 0.7rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #9b9590;
  border-bottom: 1.5px solid #e8e1d9;
}
.admin-table td {
  padding: 14px 16px;
  font-size: 0.85rem;
  color: #1a2233;
  border-bottom: 1px solid #f0eae0;
}
.table-cover {
  width: 32px;
  height: 44px;
  object-fit: cover;
  border-radius: 3px;
}

.stock-pill {
  padding: 3px 10px;
  border-radius: 12px;
  background: rgba(122, 158, 126, 0.15);
  color: #5a7e5e;
  font-weight: 600;
  font-size: 0.78rem;
}
.stock-pill.low {
  background: rgba(201, 168, 76, 0.15);
  color: #a88830;
}
.stock-pill.out {
  background: rgba(192, 69, 74, 0.15);
  color: #c0454a;
}

select {
  padding: 6px 10px;
  border-radius: 5px;
  border: 1px solid #e8e1d9;
  font-size: 0.8rem;
}

/* MODALS */
.modal-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(26, 34, 51, 0.55);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 100;
  padding: 20px;
}
.modal {
  background: #fff;
  border-radius: 12px;
  width: 100%;
  max-width: 520px;
  box-shadow: 0 24px 64px rgba(26, 34, 51, 0.2);
  overflow: hidden;
}
.modal-sm {
  max-width: 380px;
}

.modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 20px 24px 16px;
  border-bottom: 1.5px solid #f0eae0;
}
.modal-title {
  font-family: "Playfair Display", serif;
  font-size: 1.2rem;
  font-weight: 700;
  color: #1a2233;
  margin: 0;
}
.modal-close {
  background: none;
  border: none;
  font-size: 1rem;
  color: #9b9590;
  cursor: pointer;
  line-height: 1;
  padding: 4px 6px;
  border-radius: 4px;
}
.modal-close:hover {
  background: #f7f0e6;
  color: #1a2233;
}

.modal-form {
  padding: 20px 24px 24px;
  display: flex;
  flex-direction: column;
  gap: 14px;
}

.form-row {
  display: flex;
  flex-direction: column;
  gap: 5px;
}
.form-row label {
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #6b6560;
}
.form-row input,
.form-row select,
.form-row textarea {
  padding: 9px 12px;
  border: 1.5px solid #e8e1d9;
  border-radius: 6px;
  font-family: "Inter", sans-serif;
  font-size: 0.875rem;
  color: #1a2233;
  background: #fafaf8;
  transition: border-color 0.2s;
  outline: none;
}
.form-row input:focus,
.form-row select:focus,
.form-row textarea:focus {
  border-color: #c9a84c;
}
.form-row textarea {
  resize: vertical;
}

.form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
}

.required {
  color: #c0454a;
}

.form-error {
  color: #c0454a;
  font-size: 0.8rem;
  margin: 0;
}

.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 10px;
  margin-top: 4px;
}
.btn-cancel {
  padding: 9px 20px;
  border-radius: 6px;
  border: 1.5px solid #e8e1d9;
  background: transparent;
  color: #6b6560;
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
}
.btn-cancel:hover {
  background: #f7f0e6;
}
.btn-primary {
  padding: 9px 22px;
  border-radius: 6px;
  border: none;
  background: #1a2233;
  color: #f7f0e6;
  font-size: 0.85rem;
  font-weight: 700;
  cursor: pointer;
  transition: background 0.2s;
}
.btn-primary:hover:not(:disabled) {
  background: #c9a84c;
  color: #1a2233;
}
.btn-primary:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

/* VIEW BUTTON */
.view-btn {
  padding: 5px 14px; border-radius: 14px; border: 1.5px solid #E8E1D9;
  background: transparent; color: #1A2233; font-size: 0.75rem; font-weight: 600;
  cursor: pointer; transition: all 0.15s;
}
.view-btn:hover { background: #1A2233; color: #F7F0E6; border-color: #1A2233; }

/* STATUS PILL */
.status-pill {
  display: inline-block; padding: 3px 10px; border-radius: 12px;
  font-size: 0.72rem; font-weight: 700; text-transform: capitalize; letter-spacing: 0.04em;
}
.status-pill.pending   { background: rgba(201,168,76,0.15);  color: #A88830; }
.status-pill.confirmed { background: rgba(122,158,126,0.15); color: #4A7E5E; }
.status-pill.shipped   { background: rgba(74,114,196,0.15);  color: #3A5AAA; }
.status-pill.delivered { background: rgba(122,158,126,0.25); color: #2E6040; }
.status-pill.cancelled { background: rgba(192,69,74,0.12);   color: #C0454A; }

/* ORDER DETAIL MODAL */
.modal-order { max-width: 620px; }

.order-date { font-size: 0.78rem; color: #9B9590; display: block; margin-top: 2px; }

.order-body { padding: 0 24px 24px; display: flex; flex-direction: column; gap: 20px; }

.order-section { border: 1.5px solid #F0EAE0; border-radius: 8px; overflow: hidden; }
.order-section-title {
  font-size: 0.68rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase;
  color: #9B9590; padding: 10px 16px; background: #FAFAF8; border-bottom: 1.5px solid #F0EAE0;
  margin: 0;
}

.info-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 0; }
.info-item {
  display: flex; flex-direction: column; gap: 2px;
  padding: 12px 16px; border-bottom: 1px solid #F7F0E6; font-size: 0.85rem; color: #1A2233;
}
.info-item:nth-child(odd) { border-right: 1px solid #F7F0E6; }
.info-full { grid-column: 1 / -1; }
.info-label { font-size: 0.65rem; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: #B0ABA5; }

.order-items-table { width: 100%; border-collapse: collapse; }
.order-items-table th {
  text-align: left; padding: 10px 16px; font-size: 0.65rem; font-weight: 700;
  letter-spacing: 0.08em; text-transform: uppercase; color: #9B9590;
}
.order-items-table td { padding: 10px 16px; font-size: 0.85rem; color: #1A2233; border-top: 1px solid #F7F0E6; }

.order-total {
  display: flex; justify-content: space-between; align-items: center;
  padding: 12px 16px; border-top: 1.5px solid #E8E1D9; background: #FAFAF8;
  font-size: 0.8rem; font-weight: 600; color: #6B6560;
}
.order-total-price {
  font-family: 'Playfair Display', serif; font-size: 1.1rem; font-weight: 700; color: #1A2233;
}

.status-row { display: flex; align-items: center; gap: 12px; padding: 14px 16px; }

/* USERS TAB */
.users-toolbar {
  display: flex; align-items: center; justify-content: space-between;
  padding: 14px 16px; border-bottom: 1.5px solid #E8E1D9; background: #FAFAF8;
}
.user-search { max-width: 300px; }
.btn-add-admin {
  padding: 8px 18px; border-radius: 20px; border: 1.5px solid #1A2233;
  background: #1A2233; color: #F7F0E6; font-size: 0.8rem; font-weight: 700;
  cursor: pointer; white-space: nowrap; transition: background 0.2s;
}
.btn-add-admin:hover { background: #C9A84C; border-color: #C9A84C; color: #1A2233; }

.table-loading, .table-empty {
  text-align: center; padding: 32px; color: #9B9590; font-size: 0.85rem;
}

/* ADD STOCK MODAL */
.add-stock-book {
  display: flex; align-items: center; gap: 14px;
  padding: 12px; background: #FAFAF8; border-radius: 8px; border: 1.5px solid #F0EAE0;
}
.add-stock-cover {
  width: 40px; height: 56px; object-fit: cover; border-radius: 3px; flex-shrink: 0;
}
.add-stock-title {
  font-size: 0.9rem; font-weight: 700; color: #1A2233; margin-bottom: 4px;
  display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;
}
.add-stock-current { font-size: 0.78rem; color: #9B9590; }
.add-stock-preview {
  font-size: 0.78rem; color: #4A7E5E; margin-top: 6px;
}
</style>
