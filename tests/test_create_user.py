import allure

from data import AnswerText


class TestCreateUser:
    @allure.title('Тест на успешное создание пользователя')
    def test_create_user_successful(self, user_method, generate_user_data):
        user = user_method.create_user(generate_user_data[0])
        assert user.status_code == 200 and (user.json()['success'] == True)

    @allure.title('Тест на ошибку при создании двух одинаковых пользователей')
    def test_create_same_user(self, user_method, generate_user_data):
        user_method.create_user(generate_user_data[0])
        user_2 = user_method.create_user(generate_user_data[0])
        assert user_2.status_code == 403 and (user_2.json()['message'] == AnswerText.TEXT_403_SAME_USER)

    @allure.title('Тест ошибку при создании пользователя без передачи одного из обязательных полей')
    def test_create_user_without_password(self, user_method, generate_user_data_without_required_field):
        user = user_method.create_user(generate_user_data_without_required_field[0])
        assert user.status_code == 403 and (user.json()['message'] == AnswerText.TEXT_403_WITHOUT_REQUIRED_FIELD)