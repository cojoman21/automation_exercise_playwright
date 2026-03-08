from playwright.sync_api import Locator, Page

from pages.base_page import BasePage
from pages.components.navigation_module import NavigationModule
from pages.components.subscription_section import SubscriptionSection


class TestCasesPage(BasePage, NavigationModule, SubscriptionSection):
    __test__ = False

    def __init__(self, page: Page):
        super().__init__(page)
        self.READY_LOCATOR: Locator = page.get_by_text(
            "Below is the list of test Cases for you to practice the Automation. Click on the scenario for detailed Test Steps:"
        )
