import re
from typing import Self

from playwright.sync_api import Locator, Page, expect

from project.pages.base_page import BasePage
from project.pages.components.brands_section import BrandsSection
from project.pages.components.category_section import CategorySection
from project.pages.components.navigation_module import NavigationModule
from project.pages.components.products_section import ProductsSection
from project.pages.components.subscription_section import SubscriptionSection


class ProductDetailsPage(
    BasePage,
    NavigationModule,
    SubscriptionSection,
    CategorySection,
    BrandsSection,
    ProductsSection,
):
    def __init__(self, page: Page):
        super().__init__(page)
        self.READY_LOCATOR: Locator = page.locator(".product-details")
        # product info
        self.PRODUCT_INFO: Locator = page.locator(".product-information")
        self.PRODUCT_NAME: Locator = self.PRODUCT_INFO.locator("h2")
        self.PRODUCT_CATEGORY: Locator = self.PRODUCT_INFO.locator("p").first
        self.PRODUCT_PRICE: Locator = self.PRODUCT_INFO.get_by_text(
            re.compile(r"Rs\. \d+")
        )
        self.PRODUCT_QUANTITY: Locator = self.PRODUCT_INFO.locator("#quantity")
        self.ADD_TO_CART_BTN: Locator = self.PRODUCT_INFO.get_by_role(
            "button", name="Add to cart"
        )
        # extra
        self.PRODUCT_AVAILABILITY: Locator = self.PRODUCT_INFO.get_by_text(
            re.compile(r"Availability\:")
        )
        self.PRODUCT_CONDITION: Locator = self.PRODUCT_INFO.get_by_text(
            re.compile(r"Condition\:")
        )
        self.PRODUCT_BRAND: Locator = self.PRODUCT_INFO.get_by_text(
            re.compile(r"Brand\:")
        )
        # review main container
        self.REVIEW_CONTAINER: Locator = page.locator(".shop-details-tab")
        # review sublocators
        self.REVIEW_FORM: Locator = page.locator("#review-form")
        self.REVIEW_NAME_INPUT: Locator = self.REVIEW_FORM.get_by_placeholder(
            "Your Name"
        )
        self.REVIEW_EMAIL_INPUT: Locator = self.REVIEW_FORM.get_by_placeholder(
            "Email Address"
        )
        self.REVIEW_MESSAGE_INPUT: Locator = self.REVIEW_FORM.get_by_placeholder(
            "Add Review Here!"
        )
        self.REVIEW_SUBMIT_BTN: Locator = self.REVIEW_FORM.get_by_role(
            "button", name="Submit"
        )
        self.REVIEW_SUCCESS_MSG = self.REVIEW_FORM.locator(".alert-success")
        # shopping modal
        self.CONTINUE_SHOPPING_BUTTON: Locator = page.get_by_role(
            "button", name="Continue Shopping"
        )
        self.VIEW_CART: Locator = page.get_by_role("link", name="View Cart")

    def validate_product_details_are_visible(self) -> Self:
        expect(self.PRODUCT_NAME).to_be_visible()
        expect(self.PRODUCT_CATEGORY).to_be_visible()
        expect(self.PRODUCT_PRICE).to_be_visible()
        expect(self.PRODUCT_QUANTITY).to_be_visible()
        expect(self.ADD_TO_CART_BTN).to_be_visible()
        expect(self.PRODUCT_AVAILABILITY).to_be_visible()
        expect(self.PRODUCT_CONDITION).to_be_visible()
        expect(self.PRODUCT_BRAND).to_be_visible()
        return self

    def set_quantity(self, quantity: int) -> Self:
        self.PRODUCT_QUANTITY.clear()
        self.PRODUCT_QUANTITY.fill(str(quantity))
        return self

    def fill_review_form(self, data: dict) -> Self:
        self.REVIEW_NAME_INPUT.fill(data["name"])
        self.REVIEW_EMAIL_INPUT.fill(data["email"])
        self.REVIEW_MESSAGE_INPUT.fill(data["review_message"])
        return self

    def review_submit_and_wait_for_success_message(self) -> Self:
        self.REVIEW_SUBMIT_BTN.click()
        # self.REVIEW_SUCCESS_MSG.wait_for(state="attached", timeout=5000)
        expect(self.REVIEW_SUCCESS_MSG).to_be_visible()
        return self

    def click_add_to_cart(self) -> Self:
        self.ADD_TO_CART_BTN.click()
        return self
