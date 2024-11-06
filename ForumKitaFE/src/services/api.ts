import axios from 'axios';
import type { Posts, Replies } from '../models/posts';
import type { SubTopiqs } from '../models/subTopiq';
import type { Users } from '../models/users';

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000',
  headers: {
    'Content-Type': 'application/json',
  },
});

export const postService = {
  getAllPosts: () => api.get<Posts[]>('/posts/posts'),
  getPostById: (id: string) => api.get<Posts>('/posts/' + id),
  getPostBySubTopiqId: (id: string) => api.get<Posts[]>('/posts/subtopiq/' + id),
  getPostByCreatorId: (id: string) => api.get<Posts[]>('/posts/creator/' + id),
  createPost: (post: Partial<Posts>) => api.post<Posts>('/posts/', post),
  upVote: (postId: string) => api.post('/posts/' + postId + '/upvote'),
  downVote: (postId: string) => api.post('/posts/' + postId + '/downvote'),
  deletePosts: (postId: string) => api.delete('/posts/' + postId),
  createReply: (postId: string) => api.post<Replies>('/posts/reply/' + postId),
  getTopPosts: (subTopiqId: string) => api.get('/posts/top-posts/' + subTopiqId),
  getRepliesByPostId: (postId: string) => api.get<Replies[]>('/posts/replies/post/' + postId),
  getRepliesByUserId: (userId: string) => api.get<Replies[]>('/posts/replies/user/' + userId),
};

export const commentService = {
  getComments: (commentId: string) => api.get<Replies[]>('/posts/' + commentId + '/comments'),
  createComment: (commentId: string, comment: Partial<Replies>) => api.post<Replies>('/posts/' + commentId + '/comments/', comment),
};

export const subTopiqService = {
    createSubTopiq: (subtopiq: Partial<SubTopiqs>) => api.post<SubTopiqs>('/subtopiq/' + subtopiq),
    getAllSubTopiqs: () => api.get<SubTopiqs[]>('/subtopiq/all'),
    getSubTopiqById: (subTopiqId: string) => api.get<SubTopiqs>('/subtopiq/id/' + subTopiqId),
    getSubTopiqByModeratorId: (moderatorId: string) => api.get<SubTopiqs[]>('/subtopiq/moderated/' + moderatorId),
    getSubTopiqByCreatorId: (creatorId: string) => api.get<SubTopiqs[]>('/subtopiq/created/' + creatorId),
    addModerator: (subTopiqId: string, userId: string) => api.post('/subtopiq/addmod/' + subTopiqId + userId),
    subscribeSubTopiq: (subTopiqId: string, userId: string) => api.post('/subtopiq/subscribe/' + userId + "/" + subTopiqId),
    unsubscribeSubTopiq: (subTopiqId: string, userId: string) => api.post('/subtopiq/unsubscribe/' + userId + "/" + subTopiqId),
    deleteSubTopiq: (subTopiqId: string) => api.post('/subtopiq/delete/' + subTopiqId)
};

export const userService = {
    postRegister: () => api.post('/user/register'),
    postToken: () => api.post('/user/token'),
    postLogin: () => api.post('/user/login'),
    getAllUsers: () => api.get<Users[]>('/user/all'), 
    getUserById: (userId: string) => api.get('/user/id/' + userId), 
    postLogout: () => api.post('/user/logout'),
    deleteUser: (userId: string) => api.delete('/user/delete/' + userId)
};