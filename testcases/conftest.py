import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'edge':
        driver = webdriver.Edge()
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    else:
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument('headless')
        driver = webdriver.Chrome(options=chrome_option)
    driver.maximize_window()
    driver.get("https://demo.nopcommerce.com/")
    yield driver
    driver.close()
