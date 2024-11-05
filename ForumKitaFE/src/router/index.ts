import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/HomePage.vue'
import Login from '../views/LoginPage.vue'
import Register from '../views/RegisterPage.vue'
import CreatePost from '../views/CreatePost.vue'
import Subforum from '../views/SubTopiqPage.vue'
import Profile from '../views/ProfilePage.vue'
import PostComments from '../views/PostComments.vue'
import EditProfile from '../views/EditProfile.vue'
import Search from '../views/Search.vue'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    },
    {
      path: '/create-post',
      name: 'create-post',
      component: CreatePost
    },
    {
      path: '/f/:name',
      name: 'subforum',
      component: Subforum
    },
    {
      path: '/u/:username',
      name: 'profile',
      component: Profile
    },
    {
      path: '/post/:id/comments',
      name: 'post-comments',
      component: PostComments
    },
    {
      path: '/settings/profile',
      name: 'edit-profile',
      component: EditProfile
    },
    {
      path: '/search',
      name: 'search',
      component: Search
    }
  ]
})

export default router