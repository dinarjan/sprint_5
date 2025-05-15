from selenium.webdriver.common.by import By
from generators import product_name


class AllLocators:
    LOGIN = (By.XPATH, '//button[text()="Войти"]')
    LOGOUT = (By.XPATH, "//button[text()='Выйти']")
    LOGIN_REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Вход и регистрация']")
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Нет аккаунта']")
    EMAIL = (By.XPATH, "//input[@placeholder='Введите Email']")
    EMAIL_FIELD = (By.XPATH, "//input[@placeholder='Введите Email']/parent::div")
    PASSWORD = (By.XPATH, "//input[@placeholder='Пароль']")
    PASSWORD_FIELD = (By.XPATH, "//input[@placeholder='Пароль']/parent::div")
    REPEATED_PASSWORD = (By.XPATH, "//input[@placeholder='Повторите пароль']")
    REPEATED_PASSWORD_FIELD = (By.XPATH, "//input[@placeholder='Повторите пароль']/parent::div")
    ERROR = (By.XPATH, "//span[@class='input_span__yWPqB']")
    CREATE_ACC = (By.XPATH, "//button[text()='Создать аккаунт']")
    USER_AVATAR = (By.XPATH, "//button[@class='circleSmall']")
    USER_NAME = (By.XPATH, "//h3[@class='profileText name']")
    ADD_ANNOUNCEMENT = (By.XPATH, "//button[text()='Разместить объявление']")
    NOTIFICATION_WINDOW = (By.XPATH, "//h1[text()='Чтобы разместить объявление, авторизуйтесь']")
    NOTIFICATION_TEXT = 'Чтобы разместить объявление, авторизуйтесь'
    NAME_ANNOUNCEMENT = (By.XPATH, "//input[@class='input_inputStandart__JweLZ spanGlobal']")
    DESCRIPTION = (By.XPATH, "//textarea[@placeholder='Описание товара']")
    VALUE = (By.XPATH, "//input[@placeholder='Стоимость']")
    PUBLICIZE = (By.XPATH, "//button[text()='Опубликовать']")
    USED_CONDITION = (By.CSS_SELECTOR, ".radioUnput_inputRegular__FbVbr")
    DROPDOWN_CATEGORY = (By.XPATH, "//input[@name='category']/following-sibling::button[contains(@class, 'dropDownMenu_arrowDown__pfGL1')]")
    CATEGORY = (By.XPATH, "//button/span[text()='Технологии']/parent::button")
    DROPDOWN_CITY = (By.XPATH, "//input[@name='city']/following-sibling::button")
    CITY = (By.XPATH, "//button/span[text()='Санкт-Петербург']/parent::button")
    PRODUCT = (By.XPATH, f"//h2[text()='{product_name}']/parent::div")
    INPUT_BUY = (By.XPATH, "//input[@placeholder='Я хочу купить...']")
    DESC_NAME = (By.XPATH, "//div[contains(@class, 'card')]//h2")