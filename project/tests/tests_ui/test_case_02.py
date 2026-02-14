from playwright.sync_api import Page

from project.pages.account_created_page import AccountCreatedPage
from project.pages.account_deleted_page import AccountDeletedPage
from project.pages.auth_page import AuthPage
from project.pages.components.signup_form import SignupForm
from project.pages.home_page import HomePage


def test_register_user(page: Page, session_user):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    # 3. Verify that home page is visible successfully
    home_page = HomePage(page)
    home_page.goto("https://automationexercise.com")

    # 4. Click on 'Signup / Login' button
    home_page.click_on_signup_login_button()

    # 5. Verify 'New User Signup!' is visible
    auth_page = AuthPage(page).wait_for_load()
    auth_page.check_if_forms_headings_visible()

    # 6. Enter name and email address
    # 7. Click 'Signup' button
    auth_page.fill_signup_form_and_submit(session_user)

    # 8. Verify that 'ENTER ACCOUNT INFORMATION' is visible
    signup_form = SignupForm(page).wait_for_load()

    # 9. Fill details: Title, Name, Email, Password, Date of birth
    # 10. Select checkbox 'Sign up for our newsletter!'
    # 11. Select checkbox 'Receive special offers from our partners!'
    # 12. Fill details: First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number
    signup_form.fill_form(session_user)

    # 13. Click 'Create Account button'
    signup_form.submit()

    # 14. Verify that 'ACCOUNT CREATED!' is visible
    account_created_page = AccountCreatedPage(page).wait_for_load()

    # 15. Click 'Continue' button
    account_created_page.click_continue()

    # 16. Verify that 'Logged in as username' is visible
    home_page.wait_for_load()
    home_page.check_logged_in_as_user(session_user)


def test_login_with_correct_email_and_password(page: Page, session_user):
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
