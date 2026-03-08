from playwright.sync_api import Page

from api_clients.user_client import UserClient
from pages.account_deleted_page import AccountDeletedPage
from pages.auth_page import AuthPage
from pages.home_page import HomePage


def test_login_with_correct_email_and_password(
    page: Page, user_client: UserClient, session_user
):
    """This test uses the fixture user_client to create a user using the API"""
    user = UserClient(page)
    user.create_user(session_user)

    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    # 3. Verify that home page is visible successfully
    home_page = HomePage(page)
    home_page.goto("https://automationexercise.com")

    # 4. Click on 'Signup / Login' button
    home_page.click_on_signup_login_button()

    # 5. Verify 'Login to your account' is visible
    # 6. Enter correct email address and password
    # 7. Click 'login' button
    auth_page = AuthPage(page).wait_for_load()
    auth_page.fill_login_form_and_submit(session_user)

    # 8. Verify that 'Logged in as username' is visible
    home_page.check_logged_in_as_user(session_user)

    # 9. Click 'Delete Account' button
    home_page.click_delete_account()

    # 10. Verify that 'ACCOUNT DELETED!' is visible
    account_deleted_page = AccountDeletedPage(page).wait_for_load()
    account_deleted_page.click_continue()
