<script setup lang="ts">
import { ArrowUpIcon, ArrowDownIcon, ChatBubbleLeftIcon, ShareIcon } from '@heroicons/vue/24/outline'
import { formatDistanceToNow } from 'date-fns'
import { id } from 'date-fns/locale'

defineProps<{
  post: {
    id: number
    title: string
    content: string
    author: string
    votes: number
    comments: number
    createdAt: Date
    image?: string
  }
}>()
</script>

<template>
  <article class="post-card">
    <div class="votes">
      <ArrowUpIcon class="vote-arrow up" />
      <span class="vote-count">{{ post.votes }}</span>
      <ArrowDownIcon class="vote-arrow down" />
    </div>

    <div class="post-content">
      <div class="post-meta">
        Posted by {{ post.author }} {{ formatDistanceToNow(post.createdAt, { addSuffix: true, locale: id }) }}
      </div>
      
      <h2 class="post-title">{{ post.title }}</h2>
      <p class="post-text">{{ post.content }}</p>
      
      <img v-if="post.image" :src="post.image" :alt="post.title" class="post-image">

      <div class="post-actions">
        <button class="action-button">
          <ChatBubbleLeftIcon class="action-icon" />
          <span>{{ post.comments }} Komentar</span>
        </button>
        <button class="action-button">
          <ShareIcon class="action-icon" />
          <span>Bagikan</span>
        </button>
      </div>
    </div>
  </article>
</template>

<style scoped>
.post-card {
  background: white;
  border-radius: 8px;
  box-shadow: var(--shadow);
  margin-bottom: 16px;
  display: flex;
  transition: box-shadow 0.2s;
}

.post-card:hover {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.votes {
  width: 40px;
  background: var(--gray-light);
  padding: 8px;
  display: flex;
  flex-direction: column;
  align-items: center;
  border-radius: 8px 0 0 8px;
}

.vote-arrow {
  width: 24px;
  height: 24px;
  color: var(--gray-medium);
  cursor: pointer;
}

.vote-arrow.up:hover {
  color: var(--primary-color);
}

.vote-arrow.down:hover {
  color: #7193ff;
}

.vote-count {
  font-size: 14px;
  font-weight: 500;
  margin: 4px 0;
}

.post-content {
  flex: 1;
  padding: 12px;
}

.post-meta {
  font-size: 12px;
  color: var(--gray-medium);
  margin-bottom: 4px;
}

.post-title {
  font-size: 18px;
  font-weight: 500;
  margin-bottom: 8px;
}

.post-text {
  color: var(--text-color);
  margin-bottom: 12px;
}

.post-image {
  max-height: 400px;
  width: 100%;
  object-fit: cover;
  border-radius: 8px;
  margin-bottom: 12px;
}

.post-actions {
  display: flex;
  gap: 16px;
}

.action-button {
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 8px;
  border: none;
  background: none;
  color: var(--gray-medium);
  cursor: pointer;
  border-radius: 4px;
}

.action-button:hover {
  background-color: var(--gray-light);
}

.action-icon {
  width: 20px;
  height: 20px;
}
</style>