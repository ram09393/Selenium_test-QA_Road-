import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import allure


@allure.epic("Пользователи")
@allure.feature("Регистрация пользователя")
@allure.story("Успешная регистрация")
@allure.title("Проверка регистрации нового пользователя")
@allure.description("Проверка заполнения поля Имя")
@allure.severity(allure.severity_level.BLOCKER)
@allure.tag("smoke", "regression", "user")
@allure.link("https://jira.fakapdevelopment.com/BUG-777")
@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.basic_practic
def test_name_field(browser, user_names, wait):
    with allure.step("Шаг 1: Ожидаем появления поля user-name в DOM-дереве"):
        name_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='username-field']")))

    with allure.step("Шаг 2: Ожидаем что поле ввода видимое"):
        wait.until(EC.visibility_of(name_field))

    with allure.step("Шаг 3: Проверяем что поле ввода отображается на странице"):
        assert name_field.is_displayed()

    with allure.step("Шаг 4: Ожидаем наличие атрибута placeholder "):
        placeholder = name_field.get_attribute("placeholder")
        assert placeholder == user_names["placeholder"]

    with allure.step(f"Шаг 5: Вводим первое имя {user_names['first_name']}"):
        name_field.clear()
        name_field.send_keys(user_names["first_name"])

    with allure.step("Шаг 6: Очищаем поле username после ввода первого имени"):
        name_field.clear()

    with allure.step(f"Шаг 7: Вводим второе имя {user_names['second_name']}"):
        name_field.send_keys(user_names["second_name"])

    with allure.step("Шаг 8: Ожидаем появления поля second_name в DOM-дереве"):
        wait.until(EC.text_to_be_present_in_element_value((By.CSS_SELECTOR, "[data-testid='username-field']"),
                                                          user_names["second_name"]))
    with allure.step(
            "Шаг 9: Проверяем что в поле ввода на странице отображается фамилия пользователя с значением second_name "):
        assert name_field.get_attribute("value") == user_names["second_name"]


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.basic_practic
def test_email_field(browser, user_email, wait):
    with allure.step("Шаг 1: Ожидаем появления поля user-email в DOM-дереве"):
        "'# Поиск элемента по data-testid='email-field'"
    email_field = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='email-field']")))

    with allure.step("Шаг 2: Ожидаем что поле ввода видимое"):
        wait.until(EC.visibility_of(email_field))

    with allure.step("Шаг 3: Проверяем что поле ввода отображается на странице"):
        assert email_field.is_displayed()

    with allure.step("Шаг 4: Ожидаем наличие атрибута placeholder "):
        placeholder = email_field.get_attribute("placeholder")

    assert placeholder == user_email["placeholder"]

    with allure.step(f"Шаг 5: Вводим первое значение email {user_email['email_1']}"):
        email_field.send_keys(user_email["email_1"])

    with allure.step("Шаг 6: Ощищаем поле email после ввода первого значения email"):
        email_field.clear()

    with allure.step(f"Шаг 7: Вводим второе значение email {user_email['email_2']}"):
        email_field.send_keys(user_email["email_2"])

    with allure.step("Шаг 8: Ожидаем появления поля email_1 в DOM-дереве"):
        wait.until(EC.text_to_be_present_in_element_value(By.CSS_SELECTOR, "[data-testid='email-field']",
                                                          user_email['email_1']))
    with allure.step(
            "Шаг 9: Проверяем что в поле ввода на странице отображается email пользователя с значением email_2 "):
        assert email_field.get_attribute("value") == user_email["email_2"]


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.basic_practic
def test_email_field_validation(browser, wait, base_url):
    with allure.step("Ожидание видимости поля ввода Email"):
        email_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='email-field']")))
    with allure.step("Шаг 5: Вводим валидное значение email в поле"):
        valid_email = "12345@ya.ru"
    email_field.send_keys(valid_email)


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.basic_practic
def test_password_field(browser, user_password, wait):
    # Поиск элемента по data-testid='password-field'"
    with allure.step("Шаг 1: Ожидаем появления поля password в DOM-дереве"):
        password_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='password-field']")))
    with allure.step("Шаг 2: Проверяем что поле ввода для пароля отображается на странице"):
        assert password_field.is_displayed()
    with allure.step("Шаг 3: Ожидаем наличие атрибута placeholder "):
        placeholder = password_field.get_attribute("placeholder")
    with allure.step(
            "Шаг 4: Проверяем совпадает ли значение переменной placeholder со значением, хранящимся в user_password по ключу placeholder"):
        assert placeholder == user_password["placeholder"]
    with allure.step(f"Шаг 5: Вводим первый пароль {user_password['password_1']}"):
        password_field.send_keys(user_password["password_1"])
    with allure.step("Шаг 6: Очищаем поле password после ввода первого значения пароля"):
        password_field.clear()
    with allure.step(f"Шаг 5: Вводим второй пароль {user_password['password_2']}"):
        password_field.send_keys(user_password["password_2"])
    with allure.step(
            "Шаг 6: Проверяем что в поле ввода пароля на странице отображается пароль с значением password_2 "):
        assert password_field.get_attribute("value") == user_password["password_2"]


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.basic_practic
def test_password_field_masking(browser, wait, user_password):

    with allure.step("Шаг 1: Ожидаем появления поля password в DOM-дереве"):
        password_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='password-field']")))
    with allure.step("Шаг 2: Вводим значение test_password в поле ввода пароля"):
        password_field.send_keys_(user_password["test_password"])
    with allure.step("Шаг 3: Очищаем поле после ввода пароля со значением test_password"):
        password_field.clear()
    with allure.step("Шаг 4: Проверка того, что поле действительно является полем для ввода пароля."):
        assert password_field.get_attribute("type") == "password"
    with allure.step("Шаг 5:  Проверяем что в поле ввода пароля на странице отображается пароль с значением test_password"):
        assert password_field.get_attribute("value") == (user_password["test_password"])


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.basic_practic
def test_comment_field_input(browser, multiline_text, wait):
    # Поиск элемента по data-testid='comment-field'"

    comment_field = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='comment-field']")))

    assert comment_field.is_displayed()

    placeholder = comment_field.get_attribute("placeholder")

    assert placeholder == multiline_text["placeholder"]

    comment_field.send_keys(multiline_text["text_1"])

    comment_field.clear()

    comment_field.send_keys(multiline_text["text_2"])

    assert comment_field.get_attribute("value") == multiline_text["text_2"]

    comment_field.clear()

    comment_field.send_keys(multiline_text["text_3"])

    assert comment_field.get_attribute("value") == multiline_text["text_3"]

    assert comment_field.get_attribute("value") == multiline_text["text_3"]


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.basic_practic
def test_country_dropdown_list(browser, countries, wait):
    # Поиск элемента по data-testid='country-dropdown'"

    country_select_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='country-dropdown']")))

    assert country_select_button.is_enabled(), "Кнопка выбора страны заблокирована"
    assert country_select_button.is_displayed(), "Кнопка выбора страны не отображается"

    text_country = country_select_button.text

    print(country_select_button.text)

    assert text_country == "Выберите страну"

    country_select_button.click()

    russia_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Россия')]")))

    russia_option.click()

    assert "Россия" in country_select_button.text

    country_select_button.click()

    usa_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'США')]")))

    usa_option.click()

    assert "США" in country_select_button.text

    country_select_button.click()

    germany_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Германия')]")))

    germany_option.click()

    assert "Германия" in country_select_button.text

    country_select_button.click()

    france_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Франция')]")))

    france_option.click()

    assert "Франция" in country_select_button.text

    country_select_button.click()


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.basic_practic
def test_checkbox_agree_conditions(browser, wait):
    # 1. Находим чекбокс по data-testid
    checkbox = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="terms-agreement"]')))

    # 2. Сначала проверяем состояние ПО УМОЛЧАНИЮ (должен быть выключен)
    assert not checkbox.is_selected(), "Ошибка: Чекбокс должен быть выключен по умолчанию"

    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkbox)

    assert not checkbox.is_selected()

    # 3. Кликаем по нему
    checkbox.click()

    # 4. Проверяем, что чекбокс ВКЛ
    assert checkbox.is_selected(), "Ошибка: Чекбокс не включился после клика"

    # 5. Кликаем еще раз (снимаем галочку)
    checkbox.click()

    # 6. Проверяем, что он снова ВЫКЛ
    assert not checkbox.is_selected(), "Ошибка: Чекбокс не выключился после повторного клика"


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.basic_practic
def test_newsletter_radio_button_yes(browser, wait):
    # 1. Находим радиобаттон по data-testid
    radio_yes = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="newsletter-yes"]')))

    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", radio_yes)

    # 3. Проверяем начальное состояние
    assert not radio_yes.is_selected(), "Радиобаттон не должен быть выбран по умолчанию"

    browser.execute_script("arguments[0].click();", radio_yes)

    assert radio_yes.is_selected(), "Радиобаттон должен стать выбранным"


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.basic_practic
def test_newsletter_radio_button_no(browser, wait):
    # 1. Находим радиобаттон по data-testid
    radio_no = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="newsletter-no"]')))

    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", radio_no)

    # 3. Проверяем начальное состояние
    assert not radio_no.is_selected(), "Радиобаттон не должен быть выбран по умолчанию"

    browser.execute_script("arguments[0].click();", radio_no)

    assert radio_no.is_selected(), "Радиобаттон должен стать выбранным"


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.basic_practic
def test_newsletter_radio_group(browser, wait):
    # "Тест на переключение радиобаттонов"

    # 1. Находим оба радиобаттона по data-testid
    radio_yes = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="newsletter-yes"]')))
    # Предположим, у второго ID или testid заканчивается на -no
    radio_no = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="newsletter-no"]')))

    # 2. Скроллим к радиобаттону
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", radio_yes)

    # 3. Проверяем начальное состояние (обычно оба пустые или выбран один по умолчанию)
    assert not radio_yes.is_selected(), "По умолчанию 'Yes' не должен быть выбран"

    # 4. Включаем 'Yes'
    browser.execute_script("arguments[0].click();", radio_yes)  # JS-клик надежнее для кастомных стилей
    assert radio_yes.is_selected(), "После клика 'Yes' должен быть выбран"
    assert not radio_no.is_selected(), "При выбранном 'Yes', 'No' должен быть пуст"

    # 5. ПЕРЕКЛЮЧАЕМ на 'No'
    browser.execute_script("arguments[0].click();", radio_no)

    # 6. ГЛАВНАЯ ПРОВЕРКА: 'Yes' должен автоматически выключиться
    assert radio_no.is_selected(), "После клика 'No' должен быть выбран"
    assert not radio_yes.is_selected(), "Выбор должен был сняться с 'Yes' автоматически"


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.interactive_elements
def test_primary_primary_button(browser, wait):
    # 1. Находим кнопку по data-testid
    primary_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="primary-button"]')))

    # 2. Проверяем текст кнопки
    assert "Основная" in primary_btn.text

    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", primary_btn)

    browser.execute_script("arguments[0].click();", primary_btn)


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.interactive_elements
def test_secondary_button(browser, wait):
    # 1. Находим кнопку по data-testid
    secondary_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="secondary-button"]')))

    # 2. Проверяем текст кнопки
    assert "Вторичная" in secondary_btn.text

    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", secondary_btn)

    browser.execute_script("arguments[0].click();", secondary_btn)


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.interactive_elements
def test_success_button(browser, wait):
    # 1. Находим кнопку по data-testid
    success_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="success-button"]')))

    # 2. Проверяем текст кнопки
    assert "Успех" in success_btn.text

    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", success_btn)

    browser.execute_script("arguments[0].click();", success_btn)


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.interactive_elements
def test_danger_button(browser, wait):
    # 1. Находим кнопку по data-testid
    danger_btn = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="danger-button"]')))

    # 2. Проверяем текст кнопки
    assert "Опасность" in danger_btn.text

    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", danger_btn)

    browser.execute_script("arguments[0].click();", danger_btn)


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.interactive_elements
def test_button_show_notification(browser, wait):
    # 1. Находим кнопку "Показать уведомление" по data-testid
    show_btn = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="show-alert-button"]'))
    )

    # 2. Скроллим и кликаем
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", show_btn)
    browser.execute_script("arguments[0].click();", show_btn)

    # 3. Ждем появления модального окна (ждем заголовок)

    modal_title = wait.until(
        EC.visibility_of_element_located((By.XPATH, "//*[text()='Информационное сообщение']"))
    )

    # 4. Проверяем основной текст уведомления
    modal_body = browser.find_element(By.XPATH, "//*[contains(text(), 'Это важное уведомление')]")
    assert modal_body.is_displayed(), "Текст уведомления не отображается"

    # 5. Находим кнопку "Скрыть уведомление" (или "Закрыть")
    close_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Скрыть уведомление')]")))

    # 6. Закрываем уведомление
    browser.execute_script("arguments[0].click();", close_btn)

    # 7. Проверяем, что уведомление исчезло
    wait.until(EC.invisibility_of_element(modal_title))

    print("Тест уведомления успешно пройден: открыто, проверено, скрыто.")


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.interactive_elements
def test_open_modal_window(browser, wait):
    # Селекторы для стабильности
    btn_open_window = '[data-testid="open-modal-button"]'
    modal_window = '[data-testid="modal-content"]'
    btn_close_x = '[data-testid="modal-close-button"]'
    btn_cancel = '[data-testid="modal-cancel-button"]'
    btn_confirm = '[data-testid="modal-confirm-button"]'

    # --- ШАГ 1: Открытие и проверка главного модального окна ---
    open_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, btn_open_window)))

    # Скроллим и кликаем (защита от липкой шапки сайта)
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", open_btn)
    browser.execute_script("arguments[0].click();", open_btn)

    # Ждем появления модального окна
    modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, modal_window)))

    # Проверяем заголовок 2-го модального окна
    title = browser.find_element(By.CSS_SELECTOR, '[data-testid="modal-title"]')
    assert title.text == "Модальное окно", f"Неверный заголовок: {title.text}"

    # Проверяем наличие всех кнопок внутри
    assert browser.find_element(By.CSS_SELECTOR, btn_close_x).is_displayed()
    assert browser.find_element(By.CSS_SELECTOR, btn_cancel).is_displayed()
    assert browser.find_element(By.CSS_SELECTOR, btn_confirm).is_displayed()

    # --- ШАГ 2: Проверка закрытия через КРЕСТИК (X) ---
    browser.find_element(By.CSS_SELECTOR, btn_close_x).click()
    wait.until(EC.invisibility_of_element(modal))
    print("Проверка 1: Крестик закрывает окно")

    # --- ШАГ 3: Проверка закрытия через кнопку "ОТМЕНА" ---
    browser.execute_script("arguments[0].click();", open_btn)  # Снова открываем
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, modal_window)))

    cancel_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, btn_cancel)))
    cancel_btn.click()
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, modal_window)))
    print("Проверка 2: Кнопка 'Отмена' закрывает окно")

    # --- ШАГ 4: Проверка закрытия через кнопку "ПОДТВЕРДИТЬ" ---
    browser.execute_script("arguments[0].click();", open_btn)  # Снова открываем
    modal_final = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, modal_window)))

    confirm_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, btn_confirm)))
    confirm_btn.click()

    # Финальное ожидание исчезновения модального окна
    wait.until(EC.invisibility_of_element(modal_final))


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.interactive_elements
def test_success_notification(browser, wait):
    # 1. Находим по data-testid и нажимаем кнопку "Успех"
    success_btn = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="notify-success"]'))
    )
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", success_btn)
    browser.execute_script("arguments[0].click();", success_btn)

    notification_xpath = "//p[contains(text(), 'Операция выполнена успешно!')]"

    # Ждем появления уведомления "Операция выполнена успешно!"
    notification_success_ = wait.until(
        EC.visibility_of_element_located((By.XPATH, notification_xpath)))

    # 3. Проверяем, что нотификация исчезает

    is_disappeared = wait.until(
        EC.invisibility_of_element_located((By.XPATH, notification_xpath))
    )

    assert is_disappeared, "Уведомление не исчезло в течение установленного времени"


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.interactive_elements
def test_error_notification(browser, wait):
    # 1. Находим по data-testid и нажимаем кнопку "Ошибка"
    error_btn = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="notify-error"]'))
    )
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", error_btn)
    browser.execute_script("arguments[0].click();", error_btn)

    notification_xpath = "//p[contains(text(), 'Произошла ошибка!')]"

    # Ждем появления уведомления "Произошла ошибка!"
    error_notification = wait.until(
        EC.visibility_of_element_located((By.XPATH, notification_xpath)))

    # 3. Проверяем, что нотификация исчезает

    is_disappeared = wait.until(
        EC.invisibility_of_element_located((By.XPATH, notification_xpath)))

    assert is_disappeared, "Уведомление не исчезло в течение установленного времени"


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.interactive_elements
def test_warning_notification(browser, wait):
    # 1. Находим по data-testid и нажимаем кнопку "Предупреждение"
    warning_btn = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="notify-warning"]'))
    )
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", warning_btn)
    browser.execute_script("arguments[0].click();", warning_btn)

    notification_xpath = "//p[contains(text(), 'Обратите внимание!')]"

    # Ждем появления уведомления "Обратите внимание!"
    error_notification = wait.until(
        EC.visibility_of_element_located((By.XPATH, notification_xpath)))

    # 3. Проверяем, что нотификация исчезает (например, в течение 10 секунд)
    # EC.invisibility_of_element_located вернет True, когда элемент пропадет

    is_disappeared = wait.until(
        EC.invisibility_of_element_located((By.XPATH, notification_xpath)))

    assert is_disappeared, "Уведомление не исчезло в течение установленного времени"


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.interactive_elements
def test_info_notification(browser, wait):
    # 1. Находим кнопку "Инфо" и нажимаем на неё

    info_btn = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="notify-info"]'))
    )
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", info_btn)
    browser.execute_script("arguments[0].click();", info_btn)

    # 2. Определяем локатор и ожидаемый текст
    notification_xpath = "//p[contains(@class, 'text-sm')]"  # локатор самого параграфа
    expected_text = "Информация для вас"

    # 3. Проверка №1: Ждем, что в элементе появится именно этот текст
    # Это подтверждает, что нотификация не просто открылась, а содержит нужные данные
    text_is_correct = wait.until(
        EC.text_to_be_present_in_element((By.XPATH, notification_xpath), expected_text)
    )
    assert text_is_correct, f"Текст в уведомлении должен быть: '{expected_text}'"

    # 4. Проверка №2: Ждем появления (видимости) элемента для надежности

    success_notification = wait.until(
        EC.visibility_of_element_located((By.XPATH, f"//p[contains(text(), '{expected_text}')]"))
    )

    # 5. Проверка №3: Ждем исчезновения нотификации
    is_disappeared = wait.until(
        EC.invisibility_of_element_located((By.XPATH, f"//p[contains(text(), '{expected_text}')]"))
    )

    assert is_disappeared, "Уведомление не исчезло в течение установленного времени"


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.link_elements
def test_external_link_opens_in_new_window(browser, wait):
    # 1. Сохраняем ID текущего (основного) окна
    original_window = browser.current_window_handle

    # 2. Находим ссылку по data-testid и кликаем
    external_link = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="external-link"]'))
    )

    # Проверка атрибутов перед кликом
    assert external_link.get_attribute("target") == "_blank", "Ссылка должна открываться в новом окне"
    assert "https://example.com" in external_link.get_attribute("href")

    external_link.click()

    # 3. Ждем, пока откроется второе окно
    wait.until(EC.number_of_windows_to_be(2))

    # 4. Получаем список всех окон и переключаемся на последнее открытое
    all_windows = browser.window_handles
    browser.switch_to.window(all_windows[-1])

    # 5. Проверяем, что URL в новом окне верный
    wait.until(EC.url_contains("example.com"))
    assert browser.current_url == "https://example.com/"

    # 6. Закрываем новое окно и возвращаемся в исходное
    browser.close()
    browser.switch_to.window(original_window)


@pytest.mark.ui
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.link_elements
def test_anchor_link_transfer_url_practice_elements(browser, wait):
    # 1. Находим элемент якорная ссылка
    anchor_link = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="anchor-link"]'))
    )

    # Проверяем наличие корректного атрибута href
    assert anchor_link.get_attribute("href").endswith("#practice-elements")

    # 2. Кликаем по ссылке
    anchor_link.click()

    # 3. Ждем, когда в URL появится хэш якоря
    wait.until(EC.url_contains("#practice-elements"))
    assert "#practice-elements" in browser.current_url

    # 4. Проверяем, что элемент существует и виден
    target_element = wait.until(
        EC.visibility_of_element_located((By.ID, "practice-elements")))
