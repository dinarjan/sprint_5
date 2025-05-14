from locators.locators import AllLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import is_element_absent
from data import mail, pswd

class TestLogoutUser:

    def test_logout_user(self, page):
        WebDriverWait(page, 3).until(EC.visibility_of_element_located(AllLocators.LOGIN_REGISTRATION_BUTTON)).click()
        WebDriverWait(page, 3).until(EC.visibility_of_element_located(AllLocators.EMAIL)).send_keys(mail)
        WebDriverWait(page, 3).until(EC.visibility_of_element_located(AllLocators.PASSWORD)).send_keys(pswd)
        WebDriverWait(page, 3).until(EC.visibility_of_element_located(AllLocators.LOGIN)).click()
        WebDriverWait(page, 3).until(EC.visibility_of_element_located(AllLocators.LOGOUT)).click()
        is_element_absent(page, AllLocators.USER_AVATAR)
        is_element_absent(page, AllLocators.USER_NAME)
        assert WebDriverWait(page, 3).until(
            EC.visibility_of_element_located(AllLocators.LOGIN_REGISTRATION_BUTTON)), 'Не отображается кнопка'
