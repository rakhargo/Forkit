import { defineStore } from 'pinia';
import { ref } from 'vue';
import type { SubTopiqs } from '../models/subTopiq';
import { subTopiqService } from '../services/api';

export const usePostStore = defineStore('posts', () => {
    const posts = ref<SubTopiqs[]>([]);
    const loading = ref(false);
    const error = ref<string | null>(null);
  
    
    return {
      posts,
      loading,
      error,
      
    };
  });