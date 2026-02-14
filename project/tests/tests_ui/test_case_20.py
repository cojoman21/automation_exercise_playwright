from data.test_data import EXISTING_USER
from pages.auth_page import AuthPage
from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from playwright.sync_api import Page


def test_search_products_and_verify_cart_after_login(page: Page):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    home_page = HomePage(page)
    home_page.goto("https://www.automationexercise.com/")

    # 3. Click on 'Products' button
    home_page.click_on_products_button()

    # 4. Verify user is navigated to ALL PRODUCTS page successfully
    products_page = ProductsPage(page).wait_for_load()

    # 5. Enter product name in search input and click search button
    products_page.search_for("dress")

    # 6. Verify 'SEARCHED PRODUCTS' is visible
    products_page.check_searched_products_heading_visible()

    # 7. Verify all the products related to search are visible
    products_page.validate_search_results("dress")

    # 8. Add those products to cart
    products_page.add_features_product_card_by_product_name(
        "sleeveless"
    ).click_continue_shopping()

    products_page.add_features_product_card_by_product_name(
        "maxi dress"
    ).click_continue_shopping()

    # 9. Click 'Cart' button and verify that products are visible in cart
    home_page.click_on_cart_button()
    cart_page = CartPage(page).wait_for_load()
    cart_page.verify_products()

    # 10. Click 'Signup / Login' button and submit login details
    home_page.click_on_signup_login_button()
    auth_page = AuthPage(page).wait_for_load()
    auth_page.fill_login_form_and_submit(EXISTING_USER)
    home_page.wait_for_load()

    # 11. Again, go to Cart page
    home_page.click_on_cart_button()

    # 12. Verify that those products are visible in cart after login as well
    cart_page.wait_for_load()
    cart_page.verify_products()
