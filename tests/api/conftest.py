import pytest
from faker import Faker

fake = Faker('ru')


@pytest.fixture(scope="session")
def base_url_api():
    return "http://31.59.114.45:8000/api/v1/users/"

    # Если вы планируете тестировать разные эндпоинты (users, posts, auth):
    # лучше оставить в base_url только корень http://31.59.114.45,а конкретный путь добавлять уже в самом запросе.



@pytest.fixture(scope="session")
def base_url_front():
    return "http://31.59.114.45:3000/sign_up"


@pytest.fixture
def user_data():
    return {
        "username": fake.name(),
        "email": fake.email(),
        "password": fake.password()
    }

@pytest.fixture
def user_boundary_conditions_email():
    return {
        "email_50_symbol": "very.long.and.specific.address.before.50@example.com",
        "email_51_symbol": "very.long.and.specific.address.exceeds.51@example.com",
        "email_1_symbol": "a",
        "email_0_symbol": ""
    }

@pytest.fixture
def user_data_negative_password_empty():
    return {
        "username": "testuser",
        "email": fake.email(),
        "password": fake.password(),
        "password_empty": ""
    }

@pytest.fixture
def user_data_negative_duplicate_username():
    return {
        "username": "testuser",
        "email": "unique_email@example.com",
        "password": "fake.password()"
    }

@pytest.fixture
def user_data_negative_lower_username():
    return {
        "username": "Testuser",
        "email": fake.email(),
        "password": fake.password()
    }