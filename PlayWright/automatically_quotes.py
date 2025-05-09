import requests
from dotenv import load_dotenv
import os
from datetime import datetime
import pytz

# Load environment variables (Slack token)
load_dotenv()

SLACK_TOKEN = os.getenv("SLACK_TOKEN")
channel_id = "C08L16N22AU"  # Replace with your actual Slack channel ID

import requests

def fetch_random_quote():
    response = requests.get("https://zenquotes.io/api/random")
    if response.ok:
        quote = response.json()[0]['q']
        return quote
    else:
        return "Stay positive!"

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
random_quote = fetch_random_quote()
greeting = generate_time_based_greeting()
print(random_quote)

# # Send the greeting and quote to Slack as a message
# message = {
#     "channel": channel_id,
#     "text": f"{greeting}\n\n> {random_quote}"
# }
message = {
    "channel": channel_id,
    "text": f"{greeting}\n\n> {random_quote}",
    "username": "Motivator Bot",  # Name that shows as sender
    "icon_emoji": ":sun_with_face:"  # Optional emoji as bot icon
}

headers = {
    "Authorization": f"Bearer {SLACK_TOKEN}",
    "Content-Type": "application/json; charset=utf-8"
}

# Send the message to Slack
response = requests.post("https://slack.com/api/chat.postMessage", json=message, headers=headers)
print(response.text)
# Print the response status
if response.ok and response.json().get("ok"):
    print("✅ Quote and Greeting sent!")
else:
    print(f"❌ Failed to send message: {response.text}")
