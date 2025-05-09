import json
import requests
from playwright.sync_api import sync_playwright

# Slack webhook URL
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"

def send_slack_message(text):
    payload = {"text": text}
    response = requests.post(SLACK_WEBHOOK_URL, data=json.dumps(payload), headers={"Content-Type": "application/json"})
    if response.status_code == 200:
        print("✅ Slack message sent")
    else:
        print(f"❌ Failed: {response.status_code} - {response.text}")

def run_test_and_notify():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        try:
            page.goto("https://example.com")
            assert "Example Domain" in page.title()
            send_slack_message("✅ UI Test Passed: example.com loaded successfully")
        except Exception as e:
            send_slack_message(f"❌ UI Test Failed: {str(e)}")
        finally:
            browser.close()

run_test_and_notify()
