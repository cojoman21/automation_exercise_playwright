from pages.cart_page import CartPage
from pages.home_page import HomePage
from playwright.sync_api import Page, expect


def test_remove_products_from_cart(page: Page):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    # 3. Verify that home page is visible successfully
    home_page = HomePage(page)
    home_page.goto("https://www.automationexercise.com/")

    # 4. Add products to cart
    home_page.add_features_product_card_by_product_id(1).click_continue_shopping()
    home_page.add_features_product_card_by_product_id(7).click_continue_shopping()
    home_page.add_features_product_card_by_product_id(8).click_continue_shopping()

    # 5. Click 'Cart' button
    home_page.click_on_cart_button()

    # 6. Verify that cart page is displayed
    cart_page = CartPage(page).wait_for_load()

    # 7. Click 'X' button corresponding to particular product
    cart_page.delete_product_from_cart(1)

    # 8. Verify that product is removed from the cart
    expect(cart_page.CART_ITEMS).to_have_count(2)
