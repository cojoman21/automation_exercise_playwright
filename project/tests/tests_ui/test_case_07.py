from pages.home_page import HomePage
from pages.test_cases_page import TestCasesPage
from playwright.sync_api import Page


def test_test_cases_page(page: Page):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    # 3. Verify that home page is visible successfully
    home_page = HomePage(page)
    home_page.goto("https://automationexercise.com/")

    # 4. Click on 'Test Cases' button
    home_page.click_on_test_cases_button()

    # 5. Verify user is navigated to test cases page successfully
    test_cases_page = TestCasesPage(page)
    test_cases_page.wait_for_load()
