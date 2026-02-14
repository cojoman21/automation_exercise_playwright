from playwright.sync_api import Page

from project.pages.home_page import HomePage
from project.pages.products_page import ProductsPage


def test_search_product(page: Page):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    # 3. Verify that home page is visible successfully
    home_page = HomePage(page)
    home_page.goto("https://automationexercise.com/")

    # 4. Click on 'Products' button
    home_page.click_on_products_button()

    # 5. Verify user is navigated to ALL PRODUCTS page successfully
    products_page = ProductsPage(page).wait_for_load()

    # 6. Enter product name in search input and click search button
    products_page.search_for("Men Tshirt")

    # 7. Verify 'SEARCHED PRODUCTS' is visible
    products_page.check_searched_products_heading_visible()

    # 8. Verify all the products related to search are visible
    products_page.validate_search_results("Men Tshirt")
