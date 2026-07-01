import { createRouter, createWebHistory } from 'vue-router'

import DefaultLayout      from '@/components/layouts/DefaultLayout.vue'
import AdminLayout        from '@/components/layouts/AdminLayout.vue'

import HomeView           from '../views/HomeView.vue'
import AboutView          from '../views/AboutView.vue'
import ProductView        from '../views/ProductView.vue'
import ContactView        from '@/views/ContactView.vue'
import CartView           from '@/views/CartView.vue'
import ProductDetailView  from '@/views/ProductDetailView.vue'
import CheckoutView       from '@/views/CheckoutView.vue'
import AdminView          from '@/views/AdminView.vue'
import AdminLoginView     from '@/views/AdminLoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: DefaultLayout,
      children: [
        { path: '',              component: HomeView },
        { path: 'about',        component: AboutView },
        { path: 'products',     component: ProductView },
        { path: 'contact',      component: ContactView },
        { path: 'cart',         component: CartView },
        { path: 'checkout',     component: CheckoutView },
        { path: 'products/:id', component: ProductDetailView },
      ],
    },
    {
      path: '/admin/login',
      component: AdminLoginView,
    },
    {
      path: '/admin',
      component: AdminLayout,
      meta: { requiresAdmin: true },
      children: [
        { path: '', component: AdminView },
      ],
    },
  ],
})

// Navigation guard — redirect to login if not authenticated
router.beforeEach((to, _from, next) => {
  if (!to.meta.requiresAdmin) return next()

  // Lazy-import store to avoid circular dependency at module load time
  import('@/stores/auth').then(({ useAuthStore }) => {
    const auth = useAuthStore()
    if (auth.isAuthenticated) {
      next()
    } else {
      next({ path: '/admin/login', query: { redirect: to.fullPath } })
    }
  })
})

export default router
