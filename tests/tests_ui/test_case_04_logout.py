from playwright.sync_api import Page

from pages.auth_page import AuthPage
from pages.home_page import HomePage


def test_logout_user(page: Page, temp_user_client, random_user):
    """This test uses the fixture temp_user_client that automatically creates the user at setup and deletes it at teardown"""
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    # 3. Verify that home page is visible successfully
    home_page = HomePage(page)
    home_page.goto("https://automationexercise.com")

    # 4. Click on 'Signup / Login' button
    home_page.click_on_signup_login_button()

    # 5. Verify 'Login to your account' is visible
    auth_page = AuthPage(page).wait_for_load()

    # 6. Enter correct email address and password
    # 7. Click 'login' button
    auth_page.fill_login_form_and_submit(random_user)

    # 8. Verify that 'Logged in as username' is visible
    home_page.check_logged_in_as_user(random_user)

    # 9. Click 'Logout' button
    home_page.click_logout_button()

    # 10. Verify that user is navigated to login page
    auth_page.wait_for_load()
