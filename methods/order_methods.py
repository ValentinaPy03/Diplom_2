import allure
import requests
from data import Url


class OrderMethods:
    @staticmethod
    @allure.title('Получить id ингредиента из базы данных')
    def get_id_ingredients(number_ingredients):
        response = requests.get(f'{Url.BASE_URL}{Url.DATA_ABOUT_INGREDIENTS}')
        response_data = response.json()['data']
        first_item = response_data[number_ingredients]
        id_ingredient = first_item['_id']
        return id_ingredient

    @staticmethod
    @allure.title('Дернуть ручку на создание заказа через авторизованного пользователя')
    def create_order(token, body):
        return requests.post(f'{Url.BASE_URL}{Url.ORDER_URL}', headers={'authorization': token} , json=body)

    @staticmethod
    @allure.title('Дернуть ручку на создание заказа без авторизации')
    def create_order_without_auth(body):
        return requests.post(f'{Url.BASE_URL}{Url.ORDER_URL}', json=body)

    @staticmethod
    @allure.title('Дернуть ручку на получение списка заказов через авторизованного пользователя')
    def get_orders_of_user(token):
        return requests.get(f'{Url.BASE_URL}{Url.ORDER_URL}', headers={'authorization': token})

    @staticmethod
    @allure.title('Дернуть ручку на получение списка заказов без авторизации')
    def get_orders_of_unauthorized_user():
        return requests.get(f'{Url.BASE_URL}{Url.ORDER_URL}')


