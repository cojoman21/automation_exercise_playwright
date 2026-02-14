from playwright.sync_api import Page


def test_post_to_search_product(page: Page):
    response = page.request.post(
        "https://automationexercise.com/api/searchProduct",
        form={"search_product": "top"},
    )

    data = response.json()

    assert data["responseCode"] == 200
    assert "products" in data

    assert len(data["products"]) > 0

    first_product_name = data["products"][0]["name"].lower()
    assert "top" in first_product_name
