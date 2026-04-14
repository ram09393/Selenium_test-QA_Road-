import pytest
from playwright.sync_api import Browser, sync_playwright
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from faker import Faker

fake = Faker('ru')


@pytest.fixture
def page(browser_pw: Browser, base_url):
    page = browser_pw.new_page()
    page.goto(base_url)

    yield page

    page.close()


@pytest.fixture
def browser_pw():
    with sync_playwright() as playwright:
        browser_pw = playwright.chromium.launch(
            headless=False,
            slow_mo=5000
        )
        yield browser_pw
        browser_pw.close()


@pytest.fixture
def context_with_tracing(browser_pw, request):
    context = browser_pw.new_context()
    context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )

    yield context

    trace_file = f"traces/{request.node.name}.zip"
    context.tracing.stop(path=trace_file)

    context.close()


@pytest.fixture
def page_with_tracing(context_with_tracing, base_url):
    page = context_with_tracing.new_page()
    page.goto(base_url)

    yield page

    page.close()


@pytest.fixture
def browser(base_url):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--windows-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.get(base_url)

    yield driver

    driver.quit()


@pytest.fixture(scope="session")
def base_url():
    return "https://lms.threadqa.ru/xpath-practice-hub"



@pytest.fixture
def wait(browser):
    return WebDriverWait(browser, 10)


@pytest.fixture
def user_names():
    first_name = fake.name()
    second_name = fake.name_female()
    return {
        "first_name": first_name,
        "second_name": second_name,
        "placeholder": "Введите ваше имя"
    }


@pytest.fixture(params=[
    {"email": fake.email(), "username": fake.name_male(), "password": fake.password()},
    {"email": "test2@mail.ru", "username": "user", "password": "pass2"},
    {"email": "test3@mail.r", "username": "user27@", "password": "pass3/"}
])
def user_data(request):
    return request.param


@pytest.fixture
def user_email():
    email_1 = fake.email()
    email_2 = fake.free_email()
    return {
        "email_1": email_1,
        "email_2": email_2,
        "placeholder": "user@example.com"
    }


@pytest.fixture
def user_password():
    pass_1 = fake.password()
    return {
        "password_1": "12345",
        "password_2": "123",
        "test_password": "SecurePass123!",
        "placeholder": "Введите пароль"
    }


@pytest.fixture
def multiline_text():
    return {
        "text_1": "Многострочный текстМногострочный текстМногострочный текст",
        "text_2": ".........................................................",
        "text_3": "Введите ваш комментарий...\nВторая строка\nТретья строка",
        "placeholder": "Введите ваш комментарий..."
    }


@pytest.fixture
def countries():
    value_country = {'1': 'Россия', '2': 'США', '3': 'Германия', '4': 'Франция'}
