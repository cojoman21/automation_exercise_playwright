from api_clients.user_client import UserClient


def test_POST_verifyLogin_with_invalid_details(user_client: UserClient, random_user):
    """Test: POST to /verifyLogin using invalid data"""
    verify_login_res = user_client.verify_login(random_user)

    verify_login_data = verify_login_res.json()

    assert verify_login_data["responseCode"] == 404
    assert verify_login_data["message"] == "User not found!"
