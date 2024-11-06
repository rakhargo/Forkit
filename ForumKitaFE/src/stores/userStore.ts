import { defineStore } from 'pinia';
import { ref } from 'vue';
import type { Users } from '../models/users';
import { userService } from '../services/api';

export const useUserStore = defineStore('users', () => {
    const users = ref<Users[]>([]);
    const user = ref<Users>();
    const loading = ref(false);
    const error = ref<string | null>(null);

    async function postRegister() {
        try {
            loading.value = true;
            await userService.postRegister();
        } catch (err) {
            error.value = 'Failed to register';
        } finally {
            loading.value = false;
        }
    }

    async function postToken() {
        try {
            loading.value = true;
            await userService.postToken();
        } catch (err) {
            error.value = 'Token error / failed';
        } finally {
            loading.value = false;
        }
    }
    
    async function postLogin() {
        try {
            loading.value = true;
            await userService.postLogin();
        } catch (err) {
            error.value = 'Login failed';
        } finally {
            loading.value = false;
        }
    }
    
    async function postLogout() {
        try {
            loading.value = true;
            await userService.postLogout();
        } catch (err) {
            error.value = 'Logout failed';
        } finally {
            loading.value = false;
        }
    }

    async function fetchAllUsers() {
        try {
            loading.value = true;
            const response = await userService.getAllUsers();
            users.value = response.data;
        } catch (err) {
            error.value = 'Failed to fetch all users';
        } finally {
            loading.value = false;
        }
    }

    async function fetchUserById(userId: string) {
        try {
            loading.value = true;
            const response = await userService.getUserById(userId);
            users.value = response.data;
        } catch (err) {
            error.value = 'Failed to fetch user with id: ' + userId;
        } finally {
            loading.value = false;
        }
    }

    async function deleteUser(userId: string) {
        try {
            await userService.deleteUser(userId);
        } catch (err) {
            error.value = 'Failed to delete user with id' + userId;
        }
    }

    return {
        users,
        user,
        loading,
        error,
        postRegister,
        postToken,
        postLogin,
        postLogout,
        fetchAllUsers,
        fetchUserById,
        deleteUser
    };
});