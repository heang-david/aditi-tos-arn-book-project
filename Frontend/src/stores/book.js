import { defineStore } from "pinia";
import axios from "axios";
import { ref } from "vue";

export const useBookStore = defineStore("bookStore", () => {
  // state
  const books = ref([]);
  const currentBook = ref(null);   // ← separate state for single book detail
  const loading = ref(false);
  const error = ref(null);

  function fetchBooks() {
    loading.value = true;
    error.value = null;
    axios.get("http://127.0.0.1:8000/api/books/")
      .then(response => {
        books.value = response.data
      })
      .catch(err => {
        error.value = err.message || "Failed to fetch books.";
      })
      .finally(() => {
        loading.value = false;
      });
  }

  function fetchBookById(id) {
    loading.value = true;
    error.value = null;
    currentBook.value = null;        // reset while loading
    axios.get("http://127.0.0.1:8000/api/books/" + id)
      .then(response => {
        currentBook.value = response.data   // ✅ stores the single book separately
      })
      .catch(err => {
        error.value = err.message || "Failed to fetch book.";
      })
      .finally(() => {
        loading.value = false;
      });
  }

  return { books, currentBook, loading, error, fetchBooks, fetchBookById };
});