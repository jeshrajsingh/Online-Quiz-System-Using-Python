import tkinter as tk
from tkinter import scrolledtext
import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot and I'm here to assist you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm doing great!",]
    ],
    [
        r"sorry (.*)",
        ["No problem, don't worry!", "It's alright.",]
    ],
    [
        r"(.*) thank you (.*)",
        ["You're welcome!", "No problem. How can I assist you further?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hi there!",]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye, have a great day!",]
    ],
]

# Create a Chatbot
def chatbot_response(user_input, chat):
    return chat.respond(user_input)

def send():
    user_input = entry.get()
    if user_input.lower() == "quit":
        response_text.insert(tk.END, "You: " + user_input + "\n")
        response_text.insert(tk.END, "Chatbot: Bye! Take care.\n")
        entry.delete(0, tk.END)
        entry.config(state=tk.DISABLED)
    else:
        response = chatbot_response(user_input, chat)
        response_text.insert(tk.END, "You: " + user_input + "\n")
        response_text.insert(tk.END, "Chatbot: " + response + "\n")
        entry.delete(0, tk.END)

# Initialize tkinter
root = tk.Tk()
root.title("Chatbot")

# Create Chat instance
chat = Chat(pairs, reflections)

# Create UI elements
frame = tk.Frame(root)
entry = tk.Entry(frame, width=50)
send_button = tk.Button(frame, text="Send", command=send)
response_text = scrolledtext.ScrolledText(frame, width=60, height=20)

# Pack UI elements
frame.pack(pady=10)
entry.pack(side=tk.LEFT, padx=5)
send_button.pack(side=tk.LEFT, padx=5)
response_text.pack(pady=10)

# Start conversation
response_text.insert(tk.END, "Chatbot: Hi! I'm Chatbot. How can I help you today?\n")
response_text.insert(tk.END, "Chatbot: Type 'quit' to exit.\n")
entry.focus_set()

# Bind Enter key to send message
root.bind("<Return>", lambda event: send())

root.mainloop()
