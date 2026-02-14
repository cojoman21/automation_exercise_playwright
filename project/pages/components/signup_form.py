from typing import Self

from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class SignupForm(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.READY_LOCATOR = page.get_by_role(
            "heading", name="Enter Account Information"
        )
        self.TITLE_RADIO_MR = page.locator("#id_gender1")
        self.TITLE_RADIO_MRS = page.locator("#id_gender2")
        self.NAME = page.locator("#name")
        self.EMAIL = page.locator("#email")
        self.PASSWORD = page.locator("#password")
        self.DAYS_DROPDOWN = page.locator("#days")
        self.MONTHS_DROPDOWN = page.locator("#months")
        self.YEARS_DROPDOWN = page.locator("#years")
        self.CHECKBOX_NEWSLETTER = page.locator("#newsletter")
        self.CHECKBOX_OFFERS = page.locator("#optin")
        self.FIRST_NAME = page.locator("#first_name")
        self.LAST_NAME = page.locator("#last_name")
        self.COMPANY = page.locator("#company")
        self.ADDRESS = page.locator("#address1")
        self.ADDRESS2 = page.locator("#address2")
        self.SELECT_COUNTRY = page.locator("#country")
        self.STATE = page.locator("#state")
        self.CITY = page.locator("#city")
        self.ZIPCODE = page.locator("#zipcode")
        self.MOBILE_NUMBER = page.locator("#mobile_number")
        self.CREATE_ACCOUNT_BUTTON = page.get_by_role("button", name="Create Account")

    def fill_form(self, user_data: dict) -> Self:
        expect(self.NAME).to_have_value(user_data["name"])
        expect(self.EMAIL).to_have_value(user_data["email"])

        if user_data["title"]:
            self.TITLE_RADIO_MR.check()
        else:
            self.TITLE_RADIO_MRS.check()

        self.PASSWORD.fill(user_data["password"])

        self.select_date_of_birth(user_data)

        if user_data["newsletter"]:
            self.CHECKBOX_NEWSLETTER.check()
        else:
            self.CHECKBOX_NEWSLETTER.uncheck()

        if user_data["offers"]:
            self.CHECKBOX_OFFERS.check()
        else:
            self.CHECKBOX_OFFERS.uncheck()

        self.FIRST_NAME.fill(user_data["first_name"])
        self.LAST_NAME.fill(user_data["last_name"])
        self.COMPANY.fill(user_data["company"])
        self.ADDRESS.fill(user_data["address"])
        self.ADDRESS2.fill(user_data["address2"])

        self.SELECT_COUNTRY.select_option(value=user_data["country"])

        self.STATE.fill(user_data["state"])
        self.CITY.fill(user_data["city"])
        self.ZIPCODE.fill(user_data["zipcode"])
        self.MOBILE_NUMBER.fill(user_data["mobile_number"])

        return self

    def select_date_of_birth(self, user_data: dict):
        self.DAYS_DROPDOWN.select_option(value=user_data["day"])
        self.MONTHS_DROPDOWN.select_option(value=user_data["month"])
        self.YEARS_DROPDOWN.select_option(value=user_data["year"])

    def submit(self):
        self.CREATE_ACCOUNT_BUTTON.click()
