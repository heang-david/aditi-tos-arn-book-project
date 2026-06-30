<template>
  <footer class="footer">

    <!-- main footer grid -->
    <div class="footer-main">
      <div class="footer-main-inner">

        <!-- brand col -->
        <div class="footer-brand">
          <a href="#" class="footer-logo">
            <span class="logo-icon">📖</span>
            <span class="logo-text">Tos arn <em>Books</em></span>
          </a>
          <p class="footer-brand-desc">
            An online bookstore built by readers, for readers.
            Every title on our shelves has been read and loved
            by someone on our team.
          </p>
          <div class="footer-socials">
            <a v-for="s in socials" :key="s.name" :href="s.href" class="social-btn" :aria-label="s.name">
              {{ s.icon }}
            </a>
          </div>
        </div>

        <!-- link cols -->
        <div v-for="col in linkCols" :key="col.heading" class="footer-col">
          <h4 class="footer-col-heading">{{ col.heading }}</h4>
          <ul class="footer-links">
            <li v-for="link in col.links" :key="link.label">
              <a :href="link.href" class="footer-link">{{ link.label }}</a>
            </li>
          </ul>
        </div>

        <!-- newsletter col -->
        <div class="footer-col footer-newsletter">
          <h4 class="footer-col-heading">Stay in the loop</h4>
          <p class="newsletter-sub">New arrivals, staff picks, and reading-list ideas — straight to your inbox. No spam, ever.</p>
          <form class="newsletter-form" @submit.prevent="handleNewsletter" novalidate>
            <div class="newsletter-field" :class="{ error: newsletterError, success: newsletterSent }">
              <input
                v-model="email"
                type="email"
                placeholder="your@email.com"
                :disabled="newsletterSent"
                @input="newsletterError = ''"
              />
              <button type="submit" :disabled="newsletterSent">
                <span v-if="newsletterSent">✓</span>
                <svg v-else width="15" height="15" viewBox="0 0 15 15" fill="none">
                  <path d="M2 7.5h11M8.5 3l4 4.5-4 4.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </button>
            </div>
            <p v-if="newsletterError" class="newsletter-error">{{ newsletterError }}</p>
            <p v-if="newsletterSent" class="newsletter-success">You're in — happy reading! 📖</p>
          </form>
        </div>

      </div>
    </div>

    <!-- bottom bar -->
    <div class="footer-bottom">
      <div class="footer-bottom-inner">
        <p class="footer-copy">© {{ year }} Tos arn Book Store. All rights reserved.</p>
        <div class="footer-bottom-links">
          <a v-for="link in legalLinks" :key="link" href="#" class="footer-legal-link">{{ link }}</a>
        </div>
        <p class="footer-made">
          Made with <span class="heart">♥</span> in Phnom Penh
        </p>
      </div>
    </div>

  </footer>
</template>

