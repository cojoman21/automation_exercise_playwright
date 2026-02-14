from playwright.sync_api import Page

from project.pages.home_page import HomePage


def test_verify_scroll_with_arrow(page: Page):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    # 3. Verify that home page is visible successfully
    home_page = HomePage(page)
    home_page.goto("https://www.automationexercise.com/")

    # 4. Scroll down page to bottom
    home_page.scroll_with_keys("End")

    # 5. Verify 'SUBSCRIPTION' is visible
    home_page.check_subscription_text_is_visible()

    # 6. Scroll up page to top
    home_page.scroll_with_keys("Home")

    # 7. Verify that page is scrolled up and 'Full-Fledged practice website for Automation Engineers' text is visible on screen
    home_page.assert_visible(home_page.READY_LOCATOR)
