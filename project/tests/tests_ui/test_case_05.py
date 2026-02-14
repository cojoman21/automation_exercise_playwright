from data.test_data import EXISTING_USER
from playwright.sync_api import Page

from project.pages.auth_page import AuthPage
from project.pages.home_page import HomePage


def test_register_user_with_existing_email(page: Page):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    # 3. Verify that home page is visible successfully
    home_page = HomePage(page)
    home_page.goto("https://automationexercise.com")

    # 4. Click on 'Signup / Login' button
    home_page.click_on_signup_login_button()

    # 5. Verify 'New User Signup!' is visible
    auth_page = AuthPage(page).wait_for_load()

    # 6. Enter name and already registered email address
    # 7. Click 'Signup' button
    auth_page.fill_signup_form_and_submit(EXISTING_USER)

    # 8. Verify error 'Email Address already exist!' is visible
    auth_page.check_signup_email_error_visible()
