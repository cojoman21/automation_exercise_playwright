from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.product_details_page import ProductDetailsPage
from pages.products_page import ProductsPage


def test_verify_all_products_and_product_detail_page(page: Page):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    # 3. Verify that home page is visible successfully
    home_page = HomePage(page)
    home_page.goto("https://automationexercise.com/")

    # 4. Click on 'Products' button
    home_page.click_on_products_button()

    # 6. The products list is visible
    # 5. Verify user is navigated to ALL PRODUCTS page successfully
    products_page = ProductsPage(page).wait_for_load()

    # 7. Click on 'View Product' of first product
    id = 1
    products_page.view_features_product_by_product_id(id)

    # 8. User is landed to product detail page
    product_details_page = ProductDetailsPage(page).wait_for_load()

    # 9. Verify that detail detail is visible: product name, category, price, availability, condition, brand
    product_details_page.validate_product_details_are_visible()
