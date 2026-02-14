from playwright.sync_api import Locator, Page

from pages.base_page import BasePage
from pages.components.brands_section import BrandsSection
from pages.components.category_section import CategorySection
from pages.components.navigation_module import NavigationModule
from pages.components.products_section import ProductsSection
from pages.components.subscription_section import SubscriptionSection


class HomePage(
    BasePage,
    NavigationModule,
    ProductsSection,
    CategorySection,
    BrandsSection,
    SubscriptionSection,
):
    def __init__(self, page: Page):
        super().__init__(page)
        self.READY_LOCATOR: Locator = page.locator("#slider-carousel")
