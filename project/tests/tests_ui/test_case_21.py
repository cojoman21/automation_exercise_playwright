from playwright.sync_api import Page

from project.pages.home_page import HomePage
from project.pages.product_details_page import ProductDetailsPage
from project.pages.products_page import ProductsPage


def test_add_review_on_product(page: Page, random_user):
    # 1. Launch browser
    # 2. Navigate to url 'http://automationexercise.com'
    home_page = HomePage(page)
    home_page.goto("https://www.automationexercise.com/")

    # 3. Click on 'Products' button
    home_page.click_on_products_button()

    # 4. Verify user is navigated to ALL PRODUCTS page successfully
    products_page = ProductsPage(page).wait_for_load()

    # 5. Click on 'View Product' button
    products_page.view_features_product_by_product_id(1)
    product_details_page = ProductDetailsPage(page).wait_for_load()

    # 6. Verify 'Write Your Review' is visible
    # 7. Enter name, email and review
    product_details_page.fill_review_form(random_user)

    # 8. Click 'Submit' button
    # 9. Verify success message 'Thank you for your review.'
    product_details_page.review_submit_and_wait_for_success_message()
