import pytest
from playwright.sync_api import Page, expect, Browser, ViewportSize


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
def test_name_field(page: Page, user_names):
    name_field = page.locator("[data-testid='username-field']")

    expect(name_field).to_be_visible()

    expect(name_field).to_have_attribute("placeholder", user_names["placeholder"])

    name_field.fill(user_names["first_name"])
    name_field.fill(user_names["second_name"])

    expect(name_field).to_have_value(user_names["second_name"])


def test_email_field(page: Page, user_email):

    email_field = page.locator("[data-testid='email-field']")

    expect(email_field).to_be_visible()

    expect(email_field).to_have_attribute("placeholder", user_email["placeholder"])

    email_field.fill(user_email["email_1"])
    email_field.fill(user_email["email_2"])

    expect(email_field).to_have_value(user_email["email_1"])


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
def test_name_field(page_with_tracing: Page, user_names):
    name_field = page_with_tracing.locator("[data-testid='username-field']")

    expect(name_field).to_be_visible()

    expect(name_field).to_have_attribute("placeholder", user_names["placeholder"])

    name_field.fill(user_names["first_name"])
    name_field.fill(user_names["second_name"])

    expect(name_field).to_have_value(user_names["second_name"])


def test_context_with_custom_viewport(browser_pw: Browser, base_url):
    browser_pw.new_context()
    viewport_size: ViewportSize = {
        'width': 640,
        'height': 480,

    }
    context = browser_pw.new_context(
        viewport=viewport_size
    )

    page = context.new_page()
    page.goto(base_url)

    context.close()


def test_weather_api_mock_show(browser_pw: Browser):
    mock_response = {

        "coord": {
            "lon": 56.2855,
            "lat": 58.0174
        },
        "weather": [
            {
                "id": 804,
                "main": "Clouds",
                "description": "overcast clouds",
                "icon": "04d"
            }
        ],
        "base": "stations",
        "main": {
            "temp": 1.13,
            "feels_like": -2.53,
            "temp_min": 1.13,
            "temp_max": 1.13,
            "pressure": 1018,
            "humidity": 100,
            "sea_level": 1018,
            "grnd_level": 999
        },
        "visibility": 45,
        "wind": {
            "speed": 3.49,
            "deg": 255,
            "gust": 9.08
        },
        "clouds": {
            "all": 100
        },
        "dt": 1773312829,
        "sys": {
            "country": "RU",
            "sunrise": 1773283224,
            "sunset": 1773324551
        },
        "timezone": 18000,
        "id": 511196,
        "name": "Perm",
        "cod": 200
    }

    context = browser_pw.new_context()
    page = context.new_page()

    page.route("**/api.openweathermap.org/data/2.5/weather", lambda route: route.fullfill(json=mock_response))
    page.goto("https://3jo9s.csb.app/")
    page.locator("//a[@id='btn-answer-yes']").click()

    search_input = page.locator("//input[@type='search']")
    search_input.fill("Moscow")
    search_input.press("Enter")

    page.wait_for_timeout(3000)

    expect(page.locator("text=Clouds")).to_be_visible()

    context.close()
