from typing import Self

from playwright.sync_api import Locator, Page, expect


class SignupSection:
    page: Page

    @property
    def signup_heading(self) -> Locator:
        return self.page.get_by_role("heading", name="New User Signup!")

    @property
    def signup_email_error(self) -> Locator:
        return self.page.locator("form[action='/signup'] p")

    def fill_signup_form_and_submit(self, user_data: dict) -> None:
        self.page.get_by_test_id("signup-name").fill(user_data["name"])
        self.page.get_by_test_id("signup-email").fill(user_data["email"])
        self.page.get_by_test_id("signup-button").click()

    def check_signup_email_error_visible(self) -> Self:
        expect(self.signup_email_error).to_have_text("Email Address already exist!")
        return self
