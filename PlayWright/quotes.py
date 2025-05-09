import os
import requests
import random
from dotenv import load_dotenv
from datetime import datetime
import pytz

# Load environment variables (Slack token)
load_dotenv()

SLACK_TOKEN = os.getenv("SLACK_TOKEN")
channel_id = "C08GWCSNBEY"  # Replace with your actual Slack channel ID

# Predefined list of motivational quotes
QUOTES = [
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "The only way to do great work is to love what you do.",
    "Believe you can and you're halfway there.",
    "Everything you've ever wanted is on the other side of fear.",
    "Don't watch the clock; do what it does. Keep going.",
    "The future depends on what you do today.",
    "You are never too old to set another goal or to dream a new dream.",
    "Success usually comes to those who are too busy to be looking for it.",
    "The only limit to our realization of tomorrow will be our doubts of today.",
    "Do what you can, with what you have, where you are."
]


# Function to generate a random quote
def generate_random_quote():
    return random.choice(QUOTES)


# Function to generate a greeting based on current time in the specified timezone
def generate_time_based_greeting():
    # Set the timezone (e.g., for India)
    timezone = pytz.timezone('Asia/Kolkata')  # Change this to your timezone (e.g., 'America/New_York' for EST)
    current_time = datetime.now(timezone)

    # Get the hour of the day (24-hour format)
    current_hour = current_time.hour

    if 5 <= current_hour < 12:
        return "Good Morning!"
    elif 12 <= current_hour < 17:
        return "Good Afternoon!"
    elif 17 <= current_hour < 20:
        return "Good Evening!"
    else:
        return "Good Night!"


# Generate a random quote and greeting
random_quote = generate_random_quote()
greeting = generate_time_based_greeting()

# Send the greeting and quote to Slack as a message
message = {
    "channel": channel_id,
    "text": f"{greeting}\n\n> {random_quote}"
}

headers = {
    "Authorization": f"Bearer {SLACK_TOKEN}",
    "Content-Type": "application/json; charset=utf-8"
}

# Send the message to Slack
response = requests.post("https://slack.com/api/chat.postMessage", json=message, headers=headers)

# Print the response status
if response.ok and response.json().get("ok"):
    print("✅ Quote and Greeting sent!")
else:
    print(f"❌ Failed to send message: {response.text}")
