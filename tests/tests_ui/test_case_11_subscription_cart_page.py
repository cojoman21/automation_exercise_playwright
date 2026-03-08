from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.home_page import HomePage


def test_verify_subscription_in_cart_page(page: Page):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    # 3. Verify that home page is visible successfully
    home_page = HomePage(page)
    home_page.goto("http://automationexercise.com/")

    # 4. Click 'Cart' button
    home_page.click_on_cart_button()
    cart_page = CartPage(page).wait_for_load()

    # 5. Scroll down to footer
    # 6. Verify text 'SUBSCRIPTION'
    cart_page.check_subscription_text_is_visible()

    # 7. Enter email address in input and click arrow button
    cart_page.fill_subscription_email_input("Test123@bogus.com")
    cart_page.click_subscribe()

    # 8. Verify success message 'You have been successfully subscribed!' is visible
    cart_page.validate_subscribe_success()
