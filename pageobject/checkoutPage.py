from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Checkout:
    add_to_card_product_xpath = (By.XPATH, "//a[contains(text(),'Asus Laptop')]/following::button[contains(text(),"
                                           "'Add to cart')][1]")
    shopping_cart_link_xpath = (By.XPATH, "//li[@id='topcartlink']/a")
    quantity_up_id = (By.ID, "quantity-up-5")
    quantity_down_id = (By.ID, "quantity-down-5")
    continue_shopping_xpath = (By.XPATH, "//button[contains(text(),'Continue shopping')]")
    estimate_shipping_id = (By.XPATH, "open-estimate-shipping-popup")
    select_gift_wrapping_id = (By.ID, "open-estimate-shipping-popup")
    terms_agree_checkbox_id = (By.ID, "termsofservice")
    checkout_button_id = (By.ID, "checkout")
    cart_total_xpath = (By.XPATH, "//table[@class='cart-total']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait

    def 

# product_price = //table[@class='cart']/tbody/tr[1]/td[4]/span[@class='product-unit-price']
# total_price = //table[@class='cart']/tbody/tr[1]/td[6]/span[@class='product-unit-price']
