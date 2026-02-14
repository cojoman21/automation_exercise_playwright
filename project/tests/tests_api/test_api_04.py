from playwright.sync_api import Page


def test_put_to_all_brands_list(page: Page):
    response = page.request.put("https://automationexercise.com/api/brandsList")

    data = response.json()
    assert data["responseCode"] == 405
    assert data["message"] == "This request method is not supported."
