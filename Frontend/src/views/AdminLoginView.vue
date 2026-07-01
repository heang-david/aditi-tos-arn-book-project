<template>
  <div class="login-page">
    <div class="login-card">

      <div class="login-eyebrow">
        <svg width="24" height="1" viewBox="0 0 24 1"><line x1="0" y1="0.5" x2="24" y2="0.5" stroke="#C9A84C" stroke-width="1"/></svg>
        Admin Portal
        <svg width="24" height="1" viewBox="0 0 24 1"><line x1="0" y1="0.5" x2="24" y2="0.5" stroke="#C9A84C" stroke-width="1"/></svg>
      </div>
      <h1 class="login-title">Sign in</h1>
      <p class="login-sub">Sessions expire after 10 minutes.</p>

      <form class="login-form" @submit.prevent="submit">

        <div class="field">
          <label for="username">Username</label>
          <input
            id="username"
            v-model="username"
            type="text"
            placeholder="admin"
            autocomplete="username"
            required
          />
        </div>

        <div class="field">
          <label for="password">Password</label>
          <div class="password-wrap">
            <input
              id="password"
              v-model="password"
              :type="showPass ? 'text' : 'password'"
              placeholder="••••••••"
              autocomplete="current-password"
              required
            />
            <button type="button" class="toggle-pass" @click="showPass = !showPass">
              {{ showPass ? 'Hide' : 'Show' }}
            </button>
          </div>
        </div>

        <p v-if="error" class="login-error">{{ error }}</p>

        <button type="submit" class="login-btn" :disabled="loading">
          <span v-if="loading" class="spinner"></span>
          {{ loading ? 'Signing in…' : 'Sign in' }}
        </button>

      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue"
import { useRouter } from "vue-router"
import { useAuthStore } from "@/stores/auth"

const authStore = useAuthStore()
const router    = useRouter()

const username = ref("")
const password = ref("")
const showPass = ref(false)
const loading  = ref(false)
const error    = ref("")

async function submit() {
  error.value   = ""
  loading.value = true
  try {
    await authStore.login(username.value, password.value)
    router.push("/admin")
  } catch (e) {
    error.value = e.response?.data?.detail || "Invalid username or password."
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;500;600&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

.login-page {
  min-height: 100vh;
  background: #F7F0E6;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: 'Inter', sans-serif;
  padding: 24px;
}

.login-card {
  background: #fff;
  border-radius: 12px;
  padding: 48px 44px;
  width: 100%;
  max-width: 400px;
  box-shadow: 0 16px 48px rgba(26, 34, 51, 0.1);
  animation: fadeUp 0.5s ease forwards;
}

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(20px); }
  to   { opacity: 1; transform: translateY(0); }
}

.login-eyebrow {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.62rem;
  font-weight: 600;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #C9A84C;
  margin-bottom: 12px;
}

.login-title {
  font-family: 'Playfair Display', serif;
  font-size: 2rem;
  font-weight: 700;
  color: #1A2233;
  letter-spacing: -0.02em;
  margin-bottom: 6px;
}

.login-sub {
  font-size: 0.82rem;
  color: #9B9590;
  margin-bottom: 32px;
}

.login-form { display: flex; flex-direction: column; gap: 18px; }

.field { display: flex; flex-direction: column; gap: 6px; }
.field label {
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.07em;
  text-transform: uppercase;
  color: #6B6560;
}
.field input {
  padding: 10px 14px;
  border: 1.5px solid #E8E1D9;
  border-radius: 7px;
  font-family: 'Inter', sans-serif;
  font-size: 0.9rem;
  color: #1A2233;
  background: #FAFAF8;
  outline: none;
  transition: border-color 0.2s;
  width: 100%;
}
.field input:focus { border-color: #C9A84C; }

.password-wrap { position: relative; }
.password-wrap input { padding-right: 56px; }
.toggle-pass {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  font-size: 0.72rem;
  font-weight: 600;
  color: #9B9590;
  cursor: pointer;
  letter-spacing: 0.04em;
}
.toggle-pass:hover { color: #1A2233; }

.login-error {
  font-size: 0.8rem;
  color: #C0454A;
  background: rgba(192, 69, 74, 0.07);
  border: 1px solid rgba(192, 69, 74, 0.2);
  border-radius: 6px;
  padding: 8px 12px;
}

.login-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 12px;
  background: #1A2233;
  color: #F7F0E6;
  border: none;
  border-radius: 7px;
  font-family: 'Inter', sans-serif;
  font-size: 0.9rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  cursor: pointer;
  transition: background 0.2s;
  margin-top: 4px;
}
.login-btn:hover:not(:disabled) { background: #C9A84C; color: #1A2233; }
.login-btn:disabled { opacity: 0.6; cursor: not-allowed; }

.spinner {
  width: 14px;
  height: 14px;
  border: 2px solid rgba(247,240,230,0.3);
  border-top-color: #F7F0E6;
  border-radius: 50%;
  animation: spin 0.7s linear infinite;
}
@keyframes spin { to { transform: rotate(360deg); } }
</style>
