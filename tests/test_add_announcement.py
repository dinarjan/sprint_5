from locators.locators import AllLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import StaleElementReferenceException
from helpers import product_cards
from generators import product_name
from data import mail, pswd


class TestAnnouncement:

    def test_create_announcement_unauthorized_user(self, page):
        WebDriverWait(page, 3).until(EC.visibility_of_element_located(AllLocators.ADD_ANNOUNCEMENT)).click()
        assert WebDriverWait(page, 3).until(
            EC.visibility_of_element_located(AllLocators.NOTIFICATION_WINDOW)).text == AllLocators.NOTIFICATION_TEXT

    def test_create_announcement_authorized_user(self, page):
        WebDriverWait(page, 5).until(EC.visibility_of_element_located(AllLocators.LOGIN_REGISTRATION_BUTTON)).click()
        WebDriverWait(page, 5).until(EC.visibility_of_element_located(AllLocators.EMAIL)).send_keys(mail)
        WebDriverWait(page, 5).until(EC.visibility_of_element_located(AllLocators.PASSWORD)).send_keys(pswd)
        WebDriverWait(page, 5).until(EC.visibility_of_element_located(AllLocators.LOGIN)).click()
        try:
            WebDriverWait(page, 5).until(EC.visibility_of_element_located(AllLocators.ADD_ANNOUNCEMENT)).click()
        except StaleElementReferenceException:
            WebDriverWait(page, 5).until(EC.visibility_of_element_located(AllLocators.ADD_ANNOUNCEMENT)).click()
        WebDriverWait(page, 5).until(EC.visibility_of_element_located(AllLocators.NAME_ANNOUNCEMENT)).send_keys(
            product_name)
        WebDriverWait(page, 5).until(EC.visibility_of_element_located(AllLocators.DROPDOWN_CATEGORY)).click()
        WebDriverWait(page, 5).until(EC.visibility_of_element_located(AllLocators.CATEGORY)).click()
        WebDriverWait(page, 5).until(EC.visibility_of_element_located(AllLocators.USED_CONDITION)).click()
        WebDriverWait(page, 5).until(EC.visibility_of_element_located(AllLocators.DROPDOWN_CITY)).click()
        WebDriverWait(page, 5).until(EC.visibility_of_element_located(AllLocators.CITY)).click()
        WebDriverWait(page, 5).until(EC.visibility_of_element_located(AllLocators.DESCRIPTION)).send_keys(
            'В идеальном состоянии. Торг уместен')
        WebDriverWait(page, 5).until(EC.visibility_of_element_located(AllLocators.VALUE)).send_keys(
            1000)
        WebDriverWait(page, 5).until(EC.visibility_of_element_located(AllLocators.PUBLICIZE)).click()
        WebDriverWait(page, 3).until(EC.visibility_of_element_located(AllLocators.INPUT_BUY))
        WebDriverWait(page, 10).until(EC.visibility_of_element_located(AllLocators.USER_AVATAR)).click()
        WebDriverWait(page, 10).until(EC.visibility_of_element_located(AllLocators.DESC_NAME))
        assert '/profile' in page.current_url
        assert (page.find_element(*product_cards(product_name))).is_displayed()
