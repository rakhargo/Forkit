import { defineStore } from 'pinia';
import { ref } from 'vue';
import type { Posts } from '../models/posts';
import { postService } from '../services/api';

export const usePostStore = defineStore('posts', () => {
  const posts = ref<Posts[]>([]);
  const loading = ref(false);
  const error = ref<string | null>(null);

  async function fetchAllPosts() {
    try {
      loading.value = true;
      const response = await postService.getAllPosts();
      posts.value = response.data;
    } catch (err) {
      error.value = 'Failed to fetch posts';
    } finally {
      loading.value = false;
    }
  }

  async function fetchPostById(postId: string) {
    try {
        loading.value = true;
        const response = await postService.getPostById(postId);
    } catch (err) {
        error.value = 'Failed to fetch post';
    } finally {
        loading.value = false;
    }
  } 

  async function fetchPostBySubTopiqId(subTopiqId: string) {
    try {
        loading.value = true;
        const response = await postService.getPostBySubTopiqId(subTopiqId);
    } catch (err) {
        error.value = 'Failed to fetch post';
    } finally {
        loading.value = false;
    }
  }

  async function fetchPostByCreatorId(CreatorId: string) {
    try {
        loading.value = true;
        const response = await postService.getPostByCreatorId(CreatorId);
    } catch (err) {
        error.value = 'Failed to fetch post';
    } finally {
        loading.value = false;
    }
  }

//   async function votePost(postId: string, direction: 'up' | 'down') {
//     try {
//       await postService.vote(postId, direction);
//       await fetchPosts(); // Refresh posts after voting
//     } catch (err) {
//       error.value = 'Failed to vote';
//     }
//   }

  return {
    posts,
    loading,
    error,
    fetchAllPosts,
    fetchPostById,
    fetchPostBySubTopiqId,
    fetchPostByCreatorId,
    // votePost,
  };
});