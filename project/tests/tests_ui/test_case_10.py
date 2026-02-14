from playwright.sync_api import Page

from project.pages.home_page import HomePage


def test_verify_subscription_in_home_page(page: Page):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    # 3. Verify that home page is visible successfully
    home_page = HomePage(page)
    home_page.goto("https://automationexercise.com/")

    # 4. Scroll down to footer
    # 5. Verify text 'SUBSCRIPTION'
    home_page.check_subscription_text_is_visible()

    # 6. Enter email address in input and click arrow button
    home_page.fill_subscription_email_input("Test123@bogus.com")
    home_page.click_subscribe()

    # 7. Verify success message 'You have been successfully subscribed!' is visible
    home_page.validate_subscribe_success()
