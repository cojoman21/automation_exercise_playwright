from typing import Literal, Self

from playwright.sync_api import Locator, Page, expect


class BrandsSection:
    page: Page

    @property
    def brands_panel(self) -> Locator:
        return self.page.locator(".brands-name")

    def click_brand(
        self,
        brand_name: Literal[
            "Polo",
            "H&M",
            "Madame",
            "Mast & Harbour",
            "Babyhug",
            "Allen Solly Junior",
            "Kookie Kids",
            "Biba",
        ],
    ) -> Self:
        self.brands_panel.get_by_role("link", name=brand_name).click()
        return self

    def check_selected_brand_is_visible(
        self,
        brand_name: Literal[
            "Polo",
            "H&M",
            "Madame",
            "Mast & Harbour",
            "Babyhug",
            "Allen Solly Junior",
            "Kookie Kids",
            "Biba",
        ],
    ) -> Self:
        expect(
            self.page.get_by_role("heading", name=f"Brand - {brand_name} Products")
        ).to_be_visible()
        return self
