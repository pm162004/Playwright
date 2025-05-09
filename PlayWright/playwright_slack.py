import os
import requests
from dotenv import load_dotenv
from datetime import datetime
import pytz
import openai

# Load environment variables
load_dotenv()

# Get the Slack token and OpenAI API key from environment variables
SLACK_TOKEN = os.getenv("SLACK_TOKEN")
openai.api_key = os.getenv("OPENAI_API_KEY")
channel_id = "C08GWCSNBEY"

def generate_ai_quote():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Change to gpt-3.5-turbo
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates short motivational quotes."},
                {"role": "user", "content": "Give me one short motivational quote."}
            ],
            max_tokens=50,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except openai.error.AuthenticationError:
        print("❌ Authentication error: Please check your OpenAI API key")
        return "Success is not final, failure is not fatal: it is the courage to continue that counts."
    except Exception as e:
        print(f"❌ Error generating quote: {str(e)}")
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
            print("✅ AI Quote and Greeting sent!")
        else:
            print(f"❌ Failed to send message: {response.text}")
    except Exception as e:
        print(f"❌ Error sending message to Slack: {str(e)}")

# Main execution
quote = generate_ai_quote()
greeting = generate_time_based_greeting()
message_text = f"{greeting}\n\n> {quote}"
send_slack_message(message_text)