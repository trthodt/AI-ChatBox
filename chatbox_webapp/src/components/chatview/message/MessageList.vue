<template>
  <div
    class="flex-1 overflow-y-auto bg-gray-100 px-4 py-3"
  >
    <div class="flex flex-col gap-3">
      <MessageItem
        v-for="message in messages"
        :key="message.id"
        :message="message"
      />
    </div>
  </div>
</template>

<script setup>
import MessageItem from "./MessageItem.vue";

defineProps({
  messages: {
    type: Array,
    default: () => [],
  },
});
</script>