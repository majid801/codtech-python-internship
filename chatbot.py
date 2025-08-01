import nltk
from nltk.chat.util import Chat, reflections

# Download tokenizer (only once)
nltk.download('punkt')

# Define some basic patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["I'm your friendly internship chatbot!",]
    ],
    [
        r"how are you ?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"(.*) your name ?",
        ["My name is CodBot!",]
    ],
    [
        r"(.*) help (.*)",
        ["Sure, I'm here to help. Tell me what you need."]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye!", "See you later!", "Thanks for chatting!"]
    ],
    [
        r"(.*)",
        ["I didn't understand that. Can you rephrase?"]
    ]
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Start chatting
print("🔵 Welcome to CodTech NLP ChatBot!")
print("🗨️  Type 'bye' to exit.")
chatbot.converse()
