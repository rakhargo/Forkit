<script setup lang="ts">
import { MagnifyingGlassIcon, UserCircleIcon } from '@heroicons/vue/24/outline'
import { useRouter } from 'vue-router'
import IconForumKita  from './icons/IconForumKita.vue'

const router = useRouter()
</script>

<template>
  <header class="header">
    <div class="container header-content">
      <IconForumKita> </IconForumKita>
      
      <div class="search-container">
        <MagnifyingGlassIcon class="search-icon" />
        <input type="text" placeholder="Cari di ForumKita" class="search-input" />
      </div>

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
}

.header-content {
  height: 56px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
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