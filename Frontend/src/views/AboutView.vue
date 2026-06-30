<template>
  <div class="about-page">
        <!-- STORY SECTION -->
    <section class="story">
      <div class="story-inner">
        <div class="story-text" :class="{ visible: storyVisible }" ref="storyRef">
          <span class="section-label">How We Began</span>
          <h2>A corner shelf that grew into something more.</h2>
          <p>
            Tos arn started in 2018 as a modest personal collection — a few hundred
            beloved titles organized by mood rather than genre. Friends would visit and
            leave with armfuls of recommendations. Word spread. The shelves multiplied.
          </p>
          <p>
            By 2020, what began as a living-room project had become a proper online
            store — curated, purposeful, and staffed by people who actually read everything
            they sell. Today we carry over 40,000 titles across every genre, yet every
            selection still passes the same simple test: would we press it into a friend's hands?
          </p>
        </div>
        <div class="story-image" :class="{ visible: storyVisible }">
          <div class="image-frame">
            <div class="image-placeholder">
              <div class="shelf-illustration">
                <div class="shelf-row">
                  <div v-for="book in books" :key="book.id" class="book-spine" :style="{ background: book.color, height: book.height + 'px' }">
                    <span class="spine-title">{{ book.title }}</span>
                  </div>
                </div>
                <div class="shelf-board"></div>
              </div>
            </div>
            <div class="image-tag">Est. 2018 · Phnom Penh</div>
          </div>
        </div>
      </div>
    </section>

  </div>
</template>

<style>

.about-page {
  font-family: var(--ff-body);
  color: var(--ink);
  background: var(--parch);
  overflow-x: hidden;
}
.story { padding: 80px 0 100px; }
.story-inner {
  max-width: 1160px;
  margin: 0 auto;
  padding: 0 32px;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 80px;
  align-items: center;
}
.story-text, .story-image {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.7s ease, transform 0.7s ease;
}
.story-image { transition-delay: 0.15s; }
.story-text.visible, .story-image.visible { opacity: 1; transform: none; }
.section-label {
  display: block;
  font-size: 0.7rem;
  font-weight: 600;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--gold);
  margin-bottom: 16px;
}
.section-label.centered { text-align: center; }
.story-text h2 {
  font-family: var(--ff-disp);
  font-size: clamp(1.8rem, 3vw, 2.6rem);
  font-weight: 600;
  line-height: 1.2;
  color: var(--navy);
  letter-spacing: -0.02em;
  margin-bottom: 24px;
}
.story-text p {
  font-size: 0.975rem;
  line-height: 1.85;
  color: var(--muted);
  margin-bottom: 16px;
}
.image-frame {
  position: relative;
  border-radius: 6px;
  overflow: hidden;
  background: var(--navy);
  padding: 40px 32px 24px;
  box-shadow: 0 24px 64px rgba(26,34,51,0.18);
}
.shelf-illustration { display: flex; flex-direction: column; gap: 0; }
.shelf-row {
  display: flex;
  align-items: flex-end;
  gap: 4px;
  padding: 20px 0 0;
}
.book-spine {
  flex: 1;
  border-radius: 2px 0 0 2px;
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 28px;
  box-shadow: inset -3px 0 6px rgba(0,0,0,0.25);
  position: relative;
  overflow: hidden;
}
.spine-title {
  font-family: var(--ff-disp);
  font-size: 0.5rem;
  font-weight: 600;
  color: rgba(255,255,255,0.7);
  writing-mode: vertical-rl;
  text-orientation: mixed;
  transform: rotate(180deg);
  letter-spacing: 0.06em;
  padding: 8px 0;
}
.shelf-board {
  height: 12px;
  background: #8B6914;
  border-radius: 0 0 4px 4px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.3);
}
.image-tag {
  margin-top: 20px;
  font-size: 0.72rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--gold);
  text-align: center;
  opacity: 0.8;
}


@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
</style>

<script setup>
import { ref, onMounted } from 'vue'
const storyVisible = ref(false)
const storyRef = ref(null)
const books = ref([
        { id: 1, title: 'Proust',   color: '#2C4770', height: 110 },
        { id: 2, title: 'Woolf',    color: '#7A9E7E', height: 90  },
        { id: 3, title: 'Achebe',   color: '#C9A84C', height: 120 },
        { id: 4, title: 'Borges',   color: '#8B4B62', height: 95  },
        { id: 5, title: 'Le Guin',  color: '#4A7C8E', height: 105 },
        { id: 6, title: 'Bulgakov', color: '#5C3D2E', height: 115 },
        { id: 7, title: 'Lispector',color: '#7A6A52', height: 88  },
      ])


onMounted(() => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        if (entry.target === storyRef.value) storyVisible.value = true
      }
    })
  }, { threshold: 0.15 })

  if (storyRef.value) observer.observe(storyRef.value)
});

</script>