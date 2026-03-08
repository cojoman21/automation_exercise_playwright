from playwright.sync_api import Page


def test_get_all_brands_list(page: Page):
    response = page.request.get("https://automationexercise.com/api/brandsList")

    data = response.json()

    assert data["responseCode"] == 200

    assert "brands" in data
    assert len(data["brands"]) > 0

    print(f"Found {len(data['brands'])} brands.")
