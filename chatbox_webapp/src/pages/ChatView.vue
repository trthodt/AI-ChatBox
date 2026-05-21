<template>
    <div class="flex h-full">
        <ChatList  class="w-1/5"/>
        <ChatScreen class="w-4/5 h-full bg-gray-50"/>
    </div>
</template>
<script setup>
import ChatList from '@/components/chatview/ChatList.vue';
import ChatScreen from '@/components/chatview/ChatScreen.vue';

</script>