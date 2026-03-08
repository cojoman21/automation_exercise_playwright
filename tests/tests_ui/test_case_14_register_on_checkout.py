from playwright.sync_api import Page

from pages.account_created_page import AccountCreatedPage
from pages.account_deleted_page import AccountDeletedPage
from pages.auth_page import AuthPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.components.signup_form import SignupForm
from pages.home_page import HomePage
from pages.payment_page import PaymentPage
from pages.payment_successful_page import PaymentSuccessfulPage


def test_place_order_and_register_on_checkout(page: Page, random_user):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    # 3. Verify that home page is visible successfully
    home_page = HomePage(page)
    home_page.goto("http://automationexercise.com")

    # 4. Add products to cart
    home_page.add_features_product_card_by_product_id(1).click_continue_shopping()
    home_page.add_features_product_card_by_product_id(7).click_continue_shopping()
    home_page.add_features_product_card_by_product_id(8).click_continue_shopping()

    # 5. Click 'Cart' button
    home_page.click_on_cart_button()

    # 6. Verify that cart page is displayed
    cart_page = CartPage(page).wait_for_load()

    # 7. Click Proceed To Checkout
    cart_page.click_on_proceed_to_checkout()

    # 8. Click 'Register / Login' button
    cart_page.click_on_register_or_login()

    # 9. Fill all details in Signup and create account
    auth_page = AuthPage(page).wait_for_load()
    auth_page.fill_signup_form_and_submit(random_user)

    signup_form = SignupForm(page).wait_for_load()
    signup_form.fill_form(random_user)
    signup_form.submit()

    # 10. Verify 'ACCOUNT CREATED!' and click 'Continue' button
    account_created = AccountCreatedPage(page).wait_for_load()
    account_created.click_continue()
    home_page.wait_for_load()

    # 11. Verify ' Logged in as username' at top
    home_page.check_logged_in_as_user(random_user)

    # 12.Click 'Cart' button
    home_page.click_on_cart_button()

    # 13. Click 'Proceed To Checkout' button
    cart_page.wait_for_load()
    cart_page.PROCEED_TO_CHECKOUT.click()

    # 14. Verify Address Details and Review Your Order
    checkout_page = CheckoutPage(page).wait_for_load()
    checkout_page.validate_delivery_address_is_correct(random_user)
    checkout_page.validate_billing_address_is_correct(random_user)

    # 15. Enter description in comment text area and click 'Place Order'
    checkout_page.add_order_comment(random_user)
    checkout_page.PLACE_ORDER_BTN.click()

    # 16. Enter payment details: Name on Card, Card Number, CVC, Expiration date
    payment_page = PaymentPage(page).wait_for_load()
    payment_page.fill_payment_form(random_user)

    # 17. Click 'Pay and Confirm Order' button
    payment_page.submit_payment_form()

    # 18. Verify success message 'Your order has been placed successfully!'
    payment_successful_page = PaymentSuccessfulPage(page).wait_for_load()
    payment_successful_page.click_continue()

    # 19. Click 'Delete Account' button
    home_page.wait_for_load()
    home_page.click_delete_account()

    # 20. Verify 'ACCOUNT DELETED!' and click 'Continue' button
    account_deleted_page = AccountDeletedPage(page).wait_for_load()
    account_deleted_page.click_continue()
