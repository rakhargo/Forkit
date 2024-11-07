import { defineStore } from 'pinia';
import { ref } from 'vue';
import type { Users } from '../models/users';
import { userService } from '../services/api';

export const useUserStore = defineStore('users', () => {
    const users = ref<Users[]>([]);
    const user = ref<Users | null>(null);
    const userId = ref<string | null>(null);
    const token = ref<string | null>(null);
    const loading = ref(false);
    const userValid = ref(false);
    const error = ref<string | null>(null);

    async function postRegister(user: Partial<Users>) {
        try {
            loading.value = true;
            await userService.postRegister(user);
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
    
    async function postLogin(username: string, password: string) {
        try {
            loading.value = true;
            const usernamePassword = {username: username, password: password}
            // await userService.postLogin(usernamePassword);
            const response = await userService.postLogin(usernamePassword);
            await fetchUserById(response.data.user_id)
            userValid.value = true
            // console.log(user.value?.username)
            // user.value = response.data.user_id; // Set logged-in user
            userId.value = response.data.user_id; // Set logged-in user
            token.value = response.data.access_token; // Store token if available

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
            userValid.value = false;
            user.value = null; // Clear user data on logout
            token.value = null; // Clear token on logout
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
            console.log(response.data)
            user.value = response.data;
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
        userId,
        token,
        loading,
        userValid,
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