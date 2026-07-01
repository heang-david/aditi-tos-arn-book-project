<template>
  <div class="search-bar">
    <svg class="search-icon" width="16" height="16" viewBox="0 0 24 24" fill="none"
      stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/>
    </svg>
    <input
      :value="modelValue"
      type="text"
      class="search-input"
      :placeholder="placeholder"
      @input="$emit('update:modelValue', $event.target.value)"
    />
    <button v-if="modelValue" class="search-clear" @click="$emit('update:modelValue', '')">✕</button>
  </div>
</template>

<script setup>
defineProps({
  modelValue: { type: String, default: '' },
  placeholder: { type: String, default: 'Search…' },
})
defineEmits(['update:modelValue'])
</script>

<style scoped>
.search-bar {
  display: flex;
  align-items: center;
  gap: 10px;
  background: #fff;
  border: 1.5px solid #E8E1D9;
  border-radius: 24px;
  padding: 9px 16px;
  transition: border-color 0.2s;
}
.search-bar:focus-within { border-color: #C9A84C; }

.search-icon { color: #9B9590; flex-shrink: 0; }

.search-input {
  flex: 1;
  border: none;
  outline: none;
  font-family: 'Inter', sans-serif;
  font-size: 0.875rem;
  color: #1A2233;
  background: transparent;
}
.search-input::placeholder { color: #B0ABA5; }

.search-clear {
  background: none;
  border: none;
  cursor: pointer;
  color: #B0ABA5;
  font-size: 0.75rem;
  padding: 0;
  line-height: 1;
}
.search-clear:hover { color: #1A2233; }
</style>
