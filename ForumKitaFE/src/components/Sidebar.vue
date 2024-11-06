<script setup lang="ts">
import { ChartBarIcon, FireIcon, StarIcon } from '@heroicons/vue/24/outline'
import { useRouter } from 'vue-router'
import { useUserStore } from '../stores/userStore';
import { useSubTopiqStore } from '../stores/subTopiqStore';
import { onMounted } from 'vue';

const router = useRouter()

const communities = [
  { name: 'indonesia', members: '250K', description: 'Komunitas Indonesia' },
  { name: 'programming', members: '180K', description: 'Diskusi Programming' },
  { name: 'gaming', members: '150K', description: 'Komunitas Gaming' },
  { name: 'technology', members: '120K', description: 'Teknologi Terkini' },
  { name: 'science', members: '100K', description: 'Sains dan Penelitian' },
  { name: 'movies', members: '90K', description: 'Film dan Series' },
  { name: 'music', members: '85K', description: 'Musik Indonesia' },
  { name: 'food', members: '75K', description: 'Kuliner Nusantara' },
  { name: 'sports', members: '70K', description: 'Olahraga' },
  { name: 'books', members: '65K', description: 'Komunitas Buku' },
  { name: 'art', members: '60K', description: 'Seni dan Kreativitas' },
  { name: 'photography', members: '55K', description: 'Fotografi' },
  { name: 'finance', members: '50K', description: 'Keuangan dan Investasi' },
  { name: 'health', members: '45K', description: 'Kesehatan' },
  { name: 'education', members: '40K', description: 'Pendidikan' }
]

const subTopiqStore = useSubTopiqStore();
const userStore = useUserStore();
const goToSubforum = (name: string) => {
  router.push(`/f/${name}`)
}

const handleSubTopiq = async (subTopiqId: string) => {
  await subTopiqStore.fetchSubTopiqById(subTopiqId)
}

onMounted(() => {
  console.log(userStore.user?.subTopiqs)
});
</script>

<template>
  <aside class="sidebar">
    <div class="sidebar-card">
      <h2 class="sidebar-title">Subforum saya</h2>
      <div class="communities-list">
        <div
          v-for="subtopiqId in userStore.user?.subTopiqs"
          :key="subtopiqId"
          class="community-item"
          @click="goToSubforum(subtopiqId)"
        >
        {{ handleSubTopiq(subtopiqId) }}
          <div class="community-info">
            <div class="community-avatar"></div>
            <div>
              <div class="community-name">f/{{ subTopiqStore.subtopiq?.name }}</div>
              <!-- <div class="community-description">{{ subTopiqStore.subtopiq. }}</div> -->
              <!-- <div class="community-members">{{ subtopiqId }} members</div> -->
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
  display: flex;
  flex-direction: column;
  gap: 16px;
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
  align-items: flex-start;
  gap: 8px;
  flex: 1;
}

.community-avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: linear-gradient(135deg, #60a5fa, #a855f7);
  flex-shrink: 0;
}

.community-name {
  font-weight: 500;
  margin-bottom: 2px;
}

.community-description {
  font-size: 12px;
  color: var(--text-color);
  margin-bottom: 2px;
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
  white-space: nowrap;
  padding-left: 8px;
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