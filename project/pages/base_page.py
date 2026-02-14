from typing import Literal, Self

from playwright.sync_api import Locator, Page, expect

from project.pages.components.consent_popup import ConsentPopup


class BasePage:
    def __init__(self, page: Page, default_timeout_ms=10000):
        self.page: Page = page
        self.page.set_default_timeout(default_timeout_ms)
        self._default_timeout_ms = default_timeout_ms
        # READY_LOCATOR is the element that is used to identify if a page is ready
        self.READY_LOCATOR: Locator = page.locator("html")

    # This function is used to reach a url
    def goto(self, url) -> None:
        # here we reach the url
        self.page.goto(url)
        # here we use the consent_popup.py that we have created to handle the consent popup on the website
        ConsentPopup(self.page, default_timeout_ms=1500).dismiss()
        # here we use wait_for_load() that is declared below
        self.wait_for_load()

    # this is used to validate the visibility of the READY_LOCATOR
    def wait_for_load(self) -> Self:
        # checks if the page has the attribute READY_LOCATOR
        if not hasattr(self, "READY_LOCATOR"):
            # if READY_LOCATOR is missing, raise RuntimeError with message
            raise RuntimeError(
                f"{self.__class__.__name__} must define READY_LOCATOR to use goto()."
            )

        # if READY_LOCATOR attribute exists, check if it is visible
        self.assert_visible(self.READY_LOCATOR)
        # return self for chaining
        return self

    # ---------- Validation ----------
    # this is used to get the text inside an element (doesn't work for inputs)
    def get_text(self, locator: Locator) -> str:
        return locator.inner_text()

    # used to get the value inside inputs
    def get_value(self, locator: Locator) -> str:
        return locator.input_value()

    # used to check if an element is visible
    def assert_visible(self, locator: Locator):
        expect(locator).to_be_visible()

    # used to check if an element is visible now
    def is_currently_visible(self, locator: Locator) -> bool:
        return locator.is_visible()

    # used to verify if a checkbox is checked or unchecked
    def is_checked(self, locator: Locator) -> bool:
        return locator.is_checked()

    # ---------- Waits ----------
    # wait_for with custom predefined values
    def wait_for(
        self,
        locator: Locator,
        state: Literal["attached", "detached", "visible", "hidden"] = "visible",
    ) -> None:
        locator.wait_for(state=state)

    # ---------- Actions ---------
    def scroll_with_keys(
        self, key: Literal["ArrowUp", "ArrowDown", "PageDown", "Space", "Home", "End"]
    ) -> Self:
        # focus on element is needed in order to scroll with keys
        self.page.focus("body")
        # press the actual key
        self.page.keyboard.press(key)
        # return self for chaining
        return self

    def scroll_with_mouse_wheel(self, pixels: int) -> Self:
        self.page.mouse.wheel(0, pixels)
        return self

    def scroll_into_view(self, locator):
        locator.scroll_into_view_if_needed()

    def scroll_with_mouse_until_visible(self, locator: Locator):
        while not self.is_in_viewport(locator):
            self.page.mouse.wheel(0, 600)
            self.page.wait_for_timeout(300)

    # ---------- Utils ---------
    # check if element is in view; contains javascript code
    def is_in_viewport(self, locator: Locator) -> bool:
        # This evaluates the element's position relative to the screen
        return locator.evaluate("""
            element => {
                const rect = element.getBoundingClientRect();
                return (
                    rect.top >= 0 &&
                    rect.left >= 0 &&
                    rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
                    rect.right <= (window.innerWidth || document.documentElement.clientWidth)
                );
            }
        """)
