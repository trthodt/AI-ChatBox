<template>
    <section class="flex h-full flex-col bg-white">

    <MessageList class="flex-1 overflow-y-auto" />

    <MessageInput />
  </section>
</template>
<script setup>
import MessageInput from './chat-input/MessageInput.vue';
import MessageList from './message/MessageList.vue';

</script>