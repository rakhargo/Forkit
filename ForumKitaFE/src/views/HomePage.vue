<script setup lang="ts">
import PostCard from '../components/PostCard.vue'
import Sidebar from '../components/SideBar.vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const posts = [
  {
    id: 1,
    title: 'Tips Belajar Programming untuk Pemula',
    content: 'Mulai dengan dasar-dasar, pilih satu bahasa pemrograman dan konsisten belajar setiap hari. Jangan lupa untuk praktek dan membuat project sendiri.',
    author: 'programmer_sejati',
    votes: 156,
    comments: 45,
    createdAt: new Date('2024-03-10T08:00:00'),
    image: 'https://images.unsplash.com/photo-1461749280684-dccba630e2f6'
  },
  {
    id: 2,
    title: 'Rekomendasi Tempat Wisata di Indonesia',
    content: 'Berbagi pengalaman traveling ke berbagai tempat wisata di Indonesia. Dari Sabang sampai Merauke, Indonesia punya banyak tempat indah yang wajib dikunjungi.',
    author: 'traveler_indo',
    votes: 234,
    comments: 78,
    createdAt: new Date('2024-03-09T15:30:00'),
    image: 'https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9'
  },
  {
    id: 3,
    title: 'Diskusi: Masa Depan Teknologi AI di Indonesia',
    content: 'Bagaimana pendapat kalian tentang perkembangan AI di Indonesia? Apakah kita sudah siap menghadapi revolusi teknologi ini?',
    author: 'tech_enthusiast',
    votes: 89,
    comments: 32,
    createdAt: new Date('2024-03-09T10:15:00')
  }
]
</script>

<template>
  <main class="main-content">
    <div class="posts-container">
      <button 
        class="new-post-button"
        @click="router.push('/create-post')"
      >
        Buat Post Baru
      </button>

      <button 
        class="test-api-button"
        @click="router.push('/api')"
      >
        Buat Ngetes API Hehe
      </button>
      
      <PostCard
        v-for="post in posts"
        :key="post.id"
        :post="post"
      />
    </div>
    
    <Sidebar class="sidebar-container" />
  </main>
</template>

<style scoped>
.main-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 76px 20px 20px;
  display: flex;
  gap: 24px;
}

.posts-container {
  flex: 1;
}

.new-post-button {
  width: 100%;
  padding: 12px;
  background-color: white;
  border: none;
  border-radius: 8px;
  box-shadow: var(--shadow);
  margin-bottom: 16px;
  font-size: 16px;
  color: var(--gray-medium);
  cursor: pointer;
  transition: all 0.2s;
}

.new-post-button:hover {
  background-color: var(--gray-light);
  color: var(--primary-color);
}

.test-api-button {
  width: 100%;
  padding: 12px;
  background-color: white;
  border: none;
  border-radius: 8px;
  box-shadow: var(--shadow);
  margin-bottom: 16px;
  font-size: 16px;
  color: var(--gray-medium);
  cursor: pointer;
  transition: all 0.2s;
}

.test-api-button:hover {
  background-color: var(--gray-light);
  color: var(--primary-color);
}

.sidebar-container {
  display: none;
}

@media (min-width: 1024px) {
  .sidebar-container {
    display: block;
  }
}
</style>