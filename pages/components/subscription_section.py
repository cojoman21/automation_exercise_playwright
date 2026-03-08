from typing import Self

from playwright.sync_api import Locator, Page, expect


class SubscriptionSection:
    page: Page

    @property
    def subscription_heading(self) -> Locator:
        return self.page.locator("#footer").get_by_role("heading", name="Subscription")

    def fill_subscription_email_input(self, email: str) -> Self:
        self.page.locator("#footer").locator("#susbscribe_email").fill(email)
        return self

    def click_subscribe(self) -> Self:
        self.page.locator("#footer").locator("#subscribe").click()
        return self

    def validate_subscribe_success(self) -> Self:
        self.page.locator("#footer").get_by_text(
            "You have been successfully subscribed!"
        ).wait_for(state="visible")
        return self

    def check_subscription_text_is_visible(self) -> Self:
        expect(self.subscription_heading).to_be_visible()
        return self
