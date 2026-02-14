from typing import Self

from playwright.sync_api import Locator, Page, expect


class NavigationModule:
    page: Page

    @property
    def navigation_header(self) -> Locator:
        return self.page.locator("#header")

    def check_logged_in_as_user(self, user: dict):
        """Uses the "name" key from a dictionary"""
        expect(
            self.page.get_by_text(text=f"Logged in as {user['name']}")
        ).to_be_visible()

    # Clicks - Top navbar
    def click_on_home_button(self) -> None:
        self.page.locator("#header").get_by_role("link", name="Home")

    def click_on_products_button(self) -> None:
        self.page.locator("#header").get_by_role("link", name="Products").click()

    def click_on_cart_button(self) -> None:
        self.page.locator("#header").get_by_role("link", name="Cart").click()

    def click_on_signup_login_button(self) -> None:
        self.page.locator("#header").get_by_role("link", name="Signup / Login").click()

    def click_on_test_cases_button(self) -> None:
        self.page.locator("#header").get_by_role("link", name="Test Cases").click()

    def click_on_api_testing_button(self) -> None:
        self.page.locator("#header").get_by_role("link", name="API Testing").click()

    def click_on_video_tutorials_button(self) -> None:
        self.page.locator("#header").get_by_role("link", name="Video Tutorials").click()

    def click_on_contact_us_button(self) -> None:
        self.page.locator("#header").get_by_role("link", name="Contact us").click()

    def click_delete_account(self) -> None:
        self.page.locator("#header").get_by_role("link", name="Delete Account").click()

    def click_logout_button(self) -> None:
        self.page.locator("#header").get_by_role("link", name="Logout").click()

    # Clicks - Scroll arrow
    def click_scroll_up_arrow(self) -> Self:
        self.page.locator("#scrollUp").click()
        return self
