from data import AnswerText
import allure
from generators import generate_update_user_body


class TestUpdateUser:
    @allure.title('Тест на обновление email и name авторизованного пользователя')
    def test_update_authorized_user(self, user_method, generate_user_data):
        user_method.create_user(generate_user_data[0])
        user_method.log_user(generate_user_data[1], generate_user_data[2], generate_user_data[3])
        user_token = user_method.user_token_by_user_data(generate_user_data[1], generate_user_data[2],
                                                         generate_user_data[3])
        body = generate_update_user_body()
        update_user = user_method.update_data_user(user_token, body)
        assert update_user.status_code == 200 and (update_user.json()['user'] == {'email': body['email'],
                                                                                  "name": body['name']})

    @allure.title('Тест на передачу через ручку обновления уже существующего email')
    def test_update_already_existed_email(self, user_method, generate_user_data):
        user_method.create_user(generate_user_data[0])
        user_method.log_user(generate_user_data[1], generate_user_data[2], generate_user_data[3])
        user_token = user_method.user_token_by_user_data(generate_user_data[1], generate_user_data[2],
                                                         generate_user_data[3])
        with allure.step('В переменную с новыми данными передать email, который уже используется'):
            update_body ={'email' : generate_user_data[1]}
            update_user = user_method.update_data_user(user_token, update_body)
            assert update_user.status_code == 403 and (
                        update_user.json() == AnswerText.TEXT_403_EMAIL_ALREADY_EXIST)

    @allure.title('Тест на обновление email и name неавторизованного пользователя')
    def test_update_unauthorized_user(self, user_method, generate_user_data):
        user_method.create_user(generate_user_data[0])
        body = generate_update_user_body()
        update_user = user_method.update_data_unauthorized_user(body)
        assert update_user.status_code == 401 and (update_user.json()['message'] == AnswerText.TEXT_401_UNAUTHORIZED_USER)


