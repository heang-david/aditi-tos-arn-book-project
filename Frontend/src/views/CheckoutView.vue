<template>
  <div class="checkout-page">

    <!-- empty cart guard -->
    <div v-if="cart.isEmpty && !orderPlaced" class="checkout-empty">
      <h2>Your cart is empty</h2>
      <p>Add some books before checking out.</p>
      <router-link to="/products" class="empty-cta">Browse Books</router-link>
    </div>

    <!-- success state -->
    <div v-else-if="orderPlaced" class="checkout-success">
      <div class="success-icon">
        <svg width="48" height="48" viewBox="0 0 48 48" fill="none">
          <circle cx="24" cy="24" r="22" stroke="#7A9E7E" stroke-width="2"/>
          <path d="M14 24l7 7 13-13" stroke="#7A9E7E" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
      </div>
      <h2>Order placed successfully!</h2>
      <p>Order #{{ placedOrder.id }} — a confirmation has been sent to {{ placedOrder.email }}.</p>
      <router-link to="/products" class="empty-cta">Continue Shopping</router-link>
    </div>

    <!-- checkout form -->
    <div v-else class="checkout-layout">

      <!-- left — form -->
      <div class="checkout-form-col">

        <div class="checkout-header">
          <div class="section-eyebrow">
            <svg width="28" height="1" viewBox="0 0 28 1"><line x1="0" y1="0.5" x2="28" y2="0.5" stroke="#C9A84C" stroke-width="1"/></svg>
            Almost there
          </div>
          <h1 class="checkout-title">Checkout</h1>
        </div>

        <form class="checkout-form" @submit.prevent="handleSubmit" novalidate>

          <div class="form-field" :class="{ error: errors.customer_name, filled: form.customer_name }">
            <label for="customer_name">Full name</label>
            <input
              id="customer_name"
              v-model="form.customer_name"
              type="text"
              placeholder="e.g. Sophea Keo"
              autocomplete="name"
              @blur="validate('customer_name')"
            />
            <span v-if="errors.customer_name" class="field-error">{{ errors.customer_name }}</span>
          </div>

          <div class="form-row">
            <div class="form-field" :class="{ error: errors.email, filled: form.email }">
              <label for="email">Email address</label>
              <input
                id="email"
                v-model="form.email"
                type="email"
                placeholder="you@example.com"
                autocomplete="email"
                @blur="validate('email')"
              />
              <span v-if="errors.email" class="field-error">{{ errors.email }}</span>
            </div>

            <div class="form-field" :class="{ error: errors.phone, filled: form.phone }">
              <label for="phone">Phone number</label>
              <input
                id="phone"
                v-model="form.phone"
                type="tel"
                placeholder="012 345 678"
                autocomplete="tel"
                @blur="validate('phone')"
              />
              <span v-if="errors.phone" class="field-error">{{ errors.phone }}</span>
            </div>
          </div>

          <div class="form-field" :class="{ error: errors.address, filled: form.address }">
            <label for="address">Delivery address</label>
            <textarea
              id="address"
              v-model="form.address"
              rows="3"
              placeholder="Street, city, postal code…"
              @blur="validate('address')"
            ></textarea>
            <span v-if="errors.address" class="field-error">{{ errors.address }}</span>
          </div>

          <p v-if="submitError" class="submit-error">{{ submitError }}</p>

          <button type="submit" class="place-order-btn" :disabled="submitting">
            <span v-if="submitting" class="btn-loading">
              <span class="spinner"></span>
              Placing order…
            </span>
            <span v-else>
              Place Order — ${{ (cart.totalPrice * 1.1).toFixed(2) }}
              <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
                <path d="M2 7h10M9 3l4 4-4 4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
            </span>
          </button>

        </form>

      </div>

      <!-- right — order summary -->
      <div class="checkout-summary-col">
        <div class="summary-card">

          <h2 class="summary-title">Order Summary</h2>

          <div class="summary-items">
            <div v-for="item in cart.items" :key="item.id" class="summary-item">
              <img :src="item.image_url" :alt="item.title" class="summary-item-cover" />
              <div class="summary-item-info">
                <strong>{{ item.title }}</strong>
                <span>Qty: {{ item.quantity }}</span>
              </div>
              <span class="summary-item-price">${{ (item.price * item.quantity).toFixed(2) }}</span>
            </div>
          </div>

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

          <div class="summary-rows">
            <div class="summary-row">
              <span>Subtotal</span>
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

          <div class="summary-total">
            <span>Total</span>
            <strong>${{ (cart.totalPrice * 1.1).toFixed(2) }}</strong>
          </div>

        </div>
      </div>

    </div>

  </div>
