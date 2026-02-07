import allure
from data import AnswerText
from generators import generate_incorrect_password, generate_incorrect_email
from methods.user_methods import UserMethods


class TestLoginUser:
    @allure.title('Тест на успешную авторизацию')
    def test_successful_auth(self, generate_user_data, create_ang_get_token):
        UserMethods.create_user(generate_user_data[0])
        user = UserMethods.log_user(generate_user_data[1], generate_user_data[2], generate_user_data[3])
        assert user.status_code == 200 and (user.json()['success'] == True)

    @allure.title('Тест на авторизацию с некорректным password')
    def test_auth_with_non_existent_password(self, generate_user_data):
        UserMethods.create_user(generate_user_data[0])
        user = UserMethods.log_user(generate_user_data[1], generate_incorrect_password(), generate_user_data[3])
        assert user.status_code == 401 and (user.json()['message'] == AnswerText.TEXT_401_INCORRECT_LOGIN_OR_PASSWORD)

    @allure.title('Тест на авторизацию с некорректным email')
    def test_auth_with_non_existent_email(self, generate_user_data):
        UserMethods.create_user(generate_user_data[0])
        user = UserMethods.log_user(generate_incorrect_email(), generate_user_data[2], generate_user_data[3])
        assert user.status_code == 401 and (user.json()['message'] == AnswerText.TEXT_401_INCORRECT_LOGIN_OR_PASSWORD)