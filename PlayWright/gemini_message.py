import os
import requests
from dotenv import load_dotenv
from datetime import datetime
import pytz
from google.cloud import vertex_ai  # Hypothetical import for Gemini API

# Load environment variables
load_dotenv()

# Get the Slack token from environment variables
SLACK_TOKEN = os.getenv("SLACK_TOKEN")
channel_id = "C08GWCSNBEY"

# Initialize Google Cloud Vertex AI Client (hypothetical)
client = vertex_ai.PredictionServiceClient()

def generate_gemini_quote():
    try:
        # Create a request to generate text via Gemini (hypothetical request format)
        endpoint = client.endpoint_path(project="your_project", location="us-central1", endpoint="your_endpoint")
        instance = {
            "input": "Generate a short motivational quote."
        }

        response = client.predict(endpoint, instance)
        return response.predictions[0].strip()  # Adjust this based on actual API response structure
    except Exception as e:
        print(f"❌ Error generating quote with Gemini: {str(e)}")
        return "Every day is a new beginning."

def generate_time_based_greeting():
    timezone = pytz.timezone('Asia/Kolkata')
    current_hour = datetime.now(timezone).hour

    if 5 <= current_hour < 12:
        return "Good Morning!"
    elif 12 <= current_hour < 17:
        return "Good Afternoon!"
    elif 17 <= current_hour < 20:
        return "Good Evening!"
    else:
        return "Good Night!"

def send_slack_message(message_text):
    try:
        message = {
            "channel": channel_id,
            "text": message_text
        }

        headers = {
            "Authorization": f"Bearer {SLACK_TOKEN}",
            "Content-Type": "application/json; charset=utf-8"
        }

        response = requests.post("https://slack.com/api/chat.postMessage", json=message, headers=headers)

        if response.ok and response.json().get("ok"):
            print("✅ Gemini Quote and Greeting sent!")
        else:
            print(f"❌ Failed to send message: {response.text}")
    except Exception as e:
        print(f"❌ Error sending message to Slack: {str(e)}")

# Main execution
quote = generate_gemini_quote()
greeting = generate_time_based_greeting()
message_text = f"{greeting}\n\n> {quote}"
send_slack_message(message_text)
