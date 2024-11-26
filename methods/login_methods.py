import requests
from data import BASE_URL, LOGIN_URL

class LoginMethods:
    def login_user(self, data):
        response = requests.post(f'{BASE_URL}{LOGIN_URL}', json=data)
        return response.status_code, response.json()