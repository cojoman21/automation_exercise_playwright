from playwright.sync_api import Page

from project.pages.account_created_page import AccountCreatedPage
from project.pages.account_deleted_page import AccountDeletedPage
from project.pages.auth_page import AuthPage
from project.pages.cart_page import CartPage
from project.pages.checkout_page import CheckoutPage
from project.pages.components.signup_form import SignupForm
from project.pages.home_page import HomePage


def test_verify_address_details_in_checkout_page(page: Page, random_user):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    # 3. Verify that home page is visible successfully
    home_page = HomePage(page)
    home_page.goto("https://www.automationexercise.com/")

    # 4. Click 'Signup / Login' button
    home_page.click_on_signup_login_button()
    auth_page = AuthPage(page).wait_for_load()

    # 5. Fill all details in Signup and create account
    auth_page.fill_signup_form_and_submit(random_user)

    signup_form = SignupForm(page).wait_for_load()
    signup_form.fill_form(random_user)
    signup_form.submit()

    # 6. Verify 'ACCOUNT CREATED!' and click 'Continue' button
    account_created_page = AccountCreatedPage(page).wait_for_load()
    account_created_page.click_continue()

    # 7. Verify ' Logged in as username' at top
    home_page.wait_for_load()
    home_page.check_logged_in_as_user(random_user)

    # 8. Add products to cart
    home_page.add_features_product_card_by_product_id(1).click_continue_shopping()
    home_page.add_features_product_card_by_product_id(7).click_continue_shopping()
    home_page.add_features_product_card_by_product_id(8).click_continue_shopping()

    # 9. Click 'Cart' button
    home_page.click_on_cart_button()

    # 10. Verify that cart page is displayed
    cart_page = CartPage(page).wait_for_load()

    # 11. Click Proceed To Checkout
    cart_page.click_on_proceed_to_checkout()
    checkout_page = CheckoutPage(page).wait_for_load()

    # 12. Verify that the delivery address is same address filled at the time registration of account
    checkout_page.validate_delivery_address_is_correct(random_user)

    # 13. Verify that the billing address is same address filled at the time registration of account
    checkout_page.validate_billing_address_is_correct(random_user)

    # 14. Click 'Delete Account' button
    checkout_page.click_delete_account()

    # 15. Verify 'ACCOUNT DELETED!' and click 'Continue' button
    account_deleted_page = AccountDeletedPage(page).wait_for_load()
    account_deleted_page.click_continue()
