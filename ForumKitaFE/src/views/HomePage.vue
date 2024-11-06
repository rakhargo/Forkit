<script setup lang="ts">
import { ref, onMounted } from 'vue'
import PostCard from '../components/PostCard.vue'
import Sidebar from '../components/Sidebar.vue'
import { useRouter } from 'vue-router'
import { usePostStore } from '../stores/postStore';
import { useUserStore } from '../stores/userStore';

const router = useRouter()
const loading = ref(false)
const page = ref(1)
const hasMore = ref(true)

const posts = ref([
  {
    id: 1,
    title: 'Tips Belajar Programming untuk Pemula',
    content: 'Mulai dengan dasar-dasar, pilih satu bahasa pemrograman dan konsisten belajar setiap hari. Jangan lupa untuk praktek dan membuat project sendiri.',
    author: 'programmer_sejati',
    votes: 156,
    comments: 45,
    subforum: 'programming',
    createdAt: new Date('2024-03-10T08:00:00'),
    image: 'https://images.unsplash.com/photo-1461749280684-dccba630e2f6'
  },
  {
    id: 2,
    title: 'Review Film Terbaru: Petualangan Sherina 2',
    content: 'Film ini menghadirkan nostalgia sekaligus kesegaran baru. Akting, musik, dan visualnya sangat memukau.',
    author: 'moviebuff',
    votes: 245,
    comments: 89,
    subforum: 'movies',
    createdAt: new Date('2024-03-10T07:30:00')
  },
  {
    id: 3,
    title: 'Resep Rendang Padang Autentik',
    content: 'Berbagi resep rendang warisan keluarga yang sudah 3 generasi. Kuncinya ada di pemilihan rempah dan proses memasak yang tidak bisa dipercepat.',
    author: 'chef_indo',
    votes: 320,
    comments: 67,
    subforum: 'food',
    createdAt: new Date('2024-03-10T06:45:00')
  }
])

const loadMorePosts = async () => {
  if (loading.value || !hasMore.value) return
  
  loading.value = true
  
  try {
    await new Promise(resolve => setTimeout(resolve, 1000))
    
    const newPosts = [
      {
        id: posts.value.length + 1,
        title: 'Perkembangan Teknologi AI di Indonesia',
        content: 'Bagaimana perusahaan teknologi lokal mengadopsi dan mengembangkan solusi AI untuk berbagai sektor industri.',
        author: 'tech_enthusiast',
        votes: Math.floor(Math.random() * 100),
        comments: Math.floor(Math.random() * 50),
        subforum: 'technology',
        createdAt: new Date()
      },
      {
        id: posts.value.length + 2,
        title: 'Tips Investasi Reksa Dana untuk Pemula',
        content: 'Panduan lengkap memulai investasi reksa dana dengan modal minim dan risiko terukur.',
        author: 'finance_guru',
        votes: Math.floor(Math.random() * 100),
        comments: Math.floor(Math.random() * 50),
        subforum: 'finance',
        createdAt: new Date()
      },
      {
        id: posts.value.length + 3,
        title: 'Review Album Terbaru Tulus',
        content: 'Mengupas makna mendalam di balik lirik-lirik dalam album terbaru Tulus.',
        author: 'music_lover',
        votes: Math.floor(Math.random() * 100),
        comments: Math.floor(Math.random() * 50),
        subforum: 'music',
        createdAt: new Date()
      }
    ]
    
    posts.value.push(...newPosts)
    page.value++
    
    if (page.value >= 5) {
      hasMore.value = false
    }
  } finally {
    loading.value = false
  }
}

const handleScroll = (e: Event) => {
  const target = e.target as HTMLElement
  const bottom = target.scrollHeight - target.scrollTop - target.clientHeight < 50
  
  if (bottom) {
    loadMorePosts()
  }
}

const postStore = usePostStore();
const userStore = useUserStore();

onMounted(() => {
  loadMorePosts()
  postStore.fetchAllPosts();
});
</script>

<template>
  <main class="main-content">
    <div class="scrollable-content hide-scrollbar" @scroll="handleScroll">
      <!-- <PostCard
        v-for="post in posts"
        :key="post.id"
        :post="post"
      /> -->
      <PostCard 
        v-for="post in postStore.posts" 
        :key="post.id" 
        :post="post" 
      />
      <div v-if="loading" class="loading-spinner">
        Loading more posts...
      </div>
    </div>
    
    <div class="sidebar-wrapper hide-scrollbar">
      <Sidebar />
    </div>
  </main>
</template>