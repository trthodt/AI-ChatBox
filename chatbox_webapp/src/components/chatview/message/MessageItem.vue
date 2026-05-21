<template>
  <div
    class="flex"
    :class="message.isMine ? 'justify-end' : 'justify-start'"
  >
    <div
      class="max-w-[70%] rounded-2xl px-4 py-2"
      :class="
        message.isMine
          ? 'bg-blue-500 text-white'
          : 'bg-white text-black'
      "
    >
      {{ message.text }}
    </div>
  </div>
</template>

<script setup>
defineProps({
  message: Object,
});
</script>