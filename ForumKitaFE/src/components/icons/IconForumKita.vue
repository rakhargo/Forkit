<script setup lang="ts">
import { useRouter } from 'vue-router'

const router = useRouter()

</script>

<template>
    <h1 class="logo" @click="router.push('/')">
        <span class="logo-forum">Forum</span>
        <span class="logo-kita">Kita</span>
      </h1>
  </template>  

<style scoped>
.logo {
  font-size: 24px;
  font-weight: bold;
  cursor: pointer;
}

.logo-forum {
  color: var(--primary-color);
}
</style>