<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useUserStore } from '../stores/userStore';
import { useSubTopiqStore } from '../stores/subTopiqStore';
import { usePostStore } from '../stores/postStore';

const router = useRouter()
const title = ref('')
const content = ref('')
const selectedSubforum = ref('')

// const subforums = [
//   'indonesia',
//   'programming',
//   'gaming',
//   'technology',
//   'science'
// ]

const userStore = useUserStore();
const subTopiqStore = useSubTopiqStore();

const handleSubmit = () => {
  // TODO: Implement post creation logic
  // console.log('Create post:', {
  //   title: title.value,
  //   content: content.value,
  //   subforum: selectedSubforum.value
  // })
  userStore.user?.subTopiqs.forEach((subTopiq) => {
        subTopiqStore.fetchSubTopiqById(subTopiq.subTopiqId);
      });
    const postStore = usePostStore();
    postStore.createPost({
    title: title.value,
    description: content.value,
    creatorId: userStore.userId,
    subTopiqId: selectedSubforum.value,
  })
  router.push('/')
}
</script>

<template>
  <div class="create-post-container">
    <div class="create-post-card">
      <h1 class="create-post-title">Buat Post Baru</h1>
      
      <form @submit.prevent="handleSubmit" class="create-post-form">
        <div class="form-group">
          <label for="subforum">Pilih Subforum</label>
          <select
            id="subforum"
            v-model="selectedSubforum"
            required
            class="form-input"
          >
            <option value="" disabled>Pilih subforum</option>
            <option
              v-for="subtopiq in userStore.user?.subTopiqs"
              :key="subtopiq.subTopiqId"
              :value="subtopiq.subTopiqId"
            >
              f/{{ subTopiqStore.subtopiq?.name }}
            </option>
          </select>
        </div>
        
        <div class="form-group">
          <label for="title">Judul</label>
          <input
            id="title"
            v-model="title"
            type="text"
            required
            class="form-input"
            placeholder="Judul post Anda"
          />
        </div>
        
        <div class="form-group">
          <label for="content">Konten</label>
          <textarea
            id="content"
            v-model="content"
            required
            class="form-input content-input"
            placeholder="Tulis konten post Anda di sini..."
            rows="8"
          ></textarea>
        </div>
        
        <div class="form-actions">
          <button type="button" class="btn" @click="router.push('/')">
            Batal
          </button>
          <button type="submit" class="btn btn-primary">
            Post
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<style scoped>
.create-post-container {
  padding: 76px 20px 20px;
  max-width: 800px;
  margin: 0 auto;
}

.create-post-card {
  background: white;
  padding: 32px;
  border-radius: 8px;
  box-shadow: var(--shadow);
}

.create-post-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 24px;
}

.create-post-form {
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
  font-family: inherit;
}

.form-input:focus {
  outline: none;
  border-color: var(--primary-color);
}

.content-input {
  resize: vertical;
  min-height: 200px;
}

.form-actions {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
  margin-top: 16px;
}
</style>