import axiosInstance from './axiosInstance'

const sendMessage = async (message) => {
    try {
        const payload = {
            content: message
        }

        const response = await axiosInstance.post('/chatbox/chat', payload)

        return response.data.text
    } catch (error) {
        console.error(error)

        throw error
    }
}

export const chatServices = {
    sendMessage
}