from data import INCORRECT_DATA

class TestLoginUsers:
    def test_login_with_existing_user(self, login_methods, user_data):
        email, password = user_data
        login_data = {
            "email": email,
            "password": password
        }
        status_code, response_json = login_methods.login_user(login_data)
        expected_success = True

        assert status_code == 200 and response_json["success"] == expected_success

    def test_login_incorrect_email_password(self, login_methods):
        data = INCORRECT_DATA
        status_code, response_json = login_methods.login_user(data)
        expected_message = "email or password are incorrect"

        assert status_code == 401 and response_json["message"] == expected_message
