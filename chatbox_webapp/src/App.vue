<script setup>
import { RouterLink, RouterView } from 'vue-router'
import Navbar from './components/nav/Navbar.vue'
</script>

<template>
  <div>
    <Navbar />
    <main class="h-screen-minus-navbar">
      <RouterView />
    </main>
  </div>
</template>

<style scoped></style>
