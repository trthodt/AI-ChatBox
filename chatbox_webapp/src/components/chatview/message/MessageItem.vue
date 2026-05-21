<template>
  <div
    class="flex"
    :class="message.isMine ? 'justify-end' : 'justify-start'"
  >
    <div
      class="max-w-[70%] rounded-2xl px-4 py-2 markdown-content"
      :class="
        message.isMine
          ? 'bg-blue-500 text-white'
          : 'bg-white text-black'
      "
      v-html="formattedContent"
    >
    </div>
  </div>
</template>

<script setup>
import { marked } from 'marked';
import { computed } from 'vue';

const props = defineProps({
  message: Object,
})

const formattedContent = computed(() => {
  return marked(props.message?.text || '')
})
</script>