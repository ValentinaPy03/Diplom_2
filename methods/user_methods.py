import requests
from data import Url
import allure

class UserMethods:
    @staticmethod
    @allure.title('Дергаем ручку на создание пользователя')
    def create_user(body):
        return requests.post(f'{Url.BASE_URL}{Url.CREATE_USER_URL}', json=body)

    @staticmethod
    @allure.title('Узнать токен зарегистрированного пользователя')
    def user_token_by_user_data(email, password, name):
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        response = requests.post(f'{Url.BASE_URL}{Url.AUTH_URL}', json=payload)
        user_access_token = response.json()
        return user_access_token.get("accessToken")

    @staticmethod
    @allure.title('Дернуть ручку на удаление пользователя')
    def delete_user(token):
        return requests.delete(f'{Url.BASE_URL}{Url.DATA_ABOUT_USER_URL}', headers={'authorization': token})

    @staticmethod
    @allure.title('Дернуть ручку на авторизацию пользователя')
    def log_user(email, password, name):
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        return requests.post(f'{Url.BASE_URL}{Url.AUTH_URL}', json=payload)

    @staticmethod
    @allure.title('Дернуть ручку на обновление данныз авторизованного пользователя')
    def update_data_user(token, new_data):
        return requests.patch(f'{Url.BASE_URL}{Url.DATA_ABOUT_USER_URL}', headers={'authorization': token},
                              json=new_data)

    @staticmethod
    @allure.title('Дернуть ручку на обновление неавторизованного пользователя (без передачи токена)')
    def update_data_unauthorized_user(new_data):
        return requests.patch(f'{Url.BASE_URL}{Url.DATA_ABOUT_USER_URL}', json=new_data)




