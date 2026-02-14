import re
from typing import Self

from playwright.sync_api import Locator, Page, expect

from project.pages.base_page import BasePage
from project.pages.components.navigation_module import NavigationModule
from project.pages.components.subscription_section import SubscriptionSection


class CartPage(BasePage, NavigationModule, SubscriptionSection):
    def __init__(self, page: Page):
        super().__init__(page)
        self.READY_LOCATOR: Locator = page.locator("#cart_items")
        # Cart
        self.CART_TABLE: Locator = page.locator("#cart_info_table")
        self.CART_ITEMS: Locator = self.CART_TABLE.locator('[id^="product-"]')
        self.PROCEED_TO_CHECKOUT: Locator = page.locator(".check_out")

        # Product card buttons and info
        self.CATEGORY: Locator = ".cart_description p"
        self.NAME: Locator = ".cart_description a"
        self.PRICE: Locator = ".cart_price"
        self.QUANTITY: Locator = ".cart_quantity"
        self.TOTAL: Locator = ".cart_total"
        self.DELETE: Locator = ".cart_delete.cart_quantity_delete"

        # Checkout modal
        self.REGISTER_OR_LOGIN_LINK: Locator = page.get_by_role(
            "link", name="Register / Login"
        )
        self.CONTINUE_ON_CART_BTN: Locator = page.get_by_role(
            "button", name="Continue On Cart"
        )

    def validate_cart_products_count_equal_to(self, expected_count: int) -> Self:
        expect(self.CART_TABLE.locator('[id^="product-"]')).to_have_count(
            expected_count
        )
        return self

    def validate_cart_product_quantity(
        self, product_id: int, expected_quantity: int
    ) -> Self:
        expect(self.get_product_card(product_id).locator(self.QUANTITY)).to_have_text(
            f"{expected_quantity}"
        )
        return self

    def get_product_card(self, product_id: int) -> Locator:
        return self.CART_TABLE.locator(f"tr#product-{product_id}")

    def delete_product_from_cart(self, product_id: int) -> Self:
        self.get_product_card(product_id).locator(
            f'[data-product-id="{product_id}"]'
        ).click()
        return self

    def get_product_price(self, product_id: int) -> int:
        price_text = self.get_product_card(product_id).locator(self.PRICE).inner_text()
        return int(re.sub(r"\D", "", price_text))

    def get_product_quantity(self, product_id: int) -> int:
        card = self.get_product_card(product_id)
        product_quantity = card.locator(self.QUANTITY).inner_text()
        return int("".join(filter(str.isdigit, product_quantity)))

    def get_product_total_price(self, product_id: int) -> int:
        total_text = self.get_product_card(product_id).locator(self.TOTAL).inner_text()
        return int(re.sub(r"\D", "", total_text))

    def verify_product_in_cart(self, product_id: int) -> Self:
        expect(self.get_product_card(product_id)).to_be_visible()
        return self

    def verify_products(self) -> Self:
        """
        Iterates through each product row in the cart, retrieves the price, quantity, and total for each product, and asserts that the total is equal to price multiplied by quantity.
        If there is a mismatch, it raises an assertion error with details about the specific row where the error occurred.
        """
        rows = self.CART_TABLE.locator('[id^="product-"]').all()

        for row in rows:
            # Get the specific ID for this row (e.g., "product-12")
            row_id_attr = row.get_attribute("id") or ""
            # Extract just the number (12)
            product_id = int(re.sub(r"\D", "", row_id_attr))

            # 3. Use your existing methods with the correct ID; use int to avoid floating-point issues
            price: int = int(self.get_product_price(product_id))
            quantity: int = int(self.get_product_quantity(product_id))
            total: int = int(self.get_product_total_price(product_id))

            # 4. Perform the math check
            assert price * quantity == total, (
                f"Math error at {row_id_attr}: {price} * {quantity} expected {price * quantity}, but got {total}"
            )
        return self

    # Click on proceed to checkout
    def click_on_proceed_to_checkout(self) -> None:
        self.PROCEED_TO_CHECKOUT.click()

    # Proceed to checkout modal

    def click_on_register_or_login(self) -> None:
        self.REGISTER_OR_LOGIN_LINK.click()

    def click_on_continue_on_cart(self) -> Self:
        self.CONTINUE_ON_CART_BTN.click()
        return self
