from data import ORDERS_DATA
class TestCreateOrders:
    def test_successful_create_orders_with_ingredients(self, orders_methods, ingredients_details):
        ingredient_id = ingredients_details
        status_code, response_json = orders_methods.create_orders(ingredient_id)
        expected_message = "true"

        assert status_code == 200 and response_json["success"] == expected_message

    def test_create_orders_without_ingredients(self, orders_methods):
        status_code, response_json = orders_methods.create_orders()
        expected_message = "Ingredient ids must be provided"

        assert status_code == 400 and response_json["message"] == expected_message

    def test_create_orders_incorrect_hash(self, orders_methods):
        data = {
            "ingredients": ["60d3b41abdacab0023c6"]
        }
        status_code, response_json = orders_methods.create_orders(data)
        expected_message = "One or more ids provided are incorrect"

        assert status_code == 400 and response_json["message"] == expected_message

