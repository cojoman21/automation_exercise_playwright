from playwright.sync_api import Page

from api_clients.user_client import UserClient
from pages.account_deleted_page import AccountDeletedPage
from pages.auth_page import AuthPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.payment_page import PaymentPage
from pages.payment_successful_page import PaymentSuccessfulPage


def test_place_order_and_login_before_checkout(
    page: Page, user_client: UserClient, random_user
):
    """This test uses the fixture user_client to create a user using the API"""
    user = UserClient(page)
    user.create_user(random_user)

    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    # 3. Verify that home page is visible successfully
    # 4. Click 'Signup / Login' button
    home_page = HomePage(page)
    home_page.goto("https://www.automationexercise.com/")
    home_page.click_on_signup_login_button()

    # 5. Fill email, password and click 'Login' button
    auth_page = AuthPage(page).wait_for_load()
    auth_page.fill_login_form_and_submit(random_user)

    # 6. Verify 'Logged in as username' at top
    home_page.wait_for_load()
    home_page.check_logged_in_as_user(random_user)

    # 7. Add products to cart
    home_page.add_features_product_card_by_product_id(1).click_continue_shopping()
    home_page.add_features_product_card_by_product_id(7).click_continue_shopping()
    home_page.add_features_product_card_by_product_id(8).click_continue_shopping()

    # 8. Click 'Cart' button
    home_page.click_on_cart_button()

    # 9. Verify that cart page is displayed
    cart_page = CartPage(page).wait_for_load()

    # 10. Click Proceed To Checkout
    cart_page.click_on_proceed_to_checkout()

    # 11. Verify Address Details and Review Your Order
    checkout_page = CheckoutPage(page).wait_for_load()
    checkout_page.validate_delivery_address_is_correct(random_user)
    checkout_page.validate_billing_address_is_correct(random_user)

    # 12. Enter description in comment text area and click 'Place Order'
    checkout_page.add_order_comment(random_user)
    checkout_page.click_place_order()

    # 13. Enter payment details: Name on Card, Card Number, CVC, Expiration date
    payment_page = PaymentPage(page).wait_for_load()
    payment_page.fill_payment_form(random_user)

    # 14. Click 'Pay and Confirm Order' button
    payment_page.fill_payment_form(random_user)
    payment_page.submit_payment_form()

    # 15. Verify success message 'Your order has been placed successfully!'
    payment_done_page = PaymentSuccessfulPage(page).wait_for_load()
    payment_done_page.click_continue()

    # 16. Click 'Delete Account' button
    home_page.click_delete_account()

    # 17. Verify 'ACCOUNT DELETED!' and click 'Continue' button
    account_deleted_page = AccountDeletedPage(page).wait_for_load()
    account_deleted_page.click_continue()