</template>

<script setup>
import { reactive, ref } from "vue"
import { useRouter } from "vue-router"
import axios from "axios"
import { useCartStore } from "@/stores/cart"

const cart   = useCartStore()
const router = useRouter()

const form = reactive({
  customer_name: "",
  email: "",
  phone: "",
  address: "",
})

const errors = reactive({
  customer_name: "",
  email: "",
  phone: "",
  address: "",
})

const submitting  = ref(false)
const submitError = ref("")
const orderPlaced = ref(false)
const placedOrder = ref(null)

function validate(field) {
  errors[field] = ""

  if (field === "customer_name" && !form.customer_name.trim()) {
    errors.customer_name = "Please enter your full name."
  }

  if (field === "email") {
    if (!form.email.trim()) errors.email = "Please enter your email."
    else if (!/\S+@\S+\.\S+/.test(form.email)) errors.email = "That doesn't look like a valid email."
  }

  if (field === "phone") {
    if (!form.phone.trim()) errors.phone = "Please enter your phone number."
    else if (!/^[0-9+\s-]{7,15}$/.test(form.phone)) errors.phone = "Please enter a valid phone number."
  }

  if (field === "address" && !form.address.trim()) {
    errors.address = "Please enter a delivery address."
  }
}

function validateAll() {
  ["customer_name", "email", "phone", "address"].forEach(validate)
  return !Object.values(errors).some(e => e)
}

