<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import PostCard from '../components/PostCard.vue'

const route = useRoute()
const forumName = computed(() => route.params.name as string)
const searchQuery = computed(() => route.query.q as string)
const loading = ref(false)
const page = ref(1)
const hasMore = ref(true)

const forumPosts = {
  programming: [
    {
      id: 1,
      title: 'Tips Belajar Programming untuk Pemula',
      content: 'Mulai dengan dasar-dasar, pilih satu bahasa pemrograman dan konsisten belajar setiap hari. Jangan lupa untuk praktek dan membuat project sendiri.',
      author: 'programmer_sejati',
      votes: 156,
      comments: 45,
      createdAt: new Date('2024-03-10T08:00:00')
    },
    {
      id: 2,
      title: 'Perbandingan Framework JavaScript 2024',
      content: 'Analisis mendalam tentang React, Vue, Angular, dan Svelte. Mana yang cocok untuk project Anda?',
      author: 'js_master',
      votes: 134,
      comments: 67,
      createdAt: new Date('2024-03-09T15:30:00')
    }
  ],
  movies: [
    {
      id: 1,
      title: 'Review Film Terbaru: Petualangan Sherina 2',
      content: 'Film ini menghadirkan nostalgia sekaligus kesegaran baru. Akting, musik, dan visualnya sangat memukau.',
      author: 'moviebuff',
      votes: 245,
      comments: 89,
      createdAt: new Date('2024-03-10T07:30:00')
    }
  ],
  food: [
    {
      id: 1,
      title: 'Resep Rendang Padang Autentik',
      content: 'Berbagi resep rendang warisan keluarga yang sudah 3 generasi. Kuncinya ada di pemilihan rempah dan proses memasak yang tidak bisa dipercepat.',
      author: 'chef_indo',
      votes: 320,
      comments: 67,
      createdAt: new Date('2024-03-10T06:45:00')
    }
  ],
  technology: [
    {
      id: 1,
      title: 'Perkembangan Teknologi AI di Indonesia',
      content: 'Bagaimana perusahaan teknologi lokal mengadopsi dan mengembangkan solusi AI untuk berbagai sektor industri.',
      author: 'tech_enthusiast',
      votes: 178,
      comments: 45,
      createdAt: new Date('2024-03-09T14:20:00')
    }
  ]
}

const forum = ref({
  name: forumName,
  description: computed(() => {
    const descriptions = {
      programming: 'Komunitas programmer Indonesia. Diskusi seputar coding, development, dan karir IT.',
      movies: 'Diskusi film Indonesia dan internasional. Review, rekomendasi, dan berita terbaru.',
      food: 'Berbagi resep, review restoran, dan diskusi kuliner Nusantara.',
      technology: 'Perkembangan teknologi terkini, gadget, dan inovasi digital.',
      gaming: 'Komunitas gamers Indonesia. Review game, tips & tricks, dan turnamen.',
      science: 'Diskusi sains, penelitian, dan penemuan terbaru.',
      music: 'Komunitas musik Indonesia. Diskusi musik, review album, dan event.',
      sports: 'Berita olahraga, diskusi pertandingan, dan komunitas sport.',
      books: 'Komunitas pecinta buku. Review, rekomendasi, dan diskusi literatur.',
      art: 'Karya seni, diskusi, dan event seni Indonesia.',
      photography: 'Tips fotografi, review gear, dan berbagi hasil foto.',
      finance: 'Diskusi investasi, keuangan personal, dan ekonomi.',
      health: 'Tips kesehatan, fitness, dan gaya hidup sehat.',
      education: 'Diskusi pendidikan, beasiswa, dan resources belajar.'
    }
    return descriptions[forumName.value as keyof typeof descriptions] || 'Komunitas diskusi'
  }),
  members: Math.floor(Math.random() * 200000) + 50000,
  online: Math.floor(Math.random() * 1000) + 100
})

const allPosts = ref(forumPosts[forumName.value as keyof typeof forumPosts] || [])

const filteredPosts = computed(() => {
  if (!searchQuery.value) return allPosts.value
  
  const query = searchQuery.value.toLowerCase()
  return allPosts.value.filter(post => 
    post.title.toLowerCase().includes(query) ||
    post.content.toLowerCase().includes(query)
  )
})

const loadMorePosts = async () => {
  if (loading.value || !hasMore.value) return
  
  loading.value = true
  
  try {
    await new Promise(resolve => setTimeout(resolve, 1000))
    
    const newPosts = generatePostsForSubforum(forumName.value, page.value)
    allPosts.value.push(...newPosts)
    page.value++
    
    if (page.value >= 5) {
      hasMore.value = false
    }
  } finally {
    loading.value = false
  }
}

const generatePostsForSubforum = (subforum: string, page: number) => {
  const posts = []
  const baseId = allPosts.value.length

  switch (subforum) {
    case 'programming':
      posts.push({
        id: baseId + 1,
        title: 'Pengalaman Belajar Rust untuk Backend Development',
        content: 'Sharing pengalaman 6 bulan menggunakan Rust untuk microservices.',
        author: 'rust_enthusiast',
        votes: Math.floor(Math.random() * 100),
        comments: Math.floor(Math.random() * 50),
        createdAt: new Date()
      })
      break
    case 'movies':
      posts.push({
        id: baseId + 1,
        title: 'Daftar Film Indonesia Terbaik 2024',
        content: 'Kompilasi film-film Indonesia yang wajib ditonton tahun ini.',
        author: 'film_critic',
        votes: Math.floor(Math.random() * 100),
        comments: Math.floor(Math.random() * 50),
        createdAt: new Date()
      })
      break
    // Add more cases for other subforums
    default:
      posts.push({
        id: baseId + 1,
        title: `Post Baru di f/${subforum}`,
        content: 'Lorem ipsum dolor sit amet...',
        author: 'user' + Math.floor(Math.random() * 1000),
        votes: Math.floor(Math.random() * 100),
        comments: Math.floor(Math.random() * 50),
        createdAt: new Date()
      })
  }

  return posts
}

const handleScroll = (e: Event) => {
  const target = e.target as HTMLElement
  const bottom = target.scrollHeight - target.scrollTop - target.clientHeight < 50
  
  if (bottom) {
    loadMorePosts()
  }
}

onMounted(() => {
  loadMorePosts()
})
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
    
    <div class="main-content">
      <div class="scrollable-content hide-scrollbar" @scroll="handleScroll">
        <div class="new-post">
          <router-link
            :to="{ name: 'create-post' }"
            class="new-post-input"
          >
            Buat post baru di f/{{ forumName }}...
          </router-link>
        </div>
        
        <div v-if="searchQuery" class="search-info">
          Menampilkan hasil pencarian untuk "{{ searchQuery }}"
        </div>
        
        <PostCard
          v-for="post in filteredPosts"
          :key="post.id"
          :post="post"
        />
        
        <div v-if="loading" class="loading-spinner">
          Loading more posts...
        </div>
      </div>
      
      <div class="sidebar-wrapper hide-scrollbar">
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

.search-info {
  background: white;
  padding: 12px 16px;
  border-radius: 8px;
  margin-bottom: 16px;
  font-size: 14px;
  color: var(--gray-medium);
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
</style>