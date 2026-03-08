from playwright.sync_api import Page


class BaseClient:
    def __init__(self, page: Page):
        self.base_url = "https://automationexercise.com/api"
        self.session = page.request
