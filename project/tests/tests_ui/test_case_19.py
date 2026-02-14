from playwright.sync_api import Page

from project.pages.home_page import HomePage


def test_view_brands(page: Page):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    # 3. Click on 'Products' button
    # 4. Verify that Brands are visible on left side bar
    home_page = HomePage(page)
    home_page.goto("https://www.automationexercise.com/")

    # 5. Click on any brand name
    home_page.click_brand("Babyhug")

    # 6. Verify that user is navigated to brand page and brand products are displayed
    home_page.check_selected_brand_is_visible("Babyhug")

    # 7. On left side bar, click on any other brand link
    home_page.click_brand("Allen Solly Junior")

    # 8. Verify that user is navigated to that brand page and can see products
    home_page.check_selected_brand_is_visible("Allen Solly Junior")
