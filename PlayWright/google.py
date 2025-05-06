from playwright.sync_api import sync_playwright, Page, expect

def test_example(page: Page) -> None:
    page.goto("https://www.google.com/")
    page.get_by_role("combobox", name="Search").click()
    page.get_by_role("combobox", name="Search").click()
    page.get_by_role("combobox", name="Search").fill("BNJNJK")
    page.get_by_role("link", name="Sign in").click()
    page.get_by_role("textbox", name="Email or phone").fill("JHJHJH")

def run_test():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Ensures headless mode
        page = browser.new_page()
        test_example(page)
        browser.close()

run_test()
