import time

from api_clients.base_client import BaseClient


class UserClient(BaseClient):
    def create_user(self, user_data: dict):
        form = {
            "name": user_data["name"],
            "email": user_data["email"],
            "password": user_data["password"],
            "title": "Mr",
            "birth_date": user_data["day"],
            "birth_month": user_data["month"],
            "birth_year": user_data["year"],
            "firstname": user_data["first_name"],
            "lastname": user_data["last_name"],
            "company": user_data["company"],
            "address1": user_data["address"],
            "address2": user_data["address2"],
            "country": user_data["country"],
            "zipcode": user_data["zipcode"],
            "state": user_data["state"],
            "city": user_data["city"],
            "mobile_number": user_data["mobile_number"],
        }
        return self.session.post(f"{self.base_url}/createAccount", form=form)

    def get_user(self, user_data: dict):
        params = {"email": user_data["email"]}
        return self.session.get(f"{self.base_url}/getUserDetailByEmail", params=params)

    def update_user(self, current_data: dict, new_data: dict, retries=3):
        form = {
            "name": current_data["name"],
            "email": current_data["email"],
            "password": current_data["password"],
            "title": "Mr",
            "birth_date": new_data["day"],
            "birth_month": new_data["month"],
            "birth_year": new_data["year"],
            "firstname": new_data["first_name"],
            "lastname": new_data["last_name"],
            "company": new_data["company"],
            "address1": new_data["address"],
            "address2": new_data["address2"],
            "country": new_data["country"],
            "zipcode": new_data["zipcode"],
            "state": new_data["state"],
            "city": new_data["city"],
            "mobile_number": new_data["mobile_number"],
        }
        for i in range(retries):
            update_res = self.session.put(f"{self.base_url}/updateAccount", form=form)
            if update_res.json()["responseCode"] == 200:
                return update_res
            if update_res.json()["responseCode"] == 409:
                time.sleep(2)
            else:
                raise RuntimeError(
                    f"Unexpected error {update_res.json()['responseCode']}: {update_res.json()['message']}"
                )
            raise TimeoutError(
                f"AutomationExercise.com was too busy to update {current_data['email']} after {retries} attempts."
            )

    def delete_user(self, user_data: dict, retries=3):
        form = {
            "email": user_data["email"],
            "password": user_data["password"],
        }

        for i in range(retries):
            delete_res = self.session.delete(
                f"{self.base_url}/deleteAccount", form=form
            )
            if delete_res.json()["responseCode"] == 200:
                return delete_res
            if delete_res.json()["responseCode"] == 409:
                time.sleep(2)
            else:
                raise RuntimeError(
                    f"Unexpected error {delete_res.json()['responseCode']}: {delete_res.json()['message']}"
                )
            raise TimeoutError(
                f"AutomationExercise.com was too busy to delete {user_data['email']} after {retries} attempts."
            )

    def verify_login(self, user_data: dict):
        form = {
            "email": user_data["email"],
            "password": user_data["password"],
        }
        return self.session.post(f"{self.base_url}/verifyLogin", form=form)
