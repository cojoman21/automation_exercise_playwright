from typing import Self

from playwright.sync_api import Locator, Page

from project.pages.base_page import BasePage
from project.pages.components.navigation_module import NavigationModule
from project.pages.components.subscription_section import SubscriptionSection


class PaymentPage(BasePage, NavigationModule, SubscriptionSection):
    def __init__(self, page: Page):
        super().__init__(page)
        self.READY_LOCATOR: Locator = page.get_by_role("heading", name="Payment")
        self.PAYMENT_FORM: Locator = page.locator("#payment-form")
        self.CARD_NAME_INPUT: Locator = self.PAYMENT_FORM.get_by_test_id("name-on-card")
        self.CARD_NUMBER_INPUT: Locator = self.PAYMENT_FORM.get_by_test_id(
            "card-number"
        )
        self.CARD_CVC_INPUT: Locator = self.PAYMENT_FORM.get_by_test_id("cvc")
        self.CARD_MONTH_INPUT: Locator = self.PAYMENT_FORM.get_by_test_id(
            "expiry-month"
        )
        self.CARD_YEAR_INPUT: Locator = self.PAYMENT_FORM.get_by_test_id("expiry-year")
        self.PAY_AND_CONFIRM_ORDER_BTN: Locator = self.PAYMENT_FORM.get_by_role(
            "button", name="Pay and Confirm Order"
        )
        self.SUCCESS_MSG = self.PAYMENT_FORM.locator("div.alert-success")

    def fill_payment_form(self, user_data: dict) -> Self:
        self.CARD_NAME_INPUT.fill(user_data["name"])
        self.CARD_NUMBER_INPUT.fill(user_data["card_number"])
        self.CARD_CVC_INPUT.fill(user_data["card_cvc"])
        self.CARD_MONTH_INPUT.fill(user_data["card_month"])
        self.CARD_YEAR_INPUT.fill(user_data["card_year"])
        return self

    def submit_payment_form(self) -> None:
        self.PAY_AND_CONFIRM_ORDER_BTN.click()
