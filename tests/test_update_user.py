from data import AnswerText
import allure


class TestUpdateUser:
    @allure.title('Тест на обновление email и name авторизованного пользователя')
    def test_update_authorized_user(self, user_method, generate_user_data, generate_update_user_data):
        user_method.create_user(generate_user_data[0])
        user_method.log_user(generate_user_data[1], generate_user_data[2], generate_user_data[3])
        user_token = user_method.user_token_by_user_data(generate_user_data[1], generate_user_data[2],
                                                         generate_user_data[3])
        update_user = user_method.update_data_user(user_token, generate_update_user_data[0])
        assert update_user.status_code == 200 and (update_user.json()['user'] == {'email': generate_update_user_data[1],
                                                                                  "name": generate_update_user_data[2]})

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
                        update_user.json() == {"success": False, "message": "User with such email already exists"})

    @allure.title('Тест на обновление email и name неавторизованного пользователя')
    def test_update_unauthorized_user(self, user_method, generate_user_data, generate_update_user_data):
        user_method.create_user(generate_user_data[0])
        update_user = user_method.update_data_unauthorized_user(generate_update_user_data[0])
        assert update_user.status_code == 401 and (update_user.json()['message'] == AnswerText.TEXT_401_UNAUTHORIZED_USER)


