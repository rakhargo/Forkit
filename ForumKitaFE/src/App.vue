<script setup lang="ts">
import Header from './components/HeaderBar.vue'
</script>

<template>
  <div class="app">
    <Header />
    <router-view />
  </div>
</template>

<style>
.app {
  min-height: 100vh;
}
</style>