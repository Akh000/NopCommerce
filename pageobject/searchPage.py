import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Search:
    search_input_xpath = (By.ID, "small-searchterms")
    search_button_xpath = (By.XPATH, "//button[contains(text(),'Search')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def search_input(self, item):
        # self.wait.until(EC.element_to_be_clickable(*Search.search_input_xpath))
        time.sleep(3)
        self.driver.find_element(*Search.search_input_xpath).clear()
        search = self.driver.find_element(*Search.search_input_xpath)
        search.send_keys(item)

    def search_button(self):
        self.driver.find_element(*Search.search_button_xpath).click()
