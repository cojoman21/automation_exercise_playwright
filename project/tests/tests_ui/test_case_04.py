from playwright.sync_api import Page, expect

from project.data.test_data import EXISTING_USER
from project.pages.auth_page import AuthPage
from project.pages.home_page import HomePage


def test_logout_user(page: Page):
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
    auth_page.fill_login_form_and_submit(EXISTING_USER)

    # 8. Verify that 'Logged in as username' is visible
    home_page.check_logged_in_as_user(EXISTING_USER)

    # 9. Click 'Logout' button
    home_page.click_logout_button()

    # 10. Verify that user is navigated to login page
    auth_page.wait_for_load()
