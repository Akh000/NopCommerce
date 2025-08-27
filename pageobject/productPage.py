import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class ProductFilter:
    price_slider_min_xpath = (By.XPATH, "//span[@class='ui-slider-handle ui-corner-all ui-state-default'][1]")
    price_slider_max_xpath = (By.XPATH, "//span[@class='ui-slider-handle ui-corner-all ui-state-default'][2]")
    product_price_css_selector = (By.CSS_SELECTOR, ".price.actual_price")
    product_title_css_selector = (By.CSS_SELECTOR, ".product_title a")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.action = ActionChains(driver)

    def adjust_price_slider(self):
        time.sleep(3)
        # self.wait.until(EC.element_located_to_be_selected(*ProductFilter.price_slider_min_xpath))
        slider_min = self.driver.find_element(*ProductFilter.price_slider_min_xpath)
        slider_max = self.driver.find_element(*ProductFilter.price_slider_max_xpath)

        self.driver.execute_script("arguments[0].setAttribute('style', 'left: 5%;')",
                                   self.driver.find_element(slider_min))
        self.driver.execute_script("arguments[0].setAttribute('style', 'right: 14%;')",
                                   self.driver.find_element(slider_max))

        # self.action.drag_and_drop_by_offset(slider_min, offset_min, 0).perform()
        # self.action.drag_and_drop_by_offset(slider_max, offset_max, 0).perform()

    def get_all_product_prices(self):
        time.sleep(5)
        # self.wait.until(EC.presence_of_all_elements_located(*ProductFilter.product_price_css_selector))
        prices = self.driver.find_element(*ProductFilter.product_price_css_selector)
        return prices

    def get_all_product_title(self):
        return [pt.text for pt in self.driver.find_element(*ProductFilter.product_title_css_selector)]
