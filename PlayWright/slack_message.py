import requests
import os
from dotenv import load_dotenv
load_dotenv()

# Replace with Priya's OAuth token and the channel ID
SLACK_TOKEN = os.getenv("SLACK_TOKEN")
channel_id = "C08GWCSNBEY"  # Replace with your channel ID

message = {
    "channel": channel_id,
    "text": "Hello, this is Priya sending an automated message!"
}

headers = {
    "Authorization": f"Bearer {SLACK_TOKEN}",
    "Content-Type": "application/json"
}

response = requests.post("https://slack.com/api/chat.postMessage", json=message, headers=headers)

if response.ok and response.json().get("ok"):
    print("✅ Message sent as Priya!")
else:
    print(f"❌ Failed to send message: {response.text}")
