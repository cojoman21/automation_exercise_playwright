from typing import Self

from playwright.sync_api import Locator, Page, expect

from project.pages.base_page import BasePage
from project.pages.components.navigation_module import NavigationModule
from project.pages.components.subscription_section import SubscriptionSection


class CheckoutPage(BasePage, NavigationModule, SubscriptionSection):
    def __init__(self, page: Page):
        super().__init__(page)
        self.READY_LOCATOR: Locator = page.locator(".breadcrumbs").get_by_text(
            "Checkout"
        )
        self.ORDER_MSG_INPUT: Locator = page.locator("#ordermsg .form-control")
        self.PLACE_ORDER_BTN: Locator = page.get_by_role("link", name="Place Order")
        # ---> Delivery Address
        self.DELIVERY_ADDRESS: Locator = page.locator("#address_delivery")
        # ------> Sub-locators
        self.DELIVERY_NAME: Locator = self.DELIVERY_ADDRESS.locator("li").nth(1)
        self.DELIVERY_COMPANY: Locator = self.DELIVERY_ADDRESS.locator("li").nth(2)
        self.DELIVERY_ADDRESS1: Locator = self.DELIVERY_ADDRESS.locator("li").nth(3)
        self.DELIVERY_ADDRESS2: Locator = self.DELIVERY_ADDRESS.locator("li").nth(4)
        self.DELIVERY_CITY_STATE_ZIPCODE: Locator = self.DELIVERY_ADDRESS.locator(
            "li"
        ).nth(5)
        self.DELIVERY_COUNTRY: Locator = self.DELIVERY_ADDRESS.locator("li").nth(6)
        self.DELIVERY_PHONE_NUMBER: Locator = self.DELIVERY_ADDRESS.locator("li").nth(7)
        # ---> Billing Address
        self.BILLING_ADDRESS: Locator = page.locator("#address_invoice")
        # ------> Sub-locators
        self.BILLING_NAME: Locator = self.BILLING_ADDRESS.locator("li").nth(1)
        self.BILLING_COMPANY: Locator = self.BILLING_ADDRESS.locator("li").nth(2)
        self.BILLING_ADDRESS1: Locator = self.BILLING_ADDRESS.locator("li").nth(3)
        self.BILLING_ADDRESS2: Locator = self.BILLING_ADDRESS.locator("li").nth(4)
        self.BILLING_CITY_STATE_ZIPCODE: Locator = self.BILLING_ADDRESS.locator(
            "li"
        ).nth(5)
        self.BILLING_COUNTRY: Locator = self.BILLING_ADDRESS.locator("li").nth(6)
        self.BILLING_PHONE_NUMBER: Locator = self.BILLING_ADDRESS.locator("li").nth(7)

    def validate_delivery_address_is_correct(self, user_data: dict) -> Self:
        expect(self.DELIVERY_NAME).to_contain_text(user_data["first_name"])
        expect(self.DELIVERY_NAME).to_contain_text(user_data["last_name"])
        expect(self.DELIVERY_COMPANY).to_contain_text(user_data["company"])
        expect(self.DELIVERY_ADDRESS1).to_contain_text(user_data["address"])
        expect(self.DELIVERY_ADDRESS2).to_contain_text(user_data["address2"])
        expect(self.DELIVERY_CITY_STATE_ZIPCODE).to_contain_text(user_data["city"])
        expect(self.DELIVERY_CITY_STATE_ZIPCODE).to_contain_text(user_data["state"])
        expect(self.DELIVERY_CITY_STATE_ZIPCODE).to_contain_text(user_data["zipcode"])
        expect(self.DELIVERY_COUNTRY).to_contain_text(user_data["country"])
        expect(self.DELIVERY_PHONE_NUMBER).to_contain_text(
            str(user_data["mobile_number"])
        )
        return self

    def validate_billing_address_is_correct(self, user_data: dict) -> Self:
        expect(self.BILLING_NAME).to_contain_text(user_data["first_name"])
        expect(self.BILLING_NAME).to_contain_text(user_data["last_name"])
        expect(self.BILLING_COMPANY).to_contain_text(user_data["company"])
        expect(self.BILLING_ADDRESS1).to_contain_text(user_data["address"])
        expect(self.BILLING_ADDRESS2).to_contain_text(user_data["address2"])
        expect(self.BILLING_CITY_STATE_ZIPCODE).to_contain_text(user_data["city"])
        expect(self.BILLING_CITY_STATE_ZIPCODE).to_contain_text(user_data["state"])
        expect(self.BILLING_CITY_STATE_ZIPCODE).to_contain_text(user_data["zipcode"])
        expect(self.BILLING_COUNTRY).to_contain_text(user_data["country"])
        expect(self.BILLING_PHONE_NUMBER).to_contain_text(
            str(user_data["mobile_number"])
        )
        return self

    def add_order_comment(self, user_message: dict):
        self.ORDER_MSG_INPUT.fill(user_message["message"])

    def click_place_order(self) -> None:
        self.PLACE_ORDER_BTN.click()
