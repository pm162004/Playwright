import json
import requests
from playwright.sync_api import sync_playwright

# Slack webhook URL
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/XXX/YYY/ZZZ"

def send_slack_message(text):
    payload = {"text": text}
    requests.post(SLACK_WEBHOOK_URL, data=json.dumps(payload), headers={"Content-Type": "application/json"})

def test_run_test():
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto("https://example.com")

            assert "Example Domain" in page.title()
            send_slack_message("✅ Test Passed: Title is correct.")

            browser.close()
    except Exception as e:
        send_slack_message(f"❌ Test Failed: {str(e)}")

# Run the test
test_run_test()
