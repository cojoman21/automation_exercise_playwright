from playwright.sync_api import Locator, Page

from project.pages.base_page import BasePage
from project.pages.components.brands_section import BrandsSection
from project.pages.components.category_section import CategorySection
from project.pages.components.navigation_module import NavigationModule
from project.pages.components.products_section import ProductsSection
from project.pages.components.subscription_section import SubscriptionSection


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
