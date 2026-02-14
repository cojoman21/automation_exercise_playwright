from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.product_details_page import ProductDetailsPage
from playwright.sync_api import Page


def test_verify_product_quantity_in_cart(page: Page):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    # 3. Verify that home page is visible successfully
    home_page = HomePage(page)
    home_page.goto("https://www.automationexercise.com")

    # 4. Click 'View Product' for any product on home page
    home_page.view_features_product_by_product_id(1)

    # 5. Verify product detail is opened
    product_details_page = ProductDetailsPage(page).wait_for_load()

    # 6. Increase quantity to 4
    product_details_page.set_quantity(4)

    # 7. Click 'Add to cart' button
    product_details_page.click_add_to_cart()

    # 8. Click 'View Cart' button
    product_details_page.click_view_cart()
    cart_page = CartPage(page).wait_for_load()

    # 9. Verify that product is displayed in cart page with exact quantity
    cart_page.validate_cart_product_quantity(1, 4)
