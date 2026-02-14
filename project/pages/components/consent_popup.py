from typing import Optional
from playwright.sync_api import Page, Locator, Error, TimeoutError


class ConsentPopup:
    # this doesn't need anything from BasePage
    
    
    # has its own init
    def __init__(self, page: Page, default_timeout_ms: int = 2000):
        self.page: Page = page
        self.default_timeout_ms = default_timeout_ms
        self.CONSENT_BUTTON_ROLE = "button[role='Consent']"
        self.CONSENT_BUTTON_ATTR = "button[aria-label='Consent']"
        
    # this is the main method, used to dismiss the popup
    # could also contain actions for other buttons, but I wanted to keep it basic
    def dismiss(self):
        # checks if either are present
        for selector in (self.CONSENT_BUTTON_ROLE, self.CONSENT_BUTTON_ATTR):
            # tries to wait for one of these to be visible and then tries to click
            try:
                self._locator(selector).wait_for(state="visible", timeout=self.default_timeout_ms)
                self._locator(selector).click(timeout=self.default_timeout_ms)
                # if it clicks, it ends here
                return True
            except TimeoutError:
                # otherwise, continue the loop
                continue
            except Error:
                # on error, continue the loop
                continue
        # if they are not present, return false
        return False
    
    # clicks on the Consent button
    def click(self, selector: Optional[str] = None):
        # selector 
        selector = selector or self.CONSENT_BUTTON_ROLE
        self._locator(selector).click(timeout=self.default_timeout_ms)

    def is_visible(self, selector: Optional[str] = None):
        selector = selector or self.CONSENT_BUTTON_ROLE
        # checks if the element is visible and returns self or False
        try:
            return self._locator(selector).is_visible()
        except Error:
            return False

    # Utils
    def _locator(self, locator):
        return self.page.locator(locator).first