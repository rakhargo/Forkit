import { defineStore } from 'pinia';
import { ref } from 'vue';
import type { SubTopiqs } from '../models/subTopiq';
import { subTopiqService } from '../services/api';

export const useSubTopiqStore = defineStore('subtopiqs', () => {
    const subtopiqs = ref<SubTopiqs[]>([]);
    const subtopiq = ref<SubTopiqs>();
    const loading = ref(false);
    const error = ref<string | null>(null);

    // create subTopiqs belum
    
    async function fetchAllSubTopiqs() {
      try {
        loading.value = true;
        const response = await subTopiqService.getAllSubTopiqs();
        subtopiqs.value = response.data;
      } catch (err) {
        error.value = 'Failed to fetch sub topiqs';
      } finally {
        loading.value = false;
      }
    }
    
    async function fetchSubTopiqById(subTopiqId: string){
      try {
        loading.value = true;
        const response = await subTopiqService.getSubTopiqById(subTopiqId);
        subtopiq.value = response.data;
      } catch (err) {
        error.value = 'Failed to fetch sub topiq by id';
      } finally {
        loading.value = false;
      }
    }

    async function fetchSubTopiqByModeratorId(moderatorId: string){
      try {
        loading.value = true;
        const response = await subTopiqService.getSubTopiqByModeratorId(moderatorId);
        subtopiqs.value = response.data;
      } catch (err) {
        error.value = 'Failed to fetch sub topiq by moderator id';
      } finally {
        loading.value = false;
      }
    }

    async function fetchSubTopiqByCreatorId(creatorId: string){
      try {
        loading.value = true;
        const response = await subTopiqService.getSubTopiqByCreatorId(creatorId);
        subtopiqs.value = response.data;
      } catch (err) {
        error.value = 'Failed to fetch sub topiq by creator id';
      } finally {
        loading.value = false;
      }
    }

    async function addModerator(subTopiqId: string, userId: string) {
      try {
        loading.value = true;
        await subTopiqService.addModerator(subTopiqId, userId);
      } catch (err) {
        error.value = 'Failed to add moderator';
      } finally {
        loading.value = false;
      }
    }

    async function subscribeSubTopiq(subTopiqId: string, userId: string){
      try {
        await subTopiqService.subscribeSubTopiq(subTopiqId, userId);
      } catch (err) {
        error.value = 'Failed to subscribe to sub topiq';
      }
    }

    async function unsubscribeSubTopiq(subTopiqId: string, userId: string){
      try {
        await subTopiqService.unsubscribeSubTopiq(subTopiqId, userId);
      } catch (err) {
        error.value = 'Failed to unsubscribe to sub topiq';
      }
    }

    async function deleteSubTopiq(subTopiqId: string) {
      try {
        await subTopiqService.deleteSubTopiq(subTopiqId);
      } catch (err) {
        error.value = 'Failed to delete sub topiq';
      }
    }

    return {
      subtopiqs,
      subtopiq,
      loading,
      error,
      fetchAllSubTopiqs,
      fetchSubTopiqById,
      fetchSubTopiqByModeratorId,
      fetchSubTopiqByCreatorId,
      addModerator,
      subscribeSubTopiq,
      unsubscribeSubTopiq,
      deleteSubTopiq
    };
  });