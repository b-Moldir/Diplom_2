class TestLoginUsers:
    def test_login_with_existing_user(self, login_methods, user_data):
        email, name = user_data
        status_code, response_json = login_methods(email,name)
