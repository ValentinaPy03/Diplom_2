class Url:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    CREATE_USER_URL = '/api/auth/register'
    AUTH_URL = '/api/auth/login'
    DATA_ABOUT_USER_URL = '/api/auth/user' # получить, обновить и удалить данные пользователя
    DATA_ABOUT_INGREDIENTS = '/api/ingredients'
    ORDER_URL = '/api/orders' # создать заказ и узнать заказ конкреного пользователя



class AnswerText:
    TEXT_403_SAME_USER = "User already exists"
    TEXT_403_WITHOUT_REQUIRED_FIELD = 'Email, password and name are required fields'
    TEXT_401_INCORRECT_LOGIN_OR_PASSWORD = 'email or password are incorrect'
    TEXT_401_UNAUTHORIZED_USER = 'You should be authorised'
    TEXT_400_CREATE_ORDER_WITHOUT_INGREDIENTS = 'Ingredient ids must be provided'
