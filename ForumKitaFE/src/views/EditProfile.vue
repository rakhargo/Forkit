<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const profile = ref({
  username: 'myusername',
  email: 'user@example.com',
  bio: 'Ini adalah bio profil saya.',
  avatar: null as string | null
})

const handleUpdateProfile = () => {
  // TODO: Implement profile update logic
  console.log('Update profile:', profile.value)
  router.push('/u/myusername')
}

const handleAvatarChange = (event: Event) => {
  const input = event.target as HTMLInputElement
  if (input.files && input.files[0]) {
    const reader = new FileReader()
    reader.onload = (e) => {
      profile.value.avatar = e.target?.result as string
    }
    reader.readAsDataURL(input.files[0])
  }
}
</script>

<template>
  <div class="edit-profile-container">
    <div class="edit-profile-card">
      <h1 class="edit-profile-title">Edit Profil</h1>
      
      <form @submit.prevent="handleUpdateProfile" class="edit-profile-form">
        <div class="avatar-section">
          <div class="avatar-preview" :class="{ 'has-avatar': profile.avatar }">
            <img v-if="profile.avatar" :src="profile.avatar" alt="Avatar" class="avatar-image">
            <span v-else class="avatar-placeholder">{{ profile.username[0].toUpperCase() }}</span>
          </div>
          
          <div class="avatar-upload">
            <label for="avatar" class="btn">Ubah Avatar</label>
            <input
              type="file"
              id="avatar"
              accept="image/*"
              class="hidden"
              @change="handleAvatarChange"
            >
          </div>
        </div>

        <div class="form-group">
          <label for="username">Username</label>
          <input
            id="username"
            v-model="profile.username"
            type="text"
            required
            class="form-input"
          />
        </div>
        
        <div class="form-group">
          <label for="email">Email</label>
          <input
            id="email"
            v-model="profile.email"
            type="email"
            required
            class="form-input"
          />
        </div>
        
        <div class="form-group">
          <label for="bio">Bio</label>
          <textarea
            id="bio"
            v-model="profile.bio"
            class="form-input bio-input"
            rows="4"
          ></textarea>
        </div>
        
        <div class="form-actions">
          <button type="button" class="btn" @click="router.push('/u/myusername')">
            Batal
          </button>
          <button type="submit" class="btn btn-primary">
            Simpan
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<style scoped>
.edit-profile-container {
  padding: 76px 20px 20px;
  max-width: 600px;
  margin: 0 auto;
}

.edit-profile-card {
  background: white;
  padding: 32px;
  border-radius: 8px;
  box-shadow: var(--shadow);
}

.edit-profile-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 24px;
}

.edit-profile-form {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.avatar-section {
  display: flex;
  align-items: center;
  gap: 24px;
  margin-bottom: 16px;
}

.avatar-preview {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  background-color: var(--gray-light);
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.avatar-preview.has-avatar {
  background-color: transparent;
}

.avatar-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.avatar-placeholder {
  font-size: 36px;
  font-weight: bold;
  color: var(--gray-medium);
}

.hidden {
  display: none;
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
  font-family: inherit;
}

.form-input:focus {
  outline: none;
  border-color: var(--primary-color);
}

.bio-input {
  resize: vertical;
}

.form-actions {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
  margin-top: 16px;
}
</style>