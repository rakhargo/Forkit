<script setup lang="ts">
import { ChartBarIcon, FireIcon, StarIcon } from '@heroicons/vue/24/outline'
import { useRouter } from 'vue-router'

const router = useRouter()

const communities = [
  { name: 'indonesia', members: '250K' },
  { name: 'programming', members: '180K' },
  { name: 'gaming', members: '150K' },
  { name: 'technology', members: '120K' },
  { name: 'science', members: '100K' },
]

const goToSubforum = (name: string) => {
  router.push(`/f/${name}`)
}
</script>

<template>
  <aside class="sidebar">
    <div class="sidebar-card">
      <h2 class="sidebar-title">Subforum Populer</h2>
      <div class="communities-list">
        <div
          v-for="community in communities"
          :key="community.name"
          class="community-item"
          @click="goToSubforum(community.name)"
        >
          <div class="community-info">
            <div class="community-avatar"></div>
            <div>
              <div class="community-name">f/{{ community.name }}</div>
              <div class="community-members">{{ community.members }} members</div>
            </div>
          </div>
          <button class="join-button">Join</button>
        </div>
      </div>
    </div>

    <div class="sidebar-card">
      <h2 class="sidebar-title">Kategori</h2>
      <div class="categories-list">
        <div class="category-item">
          <ChartBarIcon class="category-icon" />
          <span>Trending</span>
        </div>
        <div class="category-item">
          <FireIcon class="category-icon" />
          <span>Hot</span>
        </div>
        <div class="category-item">
          <StarIcon class="category-icon" />
          <span>Top</span>
        </div>
      </div>
    </div>
  </aside>
</template>

<style scoped>
.sidebar {
  width: 320px;
}

.sidebar-card {
  background: white;
  border-radius: 8px;
  box-shadow: var(--shadow);
  padding: 16px;
  margin-bottom: 16px;
}

.sidebar-title {
  font-size: 18px;
  font-weight: 500;
  margin-bottom: 16px;
}

.communities-list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.community-item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 8px;
  border-radius: 4px;
  cursor: pointer;
}

.community-item:hover {
  background-color: var(--gray-light);
}

.community-info {
  display: flex;
  align-items: center;
  gap: 8px;
}

.community-avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: linear-gradient(135deg, #60a5fa, #a855f7);
}

.community-name {
  font-weight: 500;
}

.community-members {
  font-size: 12px;
  color: var(--gray-medium);
}

.join-button {
  color: #0079d3;
  background: none;
  border: none;
  font-size: 14px;
  cursor: pointer;
}

.join-button:hover {
  color: #1484d6;
}

.categories-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.category-item {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px;
  border-radius: 4px;
  cursor: pointer;
}

.category-item:hover {
  background-color: var(--gray-light);
}

.category-icon {
  width: 20px;
  height: 20px;
  color: var(--gray-medium);
}
</style>