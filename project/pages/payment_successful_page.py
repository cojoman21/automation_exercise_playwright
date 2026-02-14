from typing import Self

from playwright.sync_api import Locator, Page

from pages.base_page import BasePage
from pages.components.navigation_module import NavigationModule
from pages.components.subscription_section import SubscriptionSection


class PaymentSuccessfulPage(BasePage, NavigationModule, SubscriptionSection):
    def __init__(self, page: Page):
        super().__init__(page)
        self.READY_LOCATOR: Locator = page.get_by_test_id("order-placed")

    def download_invoice(self) -> Self:
        with self.page.expect_download() as download_invoice:
            self.page.get_by_role("link", name="Download Invoice").click()

        download = download_invoice.value

        download.save_as("./project/downloads/invoice.txt")
        return self

    def click_continue(self):
        self.page.get_by_role("link", name="Continue").click()
