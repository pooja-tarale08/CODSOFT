import random
from datetime import datetime

print("\nSTUDENT AI CHATBOT\n")
print("Type 'bye' to exit\n")

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the computer get cold? Because it forgot to close Windows!",
    "Why was the Java developer sad? Because he didn't get arrays."
]

motivations = [
    "Success comes from consistency.",
    "Small progress every day matters.",
    "Keep learning, keep growing.",
    "Your future self will thank you."
]

while True:

    user_input = input("You: ").lower()

    if "hello" in user_input or "hi" in user_input:
        print("Bot: Hello! How can I help you today?")

    elif "your name" in user_input:
        print("Bot: I am Student AI ChatBot.")

    elif "motivation" in user_input:
        print("Bot:", random.choice(motivations))

    elif "joke" in user_input:
        print("Bot:", random.choice(jokes))

    elif "python" in user_input:
        print("Bot: Start with variables, loops, functions, and OOP concepts.")

    elif "dsa" in user_input:
        print("Bot: Start with arrays, strings, recursion, and linked lists.")

    elif "time" in user_input:
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)

    elif "date" in user_input:
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", current_date)

    elif "study" in user_input:
        print("Bot: Study in small focused sessions with short breaks.")

    elif "bye" in user_input:
        print("Bot: Goodbye! Keep learning and coding.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")