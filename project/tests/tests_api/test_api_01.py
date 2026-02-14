from playwright.sync_api import Page


def test_get_all_products_list(page: Page):
    response = page.request.get("https://automationexercise.com/api/productsList")

    assert response.status == 200

    data = response.json()

    assert "products" in data
    assert len(data["products"]) > 0
    print(f"Found {len(data['products'])} products!")
