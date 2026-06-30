<template>
  <div class="landing">
    <LandingPageHero />
    <LandingPagerFeatured/>
    <LandingPageCategories/>
    <LandingPageContact/>
  </div>
</template>

<script setup>
import { ref} from 'vue'
import LandingPageContact from './ui/LandingPageContact.vue'
import LandingPageHero from './ui/LandingPageHero.vue'
import LandingPageCategories from './ui/LandingPageCategories.vue'
import LandingPagerFeatured from './ui/LandingPagerFeatured.vue'

</script>

<style scoped>

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body { overflow-x: hidden; }

.landing {
  min-height: 100vh;
  font-family: 'Inter', system-ui, sans-serif;
}

/* Global scroll-reveal base (each component manages its own) */
@media (prefers-reduced-motion: reduce) {
  * { animation-duration: 0.01ms !important; transition-duration: 0.01ms !important; }
}
</style>