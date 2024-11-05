<script setup lang="ts">
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router'
import { formatDistanceToNow } from 'date-fns'
import { id } from 'date-fns/locale'
import { ArrowUpIcon, ArrowDownIcon, HeartIcon } from '@heroicons/vue/24/outline'
import { ArrowUpIcon as ArrowUpSolidIcon, ArrowDownIcon as ArrowDownSolidIcon, HeartIcon as HeartSolidIcon } from '@heroicons/vue/24/solid'

const route = useRoute()
const postId = computed(() => route.params.id)

const post = ref({
  id: postId,
  title: 'Tips Belajar Programming untuk Pemula',
  content: 'Mulai dengan dasar-dasar, pilih satu bahasa pemrograman dan konsisten belajar setiap hari. Jangan lupa untuk praktek dan membuat project sendiri.',
  author: 'programmer_sejati',
  votes: 156,
  userVote: null,
  createdAt: new Date('2024-03-10T08:00:00')
})

const newComment = ref('')
const replyingTo = ref<{ commentId: number; username: string } | null>(null)
const comments = ref([
  {
    id: 1,
    content: 'Mantap',
    author: 'shijones123',
    likes: 25,
    isLiked: false,
    createdAt: new Date('2024-03-10T09:30:00'),
    replies: [
      {
        id: 2,
        content: 'emang mantap',
        author: 'atminrakha21321313',
        likes: 12,
        isLiked: false,
        createdAt: new Date('2024-03-10T10:15:00'),
        replies: []
      }
    ]
  }
])

const handlePostVote = (type: 'up' | 'down') => {
  if (post.value.userVote === type) {
    post.value.userVote = null
    post.value.votes += type === 'up' ? -1 : 1
  } else {
    if (post.value.userVote) {
      post.value.votes += post.value.userVote === 'up' ? -2 : 2
    } else {
      post.value.votes += type === 'up' ? 1 : -1
    }
    post.value.userVote = type
  }
}

const toggleLike = (target: { likes: number; isLiked: boolean }) => {
  if (target.isLiked) {
    target.likes--
  } else {
    target.likes++
  }
  target.isLiked = !target.isLiked
}

const handleSubmitComment = () => {
  if (!newComment.value.trim()) return
  
  if (replyingTo.value) {
    const parentComment = comments.value.find(c => c.id === replyingTo.value?.commentId)
    if (parentComment) {
      parentComment.replies.unshift({
        id: Date.now(),
        content: newComment.value,
        author: 'myusername',
        likes: 0,
        isLiked: false,
        createdAt: new Date(),
        replies: []
      })
    }
  } else {
    comments.value.unshift({
      id: Date.now(),
      content: newComment.value,
      author: 'myusername',
      likes: 0,
      isLiked: false,
      createdAt: new Date(),
      replies: []
    })
  }
  
  newComment.value = ''
  replyingTo.value = null
}

const startReply = (commentId: number, username: string) => {
  replyingTo.value = { commentId, username }
  const commentInput = document.querySelector('.comment-input') as HTMLTextAreaElement
  if (commentInput) {
    commentInput.focus()
  }
}

const cancelReply = () => {
  replyingTo.value = null
  newComment.value = ''
}
</script>

