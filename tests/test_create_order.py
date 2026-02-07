import allure
from data import AnswerText
from generators import generate_incorrect_ingredient_id
from methods.order_methods import OrderMethods


class TestCreateOrder:
    @allure.title('Тест на созадние заказа с ингредиентами через авторизованного пользователя')
    def test_successful_create_order(self, generate_user_data, create_ang_get_token):
        with allure.step('Создаем пользователя и получаем токен'):
            user_token = create_ang_get_token
        with allure.step('Получаем id двух ингредиентов'):
            ingredient = OrderMethods.get_id_ingredients(0)
            ingredient_2 = OrderMethods.get_id_ingredients(1)
        with allure.step('Формируем тело запроса на создание заказа'):
            list_ingredients = [ingredient, ingredient_2]
            body = {'ingredients': list_ingredients}
        with allure.step('Отправляем запрос на создание заказа'):
            response = OrderMethods.create_order(user_token, body)

        assert response.status_code == 200 and ('name' in response.json())

    @allure.title('Тест на создание заказа с ингредиентами через неавторизованного пользователя')
    def test_create_order_unauthorized_user(self):
        with allure.step('Получаем id двух ингредиентов'):
            ingredient = OrderMethods.get_id_ingredients(0)
            ingredient_2 = OrderMethods.get_id_ingredients(1)
        with allure.step('Формируем тело запроса на создание заказа'):
            list_ingredients = [ingredient, ingredient_2]
            body = {'ingredients': list_ingredients}
        with allure.step('Отправляем запрос на создание заказа'):
            response = OrderMethods.create_order_without_auth(body)

        assert response.status_code == 401

    @allure.title('Тест на создание заказа без ингредиентов')
    def test_create_order_without_ingredients(self, generate_user_data, create_ang_get_token):
        with allure.step('Создаем пользователя и получаем токен'):
            user_token = create_ang_get_token
        with allure.step('Формируем тело запроса на создание заказа'):
            list_ingredients = []
            body = {'ingredients': list_ingredients}
        with allure.step('Отправляем запрос на создание заказа'):
            response = OrderMethods.create_order(user_token, body)

        assert response.status_code == 400 and (
                    response.json()['message'] == AnswerText.TEXT_400_CREATE_ORDER_WITHOUT_INGREDIENTS)

    @allure.title('Тест на создание заказа с невалидным хешом ингредиентов')
    def test_create_order_with_incorrect_ingredients_id(self, generate_user_data, create_ang_get_token):
        with allure.step('Создаем пользователя и авторизируемся'):
            with allure.step('Создаем пользователя и получаем токен'):
                user_token = create_ang_get_token
        with allure.step('Формируем тело запроса на создание заказа, используя невалидный хеш'):
            ingredient = generate_incorrect_ingredient_id()
            body = {'ingredients': ingredient}
        with allure.step('Отправляем запрос на создание заказа'):
            response = OrderMethods.create_order(user_token, body)

        assert response.status_code == 500




