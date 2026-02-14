from playwright.sync_api import Page

from project.pages.base_page import BasePage


class AccountCreatedPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.READY_LOCATOR = page.get_by_role("heading", name="Account Created!")

    def click_continue(self):
        self.page.get_by_test_id("continue-button").click()
