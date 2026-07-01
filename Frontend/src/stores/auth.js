import { defineStore } from "pinia"
import { ref, computed } from "vue"
import axios from "axios"

const BASE = "http://127.0.0.1:8000/api/admin"

export const useAuthStore = defineStore("auth", () => {
  const token     = ref(localStorage.getItem("admin_token") || null)
  const expiresAt = ref(Number(localStorage.getItem("admin_expires_at")) || null)
  const username  = ref(localStorage.getItem("admin_username") || null)

  let _timer = null

  const isAuthenticated = computed(() => {
    if (!token.value || !expiresAt.value) return false
    return Date.now() < expiresAt.value
  })

  function _startTimer() {
    clearTimeout(_timer)
    if (!expiresAt.value) return
    const remaining = expiresAt.value - Date.now()
    if (remaining <= 0) { logout(); return }
    _timer = setTimeout(() => logout(), remaining)
  }

  // Resume timer on page reload if still within the window
  if (isAuthenticated.value) _startTimer()

  async function login(user, pass) {
    const res = await axios.post(`${BASE}/login`, {
      username: user,
      password: pass,
    })
    const { access_token, expires_in } = res.data   // expires_in in seconds
    const exp = Date.now() + expires_in * 1000

    token.value     = access_token
    expiresAt.value = exp
    username.value  = user

    localStorage.setItem("admin_token",      access_token)
    localStorage.setItem("admin_expires_at", String(exp))
    localStorage.setItem("admin_username",   user)

    _startTimer()
  }

  function logout() {
    clearTimeout(_timer)
    token.value     = null
    expiresAt.value = null
    username.value  = null
    localStorage.removeItem("admin_token")
    localStorage.removeItem("admin_expires_at")
    localStorage.removeItem("admin_username")
  }

  /** Axios config with Bearer header */
  function authHeaders() {
    return { headers: { Authorization: `Bearer ${token.value}` } }
  }

  return { token, username, isAuthenticated, login, logout, authHeaders }
})
