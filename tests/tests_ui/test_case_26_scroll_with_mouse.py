from playwright.sync_api import Page

from pages.home_page import HomePage


def test_verify_scroll_without_arrow(page: Page):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    # 3. Verify that home page is visible successfully
    home_page = HomePage(page)
    home_page.goto("https://www.automationexercise.com/")

    # 4. Scroll down page to bottom
    home_page.scroll_with_mouse_wheel(500)

    # 5. Verify 'SUBSCRIPTION' is visible
    home_page.scroll_with_mouse_until_visible(home_page.subscription_heading)
    # 6. Click on arrow at bottom right side to move upward
    home_page.click_scroll_up_arrow()

    # 7. Verify that page is scrolled up and 'Full-Fledged practice website for Automation Engineers' text is visible on screen
    home_page.is_in_viewport(home_page.subscription_heading)
    home_page.assert_visible(home_page.READY_LOCATOR)
