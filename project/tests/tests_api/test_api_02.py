from playwright.sync_api import Page


def test_post_to_all_products_list(page: Page):
    response = page.request.post("https://automationexercise.com/api/productsList")

    data = response.json()

    assert data["responseCode"] == 405
    assert data["message"] == "This request method is not supported."
