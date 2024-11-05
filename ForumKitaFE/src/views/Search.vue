<script setup lang="ts">
import { ref, onMounted, watch } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const searchQuery = ref('')
const searchResults = ref([
  {
    name: 'programming',
    description: 'Komunitas programmer Indonesia',
    members: 180000
  },
  {
    name: 'indonesia',
    description: 'Diskusi seputar Indonesia',
    members: 250000
  }
])

const performSearch = (query: string) => {
  // TODO: Implement actual search logic
  console.log('Searching for:', query)
}

watch(() => route.query.q, (newQuery) => {
  if (newQuery) {
    searchQuery.value = newQuery as string
    performSearch(searchQuery.value)
  }
})

onMounted(() => {
  if (route.query.q) {
    searchQuery.value = route.query.q as string
    performSearch(searchQuery.value)
  }
})
</script>

<template>
  <div class="search-page">
    <div class="search-results">
      <h1 class="search-title">
        Hasil pencarian untuk "{{ searchQuery }}"
      </h1>
      
      <div class="results-list">
        <div
          v-for="result in searchResults"
          :key="result.name"
          class="result-card"
          @click="$router.push(`/f/${result.name}`)"
        >
          <div class="result-info">
            <h2 class="result-name">f/{{ result.name }}</h2>
            <p class="result-description">{{ result.description }}</p>
            <p class="result-members">
              {{ result.members.toLocaleString() }} members
            </p>
          </div>
          <button class="btn btn-primary">Join</button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.search-page {
  padding: 76px 20px 20px;
  max-width: 800px;
  margin: 0 auto;
}

.search-title {
  font-size: 24px;
  font-weight: 500;
  margin-bottom: 24px;
}

.results-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.result-card {
  background: white;
  border-radius: 8px;
  box-shadow: var(--shadow);
  padding: 16px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  cursor: pointer;
  transition: box-shadow 0.2s;
}

.result-card:hover {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.result-info {
  flex: 1;
}

.result-name {
  font-size: 18px;
  font-weight: 500;
  margin-bottom: 4px;
}

.result-description {
  color: var(--text-color);
  margin-bottom: 8px;
}

.result-members {
  font-size: 14px;
  color: var(--gray-medium);
}
</style>