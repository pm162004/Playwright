from playwright.sync_api import Page

def test_hello(page:Page):
    page.goto("https://magic-data-fe-dev.webelight.co.in/sign-up")