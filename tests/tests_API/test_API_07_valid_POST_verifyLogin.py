from api_clients.user_client import UserClient


def test_post_to_verify_login_with_valid_details(
    user_client: UserClient, temp_user_client, random_user
):
    verify_login_res = user_client.verify_login(random_user)

    verify_login_data = verify_login_res.json()

    assert verify_login_data["responseCode"] == 200
    assert verify_login_data["message"] == "User exists!"
