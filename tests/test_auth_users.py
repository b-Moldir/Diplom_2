import pytest

from helpers import create_user_payload


class TestAuthUsers:
    @pytest.mark.parametrize("field_name", ["email", "password", "name"])
    def test_authorization_user_update_field(self, users_methods, auth_data, field_name):
        token = auth_data
        payload = create_user_payload()
        updated_payload = {field_name: payload[field_name]}
        status_code, response_json = users_methods.update_data_user(token, updated_payload)
        expected_message = "true"

        assert status_code == 200 and response_json["success"] == expected_message

    @pytest.mark.parametrize("field_name", ["email", "password", "name"])
    def test_without_authorization_user_update_field(self, users_methods, field_name):
        payload = create_user_payload()
        updated_payload = {field_name: payload[field_name]}
        status_code, response_json = users_methods.update_data_user(updated_payload)
        expected_message = "false"

        assert status_code == 401 and response_json["success"] == expected_message

