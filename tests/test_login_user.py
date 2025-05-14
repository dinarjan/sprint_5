from locators.locators import AllLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLoginUser:

    def test_login_user(self, page, existing_user):
        mail, pswd = existing_user
        WebDriverWait(page, 3).until(EC.visibility_of_element_located(AllLocators.LOGIN_REGISTRATION_BUTTON)).click()
        WebDriverWait(page, 3).until(EC.visibility_of_element_located(AllLocators.EMAIL)).send_keys(mail)
        WebDriverWait(page, 3).until(EC.visibility_of_element_located(AllLocators.PASSWORD)).send_keys(pswd)
        WebDriverWait(page, 3).until(EC.visibility_of_element_located(AllLocators.LOGIN)).click()
        assert '/login' in page.current_url, 'Не произошёл переход на главную страницу'
        assert WebDriverWait(page, 3).until(EC.visibility_of_element_located(AllLocators.USER_AVATAR)), \
            'Не отображается аватар'
        assert WebDriverWait(page, 3).until(EC.visibility_of_element_located(
                AllLocators.USER_NAME)).text == 'User.', 'Отличается имя пользователя'
