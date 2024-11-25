import pytest
from methods.users_methods import UsersMethods
from methods.login_methods import LoginMethods
from methods.orders_methods import OrdersMethods
from helpers import create_user_payload


@pytest.fixture()
def users_methods():
    return UsersMethods()


@pytest.fixture()
def login_methods():
    return LoginMethods()


@pytest.fixture()
def orders_methods():
    return OrdersMethods()


@pytest.fixture()
def user_data(users_methods):
    payload = create_user_payload()
    status_code, response_json = users_methods.create_user(payload)
    password = payload["password"]
    email = response_json["user"]["email"]
    return email, password


@pytest.fixture()
def auth_data(user_data, login_methods, users_methods):
    email, password = user_data
    login_payload = {
        "email": email,
        "password": password
    }
    status_code, response_json = login_methods.login_user(login_payload)
    token = response_json.get("accessToken")
    yield token
    users_methods.delete_user(token)


@pytest.fixture()
def ingredients_details(orders_methods):
    status_code, response_json = orders_methods.get_orders()
    ingredient_id = response_json["data"][0]["_id"]
    return ingredient_id







