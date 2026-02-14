from playwright.sync_api import Page

from project.pages.home_page import HomePage


def test_view_category_products(page: Page):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    # 3. Verify that categories are visible on left side bar
    home_page = HomePage(page)
    home_page.goto("https://www.automationexercise.com/")

    # 4. Click on 'Women' category
    # 5. Click on any category link under 'Women' category, for example: Dress
    home_page.expand_category("#Women").click_dress()

    # 6. Verify that category page is displayed and confirm text 'WOMEN - TOPS PRODUCTS'
    home_page.check_selected_category_is_visible("Women", "Dress")

    # 7. On left side bar, click on any sub-category link of 'Men' category
    home_page.expand_category("#Men").click_jeans()

    # 8. Verify that user is navigated to that category page
    home_page.check_selected_category_is_visible("Men", "Jeans")
