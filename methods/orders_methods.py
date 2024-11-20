import requests
from data import BASE_URL, ORDERS_URL, INGREDIENT_URL, order_data, get_headers


class OrdersMethods:

    def get_orders(self):
        response = requests.get(f"{BASE_URL}{INGREDIENT_URL}")
        return response.status_code, response.json()

    def create_orders(self, data):
        order_data["ingredients"] = data
        response = requests.post(f'{BASE_URL}{ORDERS_URL}', json=data)
        return response.status_code, response.json()

    def create_orders_with_auth(self, token):
        headers = get_headers(token)
        response = requests.post(f'{BASE_URL}{ORDERS_URL}', headers=headers)
        return response.status_code, response.json()

    def get_orders_specific_users(self, token):
        headers = get_headers(token)
        response = requests.get(f'{BASE_URL}{ORDERS_URL}', headers=headers)
        return response.status_code, response.json()


