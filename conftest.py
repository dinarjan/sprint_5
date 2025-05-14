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


@pytest.fixture(scope="session")
def user_credentials_email():
    email = generate_email()
    return email


@pytest.fixture(scope="session")
def user_credentials_password():
    password = generate_password()
    return password


@pytest.fixture
def existing_user():
    mail = 'buranbaev_30@mail.ru'
    pswd = 'Dinar789'
    return mail, pswd

