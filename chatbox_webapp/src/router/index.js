import ChatView from '@/components/ChatView.vue'
import HomeView from '@/components/HomeView.vue'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', component: HomeView },
    { path: '/chat', component: ChatView },
  ],
})

export default router
