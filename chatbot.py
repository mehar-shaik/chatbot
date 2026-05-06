import time
import random

def chatbot():
    print("🤖 Chatbot: Hello! I'm your friendly chatbot.")
    name = input("👤 You: What's your name? ").strip().title()
    print(f"🤖 Chatbot: Nice to meet you, {name}!")

    while True:
        user_input = input("👤 You: ").lower().strip()

        # Greetings
        if user_input in ["hi", "hello", "hey"]:
            print("🤖 Chatbot:", random.choice([
                "Hello there!",
                "Hey! How can I help you?",
                "Hi! Nice to chat with you 😊"
            ]))

        # How are you
        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm doing great! Thanks for asking 😊")

        # Name
        elif "your name" in user_input:
            print("🤖 Chatbot: I'm a Python chatbot created by you!")

        # Age
        elif "age" in user_input:
            print("🤖 Chatbot: I don't have an age, but I'm always learning!")

        # Time
        elif "time" in user_input:
            current_time = time.strftime("%I:%M %p")
            print(f"🤖 Chatbot: Current time is {current_time}")

        # Joke
        elif "joke" in user_input:
            jokes = [
                "Why do programmers hate nature? Too many bugs 🐛",
                "Why did Python go to school? To improve its 'class' 😄",
                "Why do Java developers wear glasses? Because they can't C 😆"
            ]
            print("🤖 Chatbot:", random.choice(jokes))

        # Help
        elif "help" in user_input:
            print("🤖 Chatbot: You can ask me about time, jokes, or just chat!")

        # Exit
        elif user_input in ["bye", "exit", "quit"]:
            print(f"🤖 Chatbot: Goodbye {name}! Have a great day 👋")
            break

        # Default response
        else:
            print("🤖 Chatbot: Sorry, I didn't understand that. Try asking something else!")

# Run chatbot
chatbot()