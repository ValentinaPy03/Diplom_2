import allure
from data import AnswerText
from methods.order_methods import OrderMethods


class TestGetOrderOfUser:
    @allure.title('Получение списка заказов авторизованного пользователя')
    def test_get_orders_of_auth_user(self, generate_user_data, create_ang_get_token):
        with allure.step('Создаем пользователя и получаем токен'):
            user_token = create_ang_get_token
        with allure.step('Получаем id двух ингредиентов'):
            ingredient = OrderMethods.get_id_ingredients(4)
            ingredient_2 = OrderMethods.get_id_ingredients(5)
        with allure.step('Формируем тело запроса на создание заказа'):
            list_ingredients = [ingredient, ingredient_2]
            body = {'ingredients': list_ingredients}
        with allure.step('Отправляем запрос на создание заказа'):
            OrderMethods.create_order(user_token, body)
        response = OrderMethods.get_orders_of_user(user_token)
        response_json = response.json()['orders']

        assert response.status_code == 200 and len(response_json) == 1

    @allure.title('Получение списка заказов авторизованного пользователя')
    def test_get_orders_of_unauth_user(self, generate_user_data):
        response = OrderMethods.get_orders_of_unauthorized_user()

        assert response.status_code == 401 and (response.json()['message'] == AnswerText.TEXT_401_UNAUTHORIZED_USER)