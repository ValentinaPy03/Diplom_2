import pytest
from generators import generate_user_body, generate_user_body_without_password, generate_update_user_body
from methods.order_methods import OrderMethods
from methods.user_methods import UserMethods


@pytest.fixture()
def user_method():
    return UserMethods

@pytest.fixture()
def order_method():
    return OrderMethods

@pytest.fixture()
def generate_user_data():
    user_data = generate_user_body()
    email = user_data['email']
    password = user_data['password']
    name = user_data['name']
    yield [user_data, email, password, name]
    user_token = UserMethods().user_token_by_user_data(email, password, name)
    UserMethods().delete_user(user_token)

@pytest.fixture()
def generate_user_data_without_required_field():
    user_data = generate_user_body_without_password()
    email = user_data['email']
    name = user_data['name']
    yield [user_data, email, name]

@pytest.fixture()
def generate_update_user_data():
    user_data = generate_update_user_body()
    email = user_data['email']
    name = user_data['name']
    yield [user_data, email, name]



