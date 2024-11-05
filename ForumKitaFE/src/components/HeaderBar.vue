<script setup lang="ts">
import { ref } from 'vue'
import { MagnifyingGlassIcon, UserCircleIcon, PlusIcon } from '@heroicons/vue/24/outline'
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()
const searchQuery = ref('')

const handleSearch = () => {
  if (!searchQuery.value.trim()) return
  
  if (route.name === 'subforum') {
    // Search within subforum
    router.push({
      name: 'subforum',
      params: { name: route.params.name },
      query: { q: searchQuery.value }
    })
  } else {
    // Global search
    router.push({
      name: 'search',
      query: { q: searchQuery.value }
    })
  }
}
</script>

<template>
  <header class="header">
    <div class="container header-content">
      <h1 class="logo" @click="router.push('/')">
        <span class="logo-forum">Forum</span>
        <span class="logo-kita">Kita</span>
      </h1>
      
      <form class="search-container" @submit.prevent="handleSearch">
        <MagnifyingGlassIcon class="search-icon" />
        <input 
          v-model="searchQuery"
          type="text" 
          :placeholder="route.name === 'subforum' ? 'Cari di subforum ini...' : 'Cari subforum...'" 
          class="search-input" 
        />
      </form>

      <div class="header-actions">
        <button 
          class="btn btn-primary new-post-btn"
          @click="router.push('/create-post')"
        >
          <PlusIcon class="btn-icon" />
          <span>Post Baru</span>
        </button>
        
        <div class="auth-buttons">
          <router-link to="/login" class="btn btn-primary">
            Masuk
          </router-link>
          <UserCircleIcon
            class="user-icon"
            @click="router.push('/u/myusername')"
          />
        </div>
      </div>
    </div>
  </header>
</template>

<style scoped>
.header {
  background: white;
  box-shadow: var(--shadow);
  position: fixed;
  width: 100%;
  top: 0;
  z-index: 1000;
  height: var(--header-height);
}

.header-content {
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
}

.logo {
  font-size: 24px;
  font-weight: bold;
  cursor: pointer;
  white-space: nowrap;
}

.logo-forum {
  color: var(--primary-color);
}

.search-container {
  position: relative;
  flex: 1;
  max-width: 600px;
  margin: 0 20px;
}

.search-input {
  width: 100%;
  padding: 8px 16px 8px 40px;
  border-radius: 20px;
  border: 1px solid #ccc;
  background-color: var(--gray-light);
}

.search-input:focus {
  outline: none;
  border-color: var(--primary-color);
}

.search-icon {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  width: 20px;
  height: 20px;
  color: var(--gray-medium);
}

.header-actions {
  display: flex;
  align-items: center;
  gap: 16px;
}

.new-post-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 16px;
}

.btn-icon {
  width: 20px;
  height: 20px;
}

.auth-buttons {
  display: flex;
  align-items: center;
  gap: 16px;
}

.user-icon {
  width: 32px;
  height: 32px;
  color: var(--gray-medium);
  cursor: pointer;
}
</style>