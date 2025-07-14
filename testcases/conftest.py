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
        chrome_option.add_argument("--headless")
        chrome_option.add_argument("--disable-gpu")
        chrome_option.add_argument("--window-size=1920,1080")  # Important!
        chrome_option.add_argument("--disable-extensions")
        chrome_option.add_argument("--no-sandbox")
        chrome_option.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=chrome_option)
    driver.maximize_window()
    driver.get("https://demo.nopcommerce.com/")
    yield driver
    driver.close()