async function handleSubmit() {
  submitError.value = ""

  if (!validateAll()) return

  submitting.value = true

  const payload = {
    customer_name: form.customer_name,
    email:         form.email,
    phone:         form.phone,
    address:       form.address,
    items: cart.items.map(item => ({
      book_id:  item.id,
      quantity: item.quantity,
    })),
  }

  try {
    const response = await axios.post("http://127.0.0.1:8000/api/orders/", payload)
    placedOrder.value = response.data
    orderPlaced.value = true
    cart.clearCart()
  } catch (err) {
    submitError.value =
      err.response?.data?.detail || "Something went wrong placing your order. Please try again."
  } finally {
    submitting.value = false
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Inter:wght@300;400;500;600&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

.checkout-page {
  min-height: 100vh;
  background: #F7F0E6;
  padding: 56px 40px 100px;
  font-family: 'Inter', system-ui, sans-serif;
}

/* EMPTY / SUCCESS STATES */
.checkout-empty,
.checkout-success {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 60vh;
  text-align: center;
  gap: 14px;
}
.checkout-empty h2,
.checkout-success h2 {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: 1.8rem;
  font-weight: 700;
  color: #1A2233;
  letter-spacing: -0.02em;
}
.checkout-empty p,
.checkout-success p {
  font-size: 0.92rem;
  color: #9B9590;
  max-width: 360px;
}
.success-icon { margin-bottom: 6px; }
.empty-cta {
  display: inline-flex;
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

/* LAYOUT */
.checkout-layout {
  max-width: 1100px;
  margin: 0 auto;
  display: grid;
  grid-template-columns: 1fr 380px;
  gap: 40px;
  align-items: start;
}

/* HEADER */
.checkout-header { margin-bottom: 28px; }
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
.checkout-title {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(2rem, 3.5vw, 2.8rem);
  font-weight: 700;
  color: #1A2233;
  letter-spacing: -0.03em;
}

/* FORM */
.checkout-form {
  background: #fff;
  border-radius: 10px;
  padding: 32px;
  box-shadow: 0 4px 20px rgba(26, 34, 51, 0.06);
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }

.form-field { display: flex; flex-direction: column; gap: 6px; }
.form-field label {
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #6B6560;
  transition: color 0.2s;
}
.form-field.filled label, .form-field:focus-within label { color: #1A2233; }

.form-field input,
.form-field textarea {
  font-family: 'Inter', sans-serif;
  font-size: 0.9rem;
  color: #1A2233;
  background: #F7F0E6;
  border: 1.5px solid #E8E1D9;
  border-radius: 5px;
  padding: 12px 14px;
  outline: none;
  transition: border-color 0.2s, background 0.2s;
  resize: none;
}
.form-field input::placeholder,
.form-field textarea::placeholder { color: #B0ABA5; }
.form-field input:focus,
.form-field textarea:focus { border-color: #C9A84C; background: #fff; }
.form-field.error input,
.form-field.error textarea { border-color: #C0454A; background: #FEF7F7; }

.field-error {
  font-size: 0.7rem;
  color: #C0454A;
  font-weight: 500;
}

.submit-error {
  font-size: 0.82rem;
  color: #C0454A;
  font-weight: 500;
  background: #FEF7F7;
  border: 1px solid rgba(192, 69, 74, 0.25);
  border-radius: 5px;
  padding: 10px 14px;
}

.place-order-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  background: #C9A84C;
  color: #1A2233;
  border: none;
  padding: 16px 24px;
  border-radius: 5px;
  font-family: 'Inter', sans-serif;
  font-size: 0.85rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  cursor: pointer;
  transition: background 0.2s, transform 0.15s;
}
.place-order-btn:hover:not(:disabled) { background: #E8C96A; transform: translateY(-1px); }
.place-order-btn:disabled { opacity: 0.75; cursor: not-allowed; }

.btn-loading { display: flex; align-items: center; gap: 10px; }
.spinner {
  width: 14px; height: 14px;
  border: 2px solid rgba(26, 34, 51, 0.3);
  border-top-color: #1A2233;
  border-radius: 50%;
  animation: spin 0.7s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }

/* SUMMARY */
.checkout-summary-col { position: sticky; top: 32px; }

.summary-card {
  background: #1A2233;
  border-radius: 10px;
  padding: 28px 26px;
  box-shadow: 0 12px 40px rgba(26, 34, 51, 0.2);
  border: 1px solid rgba(201, 168, 76, 0.12);
}
.summary-title {
  font-family: 'Playfair Display', serif;
  font-size: 1.2rem;
  font-weight: 700;
  color: #F7F0E6;
  letter-spacing: -0.02em;
  margin-bottom: 20px;
}

.summary-items {
  display: flex;
  flex-direction: column;
  gap: 14px;
  margin-bottom: 16px;
  max-height: 280px;
  overflow-y: auto;
}
.summary-item {
  display: flex;
  align-items: center;
  gap: 12px;
}
.summary-item-cover {
  width: 36px;
  height: 50px;
  object-fit: cover;
  border-radius: 3px;
  flex-shrink: 0;
}
.summary-item-info {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: 2px;
}
.summary-item-info strong {
  font-size: 0.8rem;
  font-weight: 600;
  color: #F7F0E6;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
.summary-item-info span {
  font-size: 0.68rem;
  color: rgba(247, 240, 230, 0.4);
}
.summary-item-price {
  font-size: 0.82rem;
  font-weight: 600;
  color: #C9A84C;
  flex-shrink: 0;
}

.summary-divider { margin: 4px 0 16px; opacity: 0.8; }

.summary-rows {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 18px;
}
.summary-row {
  display: flex;
  justify-content: space-between;
  font-size: 0.84rem;
  color: rgba(247, 240, 230, 0.55);
}
.free-tag {
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #7A9E7E;
}

.summary-total {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  padding-top: 14px;
  border-top: 1px solid rgba(247, 240, 230, 0.1);
}
.summary-total span {
  font-size: 0.74rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: rgba(247, 240, 230, 0.5);
}
.summary-total strong {
  font-family: 'Playfair Display', serif;
  font-size: 1.6rem;
  font-weight: 700;
  color: #F7F0E6;
  letter-spacing: -0.03em;
}

/* RESPONSIVE */
@media (max-width: 880px) {
  .checkout-layout { grid-template-columns: 1fr; }
  .checkout-summary-col { position: static; }
  .form-row { grid-template-columns: 1fr; }
}
@media (max-width: 500px) {
  .checkout-page { padding: 32px 18px 80px; }
  .checkout-form { padding: 22px; }
}
</style>