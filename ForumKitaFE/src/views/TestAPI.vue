<script setup lang="ts">
import axios from 'axios';
import { ref, onMounted } from 'vue';

const data = ref([]);       // Reactive array to store data
const loading = ref(true);   // Loading state
const error = ref(null);     // Error handling

onMounted(async () => {
  try {
    console.log("Fetching data from API...");
    const response = await axios.get('http://127.0.0.1:8000/subtopiq/all');
    console.log("API response received:", response.data);
    
    if (Array.isArray(response.data)) {
      data.value = response.data; // Assign data if it's an array
      console.log("Data stored in component:", data.value);
    } else {
      error.value = "Unexpected data format from API";
      console.warn("Expected an array, got:", typeof response.data);
    }
  } catch (err) {
    console.error("Error fetching data:", err);
    error.value = err instanceof Error ? err.message : 'An error occurred';
  } finally {
    loading.value = false;
  }
});
</script>

<template>
  <div>
    <h1>Data from MongoDB API</h1>
    
    <div v-if="error" class="error">Error: {{ error }}</div>
    <div v-if="loading">Loading...</div>
    
    <div v-if="!loading && data.length">
      <div v-for="(item, index) in data" :key="item.id" class="data-item">
        <h2>{{ item.name }}</h2>
        <p><strong>Creator ID:</strong> {{ item.creatorId }}</p>
        
        <p><strong>Moderators:</strong></p>
        <ul>
          <li v-for="mod in item.moderators" :key="mod.moderatorId">
            Moderator ID: {{ mod.moderatorId }}
          </li>
        </ul>

        <p><strong>Posts:</strong></p>
        <ul>
          <li v-for="post in item.posts" :key="post.postId">
            Post ID: {{ post.postId }}
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<style scoped>
.error {
  color: red;
}
.data-item {
  border: 1px solid #ddd;
  padding: 1em;
  margin-bottom: 1em;
}
</style>