<script>
export default {
  name: 'FooterSection',
  data() {
    return {
      email: '',
      newsletterError: '',
      newsletterSent: false,
      year: new Date().getFullYear(),
      socials: [
        { name: 'Instagram', icon: '◈', href: '#' },
        { name: 'Facebook',  icon: '◉', href: '#' },
        { name: 'Twitter/X', icon: '✦', href: '#' },
        { name: 'Pinterest', icon: '◇', href: '#' },
      ],
      linkCols: [
        {
          heading: 'Shop',
          links: [
            { label: 'New Arrivals',      href: '#' },
            { label: 'Featured Books',    href: '#featured' },
            { label: 'Best Sellers',      href: '#' },
            { label: 'Staff Picks',       href: '#' },
            { label: 'Gift Cards',        href: '#' },
          ],
        },
        {
          heading: 'Categories',
          links: [
            { label: 'Fiction',           href: '#' },
            { label: 'Non-Fiction',       href: '#' },
            { label: 'Essays & Criticism',href: '#' },
            { label: 'Classics',          href: '#' },
            { label: 'All Categories',    href: '#categories' },
          ],
        },
        {
          heading: 'Help',
          links: [
            { label: 'FAQs',              href: '#' },
            { label: 'Shipping & Returns',href: '#' },
            { label: 'Track Your Order',  href: '#' },
            { label: 'Contact Us',        href: '#contact' },
            { label: 'About Us',          href: '#' },
          ],
        },
      ],
      legalLinks: ['Privacy Policy', 'Terms of Service', 'Cookie Settings'],
    }
  },
  methods: {
    handleNewsletter() {
      if (!this.email.trim()) {
        this.newsletterError = 'Please enter your email address.'
        return
      }
      if (!/\S+@\S+\.\S+/.test(this.email)) {
        this.newsletterError = 'That doesn\'t look like a valid email.'
        return
      }
      this.newsletterSent = true
    },
  },
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Inter:wght@300;400;500;600&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

.footer {
  background: #1A2233;
  font-family: 'Inter', system-ui, sans-serif;
}

/* TOP CTA BAND */
.footer-top {
  border-bottom: 1px solid rgba(201,168,76,0.15);
  padding: 64px 0;
}
.footer-top-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 40px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 40px;
  flex-wrap: wrap;
}
.footer-cta-eyebrow {
  display: block;
  font-size: 0.68rem;
  font-weight: 600;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #C9A84C;
  margin-bottom: 10px;
  opacity: 0.8;
}
.footer-cta-title {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(1.6rem, 3vw, 2.4rem);
  font-weight: 700;
  color: #F7F0E6;
  letter-spacing: -0.03em;
  line-height: 1.15;
}
.footer-cta-title em { font-style: italic; color: #C9A84C; }
.footer-cta-btn {
  flex-shrink: 0;
  text-decoration: none;
  background: #C9A84C;
  color: #1A2233;
  padding: 15px 32px;
  border-radius: 4px;
  font-size: 0.8rem;
  font-weight: 700;
  letter-spacing: 0.07em;
  text-transform: uppercase;
  white-space: nowrap;
  transition: background 0.2s, transform 0.15s;
}
.footer-cta-btn:hover { background: #E8C96A; transform: translateY(-1px); }

/* BOOK DIVIDER */
.book-divider {
  max-width: 960px;
  margin: 0 auto;
  padding: 0 40px;
  opacity: 0.5;
}

/* MAIN GRID */
.footer-main {
  padding: 64px 0 48px;
  border-bottom: 1px solid rgba(247,240,230,0.07);
}
.footer-main-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 40px;
  display: grid;
  grid-template-columns: 1.6fr 1fr 1fr 1fr 1.5fr;
  gap: 48px;
}

/* BRAND COL */
.footer-brand { display: flex; flex-direction: column; gap: 0; }
.footer-logo {
  display: inline-flex;
  align-items: center;
  gap: 10px;
  text-decoration: none;
  margin-bottom: 18px;
}
.logo-icon { font-size: 1.3rem; }
.logo-text {
  font-family: 'Playfair Display', serif;
  font-size: 1.15rem;
  font-weight: 700;
  color: #F7F0E6;
  letter-spacing: -0.02em;
}
.logo-text em { font-style: italic; color: #C9A84C; margin-left: 3px; }
.footer-brand-desc {
  font-size: 0.84rem;
  line-height: 1.75;
  color: rgba(247,240,230,0.45);
  margin-bottom: 24px;
}
.footer-socials { display: flex; gap: 8px; }
.social-btn {
  text-decoration: none;
  width: 34px; height: 34px;
  border: 1.5px solid rgba(247,240,230,0.12);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.78rem;
  color: rgba(247,240,230,0.4);
  transition: border-color 0.2s, color 0.2s, background 0.2s;
}
.social-btn:hover {
  border-color: #C9A84C;
  color: #C9A84C;
  background: rgba(201,168,76,0.08);
}

/* LINK COLS */
.footer-col { display: flex; flex-direction: column; }
.footer-col-heading {
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: #F7F0E6;
  margin-bottom: 20px;
}
.footer-links { list-style: none; display: flex; flex-direction: column; gap: 10px; }
.footer-link {
  text-decoration: none;
  font-size: 0.85rem;
  font-weight: 400;
  color: rgba(247,240,230,0.45);
  transition: color 0.2s;
  line-height: 1.4;
}
.footer-link:hover { color: #C9A84C; }

/* NEWSLETTER */
.footer-newsletter {}
.newsletter-sub {
  font-size: 0.82rem;
  line-height: 1.7;
  color: rgba(247,240,230,0.45);
  margin-bottom: 18px;
}
.newsletter-form { display: flex; flex-direction: column; gap: 8px; }
.newsletter-field {
  display: flex;
  border: 1.5px solid rgba(247,240,230,0.12);
  border-radius: 5px;
  overflow: hidden;
  transition: border-color 0.2s;
}
.newsletter-field:focus-within { border-color: #C9A84C; }
.newsletter-field.error { border-color: #C0454A; }
.newsletter-field.success { border-color: #7A9E7E; }
.newsletter-field input {
  flex: 1;
  background: transparent;
  border: none;
  outline: none;
  padding: 11px 14px;
  font-family: 'Inter', sans-serif;
  font-size: 0.84rem;
  color: #F7F0E6;
}
.newsletter-field input::placeholder { color: rgba(247,240,230,0.25); }
.newsletter-field input:disabled { opacity: 0.5; }
.newsletter-field button {
  flex-shrink: 0;
  background: #C9A84C;
  border: none;
  padding: 0 16px;
  color: #1A2233;
  cursor: pointer;
  font-size: 0.9rem;
  font-weight: 700;
  transition: background 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
}
.newsletter-field button:hover:not(:disabled) { background: #E8C96A; }
.newsletter-field button:disabled { opacity: 0.7; cursor: default; }
.newsletter-error {
  font-size: 0.7rem;
  color: #C0454A;
  font-weight: 500;
}
.newsletter-success {
  font-size: 0.78rem;
  color: #7A9E7E;
  font-weight: 500;
}

/* BOTTOM BAR */
.footer-bottom { padding: 24px 0; }
.footer-bottom-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 40px;
  display: flex;
  align-items: center;
  gap: 32px;
  flex-wrap: wrap;
}
.footer-copy {
  font-size: 0.75rem;
  color: rgba(247,240,230,0.25);
}
.footer-bottom-links {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
}
.footer-legal-link {
  text-decoration: none;
  font-size: 0.75rem;
  color: rgba(247,240,230,0.25);
  transition: color 0.2s;
}
.footer-legal-link:hover { color: #C9A84C; }
.footer-made {
  margin-left: auto;
  font-size: 0.75rem;
  color: rgba(247,240,230,0.2);
}
.heart { color: #C9A84C; }

/* RESPONSIVE */
@media (max-width: 1100px) {
  .footer-main-inner { grid-template-columns: 1fr 1fr 1fr; }
  .footer-brand { grid-column: span 2; }
  .footer-newsletter { grid-column: span 1; }
}
@media (max-width: 700px) {
  .footer-main-inner { grid-template-columns: 1fr 1fr; }
  .footer-brand { grid-column: span 2; }
  .footer-newsletter { grid-column: span 2; }
  .footer-top-inner { flex-direction: column; align-items: flex-start; }
  .footer-bottom-inner { flex-direction: column; align-items: flex-start; gap: 12px; }
  .footer-made { margin-left: 0; }
}
@media (max-width: 420px) {
  .footer-main-inner { grid-template-columns: 1fr; }
  .footer-brand { grid-column: span 1; }
  .footer-newsletter { grid-column: span 1; }
  .footer-main-inner { padding: 0 20px; }
  .footer-top-inner, .footer-bottom-inner { padding: 0 20px; }
  .book-divider { padding: 0 20px; }
}
</style>