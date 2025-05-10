from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError, expect

def test_example(page: Page) -> None:
    page.goto("https://app.dev-shrubs.com/")

    # Step 1: Interact with login form
    email_input = page.get_by_role("textbox", name="Enter your email")
    password_input = page.get_by_role("textbox", name="Enter your password")
    login_button = page.get_by_role("button", name="Login with Email")

    # Fill in credentials
    email_input.fill("testp567@yopmail.com")
    password_input.fill("Test@123")

    # Press Enter as alternate submit method (optional)
    password_input.press("Enter")

    # Step 2: Wait for overlay spinner to disappear before clicking login
    try:
        page.wait_for_selector("#overlay-spinner", state="hidden", timeout=30000)
    except PlaywrightTimeoutError:
        raise Exception("❌ Login spinner never disappeared. Test aborted.")

    # Step 3: Click the login button
    login_button.click()

    # Step 4: Confirm login success (adjust as per your dashboard URL or text)
    page.wait_for_load_state("networkidle")  # Ensure page is fully loaded
    assert "platform" in page.url or page.locator("text=Dashboard").is_visible(), "Login may have failed."
