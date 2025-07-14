import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Home:
    # locators
    currency_list_id = (By.ID, "customerCurrency")
    register_link_text = (By.LINK_TEXT, "Register")
    login_link_text = (By.LINK_TEXT, "Log in")
    wish_list_xpath = (By.XPATH, "//span[text()='Wishlist']")
    shopping_cart_xpath = (By.XPATH, "//span[contains(text(),'Shopping cart')]")
    header_logo_xpath = (By.XPATH, "//div[@class='header-logo']/a/img")
    search_input_id = (By.ID, "small-searchterms")
    search_button_xpath = (By.XPATH, "//button[contains(text(),'Search')]")

    # Top menu locators
    computers_link_text = (By.XPATH,"//ul[@class='top-menu notmobile']/li[1]/a[contains(text(),'Computers ')]")
    electronic_link_text = (By.XPATH, "//ul[@class='top-menu notmobile']/li[2]/a[contains(text(),'Electronics ')]")
    apparel_link_text = (By.LINK_TEXT, "//ul[@class='top-menu notmobile']/li[3]/a[contains(text(),'Apparel ')]")
    digital_downloads_link_text = (By.LINK_TEXT, "//ul[@class='top-menu notmobile']/li[4]/a[contains(text(),'Digital "
                                                 "downloads ')]")
    books_link_text = (By.LINK_TEXT, "//ul[@class='top-menu notmobile']/li[5]/a[contains(text(),'Books ')]")
    jewelry_link_text = (By.LINK_TEXT, "//ul[@class='top-menu notmobile']/li[6]/a[contains(text(),'Jewelry ')]")
    gift_cards_link_text = (By.LINK_TEXT, "//ul[@class='top-menu notmobile']/li[7]/a[contains(text(),'Gift Cards ')]")

    # Top sub menu locators
    desktops_xpath = (By.XPATH,"//ul[@class='top-menu notmobile']/li[1]/ul/li[1]/a")
    notebooks_xpath  = (By.XPATH,"//ul[@class='top-menu notmobile']/li[1]/ul/li[2]/a")
    software_xpath = (By.XPATH,"//ul[@class='top-menu notmobile']/li[1]/ul/li[3]/a")
    camera_photos_xpath = (By.XPATH,"//ul[@class='top-menu notmobile']/li[2]/ul/li[1]/a")
    cell_phones_xpath = (By.XPATH,"//ul[@class='top-menu notmobile']/li[2]/ul/li[1]/a")
    others_xpath = (By.XPATH,"//ul[@class='top-menu notmobile']/li[2]/ul/li[1]/a")
    shoes_xpath = (By.XPATH,"//ul[@class='top-menu notmobile']/li[3]/ul/li[1]/a")
    clothing_xpath = (By.XPATH,"//ul[@class='top-menu notmobile']/li[3]/ul/li[1]/a")
    accessories_xpath = (By.XPATH,"//ul[@class='top-menu notmobile']/li[3]/ul/li[1]/a")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait
        self.action = ActionChains(driver)

    # def is_currency_list_clickable(self, curr):
    #     if  currency == curr:

    def click_register_link(self):
        self.driver.find_element(*Home.register_link_text).click()

    def click_login_link(self):
        self.driver.find_element(*Home.login_link_text).click()

    def click_wishlist(self):
        self.driver.find_element(*Home.wish_list_xpath).click()

    def shopping_cart(self):
        self.driver.find_element(*Home.shopping_cart_xpath).click()
        text = self.driver.find_element(By.XPATH, "//div[@class='page-title']/h1").text
        return text

    def is_logo_visible(self):
        header_logo = self.driver.find_element(*Home.header_logo_xpath).is_displayed()
        return header_logo

    def is_search_input_clickable(self, search_product):
        self.driver.find_element(*Home.search_input_id).clear()
        self.driver.find_element(*Home.search_input_id).send_keys(search_product)

    def click_on_search_button(self):
        self.driver.find_element(*Home.search_button_xpath).click()

    # Top Menu and Sub-Menu
    def top_menu_computers(self):
        computer = self.driver.find_element(*Home.computers_link_text)
        self.action.move_to_element(computer).click().perform()

    def sub_menu_computer_desktop(self):
        computer = self.driver.find_element(*Home.computers_link_text)
        desktop = self.driver.find_element(*Home.desktops_xpath)
        self.action.move_to_element(computer).move_to_element(desktop).click().perform()

    def sub_menu_computer_notebooks(self):
        computer = self.driver.find_element(*Home.computers_link_text)
        notebooks = self.driver.find_element(*Home.notebooks_xpath)
        self.action.move_to_element(computer).move_to_element(notebooks).click().perform()

    def sub_menu_computer_software(self):
        computer = self.driver.find_element(*Home.computers_link_text)
        software = self.driver.find_element(*Home.desktops_xpath)
        self.action.move_to_element(computer).move_to_element(software).click().perform()

    def top_menu_electronic(self):
        electronic = self.driver.find_element(*Home.electronic_link_text)
        self.action.move_to_element(electronic).click().perform()

    def sub_menu_electronic_camera_photo(self):
        electronic = self.driver.find_element(*Home.electronic_link_text)
        camera_photo = self.driver.find_element(*Home.camera_photos_xpath)
        self.action.move_to_element(electronic).move_to_element(camera_photo).click().perform()

    def sub_menu_electronic_cell_phones(self):
        electronic = self.driver.find_element(*Home.electronic_link_text)
        cell_phones = self.driver.find_element(*Home.cell_phones_xpath)
        self.action.move_to_element(electronic).move_to_element(cell_phones).click().perform()

    def sub_menu_electronic_others(self):
        electronic = self.driver.find_element(*Home.electronic_link_text)
        others = self.driver.find_element(*Home.others_xpath)
        self.action.move_to_element(electronic).move_to_element(others).click().perform()

    def top_menu_apparel(self):
        apparel = self.driver.find_element(*Home.apparel_link_text)
        self.action.move_to_element(apparel).click().perform()

    def sub_menu_apparel_shoes(self):
        apparel = self.driver.find_element(*Home.apparel_link_text)
        shoes = self.driver.find_element(*Home.shoes_xpath)
        self.action.move_to_element(apparel).move_to_element(shoes).click().perform()

    def sub_menu_apparel_clothing(self):
        apparel = self.driver.find_element(*Home.apparel_link_text)
        clothing = self.driver.find_element(*Home.clothing_xpath)
        self.action.move_to_element(apparel).move_to_element(clothing).click().perform()

    def sub_menu_apparel_accessories(self):
        apparel = self.driver.find_element(*Home.apparel_link_text)
        accessories = self.driver.find_element(*Home.accessories_xpath)
        self.action.move_to_element(apparel).move_to_element(accessories).click().perform()

    def top_menu_digital_download(self):
        digital_download = self.driver.find_element(*Home.digital_downloads_link_text)
        self.action.move_to_element(digital_download).click().perform()

    def top_menu_books(self):
        books = self.driver.find_element(*Home.books_link_text)
        self.action.move_to_element(books).click().perform()

    def top_menu_jewelry(self):
        jewelry = self.driver.find_element(*Home.jewelry_link_text)
        self.action.move_to_element(jewelry).click().perform()

    def top_menu_gift_cards(self):
        gift_card = self.driver.find_element(*Home.gift_cards_link_text)
        self.action.move_to_element(gift_card).click().perform()



# //ul[@class='top-menu notmobile']/li/a[contains(text(),'Computers ')]/parent::li[1]/ul/li[1]