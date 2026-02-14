from playwright.sync_api import Locator, Page

from pages.base_page import BasePage
from pages.components.navigation_module import NavigationModule
from pages.components.subscription_section import SubscriptionSection


class ContactPage(BasePage, NavigationModule, SubscriptionSection):
    def __init__(self, page: Page):
        super().__init__(page)
        self.READY_LOCATOR: Locator = page.get_by_text("GET IN TOUCH")
        self.NAME: Locator = page.get_by_test_id("name")
        self.EMAIL: Locator = page.get_by_test_id("email")
        self.SUBJECT: Locator = page.get_by_test_id("subject")
        self.MESSAGE: Locator = page.get_by_test_id("message")
        self.UPLOAD_BUTTON: Locator = page.locator("input[name='upload_file']")
        self.SUBMIT_BUTTON: Locator = page.get_by_test_id("submit-button")
        self.SUCCESS_FLASH: Locator = page.get_by_text(
            "Success! Your details have been submitted successfully."
        )
        self.HOME_BUTTON: Locator = page.get_by_text("Home")

    def fill_contact_us_form_and_submit(self, user_data: dict) -> None:
        self.NAME.fill(user_data["name"])
        self.EMAIL.fill(user_data["email"])
        self.SUBJECT.fill(user_data["subject"])
        self.MESSAGE.fill(user_data["message"])

        self._upload_file(self.UPLOAD_BUTTON, user_data["path"])
        self._dialog_listener()

        self.SUBMIT_BUTTON.click()
        self.HOME_BUTTON.click()

    def _upload_file(self, locator, path):
        locator.set_input_files(path)

    def _dialog_listener(self):
        self.page.on("dialog", lambda dialog: dialog.accept())
