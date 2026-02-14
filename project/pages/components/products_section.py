from typing import Self

from playwright.sync_api import Locator, Page, expect


class ProductsSection:
    page: Page

    # Locators of properties
    @property
    def features_items_heading(self) -> Locator:
        return self.page.get_by_role("heading", name="Features Items")

    @property
    def recommended_items_heading(self) -> Locator:
        return self.page.get_by_role("heading", name="recommended items")

    @property
    def features_product_card(self) -> Locator:
        return self.page.locator(".features_items .product-image-wrapper")

    @property
    def recommended_product_card(self) -> Locator:
        return self.page.locator(".recommended_items .product-image-wrapper")

    @property
    def searched_products_heading(self) -> Locator:
        return self.page.get_by_role("heading", name="Searched Products")

    # Methods
    def check_searched_products_heading_visible(self) -> Self:
        expect(self.searched_products_heading).to_be_visible()
        return self

    def add_features_product_card_by_product_name(self, product_name: str) -> Self:
        self.features_product_card.filter(has_text=product_name).first.locator(
            ".productinfo"
        ).locator("text=Add to cart").click()
        return self

    def add_features_product_card_by_product_id(self, product_id: int) -> Self:
        self.features_product_card.filter(
            has=self.page.locator(f'a[data-product-id="{product_id}"]')
        ).locator(".productinfo").locator("text=Add to cart").click()
        return self

    def add_recommended_product_card_by_product_id(self, product_id: int) -> Self:
        self.recommended_product_card.filter(
            has=self.page.locator(f'a[data-product-id="{product_id}"]')
        ).locator(".productinfo").locator("text=Add to cart").click()
        return self

    def view_features_product_by_product_id(self, product_id: int) -> None:
        self.features_product_card.filter(
            has=self.page.locator(f'a[data-product-id="{product_id}"]')
        ).locator("text=View Product").click()

    def view_recommended_product_by_product_id(self, product_id: int) -> None:
        self.recommended_product_card.filter(
            has=self.page.locator(f'a[data-product-id="{product_id}"]')
        ).locator("text=View Product").click()

    # validate
    def check_recommended_heading_visible(self) -> Self:
        expect(self.recommended_items_heading).to_be_visible()
        return self

    # Shopping modal
    def click_view_cart(self) -> None:
        self.page.get_by_role("link", name="View Cart").click()

    def click_continue_shopping(self) -> Self:
        self.page.get_by_role("button", name="Continue Shopping").click()
        return self
