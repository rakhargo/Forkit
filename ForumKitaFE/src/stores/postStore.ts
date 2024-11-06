import { defineStore } from 'pinia';
import { ref } from 'vue';
import type { Posts, Replies } from '../models/posts';
import { postService } from '../services/api';

export const usePostStore = defineStore('posts', () => {
  const posts = ref<Posts[]>([]);
  const post = ref<Posts>();
  const replies = ref<Replies[]>([]);
  // const reply = ref<Replies>(); // const variable for single reply
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
        post.value = response.data;
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
        posts.value = response.data;
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
        posts.value = response.data;
      } catch (err) {
        error.value = 'Failed to fetch post';
    } finally {
        loading.value = false;
    }
  }

  // create post belum

  async function upVotePost(postId: string) {
    try {
      await postService.upVote(postId);
    } catch (err) {
      error.value = 'Failed to upvote';
    }
  }

  async function downVotePost(postId: string) {
    try {
      await postService.downVote(postId);
    } catch (err) {
      error.value = 'Failed to downvote';
    }
  }

  async function deletePost(postId: string) {
    try {
      await postService.deletePosts(postId);
    } catch (err) {
      error.value = 'Failed to delete post';
    }
  }

  // create reply belum

  async function fetchTopPosts(subTopiqId: string) {
    try {
      loading.value = true;
      const response = await postService.getTopPosts(subTopiqId);
      posts.value = response.data;
    } catch (err) {
      error.value = 'Failed to fetch top posts';
    } finally {
      loading.value = false;
    }
  }

  async function fetchRepliesByPostId(postId: string) {
    try {
      loading.value = true;
      const response = await postService.getRepliesByPostId(postId);
      replies.value = response.data;
    } catch (err) {
      error.value = 'Failed to fetch replies by (post_id)';
    } finally {
      loading.value = false;
    }
  }

  async function fetchRepliesByUserId(userId: string) {
    try {
      loading.value = true;
      const response = await postService.getRepliesByUserId(userId);
      replies.value = response.data;
    } catch (err) {
      error.value = 'Failed to fetch replies by (user_id)';
    } finally {
      loading.value = false;
    }
  }

  return {
    posts,
    post,
    replies,
    // reply,
    loading,
    error,
    fetchAllPosts,
    fetchPostById,
    fetchPostBySubTopiqId,
    fetchPostByCreatorId,
    upVotePost,
    downVotePost,
    deletePost,
    fetchTopPosts,
    fetchRepliesByPostId,
    fetchRepliesByUserId
  };
});