<template>
  <section id="contact" class="contact">

    <div class="contact-inner">

      <!-- left — info -->
      <div class="contact-info" :class="{ visible: mounted }">

        <div class="section-eyebrow">
          <svg width="40" height="1" viewBox="0 0 40 1"><line x1="0" y1="0.5" x2="40" y2="0.5" stroke="#C9A84C" stroke-width="1"/></svg>
          Get in touch
        </div>

        <h2 class="contact-title">
          We'd love to<br/>
          <em>hear from you.</em>
        </h2>

        <p class="contact-sub">
          Can't find a title? Have a question about an order?
          Want a personalised reading list? Our team reads every message — 
          and usually replies within a few hours.
        </p>

        <ul class="contact-details">
          <li v-for="detail in details" :key="detail.label" class="detail-item">
            <div class="detail-icon">{{ detail.icon }}</div>
            <div class="detail-body">
              <span class="detail-label">{{ detail.label }}</span>
              <a :href="detail.href" class="detail-value">{{ detail.value }}</a>
            </div>
          </li>
        </ul>

        <div class="contact-social">
          <span class="social-label">Follow us</span>
          <div class="social-links">
            <a v-for="s in socials" :key="s.name" :href="s.href" class="social-link" :aria-label="s.name">
              <span>{{ s.icon }}</span>
            </a>
          </div>
        </div>

      </div>

      <!-- right — form -->
      <div class="contact-form-wrap" :class="{ visible: mounted }">
        <div class="form-card">

          <div class="form-header">
            <h3>Send us a message</h3>
            <p>We'll get back to you within 24 hours.</p>
          </div>

          <form class="contact-form" @submit.prevent="handleSubmit" novalidate>

            <div class="form-row">
              <div class="form-field" :class="{ error: errors.name, filled: form.name }">
                <label for="contact-name">Your name</label>
                <input
                  id="contact-name"
                  v-model="form.name"
                  type="text"
                  placeholder="e.g. Sophea Keo"
                  autocomplete="name"
                  @blur="validate('name')"
                />
                <span v-if="errors.name" class="field-error">{{ errors.name }}</span>
              </div>
              <div class="form-field" :class="{ error: errors.email, filled: form.email }">
                <label for="contact-email">Email address</label>
                <input
                  id="contact-email"
                  v-model="form.email"
                  type="email"
                  placeholder="you@example.com"
                  autocomplete="email"
                  @blur="validate('email')"
                />
                <span v-if="errors.email" class="field-error">{{ errors.email }}</span>
              </div>
            </div>

            <div class="form-field" :class="{ error: errors.subject, filled: form.subject }">
              <label for="contact-subject">Subject</label>
              <select id="contact-subject" v-model="form.subject" @blur="validate('subject')">
                <option value="" disabled>Choose a topic…</option>
                <option v-for="opt in subjects" :key="opt" :value="opt">{{ opt }}</option>
              </select>
              <span v-if="errors.subject" class="field-error">{{ errors.subject }}</span>
            </div>

            <div class="form-field" :class="{ error: errors.message, filled: form.message }">
              <label for="contact-message">Message</label>
              <textarea
                id="contact-message"
                v-model="form.message"
                rows="5"
                placeholder="Tell us what's on your mind…"
                @blur="validate('message')"
              ></textarea>
              <div class="char-count" :class="{ warn: form.message.length > 460 }">
                {{ form.message.length }}/500
              </div>
              <span v-if="errors.message" class="field-error">{{ errors.message }}</span>
            </div>

            <button type="submit" class="submit-btn" :disabled="submitting || submitted">
              <span v-if="submitting" class="btn-loading">
                <span class="spinner"></span>
                Sending…
              </span>
              <span v-else-if="submitted" class="btn-success">
                ✓ Message sent!
              </span>
              <span v-else>
                Send message
                <svg width="15" height="15" viewBox="0 0 15 15" fill="none">
                  <path d="M2 7.5h11M8.5 3l4 4.5-4 4.5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
              </span>
            </button>

          </form>

        </div>
      </div>

    </div>

  </section>
</template>

