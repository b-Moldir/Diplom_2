import pytest
from methods.users_methods import UsersMethods
from methods.orders_methods import OrdersMethods


@pytest.fixture()
def users_methods():
    return UsersMethods


@pytest.fixture()
def orders_methods():
    return OrdersMethods


