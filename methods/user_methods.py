import requests
from urls import Url


class UserMethods:
    @staticmethod
    def create_user(body):
        return requests.post(Url.CREATE_USER_URL, json=body)

    @staticmethod
    def user_token_by_user_data(email, password, name):
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        response = requests.post(Url.AUTH_URL, json=payload)
        user_access_token = response.json()
        return user_access_token.get("accessToken")

    @staticmethod
    def delete_user(token):
        return requests.delete(Url.DATA_ABOUT_USER_URL, headers={'authorization': token})

    @staticmethod
    def log_user(email, password, name):
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        return requests.post(Url.AUTH_URL, json=payload)

    @staticmethod
    def update_data_user(token, new_data):
        return requests.patch(Url.DATA_ABOUT_USER_URL, headers={'authorization': token},
                              json=new_data)

    @staticmethod
    def update_data_unauthorized_user(new_data):
        return requests.patch(Url.DATA_ABOUT_USER_URL, json=new_data)




