class Url:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    CREATE_USER_URL = f'{BASE_URL}/api/auth/register'
    AUTH_URL = f'{BASE_URL}/api/auth/login'
    DATA_ABOUT_USER_URL = f'{BASE_URL}/api/auth/user' # получить, обновить и удалить данные пользователя
    DATA_ABOUT_INGREDIENTS = f'{BASE_URL}/api/ingredients'
    ORDER_URL = f'{BASE_URL}/api/orders' # создать заказ и узнать заказ конкреного пользователя