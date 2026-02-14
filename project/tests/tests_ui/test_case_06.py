from pages.contact_page import ContactPage
from pages.home_page import HomePage
from playwright.sync_api import Page


def test_contact_us_form(page: Page, random_user):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    # 3. Verify that home page is visible successfully
    home_page = HomePage(page)
    home_page.goto("https://www.automationexercise.com")

    # 4. Click on 'Contact Us' button
    home_page.click_on_contact_us_button()

    # 5. Verify 'GET IN TOUCH' is visible
    contact_page = ContactPage(page).wait_for_load()

    # 6. Enter name, email, subject and message
    # 7. Upload file
    # 8. Click 'Submit' button
    # 9. Click OK button
    # 10. Verify success message 'Success! Your details have been submitted successfully.' is visible
    contact_page.fill_contact_us_form_and_submit(random_user)

    # 11. Click 'Home' button and verify that landed to home page successfully
    home_page.wait_for_load()
