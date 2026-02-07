import allure
from data import AnswerText
from generators import generate_user_body_without_password
from methods.user_methods import UserMethods


class TestCreateUser:
    @allure.title('Тест на успешное создание пользователя')
    def test_create_user_successful(self, generate_user_data):
        user = UserMethods.create_user(generate_user_data[0])
        assert user.status_code == 200 and (user.json()['success'] == True)

    @allure.title('Тест на ошибку при создании двух одинаковых пользователей')
    def test_create_same_user(self, generate_user_data):
        UserMethods.create_user(generate_user_data[0])
        user_2 = UserMethods.create_user(generate_user_data[0])
        assert user_2.status_code == 403 and (user_2.json()['message'] == AnswerText.TEXT_403_SAME_USER)

    @allure.title('Тест ошибку при создании пользователя без передачи одного из обязательных полей')
    def test_create_user_without_password(self):
        user = UserMethods.create_user(generate_user_body_without_password())
        assert user.status_code == 403 and (user.json()['message'] == AnswerText.TEXT_403_WITHOUT_REQUIRED_FIELD)