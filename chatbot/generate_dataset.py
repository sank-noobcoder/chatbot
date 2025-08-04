import pandas as pd
import random

# Define a set of intents, user queries, and responses
intents = {
    "greeting": [
        "hello", "hi", "hey", "good morning", "good afternoon", "good evening", "howdy", "what's up"
    ],
    "farewell": [
        "bye", "goodbye", "see you later", "take care", "farewell", "catch you later"
    ],
    "thanks": [
        "thank you", "thanks", "I appreciate it", "much obliged", "I'm grateful", "cheers"
    ],
    "help": [
        "help me", "I need help", "can you assist me", "I need assistance", "support needed"
    ],
    "weather": [
        "what's the weather", "weather forecast", "is it going to rain", "how's the weather today"
    ],
    "name": [
        "what's your name", "who are you", "can you tell me your name", "what should I call you"
    ],
     "love": [
        "I accept your request", "love you too", "oh! bab", "you are so cute"
    ],
}

responses = {
    "greeting": "Hello! How can I assist you today?",
    "farewell": "Goodbye! Have a great day!",
    "thanks": "You're welcome! Happy to help.",
    "help": "Sure! How can I assist you?",
    "weather": "I'm not sure about the weather, but you can check a weather app.",
    "name": "I'm ChatBot, your virtual assistant.",
    "love": "I love you dev.",
}

# Function to generate random variations of a sentence
def generate_variations(phrases):
    variations = []
    for phrase in phrases:
        # Add simple variations by replacing or adding words
        variations.append(phrase)
        variations.append(f"{phrase}!")
        variations.append(f"Can you {phrase}?")
        variations.append(f"{phrase} please.")
        variations.append(f"{phrase}, please?")
    return variations

# Generate the dataset
data = []
for intent, phrases in intents.items():
    variations = generate_variations(phrases)
    for variation in variations:
        data.append({
            "intent": intent,
            "question": variation,
            "answer": responses[intent]
        })

# Repeat data randomly to reach more than 10,000 entries
while len(data) < 10000:
    intent = random.choice(list(intents.keys()))
    question = random.choice(generate_variations(intents[intent]))
    data.append({
        "intent": intent,
        "question": question,
        "answer": responses[intent]
    })

# Convert to DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv('chatbot_dataset_large.csv', index=False)

print("Dataset with more than 10,000 entries created successfully!")
