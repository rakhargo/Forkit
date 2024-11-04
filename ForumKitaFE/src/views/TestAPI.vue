<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()

<template>
    <div>
      <h1>Data from MongoDB API</h1>
      <div v-if="error" class="error">Error: {{ error }}</div>
      <div v-if="loading">Loading...</div>
      
      <div v-if="!loading && data">
        <div v-for="(item, index) in data" :key="item.id" class="data-item">
          <h2>{{ item.name }}</h2>
          <p><strong>Creator ID:</strong> {{ item.creatorId }}</p>
          <p><strong>Moderators:</strong> {{ item.moderators.join(', ') || 'No moderators' }}</p>
          <p><strong>Posts:</strong> {{ item.posts.length }} posts</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    name: 'DataDisplay',
    data() {
      return {
        data: [],      // Store array of data here
        loading: true, // Show loading state initially
        error: null,   // To catch any errors
      };
    },
    async created() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/subtopiq/all');
        this.data = response.data; // Assuming response.data is the array of objects
      } catch (error) {
        this.error = error.message || 'An error occurred';
      } finally {
        this.loading = false;
      }
    },
  };
  </script>
  
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
  