import os
import pytest
from Utilities.logs import LogGenerator
from pageobject.productPage import ProductFilter
from pageobject.searchPage import Search


@pytest.mark.filter
class Test_Product_filter:
    log = LogGenerator.loggen()
    file = os.path.abspath("testdata/NopCommerce_Registration.xlsx")

    def test_filter_product_by_price(self, setup):
        self.driver = setup
        self.log.info("Opening Browser")
        self.pf = ProductFilter(self.driver)
        # self.sp = Search(self.driver)
        self.log.info("Search product laptop")
        # self.sp.search_input('laptop')
        self.log.info("Click on search button")
        # self.sp.search_button()
        self.log.info("adjust to set price slider between $500-$1400")
        self.pf.adjust_price_slider()
        self.log.info("Get all product prices")
        product_prices = self.pf.get_all_product_prices()
        print(product_prices)
        product_name = self.pf.get_all_product_title()
        print(product_name)