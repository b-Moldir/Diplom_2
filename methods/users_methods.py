import requests

from data import BASE_URL, USER_URL


class UsersMethods:
    def create_user(self, data):
        response = requests.post(f'{BASE_URL}{USER_URL}', json=data)
        return response.status_code, response.json()

