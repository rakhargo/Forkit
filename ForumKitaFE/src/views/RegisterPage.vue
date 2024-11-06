<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '../stores/userStore';

const router = useRouter()
const usernameForm = ref('')
const emailForm = ref('')
const phoneForm = ref('')
const passwordForm = ref('')
const confirmPasswordForm = ref('')

const handleRegister = () => {
  // TODO: Implement register logic
  const userStore = useUserStore();
  userStore.postRegister({
    username: usernameForm.value,
    email: emailForm.value,
    phone: phoneForm.value,
    password: passwordForm.value,
  })
  router.push('/login')
}


</script>

<template>
  <div class="auth-container">
    <div class="auth-card">
      <h1 class="auth-title">Daftar di ForumKita</h1>
      
      <form @submit.prevent="handleRegister" class="auth-form">
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
          <label for="email">Email</label>
          <input
            id="email"
            v-model="emailForm"
            type="email"
            required
            class="form-input"
          />
        </div>

        <div class="form-group">
          <label for="phone">No. HP</label>
          <input
            id="phone"
            v-model="phoneForm"
            type="phone"
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
        
        <div class="form-group">
          <label for="confirm-password">Konfirmasi Password</label>
          <input
            id="confirm-password"
            v-model="confirmPasswordForm"
            type="password"
            required
            class="form-input"
          />
        </div>
        
        <button type="submit" class="btn btn-primary w-full">
          Daftar
        </button>
      </form>
      
      <p class="auth-footer">
        Sudah punya akun?
        <router-link to="/login" class="auth-link">
          Masuk
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