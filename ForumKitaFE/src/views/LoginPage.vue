<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '../stores/userStore';

const router = useRouter()
const usernameForm = ref('')
const passwordForm = ref('')

const handleLogin = async () => {
  // TODO: Implement login logic
  // console.log('Login:', { username: username.value, password: password.value })
  // const userStore = useUserStore();
  // const login = userStore.postLogin(usernameForm.value, passwordForm.value)
  // console.log(login)
  // router.push('/')
  const userStore = useUserStore();
  await userStore.postLogin(usernameForm.value, passwordForm.value);
  
  if (userStore.user) {
    router.push('/');
  }
}
</script>

<template>
  <div class="auth-container">
    <div class="auth-card">
      <h1 class="auth-title">Masuk ke ForumKita</h1>
      
      <form @submit.prevent="handleLogin" class="auth-form">
        <div class="form-group">
          <label for="username">Username</label>
          <input
            id="username"
            v-model="usernameForm"
            type="text"
            required
            class="form-input"
          />
        </div>
        
        <div class="form-group">
          <label for="password">Password</label>
          <input
            id="password"
            v-model="passwordForm"
            type="password"
            required
            class="form-input"
          />
        </div>
        
        <button type="submit" class="btn btn-primary w-full">
          Masuk
        </button>
      </form>
      
      <p class="auth-footer">
        Belum punya akun?
        <router-link to="/register" class="auth-link">
          Daftar
        </router-link>
      </p>
    </div>
  </div>
</template>

<style scoped>
.auth-container {
  min-height: calc(100vh - 56px);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 76px 20px 20px;
}

.auth-card {
  background: white;
  padding: 32px;
  border-radius: 8px;
  box-shadow: var(--shadow);
  width: 100%;
  max-width: 400px;
}

.auth-title {
  font-size: 24px;
  font-weight: bold;
  text-align: center;
  margin-bottom: 24px;
}

.auth-form {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.form-input {
  padding: 8px 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.form-input:focus {
  outline: none;
  border-color: var(--primary-color);
}

.w-full {
  width: 100%;
}

.auth-footer {
  margin-top: 16px;
  text-align: center;
  font-size: 14px;
}

.auth-link {
  color: var(--primary-color);
  text-decoration: none;
}

.auth-link:hover {
  text-decoration: underline;
}
</style>