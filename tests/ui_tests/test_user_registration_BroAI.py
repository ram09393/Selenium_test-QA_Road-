import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker

fake = Faker('ru_RU')


def test_registration(browser, wait):
    email = fake.ascii_free_email()
    username = fake.first_name()
    password = fake.password(length=10)

    wait.until(EC.visibility_of_element_located((By.ID, "email"))).send_keys(email)
    browser.find_element(By.ID, "username").send_keys(username)
    browser.find_element(By.ID, "username").send_keys(password)
    browser.find_element(By.ID, "username").send_keys(password)

    print(email)
    print(username)

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    wait.until(EC.url_to_be("http://31.59.114.45:3000/login"))

    assert browser.current_url == "http://31.59.114.45:3000/login"

    api_url = "http://31.59.114.45:8000/api/v1"

    auth_response = requests.post(f"{api_url}/jwt/create/", json={
        "email": email,
        "password": password

    })
    token = auth_response.json()["access"]
    print(auth_response.json()["access"])

    me_response = requests.get(
        f"{api_url}/users/me",
        headers={"Authorization": f"Bearer {token}"}
    )
    print(me_response)

    get_user_data = me_response.json()
    assert get_user_data["email"] == email
    assert get_user_data["username"] == username
