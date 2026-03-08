from playwright.sync_api import Page

from api_clients.user_client import UserClient


def test_CRUD_user(page: Page, user_client: UserClient, session_user, random_user):
    """Test: CRUD worflow for user API endpoint"""
    create_user_res = user_client.create_user(session_user)

    create_data = create_user_res.json()

    assert create_data["responseCode"] == 201
    assert create_data["message"] == "User created!"

    update_user_res = user_client.update_user(session_user, random_user)

    update_data = update_user_res.json()

    assert update_data["responseCode"] == 200
    assert update_data["message"] == "User updated!"

    get_user_res = user_client.get_user(session_user)

    get_data = get_user_res.json()

    assert get_data["responseCode"] == 200
    assert "user" in get_data
    assert get_data["user"]["email"] == session_user["email"]

    delete_user_res = user_client.delete_user(session_user)

    delete_data = delete_user_res.json()

    assert delete_data["responseCode"] == 200
    assert delete_data["message"] == "Account deleted!"
