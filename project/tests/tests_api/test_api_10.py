from playwright.sync_api import Page


def test_post_to_verify_login_with_invalid_details(page: Page, random_user):
    response = page.request.post(
        "https://automationexercise.com/api/verifyLogin",
        form={"email": random_user["email"], "password": "WrongPassword123"},
    )

    data = response.json()

    assert data["responseCode"] == 404
    assert data["message"] == "User not found!"
