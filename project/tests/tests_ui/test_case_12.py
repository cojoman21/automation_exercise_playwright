from playwright.sync_api import Page

from project.pages.cart_page import CartPage
from project.pages.home_page import HomePage
from project.pages.products_page import ProductsPage


def test_add_products_in_cart(page: Page):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    # 3. Verify that home page is visible successfully
    home_page = HomePage(page)
    home_page.goto("http://automationexercise.com/")

    # 4. Click 'Products' button
    home_page.click_on_products_button()
    products_page: ProductsPage = ProductsPage(page).wait_for_load()

    # 5. Hover over first product and click 'Add to cart'
    products_page.add_features_product_card_by_product_id(1)

    # 6. Click 'Continue Shopping' button
    products_page.click_continue_shopping()

    # 7. Hover over second product and click 'Add to cart'
    products_page.add_features_product_card_by_product_id(2)

    # 8. Click 'View Cart' button
    products_page.click_view_cart()
    cart_page = CartPage(page).wait_for_load()

    # 9. Verify both products are added to Cart
    cart_page.validate_cart_products_count_equal_to(2)

    # 10. Verify their prices, quantity and total price
    cart_page.verify_products()
