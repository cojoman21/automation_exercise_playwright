from data.test_data import EXISTING_USER
from playwright.sync_api import Page


def test_post_to_verify_login_with_valid_details(page: Page):
    response = page.request.post(
        "https://automationexercise.com/api/verifyLogin",
        form={"email": EXISTING_USER["email"], "password": EXISTING_USER["password"]},
    )

    data = response.json()

    assert data["responseCode"] == 200
    assert data["message"] == "User exists!"
