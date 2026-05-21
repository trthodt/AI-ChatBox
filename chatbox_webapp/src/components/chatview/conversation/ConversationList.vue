<template>
    <div class="border-b border-gray-200 p-2 cursor-pointer hover:bg-gray-100">
        <div class="font-semibold">{{ title }}</div>
        <div>{{ lastMessage }}</div>
    </div>
</template>
<script setup>
defineProps({
  id: String,
  title: String,
  lastMessage: String
})
</script>