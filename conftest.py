import pytest
from methods.users_methods import UsersMethods
from methods.login_methods import LoginMethods
from helpers import create_user_payload


@pytest.fixture()
def users_methods():
    return UsersMethods


@pytest.fixture()
def login_methods():
    return LoginMethods


@pytest.fixture()
def user_data(users_methods):
    payload = create_user_payload()
    response_json = users_methods.create_user(payload)
    email = response_json["user"]["email"]
    name = response_json["user"]["name"]
    return email, name