<template>
  <div class="comments-container">
    <div class="post-preview">
      <div class="vote-buttons">
        <button 
          class="vote-button" 
          :class="{ 'voted': post.userVote === 'up' }"
          @click="handlePostVote('up')"
        >
          <ArrowUpSolidIcon v-if="post.userVote === 'up'" class="vote-icon" />
          <ArrowUpIcon v-else class="vote-icon" />
        </button>
        <span class="vote-count" :class="{
          'positive': post.votes > 0,
          'negative': post.votes < 0
        }">{{ post.votes }}</span>
        <button 
          class="vote-button" 
          :class="{ 'voted': post.userVote === 'down' }"
          @click="handlePostVote('down')"
        >
          <ArrowDownSolidIcon v-if="post.userVote === 'down'" class="vote-icon" />
          <ArrowDownIcon v-else class="vote-icon" />
        </button>
      </div>
      
      <div class="post-content">
        <div class="post-meta">
          Posted by {{ post.author }} {{ formatDistanceToNow(post.createdAt, { addSuffix: true, locale: id }) }}
        </div>
        <h1 class="post-title">{{ post.title }}</h1>
        <p class="post-text">{{ post.content }}</p>
      </div>
    </div>

    <div class="comments-section">
      <div class="comment-form">
        <div v-if="replyingTo" class="reply-indicator">
          <span>Membalas ke @{{ replyingTo.username }}</span>
          <button class="cancel-reply" @click="cancelReply">×</button>
        </div>
        <textarea
          v-model="newComment"
          :placeholder="replyingTo ? 'Tulis balasan Anda...' : 'Tulis komentar Anda...'"
          class="comment-input"
        ></textarea>
        <button 
          class="btn btn-primary"
          @click="handleSubmitComment"
          :disabled="!newComment.trim()"
        >
          {{ replyingTo ? 'Balas' : 'Kirim' }}
        </button>
      </div>

      <div class="comments-list">
        <div v-for="comment in comments" :key="comment.id" class="comment">
          <div class="comment-content">
            <div class="comment-meta">
              {{ comment.author }} • {{ formatDistanceToNow(comment.createdAt, { addSuffix: true, locale: id }) }}
            </div>
            <p class="comment-text">{{ comment.content }}</p>
            
            <div class="comment-actions">
              <button 
                class="like-button" 
                :class="{ 'liked': comment.isLiked }"
                @click="toggleLike(comment)"
              >
                <HeartSolidIcon v-if="comment.isLiked" class="heart-icon" />
                <HeartIcon v-else class="heart-icon" />
                <span>{{ comment.likes }}</span>
              </button>
              <button 
                class="action-link"
                @click="startReply(comment.id, comment.author)"
              >
                Reply
              </button>
              <button class="action-link">Share</button>
            </div>

            <div v-if="comment.replies?.length" class="replies">
              <div v-for="reply in comment.replies" :key="reply.id" class="comment reply">
                <div class="comment-content">
                  <div class="comment-meta">
                    {{ reply.author }} • {{ formatDistanceToNow(reply.createdAt, { addSuffix: true, locale: id }) }}
                  </div>
                  <p class="comment-text">{{ reply.content }}</p>
                  
                  <div class="comment-actions">
                    <button 
                      class="like-button" 
                      :class="{ 'liked': reply.isLiked }"
                      @click="toggleLike(reply)"
                    >
                      <HeartSolidIcon v-if="reply.isLiked" class="heart-icon" />
                      <HeartIcon v-else class="heart-icon" />
                      <span>{{ reply.likes }}</span>
                    </button>
                    <button class="action-link">Share</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.comments-container {
  padding: 76px 20px 20px;
  max-width: 800px;
  margin: 0 auto;
}

.post-preview {
  background: white;
  border-radius: 8px;
  box-shadow: var(--shadow);
  margin-bottom: 20px;
  display: flex;
}

.vote-buttons {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 8px;
  background: var(--gray-light);
  border-radius: 8px 0 0 8px;
}

.vote-button {
  background: none;
  border: none;
  padding: 4px;
  cursor: pointer;
  color: var(--gray-medium);
}

.vote-button:hover {
  color: var(--primary-color);
}

.vote-button.voted {
  color: var(--primary-color);
}

.vote-icon {
  width: 20px;
  height: 20px;
}

.vote-count {
  font-weight: 600;
  margin: 4px 0;
}

.vote-count.positive {
  color: var(--primary-color);
}

.vote-count.negative {
  color: var(--error-color);
}

.post-content {
  flex: 1;
  padding: 20px;
}

.post-meta {
  font-size: 12px;
  color: var(--gray-medium);
  margin-bottom: 8px;
}

.post-title {
  font-size: 24px;
  font-weight: 600;
  margin-bottom: 12px;
}

.post-text {
  color: var(--text-color);
  margin-bottom: 16px;
}

.comments-section {
  background: white;
  border-radius: 8px;
  box-shadow: var(--shadow);
  padding: 20px;
}

.comment-form {
  margin-bottom: 20px;
}

.reply-indicator {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: var(--gray-light);
  padding: 8px 12px;
  border-radius: 4px;
  margin-bottom: 8px;
}

.cancel-reply {
  background: none;
  border: none;
  font-size: 18px;
  color: var(--gray-medium);
  cursor: pointer;
}

.comment-input {
  width: 100%;
  min-height: 100px;
  padding: 12px;
  border: 1px solid #ccc;
  border-radius: 4px;
  margin-bottom: 12px;
  font-family: inherit;
  resize: vertical;
}

.comment-input:focus {
  outline: none;
  border-color: var(--primary-color);
}

.comments-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.comment {
  display: flex;
  gap: 12px;
}

.comment-content {
  flex: 1;
}

.comment-meta {
  font-size: 12px;
  color: var(--gray-medium);
  margin-bottom: 4px;
}

.comment-text {
  margin-bottom: 8px;
}

.comment-actions {
  display: flex;
  gap: 16px;
  align-items: center;
}

.like-button {
  display: flex;
  align-items: center;
  gap: 4px;
  background: none;
  border: none;
  color: var(--gray-medium);
  cursor: pointer;
  padding: 4px 8px;
  border-radius: 12px;
  transition: all 0.2s;
}

.like-button:hover {
  background-color: var(--gray-light);
}

.like-button.liked {
  color: #ff4757;
}

.heart-icon {
  width: 16px;
  height: 16px;
}

.action-link {
  background: none;
  border: none;
  color: var(--gray-medium);
  font-size: 12px;
  cursor: pointer;
  padding: 4px 0;
}

.action-link:hover {
  color: var(--primary-color);
}

.replies {
  margin-left: 20px;
  margin-top: 12px;
  padding-left: 20px;
  border-left: 2px solid var(--gray-light);
}

.reply {
  margin-top: 12px;
}
</style>