import pytest
from playwright.sync_api import sync_playwright, expect

def test_example():
    # Initialize Playwright
    with sync_playwright() as playwright:
        # Launch the browser in headless mode
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to the target page
        page.goto("https://rahulshettyacademy.com/loginpagePractise/")

        # Fill in the username and password fields
        page.locator("input[name='username']").fill("rahulshettyacademy")
        page.locator("input[name='password']").fill("learning")

        # Agree to the terms
        page.locator("input[type='checkbox']").check()

        # Wait for the button to be fully visible and clickable
        button = page.locator("button[type='submit']")
        button.wait_for(state="attached")  # Ensure the button is in the DOM
        button.wait_for(state="visible")  # Ensure the button is visible
        button.click()

        # Wait for navigation after the click (This is often implicit after clicking)
        page.wait_for_navigation(timeout=60000)  # You can specify a timeout if needed

        # Optionally, add assertions to verify login success
        expect(page).to_have_url("https://rahulshettyacademy.com/tryOurCourses.php")

        # Close the browser after the test
        browser.close()
