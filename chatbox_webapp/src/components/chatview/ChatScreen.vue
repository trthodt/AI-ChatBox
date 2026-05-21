<template>
    <section class="flex h-full flex-col bg-white">

    <MessageList class="flex-1 overflow-y-auto"
                    :messages="messages" />

    <MessageInput :sendMessage="sendMessage" />
  </section>
</template>
<script setup>
import { ref } from 'vue';
import MessageInput from './chat-input/MessageInput.vue';
import MessageList from './message/MessageList.vue';
import { chatServices } from '@/services/chat.service';

const sendMessage = async (text) => {
  messages.value.push({
    id: Date.now(),
    text: text,
    isMine: true,
    createdAt: new Date().toLocaleTimeString(),
  });
  await handleSend(text);
};

const handleSend = async (text) => {
    try {
        const response = await chatServices.sendMessage(text)
        messages.value.push({
            id: Date.now(),
            text: response,
            isMine: false,
            createdAt: new Date().toLocaleTimeString(),
        });
        console.log(response)
    } catch (error) {
        console.log('Send message failed: ', error)
    }
}

const messages = ref([
  {
    id: 1,
    text: "Hey bro 👋",
    isMine: false,
    createdAt: "10:00 AM",
  },
  {
    id: 2,
    text: "Hi, what's up?",
    isMine: true,
    createdAt: "10:01 AM",
  },
  {
    id: 3,
    text: "Are you free tonight?",
    isMine: false,
    createdAt: "10:02 AM",
  },
  {
    id: 4,
    text: "Yeah, probably 😄",
    isMine: true,
    createdAt: "10:03 AM",
  },
  {
    id: 5,
    text: "Let's play some games together.",
    isMine: false,
    createdAt: "10:03 AM",
  },
  {
    id: 6,
    text: "Sure! What game?",
    isMine: true,
    createdAt: "10:04 AM",
  },
  {
    id: 7,
    text: "Maybe Valorant or Pico Park 😂",
    isMine: false,
    createdAt: "10:05 AM",
  },
  {
    id: 8,
    text: "Pico Park sounds fun haha",
    isMine: true,
    createdAt: "10:05 AM",
  },
  {
    id: 9,
    text: "Okay deal 👍",
    isMine: false,
    createdAt: "10:06 AM",
  },
]);

</script>