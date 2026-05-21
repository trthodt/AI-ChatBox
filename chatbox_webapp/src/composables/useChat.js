import { chatServices } from '@/services/chat.service'
import { ref } from 'vue'

export function useChat() {
    const messages = ref([])
    const loading = ref(false)

    const sendMessage = async (content) => {
        loading.value = true

        try {
            const reply = await chatServices.sendMessage(content)

            messages.value.push({
                role: 'user',
                content
            })

            messages.value.push({
                role: 'assistant',
                content: reply
            })
        } finally {
            loading.value = false
        }
    }

    return {
        messages,
        loading,
        sendMessage
    }
}