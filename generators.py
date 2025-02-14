from faker import Faker

fake = Faker()

def generate_user_body():
    return {
    "email": fake.email(),
    "password": fake.password(),
    "name": fake.name()
    }

def generate_user_body_without_password():
    return {
    "email": fake.email(),
    "name": fake.name()
    }

def generate_incorrect_password():
    return fake.password()

def generate_incorrect_email():
    return fake.email()

def generate_update_user_body():
    return {
    "email": fake.email(),
    "name": fake.name()
    }

def generate_incorrect_ingredient_id():
    return fake.password()