<script>
export default {
  name: 'ContactSection',
  data() {
    return {
      mounted: false,
      submitting: false,
      submitted: false,
      form: {
        name: '',
        email: '',
        subject: '',
        message: '',
      },
      errors: {
        name: '',
        email: '',
        subject: '',
        message: '',
      },
      subjects: [
        'Order enquiry',
        'Book recommendation',
        'Bulk / wholesale order',
        'Press & partnerships',
        'Something else',
      ],
      details: [
        { icon: '✉', label: 'Email us',     href: 'mailto:hello@tosarnbooks.com', value: 'hello@tosarnbooks.com' },
        { icon: '◎', label: 'Visit us',      href: '#',                            value: '45 Norodom Blvd, Phnom Penh' },
        { icon: '◷', label: 'Opening hours', href: '#',                            value: 'Mon – Sat, 9 am – 7 pm' },
      ],
      socials: [
        { name: 'Instagram', icon: '◈', href: '#' },
        { name: 'Facebook',  icon: '◉', href: '#' },
        { name: 'Twitter/X', icon: '✦', href: '#' },
      ],
    }
  },
  methods: {
    validate(field) {
      this.errors[field] = ''
      if (field === 'name' && !this.form.name.trim()) {
        this.errors.name = 'Please enter your name.'
      }
      if (field === 'email') {
        if (!this.form.email.trim()) this.errors.email = 'Please enter your email.'
        else if (!/\S+@\S+\.\S+/.test(this.form.email)) this.errors.email = 'That doesn\'t look like a valid email.'
      }
      if (field === 'subject' && !this.form.subject) {
        this.errors.subject = 'Please choose a topic.'
      }
      if (field === 'message') {
        if (!this.form.message.trim()) this.errors.message = 'Please write a message.'
        else if (this.form.message.length > 500) this.errors.message = 'Message is too long (max 500 characters).'
      }
    },
    handleSubmit() {
      ['name', 'email', 'subject', 'message'].forEach(f => this.validate(f))
      const hasErrors = Object.values(this.errors).some(e => e)
      if (hasErrors) return

      this.submitting = true
      // Simulate async send
      setTimeout(() => {
        this.submitting = false
        this.submitted = true
        this.form = { name: '', email: '', subject: '', message: '' }
      }, 1800)
    },
  },
  mounted() {
    this.$nextTick(() => { this.mounted = true })
  },
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Inter:wght@300;400;500;600&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

.contact {
  background: #F7F0E6;
  padding: 100px 0 110px;
}
.contact-inner {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 40px;
  display: grid;
  grid-template-columns: 1fr 1.3fr;
  gap: 80px;
  align-items: start;
}

/* INFO SIDE */
.contact-info {
  opacity: 0;
  transform: translateX(-24px);
  transition: opacity 0.6s ease, transform 0.6s ease;
}
.contact-info.visible { opacity: 1; transform: none; }

.section-eyebrow {
  display: inline-flex;
  align-items: center;
  gap: 12px;
  font-family: 'Inter', sans-serif;
  font-size: 0.7rem;
  font-weight: 600;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #C9A84C;
  margin-bottom: 20px;
}
.contact-title {
  font-family: 'Playfair Display', Georgia, serif;
  font-size: clamp(2rem, 3.5vw, 3rem);
  font-weight: 700;
  color: #1A2233;
  letter-spacing: -0.03em;
  line-height: 1.1;
  margin-bottom: 20px;
}
.contact-title em { font-style: italic; color: #C9A84C; }
.contact-sub {
  font-family: 'Inter', sans-serif;
  font-size: 0.95rem;
  font-weight: 300;
  line-height: 1.8;
  color: #6B6560;
  margin-bottom: 40px;
  max-width: 380px;
}

.contact-details { list-style: none; display: flex; flex-direction: column; gap: 20px; margin-bottom: 40px; }
.detail-item { display: flex; align-items: flex-start; gap: 16px; }
.detail-icon {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border: 1.5px solid #E8E1D9;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.9rem;
  color: #C9A84C;
  flex-shrink: 0;
  margin-top: 2px;
}
.detail-body { display: flex; flex-direction: column; gap: 2px; }
.detail-label {
  font-family: 'Inter', sans-serif;
  font-size: 0.68rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #9B9590;
}
.detail-value {
  font-family: 'Inter', sans-serif;
  font-size: 0.9rem;
  font-weight: 500;
  color: #1A2233;
  text-decoration: none;
  transition: color 0.2s;
}
.detail-value:hover { color: #C9A84C; }

.contact-social { display: flex; align-items: center; gap: 16px; }
.social-label {
  font-family: 'Inter', sans-serif;
  font-size: 0.68rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #9B9590;
}
.social-links { display: flex; gap: 8px; }
.social-link {
  text-decoration: none;
  width: 36px; height: 36px;
  border: 1.5px solid #E8E1D9;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.8rem;
  color: #6B6560;
  transition: border-color 0.2s, color 0.2s, background 0.2s;
}
.social-link:hover { border-color: #C9A84C; color: #C9A84C; background: rgba(201,168,76,0.08); }

/* FORM SIDE */
.contact-form-wrap {
  opacity: 0;
  transform: translateX(24px);
  transition: opacity 0.6s ease 0.15s, transform 0.6s ease 0.15s;
}
.contact-form-wrap.visible { opacity: 1; transform: none; }

.form-card {
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 8px 48px rgba(26,34,51,0.1);
  overflow: hidden;
}
.form-header {
  background: #1A2233;
  padding: 28px 36px;
}
.form-header h3 {
  font-family: 'Playfair Display', serif;
  font-size: 1.35rem;
  font-weight: 700;
  color: #F7F0E6;
  letter-spacing: -0.02em;
  margin-bottom: 4px;
}
.form-header p {
  font-family: 'Inter', sans-serif;
  font-size: 0.8rem;
  color: rgba(247,240,230,0.45);
}

.contact-form { padding: 32px 36px 36px; display: flex; flex-direction: column; gap: 20px; }

.form-row { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }

.form-field { display: flex; flex-direction: column; gap: 6px; position: relative; }
.form-field label {
  font-family: 'Inter', sans-serif;
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #6B6560;
  transition: color 0.2s;
}
.form-field.filled label, .form-field:focus-within label { color: #1A2233; }

.form-field input,
.form-field select,
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
  appearance: none;
  -webkit-appearance: none;
}
.form-field input::placeholder,
.form-field textarea::placeholder { color: #B0ABA5; }
.form-field input:focus,
.form-field select:focus,
.form-field textarea:focus {
  border-color: #C9A84C;
  background: #fff;
}
.form-field.error input,
.form-field.error select,
.form-field.error textarea { border-color: #C0454A; background: #FEF7F7; }

.field-error {
  font-family: 'Inter', sans-serif;
  font-size: 0.7rem;
  color: #C0454A;
  font-weight: 500;
}

.char-count {
  position: absolute;
  bottom: 10px;
  right: 12px;
  font-family: 'Inter', sans-serif;
  font-size: 0.65rem;
  color: #B0ABA5;
}
.char-count.warn { color: #C0454A; }

.submit-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  font-family: 'Inter', sans-serif;
  font-size: 0.82rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #1A2233;
  background: #C9A84C;
  border: none;
  padding: 16px 28px;
  border-radius: 5px;
  cursor: pointer;
  transition: background 0.2s, transform 0.15s;
  width: 100%;
  margin-top: 4px;
}
.submit-btn:hover:not(:disabled) { background: #E8C96A; transform: translateY(-1px); }
.submit-btn:disabled { opacity: 0.75; cursor: not-allowed; }
.submit-btn .btn-success { color: #1A2233; }

.spinner {
  display: inline-block;
  width: 14px; height: 14px;
  border: 2px solid rgba(26,34,51,0.3);
  border-top-color: #1A2233;
  border-radius: 50%;
  animation: spin 0.7s linear infinite;
}
@keyframes spin {
  to { transform: rotate(360deg); }
}

/* RESPONSIVE */
@media (max-width: 900px) {
  .contact-inner { grid-template-columns: 1fr; gap: 48px; }
  .contact-info { transform: none; }
  .contact-form-wrap { transform: none; }
  .contact-sub { max-width: 100%; }
}
@media (max-width: 600px) {
  .contact { padding: 80px 0 90px; }
  .contact-inner { padding: 0 20px; }
  .form-row { grid-template-columns: 1fr; }
  .contact-form { padding: 24px 20px; }
  .form-header { padding: 22px 20px; }
}
</style>
