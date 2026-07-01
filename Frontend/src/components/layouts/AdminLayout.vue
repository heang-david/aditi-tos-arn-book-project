<template>
  <div class="admin-shell">
    <header class="admin-topbar">
      <span class="admin-brand">
        <svg width="20" height="1" viewBox="0 0 20 1"><line x1="0" y1="0.5" x2="20" y2="0.5" stroke="#C9A84C" stroke-width="1"/></svg>
        Tos arn Admin
      </span>
      <div class="admin-user">
        <span class="admin-username">{{ authStore.username }}</span>
        <span class="session-badge" :class="{ expiring: minutesLeft <= 2 }">
          {{ minutesLeft }}m left
        </span>
        <button class="logout-btn" @click="handleLogout">Sign out</button>
      </div>
    </header>

    <RouterView />
  </div>
</template>

<script setup>
import { computed, onMounted, onUnmounted, ref } from 'vue'
import { RouterView, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()
const router    = useRouter()

const minutesLeft = ref(0)
let ticker = null

function calcMinutes() {
  if (!authStore.isAuthenticated) { minutesLeft.value = 0; return }
  const ms = authStore.expiresAt - Date.now()
  minutesLeft.value = Math.max(0, Math.ceil(ms / 60000))
}

onMounted(() => {
  calcMinutes()
  ticker = setInterval(calcMinutes, 10_000)
})
onUnmounted(() => clearInterval(ticker))

function handleLogout() {
  authStore.logout()
  router.push('/admin/login')
}
</script>

<style scoped>
.admin-shell { min-height: 100vh; background: #F7F0E6; }

.admin-topbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 40px;
  height: 56px;
  background: #1A2233;
  font-family: 'Inter', sans-serif;
}

.admin-brand {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #C9A84C;
}

.admin-user {
  display: flex;
  align-items: center;
  gap: 14px;
}

.admin-username {
  font-size: 0.82rem;
  font-weight: 600;
  color: rgba(247, 240, 230, 0.75);
}

.session-badge {
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  padding: 3px 9px;
  border-radius: 10px;
  background: rgba(122, 158, 126, 0.2);
  color: #7AE07A;
  transition: background 0.3s, color 0.3s;
}
.session-badge.expiring {
  background: rgba(192, 69, 74, 0.2);
  color: #FF8080;
  animation: pulse 1.2s ease-in-out infinite;
}
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50%       { opacity: 0.5; }
}

.logout-btn {
  padding: 6px 16px;
  border-radius: 5px;
  border: 1.5px solid rgba(247, 240, 230, 0.2);
  background: transparent;
  color: rgba(247, 240, 230, 0.7);
  font-family: 'Inter', sans-serif;
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  cursor: pointer;
  transition: all 0.2s;
}
.logout-btn:hover {
  background: rgba(192, 69, 74, 0.15);
  border-color: #C0454A;
  color: #FF8080;
}
</style>
