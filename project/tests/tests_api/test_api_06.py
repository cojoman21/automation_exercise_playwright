from playwright.sync_api import Page


def test_post_to_search_product_without_search_product_parameter(page: Page):
    response = page.request.post("https://automationexercise.com/api/searchProduct")

    data = response.json()

    assert data["responseCode"] == 400
    assert (
        data["message"]
        == "Bad request, search_product parameter is missing in POST request."
    )
