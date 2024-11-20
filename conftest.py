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
def auth_data(user_data, login_methods):
    status_code, response_json = login_methods.login_user(user_data)
    token = response_json["accessToken"]
    return token


@pytest.fixture()
def user_token(users_methods):
    payload = create_user_payload()
    status_code, response_json = users_methods.create_user(payload)
    access_token = response_json["accessToken"]
    yield access_token
    users_methods.delete_user(access_token)


@pytest.fixture()
def ingredients_details(orders_methods):
    response_json = orders_methods.get_orders()
    ingredient_id = response_json["id"]
    return ingredient_id







