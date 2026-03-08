from typing import Self

from playwright.sync_api import Locator, Page, expect


class LoginSection:
    page: Page

    @property
    def login_heading(self) -> Locator:
        return self.page.get_by_role("heading", name="Login to your account")

    @property
    def login_email_or_password_error(self) -> Locator:
        return self.page.locator("form[action='/login'] p")

    def fill_login_form_and_submit(self, user_data: dict) -> None:
        self.page.get_by_test_id("login-email").fill(user_data["email"])
        self.page.get_by_test_id("login-password").fill(user_data["password"])
        self.page.get_by_test_id("login-button").click()

    def check_login_email_error_visible(self) -> Self:
        expect(self.login_email_or_password_error).to_have_text(
            "Your email or password is incorrect!"
        )
        return self
