from helpers import create_user_payload
from data import U_DATA


class TestCreateUser:
    def test_successfull_create_new_user(self, users_methods):
        user_data = create_user_payload()
        status_code, response_json = users_methods.create_user(user_data)

        assert status_code == 200 and response_json


    def test_create_registered_user(self, users_methods):
        user_data = create_user_payload()
        users_methods.create_user(user_data)
        status_code, response_json = users_methods(user_data)
        expected_message = "User already exists"

        assert status_code == 403 and response_json["message"] == expected_message

    def test_create_user_missing_fields(self, users_methods):
        user_data = U_DATA
        status_code, response_json = users_methods(user_data)
        expected_message = "Email, password and name are required fields"

        assert status_code == 403 and response_json["message"] == expected_message




