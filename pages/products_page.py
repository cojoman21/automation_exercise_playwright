from typing import Self

from playwright.sync_api import Locator, Page, expect

from pages.base_page import BasePage
from pages.components.brands_section import BrandsSection
from pages.components.category_section import CategorySection
from pages.components.navigation_module import NavigationModule
from pages.components.products_section import ProductsSection
from pages.components.subscription_section import SubscriptionSection


class ProductsPage(
    BasePage,
    ProductsSection,
    NavigationModule,
    SubscriptionSection,
    BrandsSection,
    CategorySection,
):
    def __init__(self, page: Page):
        super().__init__(page)
        self.READY_LOCATOR: Locator = page.get_by_text("ALL PRODUCTS")

    def search_for(self, product_name: str) -> None:
        self.page.locator("#search_product").fill(product_name)
        self.page.locator("#submit_search").click()

    def validate_search_results(self, product_name: str) -> Self:
        expect(
            self.features_product_card.filter(has_text=product_name).first
        ).to_be_visible()
        return self
