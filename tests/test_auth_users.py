import pytest

from helpers import create_user_payload


class TestAuthUsers:
    def test_authorization_user_update_email(self, users_methods, auth_data):
        payload = create_user_payload()
        updated_email = {"email": payload["email"] }
        status_code, response_json = users_methods.update_data_user(auth_data, updated_email)

        assert status_code == 200 and  response_json["user"]["email"] == updated_email["email"]

    def test_authorization_user_update_name(self, users_methods, auth_data):
        payload = create_user_payload()
        updated_name = {"name": payload["name"] }
        status_code, response_json = users_methods.update_data_user(auth_data, updated_name)

        assert status_code == 200 and  response_json["user"]["name"] == updated_name["name"]

    def test_authorization_user_update_password(self, users_methods, auth_data):
        payload = create_user_payload()
        updated_password = {"password": payload["password"] }
        status_code, response_json = users_methods.update_data_user(auth_data, updated_password)
        expected_message = True

        assert status_code == 200 and response_json["success"] == expected_message

    @pytest.mark.parametrize("field_name", ["email", "password", "name"])
    def test_without_authorization_user_update_field(self, users_methods, field_name):
        payload = create_user_payload()
        updated_payload = {field_name: payload[field_name]}
        status_code, response_json = users_methods.update_data_user("",updated_payload)
        expected_message = "You should be authorised"

        assert status_code == 401 and response_json["message"] == expected_message

