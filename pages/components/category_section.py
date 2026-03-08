from typing import Literal, Self

from playwright.sync_api import Locator, Page, expect


class CategorySection:
    page: Page

    @property
    def category_panel(self) -> Locator:
        return self.page.locator("#accordian")

    def expand_category(
        self, category_name: Literal["#Women", "#Men", "#Kids"]
    ) -> Self:
        self.category_panel.locator(f'a[href="{category_name}"]').click()
        return self

    def click_dress(self) -> Self:
        self.page.locator("#accordian").get_by_role("link", name="Dress").click()
        return self

    def click_tops(self) -> Self:
        self.page.locator("#accordian").get_by_role("link", name="Tops").click()
        return self

    def click_saree(self) -> Self:
        self.page.locator("#accordian").get_by_role("link", name="Saree").click()
        return self

    def click_tshirts(self) -> Self:
        self.page.locator("#accordian").get_by_role("link", name="Tshirts").click()
        return self

    def click_jeans(self) -> Self:
        self.page.locator("#accordian").get_by_role("link", name="Jeans").click()
        return self

    def click_tops_and_shirts(self) -> Self:
        self.page.locator("#accordian").get_by_role(
            "link", name="Tops & Shirts"
        ).click()
        return self

    def check_selected_category_is_visible(
        self,
        category_name: Literal["Women", "Men", "Kids"],
        subcategory_name: Literal[
            "Dress", "Tops", "Saree", "Tshirts", "Jeans", "Tops & Shirts"
        ],
    ) -> Self:
        expect(
            self.page.get_by_role(
                "heading", name=f"{category_name} - {subcategory_name} Products"
            )
        ).to_be_visible()
        return self
