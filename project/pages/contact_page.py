from typing import Self

from playwright.sync_api import Locator, Page, expect

from project.pages.base_page import BasePage
from project.pages.components.navigation_module import NavigationModule
from project.pages.components.subscription_section import SubscriptionSection


class ContactPage(BasePage, NavigationModule, SubscriptionSection):
    def __init__(self, page: Page):
        super().__init__(page)
        self.READY_LOCATOR: Locator = page.get_by_text("GET IN TOUCH")

    def fill_contact_us_form_and_submit(self, user_data: dict) -> Self:
        self.page.on("dialog", lambda dialog: dialog.accept())

        self.page.locator("input[name='upload_file']").set_input_files(
            user_data["upload_path"]
        )
        self.page.wait_for_load_state("networkidle")

        self.page.get_by_test_id("name").fill(user_data["name"])
        self.page.get_by_test_id("email").fill(user_data["email"])
        self.page.get_by_test_id("subject").fill(user_data["subject"])
        self.page.get_by_test_id("message").fill(user_data["message"])

        self.page.get_by_test_id("submit-button").click()
        return self

    def check_contact_us_success_message_visible(self) -> Self:
        self.page.locator(".contact-form").get_by_text(
            "Success! Your details have been submitted successfully.", exact=False
        ).wait_for(state="visible", timeout=15000)
        return self

    def check_special_home_post_contact_us_success_visible(self) -> Self:
        self.page.locator("#form-section").get_by_text("Home").wait_for(state="visible")
        return self

    def click_special_home_post_contact_us_success(self) -> None:
        self.page.locator("#form-section").get_by_text("Home").click()
