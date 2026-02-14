from playwright.sync_api import Page


def test_post_to_verify_login_without_email_parameter(page: Page, random_user):
    response = page.request.post(
        "https://automationexercise.com/api/verifyLogin",
        form={"password": random_user["password"]},
    )

    data = response.json()

    assert data["responseCode"] == 400
    assert (
        data["message"]
        == "Bad request, email or password parameter is missing in POST request."
    )
