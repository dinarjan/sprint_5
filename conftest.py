import pytest
from selenium import webdriver
from data import main_page
from generators import generate_email, generate_password


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def page(driver):
    driver.get(main_page)
    return driver
