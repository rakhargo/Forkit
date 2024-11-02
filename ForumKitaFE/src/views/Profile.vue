<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router'
import PostCard from '../components/PostCard.vue'

const route = useRoute()
const username = computed(() => route.params.username as string)

const profile = ref({
  username: username,
  joinDate: new Date('2024-01-01'),
  karma: 1250,
  description: 'Ini adalah bio profil saya.',
  isOwnProfile: username.value === 'myusername'
})

const posts = ref([
  {
    id: 1,
    title: 'Post dari profil ini',
    content: 'Ini adalah konten post yang dibuat oleh pengguna ini.',
    author: username,
    votes: 25,
    comments: 8,
    createdAt: new Date('2024-03-10T08:00:00')
  }
])
</script>

<template>
  <div class="profile-container">
    <div class="profile-header">
      <div class="profile-info">
        <h1 class="profile-username">u/{{ username }}</h1>
        <p class="profile-stats">
          {{ profile.karma }} karma • 
          Bergabung {{ profile.joinDate.toLocaleDateString() }}
        </p>
        <p class="profile-description">
          {{ profile.description }}
        </p>
      </div>
      <button
        v-if="!profile.isOwnProfile"
        class="btn btn-primary"
      >
        Follow
      </button>
      <button
        v-else
        class="btn"
      >
        Edit Profile
      </button>
    </div>
    
    <div class="profile-content">
      <div class="posts-container">
        <h2 class="section-title">Post</h2>
        <PostCard
          v-for="post in posts"
          :key="post.id"
          :post="post"
        />
      </div>
      
      <div class="profile-sidebar">
        <div class="sidebar-card">
          <h2 class="sidebar-title">Tentang u/{{ username }}</h2>
          <div class="sidebar-stats">
            <div class="stat-item">
              <div class="stat-value">{{ profile.karma }}</div>
              <div class="stat-label">Karma</div>
            </div>
            <div class="stat-item">
              <div class="stat-value">
                {{ new Date().getFullYear() - profile.joinDate.getFullYear() }}
              </div>
              <div class="stat-label">Tahun</div>
            </div>
          </div>
          <p class="sidebar-description">
            {{ profile.description }}
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.profile-container {
  padding: 76px 20px 20px;
}

.profile-header {
  background: white;
  padding: 20px;
  margin-bottom: 20px;
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.profile-username {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 8px;
}

.profile-stats {
  color: var(--gray-medium);
  font-size: 14px;
  margin-bottom: 8px;
}

.profile-description {
  color: var(--text-color);
}

.profile-content {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  gap: 24px;
}

.posts-container {
  flex: 1;
}

.section-title {
  font-size: 20px;
  font-weight: 500;
  margin-bottom: 16px;
}

.profile-sidebar {
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
  margin-top: 16px;
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
  .profile-sidebar {
    display: block;
  }
}
</style>