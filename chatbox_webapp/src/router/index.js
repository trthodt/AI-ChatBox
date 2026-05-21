import ChatView from '@/pages/ChatView.vue'
import HomeView from '@/pages/HomeView.vue'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', component: HomeView },
    { path: '/chat', component: ChatView },
  ],
})

export default router
