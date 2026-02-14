# api_case_11, 12, 13, 14 (register (11), update (13), get details (14) & delete (12))

from playwright.sync_api import Page


def test_post_to_register_user_account(page: Page, session_user):
    response = page.request.post(
        "https://automationexercise.com/api/createAccount",
        form={
            "name": session_user["name"],
            "email": session_user["email"],
            "password": session_user["password"],
            "title": "Mr",
            "birth_date": session_user["day"],
            "birth_month": session_user["month"],
            "birth_year": session_user["year"],
            "firstname": session_user["first_name"],
            "lastname": session_user["last_name"],
            "company": session_user["company"],
            "address1": session_user["address"],
            "address2": session_user["address2"],
            "country": session_user["country"],
            "zipcode": session_user["zipcode"],
            "state": session_user["state"],
            "city": session_user["city"],
            "mobile_number": session_user["mobile_number"],
        },
    )

    data = response.json()

    assert data["responseCode"] == 201
    assert data["message"] == "User created!"


def test_put_to_update_user_account(page: Page, session_user, random_user):
    response = page.request.put(
        "https://automationexercise.com/api/updateAccount",
        form={
            "name": random_user["name"],
            "email": session_user["email"],
            "password": session_user["password"],
            "title": "Mrs",
            "birth_date": random_user["day"],
            "birth_month": random_user["month"],
            "birth_year": random_user["year"],
            "firstname": random_user["first_name"],
            "lastname": random_user["last_name"],
            "company": random_user["company"],
            "address1": random_user["address"],
            "address2": random_user["address2"],
            "country": random_user["country"],
            "zipcode": random_user["zipcode"],
            "state": random_user["state"],
            "city": random_user["city"],
            "mobile_number": random_user["mobile_number"],
        },
    )

    data = response.json()

    assert data["responseCode"] == 200
    assert data["message"] == "User updated!"


def test_get_user_account_detail_by_email(page: Page, session_user):
    response = page.request.get(
        "https://automationexercise.com/api/getUserDetailByEmail",
        params={"email": session_user["email"]},
    )

    data = response.json()

    assert data["responseCode"] == 200
    assert "user" in data
    assert data["user"]["email"] == session_user["email"]


def test_delete_method_to_delete_user_account(page: Page, session_user):
    response = page.request.delete(
        "https://automationexercise.com/api/deleteAccount",
        form={"email": session_user["email"], "password": session_user["password"]},
    )

    data = response.json()

    assert data["responseCode"] == 200
    assert data["message"] == "Account deleted!"
