import requests
from data import BASE_URL, ORDERS_URL, INGREDIENT_URL


class OrdersMethods:

    def get_orders(self):
        response = requests.get(f"{BASE_URL}{INGREDIENT_URL}")
        return response.status_code, response.json()
    def create_orders(self, data):
        data = {
            "ingredients": [{data}]
        }
        response = requests.post(f'{BASE_URL}{ORDERS_URL}', json=data)
        return response.status_code, response.json()