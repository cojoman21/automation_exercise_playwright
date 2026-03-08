from typing import Self

from playwright.sync_api import Locator, Page, expect

from pages.base_page import BasePage
from pages.components.login_section import LoginSection
from pages.components.navigation_module import NavigationModule
from pages.components.signup_section import SignupSection
from pages.components.subscription_section import SubscriptionSection


class AuthPage(
    BasePage, LoginSection, SignupSection, NavigationModule, SubscriptionSection
):
    def __init__(self, page: Page):
        super().__init__(page)
        self.READY_LOCATOR: Locator = self.page.get_by_role("heading", name="OR")

    def check_if_forms_headings_visible(self) -> Self:
        expect(self.login_heading).to_be_visible()
        expect(self.signup_heading).to_be_visible()
        return self
