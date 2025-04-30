# import pytest
# from playwright.sync_api import sync_playwright
# def test_playwrightBasics():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = browser.new_page()
#         page.goto("https://www.google.com")
#         page.screenshot(path="google.png")
#         browser.close()
def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)
    browser.new_context()
    page = browser.new_page()
    page.goto("https://www.google.com")
    browser.close()