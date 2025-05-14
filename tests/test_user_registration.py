from locators.locators import AllLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from generators import incorrect_login_name


class TestUserRegistration:

    def test_user_registration(self, page, user_credentials_email, user_credentials_password):
        WebDriverWait(page, 3).until(EC.visibility_of_element_located(AllLocators.LOGIN_REGISTRATION_BUTTON)).click()
        WebDriverWait(page, 3).until(EC.visibility_of_element_located(AllLocators.NO_ACCOUNT_BUTTON)).click()
        WebDriverWait(page, 3).until(EC.visibility_of_element_located(AllLocators.EMAIL)).send_keys(
            user_credentials_email)
        WebDriverWait(page, 3).until(EC.visibility_of_element_located(AllLocators.PASSWORD)).send_keys(
            user_credentials_password)
        WebDriverWait(page, 3).until(EC.visibility_of_element_located(AllLocators.REPEATED_PASSWORD)).send_keys(
            user_credentials_password)
        WebDriverWait(page, 3).until(EC.visibility_of_element_located(AllLocators.CREATE_ACC)).click()
        assert '/regiatration' in page.current_url, 'Не произошёл переход на главную страницу'
        assert WebDriverWait(page, 3).until(
            EC.visibility_of_element_located(AllLocators.USER_AVATAR)), 'Не отображается аватар'
        assert WebDriverWait(page, 3).until(
            EC.visibility_of_element_located(AllLocators.USER_NAME)).text == 'User.', 'Отличается имя пользователя'

    def test_user_with_incorrect_email(self, page):
        WebDriverWait(page, 3).until(EC.visibility_of_element_located(AllLocators.LOGIN_REGISTRATION_BUTTON)).click()
        WebDriverWait(page, 3).until(EC.visibility_of_element_located(AllLocators.NO_ACCOUNT_BUTTON)).click()
        WebDriverWait(page, 3).until(EC.visibility_of_element_located(AllLocators.EMAIL)).send_keys(
            incorrect_login_name)
        WebDriverWait(page, 3).until(EC.visibility_of_element_located(AllLocators.CREATE_ACC)).click()
        assert WebDriverWait(page, 3).until(
            EC.visibility_of_element_located(AllLocators.ERROR)).text == 'Ошибка'
        assert WebDriverWait(page, 3).until(EC.visibility_of_element_located(
            AllLocators.EMAIL_FIELD)).value_of_css_property("border-color") == 'rgb(255, 105, 114)', 'Другой цвет'
        assert WebDriverWait(page, 3).until(EC.visibility_of_element_located(
            AllLocators.PASSWORD_FIELD)).value_of_css_property("border-color") == 'rgb(255, 105, 114)', 'Другой цвет'
        assert WebDriverWait(page, 3).until(EC.visibility_of_element_located(
            AllLocators.REPEATED_PASSWORD_FIELD)).value_of_css_property("border-color") == 'rgb(255, 105, 114)', 'Другой цвет'

    def test_registering_an_existing_user(self, page, user_credentials_email, user_credentials_password):
        WebDriverWait(page, 3).until(EC.visibility_of_element_located(AllLocators.LOGIN_REGISTRATION_BUTTON)).click()
        WebDriverWait(page, 3).until(EC.visibility_of_element_located(AllLocators.NO_ACCOUNT_BUTTON)).click()
        WebDriverWait(page, 3).until(EC.visibility_of_element_located(AllLocators.EMAIL)).send_keys(
            user_credentials_email)
        WebDriverWait(page, 3).until(EC.visibility_of_element_located(AllLocators.PASSWORD)).send_keys(
            user_credentials_password)
        WebDriverWait(page, 3).until(EC.visibility_of_element_located(AllLocators.REPEATED_PASSWORD)).send_keys(
            user_credentials_password)
        WebDriverWait(page, 3).until(EC.visibility_of_element_located(AllLocators.CREATE_ACC)).click()
        assert WebDriverWait(page, 3).until(EC.visibility_of_element_located(AllLocators.ERROR)).text == "Ошибка"
        assert WebDriverWait(page, 3).until(EC.visibility_of_element_located(
            AllLocators.EMAIL_FIELD)).value_of_css_property("border-color") == 'rgb(255, 105, 114)', 'Другой цвет'
        assert WebDriverWait(page, 3).until(EC.visibility_of_element_located(
            AllLocators.PASSWORD_FIELD)).value_of_css_property("border-color") == 'rgb(255, 105, 114)', 'Другой цвет'
        assert WebDriverWait(page, 3).until(EC.visibility_of_element_located(
            AllLocators.REPEATED_PASSWORD_FIELD)).value_of_css_property("border-color") == 'rgb(255, 105, 114)', 'Другой цвет'
