import pytest
from generators import generate_user_body
from methods.user_methods import UserMethods

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
def create_ang_get_token(generate_user_data):
    UserMethods.create_user(generate_user_data[0])
    user_token = UserMethods.user_token_by_user_data(generate_user_data[1], generate_user_data[2],
                                                     generate_user_data[3])
    return user_token



