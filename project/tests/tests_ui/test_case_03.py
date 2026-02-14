from playwright.sync_api import Page

from project.pages.auth_page import AuthPage
from project.pages.home_page import HomePage


def test_login_with_incorrect_email_and_password(page: Page, random_user):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    # 3. Verify that home page is visible successfully
    home_page = HomePage(page)
    home_page.goto("https://automationexercise.com")

    # 4. Click on 'Signup / Login' button
    home_page.click_on_signup_login_button()

    # 5. Verify 'Login to your account' is visible
    auth_page = AuthPage(page).wait_for_load()

    # 6. Enter incorrect email address and password
    # 7. Click 'login' button
    auth_page.fill_login_form_and_submit(random_user)

    # 8. Verify error 'Your email or password is incorrect!' is visible
    auth_page.check_login_email_error_visible()
