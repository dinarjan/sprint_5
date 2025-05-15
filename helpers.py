from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By


def is_element_absent(page, element):
    try:
        WebDriverWait(page, 3).until_not(EC.presence_of_element_located(element))
        element_present = False
    except TimeoutException:
        element_present = True
    assert not element_present


def product_cards(product_name):
    return By.XPATH, f"//img[contains(@alt, '{product_name}')]"
