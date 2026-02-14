from playwright.sync_api import Page

from project.pages.cart_page import CartPage
from project.pages.home_page import HomePage


def test_add_to_cart_from_recommended_items(page: Page):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    home_page = HomePage(page)
    home_page.goto("https://www.automationexercise.com/")

    # 3. Scroll to bottom of page
    # 4. Verify 'RECOMMENDED ITEMS' are visible
    home_page.check_recommended_heading_visible()

    # 5. Click on 'Add To Cart' on Recommended product
    home_page.add_recommended_product_card_by_product_id(4).click_continue_shopping()

    # 6. Click on 'View Cart' button
    home_page.click_on_cart_button()
    cart_page = CartPage(page).wait_for_load()

    # 7. Verify that product is displayed in cart page
    cart_page.verify_product_in_cart(4)
