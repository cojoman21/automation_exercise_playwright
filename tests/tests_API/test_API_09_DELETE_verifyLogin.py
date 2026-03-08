from playwright.sync_api import Page


def test_delete_to_verify_login(page: Page):
    response = page.request.delete("https://automationexercise.com/api/verifyLogin")

    data = response.json()

    assert data["responseCode"] == 405
    assert data["message"] == "This request method is not supported."
