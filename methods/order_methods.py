
import requests
from urls import Url


class OrderMethods:
    @staticmethod
    def get_id_ingredients(number_ingredients):
        response = requests.get(Url.DATA_ABOUT_INGREDIENTS)
        response_data = response.json()['data']
        first_item = response_data[number_ingredients]
        id_ingredient = first_item['_id']
        return id_ingredient

    @staticmethod
    def create_order(token, body):
        return requests.post(Url.ORDER_URL, headers={'authorization': token} , json=body)

    @staticmethod
    def create_order_without_auth(body):
        return requests.post(Url.ORDER_URL, json=body)

    @staticmethod
    def get_orders_of_user(token):
        return requests.get(Url.ORDER_URL, headers={'authorization': token})

    @staticmethod
    def get_orders_of_unauthorized_user():
        return requests.get(Url.ORDER_URL)


