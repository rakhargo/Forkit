<script setup lang="ts">
import { computed } from 'vue'
import { useRouter } from 'vue-router'
import { formatDistanceToNow } from 'date-fns'
import { id } from 'date-fns/locale'
import { ArrowUpIcon, ArrowDownIcon } from '@heroicons/vue/24/outline'
import { ArrowUpIcon as ArrowUpSolidIcon, ArrowDownIcon as ArrowDownSolidIcon } from '@heroicons/vue/24/solid'

const router = useRouter()
const props = defineProps<{
  post: {
    id: string;
    title: string;
    description: string;
    upVote: number;
    downVote: number;
    // replies: Replies[];
    creatorId: string;
    subTopiqId: string;
  }
}>()

// const handleVote = (type: 'up' | 'down') => {
//   if (props.post.userVote === type) {
//     props.post.userVote = null
//     props.post.votes += type === 'up' ? -1 : 1
//   } else {
//     if (props.post.userVote) {
//       props.post.votes += props.post.userVote === 'up' ? -2 : 2
//     } else {
//       props.post.votes += type === 'up' ? 1 : -1
//     }
//     props.post.userVote = type
//   }
// }

const navigateToPost = () => {
  router.push(`/post/${props.post.id}/comments`)
}
</script>

<template>
  <div class="post-card">
    <!-- <div class="vote-buttons"> -->
      <!-- <button 
        class="vote-button" 
        :class="{ 'voted': post.userVote === 'up' }"
        @click.stop="handleVote('up')"
      >
        <ArrowUpSolidIcon v-if="post.userVote === 'up'" class="vote-icon" />
        <ArrowUpIcon v-else class="vote-icon" />
      </button> -->
      <!-- <span class="vote-count" :class="{
        'positive': post.votes > 0,
        'negative': post.votes < 0
      }">{{ post.votes }}</span> -->
      <!-- <button 
        class="vote-button" 
        :class="{ 'voted': post.userVote === 'down' }"
        @click.stop="handleVote('down')"
      >
        <ArrowDownSolidIcon v-if="post.userVote === 'down'" class="vote-icon" />
        <ArrowDownIcon v-else class="vote-icon" />
      </button> -->
    <!-- </div> -->
    
    <div class="post-content" @click="navigateToPost">
      <div class="post-meta">
        {{ post.subTopiqId ? `f/${post.subTopiqId} • ` : '' }}
        Posted by {{ post.creatorId }}
      </div>
      
      <h2 class="post-title">{{ post.title }}</h2>
      
      <p class="post-text">{{ post.description }}</p>
      
      <div class="post-actions">
        <button class="action-button">
          <!-- {{ post.comments }}  -->
          Comments
        </button>
        <button class="action-button">Share</button>
      </div>
    </div>
  </div>
</template>

<style scoped>
.post-card {
  background: white;
  border-radius: 8px;
  box-shadow: var(--shadow);
  margin-bottom: 16px;
  display: flex;
  cursor: pointer;
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
  padding: 16px;
}

.post-meta {
  font-size: 12px;
  color: var(--gray-medium);
  margin-bottom: 8px;
}

.post-title {
  font-size: 18px;
  font-weight: 600;
  margin-bottom: 8px;
}

.post-text {
  color: var(--text-color);
  margin-bottom: 12px;
}

.post-image {
  width: 100%;
  max-height: 400px;
  object-fit: cover;
  border-radius: 4px;
  margin-bottom: 12px;
}

.post-actions {
  display: flex;
  gap: 16px;
}

.action-button {
  background: none;
  border: none;
  color: var(--gray-medium);
  font-size: 12px;
  cursor: pointer;
  padding: 4px 0;
}

.action-button:hover {
  color: var(--primary-color);
}
</style>