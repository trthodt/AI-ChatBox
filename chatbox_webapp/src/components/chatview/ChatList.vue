<template>
    <div class="flex flex-col h-full overflow-y-auto ">
        <ChatItem v-for="chat in chatList" :key="chat.id" :id="chat.id" :title="chat.title" :lastMessage="chat.lastMessage" 
         />
    </div>
</template>
<script setup>
import ChatItem from './conversation/ConversationList.vue';
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
    },
    {
        id: '3',
        title: 'Chat 3',
        lastMessage: 'Last message 3'
    },
    {
        id: '4',
        title: 'Chat 4',
        lastMessage: 'Last message 4'
    },
    {
        id: '1',
        title: 'Chat 1',
        lastMessage: 'Last message 1'
    },
    {
        id: '2',
        title: 'Chat 2',
        lastMessage: 'Last message 2'
    },
    {
        id: '3',
        title: 'Chat 3',
        lastMessage: 'Last message 3'
    },
    {
        id: '4',
        title: 'Chat 4',
        lastMessage: 'Last message 4'
    },
    {
        id: '1',
        title: 'Chat 1',
        lastMessage: 'Last message 1'
    },
    {
        id: '2',
        title: 'Chat 2',
        lastMessage: 'Last message 2'
    },
    {
        id: '3',
        title: 'Chat 3',
        lastMessage: 'Last message 3'
    },
    {
        id: '4',
        title: 'Chat 4',
        lastMessage: 'Last message 4'
    }

]);
</script>