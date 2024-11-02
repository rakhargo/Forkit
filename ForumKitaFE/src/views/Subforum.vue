<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router'
import PostCard from '../components/PostCard.vue'

const route = useRoute()
const forumName = computed(() => route.params.name as string)

const forum = ref({
  name: forumName,
  description: 'Deskripsi subforum ini akan muncul di sini.',
  members: 12500,
  online: 150
})

const posts = ref([
  {
    id: 1,
    title: 'Post pertama di subforum ini',
    content: 'Ini adalah konten dari post pertama di subforum ini.',
    author: 'user123',
    votes: 42,
    comments: 15,
    createdAt: new Date('2024-03-10T08:00:00')
  }
])
</script>

<template>
  <div class="subforum-container">
    <div class="subforum-header">
      <div class="subforum-info">
        <h1 class="subforum-title">f/{{ forumName }}</h1>
        <p class="subforum-stats">
          {{ forum.members.toLocaleString() }} members • 
          {{ forum.online.toLocaleString() }} online
        </p>
        <p class="subforum-description">
          {{ forum.description }}
        </p>
      </div>
      <button class="btn btn-primary">Join</button>
    </div>
    
    <div class="subforum-content">
      <div class="posts-container">
        <div class="new-post">
          <router-link
            :to="{ name: 'create-post' }"
            class="new-post-input"
          >
            Buat post baru di f/{{ forumName }}...
          </router-link>
        </div>
        
        <PostCard
          v-for="post in posts"
          :key="post.id"
          :post="post"
        />
      </div>
      
      <div class="subforum-sidebar">
        <div class="sidebar-card">
          <h2 class="sidebar-title">Tentang Komunitas</h2>
          <p class="sidebar-description">
            {{ forum.description }}
          </p>
          <div class="sidebar-stats">
            <div class="stat-item">
              <div class="stat-value">{{ forum.members.toLocaleString() }}</div>
              <div class="stat-label">Members</div>
            </div>
            <div class="stat-item">
              <div class="stat-value">{{ forum.online.toLocaleString() }}</div>
              <div class="stat-label">Online</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.subforum-container {
  padding: 76px 20px 20px;
}

.subforum-header {
  background: white;
  padding: 20px;
  margin-bottom: 20px;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.subforum-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 8px;
}

.subforum-stats {
  color: var(--gray-medium);
  font-size: 14px;
  margin-bottom: 8px;
}

.subforum-description {
  color: var(--text-color);
}

.subforum-content {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  gap: 24px;
}

.posts-container {
  flex: 1;
}

.new-post {
  background: white;
  padding: 16px;
  border-radius: 8px;
  box-shadow: var(--shadow);
  margin-bottom: 16px;
}

.new-post-input {
  display: block;
  width: 100%;
  padding: 8px 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: var(--gray-light);
  text-decoration: none;
  color: var(--gray-medium);
}

.new-post-input:hover {
  border-color: var(--primary-color);
}

.subforum-sidebar {
  width: 320px;
  display: none;
}

.sidebar-card {
  background: white;
  border-radius: 8px;
  box-shadow: var(--shadow);
  padding: 16px;
}

.sidebar-title {
  font-size: 18px;
  font-weight: 500;
  margin-bottom: 12px;
}

.sidebar-description {
  margin-bottom: 16px;
}

.sidebar-stats {
  display: flex;
  gap: 24px;
}

.stat-item {
  flex: 1;
}

.stat-value {
  font-size: 18px;
  font-weight: 500;
}

.stat-label {
  font-size: 12px;
  color: var(--gray-medium);
}

@media (min-width: 1024px) {
  .subforum-sidebar {
    display: block;
  }
}
</style>