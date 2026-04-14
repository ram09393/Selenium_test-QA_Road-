import pytest
import requests
from faker import Faker
import allure

fake = Faker('ru_RU')


@allure.epic("Пользователи")
@allure.feature("Регистрация пользователя")
@allure.story("Успешная регистрация")
@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.registration
def test_user_positive_registration(user_data, base_url_api):
    response = requests.post(base_url_api, json=user_data)

    # print(response.status_code)
    # print(response.json())
    # print(response.text)
    # print(response.headers)
    # print(response.url)
    with allure.step("Шаг 1: Проверяем что статус кода ответа пришел верный "):
        # Генерирует исключение HTTPError, если статус-код ошибки 400 или 500
        response.raise_for_status()
        # Если статус не 201, тест упадет и покажет тело ответа с ошибкой
        assert response.status_code == 201, f"Ошибка! Статус: {response.status_code}, Ответ: {response.text}"

    with allure.step("Шаг 2: Проверяем что в теле ответа есть параметр id "):
        assert "id" in response.json()

    with allure.step("Шаг 3: Проверяем что в ответе API вернуло данные 'username', которые мы отправили в запросе."):
        assert response.json()["username"] == user_data["username"], "username в ответе не совпадает с отправленным"
    # print(response.json()["username"])
    with allure.step("Шаг 4: Проверяем что в ответе API вернуло данные 'email', которые мы отправили в запросе."):
        assert response.json()["email"] == user_data["email"], "email в ответе не совпадает с отправленным"
        # print(response.json()["email"])

        # Если вы специально отправляете плохие данные (например, пустой email), используйте такой подход:


def test_user_negative_registration_with_empty_email(base_url_api):
    empty_email = ""  # Портим данные из фикстуры

    response = requests.post(base_url_api)

    assert response.status_code == 400
    assert "email" in response.json(), "Сервер должен вернуть ошибку валидации поля email"


def test_user_negative_registration_email(base_url_api, user_data):
    empty_email = "rkomiakovmail.ru"  # Почта без @

    response = requests.post(base_url_api)

    # 1. Получаем JSON
    result = response.json()

    # 2. Проверяем, что поле email есть и в нем содержится символ @
    assert "email" in result, "Поле 'email' отсутствует в ответе сервера"
    assert "@" in result["email"], f"Email '{result['email']}' не содержит символ @"

    assert response.status_code == 400

    assert "email" in response.json(), "Сервер должен вернуть ошибку валидации поля email"


def test_user_negative_registration_boundary_conditions_email(base_url_api, user_boundary_conditions_email):
    response = requests.post(base_url_api)

    assert response.status_code == 403


def test_user_negative_registration(user_data_negative_password_empty, base_url_api):
    response = requests.post(base_url_api, json=user_data_negative_password_empty)

    assert response.status_code == 400, (f"Ошибка! Статус: {response.status_code}")
    assert "id" in response.json()
    assert response.json()["username"] == user_data_negative_password_empty[
        "username"], "username в ответе не совпадает с отправленным"
    assert response.json()["email"] == user_data_negative_password_empty[
        "email"], "email в ответе не совпадает с отправленным"
    assert response.json()["password"] == user_data_negative_password_empty[
        "password_empty"], "password в ответе не совпадает с отправленным"


def test_user_negative_registration_duplicate_username(user_data_negative_duplicate_username, base_url_api):
    response = requests.post(base_url_api, json=user_data_negative_duplicate_username)

    assert response.status_code == 400, f"Ошибка! Статус: {response.status_code}"

    assert response.json()["username"] == user_data_negative_duplicate_username[
        "username"], "username в ответе не совпадает с отправленным"


def test_user_negative_registration_lower_username(base_url_api, user_data_negative_lower_username):
    response = requests.post(base_url_api, json=user_data_negative_lower_username)

    assert response.status_code == 200, f"Ошибка! Статус: {response.status_code}"

    assert response.json()["username"] == user_data_negative_lower_username[
        "username"], "username в ответе не совпадает с отправленным"
