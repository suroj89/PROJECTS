def get_response(message):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! How can I help you? 😊"
    elif "name" in message:
        return "I am a simple chatbot 🤖"
    elif "bye" in message:
        return "Goodbye! Have a nice day 👋"
    elif "help" in message:
        return "I can answer simple questions. Try asking my name!"
    else:
        return "Sorry, I don't understand that yet 😅"
