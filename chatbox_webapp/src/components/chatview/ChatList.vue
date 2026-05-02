<template>
    <div class="flex flex-col">
        <ChatItem v-for="chat in chatList" :key="chat.id" :id="chat.id" :title="chat.title" :lastMessage="chat.lastMessage" 
         />
    </div>
</template>
<script setup>
import ChatItem from './chatcomp/ChatItem.vue';
import { ref } from 'vue';
const chatList = ref([
    {
        id: '1',
        title: 'Chat 1',
        lastMessage: 'Last message 1'
    },
    {
        id: '2',
        title: 'Chat 2',
        lastMessage: 'Last message 2'
    }
]);
</script>