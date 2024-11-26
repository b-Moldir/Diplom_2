class TestGetOrdersSpecificUsers:
    def test_get_orders_authorization_user(self, orders_methods,auth_data):
        status_code, response_json = orders_methods.get_orders_specific_users(auth_data)
        expected_message = True

        assert status_code == 200 and response_json["success"] == expected_message

    def test_get_orders_without_authorization_user(self, orders_methods):
        status_code, response_json = orders_methods.get_orders_specific_users("")
        expected_message = False

        assert status_code == 401 and response_json["success"] == expected_message
