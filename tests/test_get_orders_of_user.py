import allure
from data import AnswerText


class TestGetOrderOfUser:
    @allure.title('Получение списка заказов авторизованного пользователя')
    def test_get_orders_of_auth_user(self, user_method, generate_user_data, order_method):
        with allure.step('Создаем пользователя и получаем токен'):
            user_method.create_user(generate_user_data[0])
            user_token = user_method.user_token_by_user_data(generate_user_data[1], generate_user_data[2],
                                                             generate_user_data[3])
        with allure.step('Получаем id двух ингредиентов'):
            ingredient = order_method.get_id_ingredients(4)
            ingredient_2 = order_method.get_id_ingredients(5)
        with allure.step('Формируем тело запроса на создание заказа'):
            list_ingredients = [ingredient, ingredient_2]
            body = {'ingredients': list_ingredients}
        with allure.step('Отправляем запрос на создание заказа'):
            order_method.create_order(user_token, body)
        response = order_method.get_orders_of_user(user_token)
        response_json = response.json()['orders']

        assert response.status_code == 200 and len(response_json) == 1

    @allure.title('Получение списка заказов авторизованного пользователя')
    def test_get_orders_of_unauth_user(self, user_method, generate_user_data, order_method):
        response = order_method.get_orders_of_unauthorized_user()

        assert response.status_code == 401 and (response.json()['message'] == AnswerText.TEXT_401_UNAUTHORIZED_USER)