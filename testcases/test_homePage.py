import time

import pytest
from Utilities.logs import LogGenerator
from pageobject.homePage import Home


class TestHomePage:
    log = LogGenerator.loggen()

    # def __init__(self, setup):
    #     self.driver = setup

    def test_navigation_register_page(self, setup):
        self.driver = setup
        self.log.info("Opening website")
        self.hp = Home(self.driver)
        self.log.info("Click on Register link")
        self.hp.click_register_link()
        assert 'register' in self.driver.current_url.lower()

    def test_navigate_login_page(self, setup):
        self.driver = setup
        self.log.info("Opening website")
        self.lg = Home(self.driver)
        self.log.info("Click on Login link")
        self.lg.click_login_link()

    def test_wishlist(self, setup):
        self.driver = setup
        self.log.info("Opening website")
        self.wl = Home(self.driver)
        self.log.info("click on wishlist")
        self.wl.click_wishlist()
        assert 'wishlist' in self.driver.current_url.lower()

    def test_shopping_cart(self, setup):
        self.driver = setup
        self.log.info("Opening website")
        self.sc = Home(self.driver)
        self.log.info("click on shopping cart link")
        assert self.sc.shopping_cart() == "Shopping cart"

    def test_logo_visibility(self, setup):
        self.driver = setup
        self.log.info("Opening website")
        self.logo = Home(self.driver)
        self.log.info("Visibility of project Logo")
        assert self.logo.is_logo_visible()

    def test_search_product(self, setup):
        self.driver = setup
        self.log.info("Opening website")
        self.sp = Home(self.driver)
        self.log.info("Search box is present and Clickable")
        self.sp.is_search_input_clickable('mobile')
        self.log.info("Click on Search Button")
        self.sp.click_on_search_button()
        assert 'mobile' in self.driver.current_url.lower()


class Test_Top_Menu:
    log = LogGenerator.loggen()

    def test_top_menu_computer(self,setup):
        self.driver = setup
        self.log.info("Opening website")
        self.tm = Home(self.driver)
        self.log.info("Get the list of menu")
        self.tm.top_menu_computers()
        assert 'computers' in self.driver.current_url.lower()

    def test_sub_menu_computer_desktop(self,setup):
        self.driver = setup
        self.log.info("Opening website")
        self.tm = Home(self.driver)
        self.tm.sub_menu_computer_desktop()
        assert 'desktops' in self.driver.current_url.lower()

    def test_sub_menu_computer_notebooks(self, setup):
        self.driver = setup
        self.log.info("Opening website")
        self.tm = Home(self.driver)
        self.tm.sub_menu_computer_notebooks()
        assert 'notebooks' in self.driver.current_url.lower()

    def test_sub_menu_computer_software(self, setup):
        self.driver = setup
        self.log.info("Opening website")
        self.tm = Home(self.driver)
        self.tm.sub_menu_computer_software()
        assert 'software' in self.driver.current_url.lower()

    def test_top_menu_electronic(self,setup):
        self.driver = setup
        self.log.info("Opening website")
        self.tm = Home(self.driver)
        self.log.info("Get the list of menu")
        self.tm.top_menu_electronic()
        assert 'electronics' in self.driver.current_url.lower()

    def test_sub_menu_electronic_camera_photo(self,setup):
        self.driver = setup
        self.log.info("Opening website")
        self.tm = Home(self.driver)
        self.tm.sub_menu_electronic_camera_photo()
        assert 'camera-photo' in self.driver.current_url.lower()

    def test_sub_menu_electronic_cell_phone(self, setup):
        self.driver = setup
        self.log.info("Opening website")
        self.tm = Home(self.driver)
        self.tm.sub_menu_electronic_cell_phones()
        assert 'cell-phones' in self.driver.current_url.lower()

    def test_sub_menu_electronic_others(self, setup):
        self.driver = setup
        self.log.info("Opening website")
        self.tm = Home(self.driver)
        self.tm.sub_menu_electronic_others()
        assert 'others' in self.driver.current_url.lower()

    def test_top_menu_apparel(self,setup):
        self.driver = setup
        self.log.info("Opening website")
        self.tm = Home(self.driver)
        self.log.info("Get the list of menu")
        self.tm.top_menu_apparel()
        assert 'apparel' in self.driver.current_url.lower()

    def test_sub_menu_apparel_shoes(self,setup):
        self.driver = setup
        self.log.info("Opening website")
        self.tm = Home(self.driver)
        self.tm.sub_menu_apparel_shoes()
        assert 'shoes' in self.driver.current_url.lower()

    def test_sub_menu_apparel_clothing(self, setup):
        self.driver = setup
        self.log.info("Opening website")
        self.tm = Home(self.driver)
        self.tm.sub_menu_apparel_clothing()
        assert 'clothing' in self.driver.current_url.lower()

    def test_sub_menu_apparel_accessories(self, setup):
        self.driver = setup
        self.log.info("Opening website")
        self.tm = Home(self.driver)
        self.tm.sub_menu_apparel_accessories()
        assert 'accessories' in self.driver.current_url.lower()

    def test_top_menu_digital_download(self,setup):
        self.driver = setup
        self.log.info("Opening website")
        self.tm = Home(self.driver)
        self.log.info("Get the list of menu")
        self.tm.top_menu_digital_download()
        assert 'digital-downloads' in self.driver.current_url.lower()

    def test_top_menu_books(self,setup):
        self.driver = setup
        self.log.info("Opening website")
        self.tm = Home(self.driver)
        self.log.info("Get the list of menu")
        self.tm.top_menu_books()
        assert 'books' in self.driver.current_url.lower()

    def test_top_menu_jewelry(self,setup):
        self.driver = setup
        self.log.info("Opening website")
        self.tm = Home(self.driver)
        self.log.info("Get the list of menu")
        self.tm.top_menu_jewelry()
        assert 'jewelry' in self.driver.current_url.lower()

    def test_top_menu_gift_cards(self,setup):
        self.driver = setup
        self.log.info("Opening website")
        self.tm = Home(self.driver)
        self.log.info("Get the list of menu")
        self.tm.top_menu_gift_cards()
        assert 'gift-cards' in self.driver.current_url.lower()
