# import pytest
from playwright.sync_api import Page, sync_playwright
def test_playwrightBasics(page: Page):
    page.goto("https://www.google.com")

def test_coreLocators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("button", name="Login").click()












# def test_playwrightBasics():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         context = browser.new_context()
#         page = browser.new_page()
#         page.goto("https://www.google.com")
#         page.screenshot(path="google.png")
#         browser.close()
# def test_playwrightBasics(playwright):
#     browser = playwright.chromium.launch(headless=False)
#     browser.new_context()
#     page = browser.new_page()
#     page.goto("https://www.google.com")
#     browser.close()


# def test_playwrightBasics(page: Page):
#     page.goto("https://www.google.com")