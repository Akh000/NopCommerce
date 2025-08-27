import os
import pytest
from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from Utilities.logs import LogGenerator
from pageobject.searchPage import Search


@pytest.mark.smoke
class TestSearchFunctionality:
    log = LogGenerator.loggen()
    file = os.path.abspath("testdata/NopCommerce_Registration.xlsx")

    def test_search_valid_product(self,setup):
        self.driver = setup
        self.log.info("Opening Browser")
        self.svp = Search(self.driver)
        self.log.info("Input Search Item")
        self.svp.search_input('laptop')
        self.log.info("Click on search button")
        self.svp.search_button()
        assert 'laptop' in self.driver.current_url.lower()
        assert ('nopCommerce demo store. Search' == self.driver.title) or "No products were found"

    def test_search_empty_input(self,setup):
        self.driver = setup
        self.log.info("Opening Browser")
        self.sei = Search(self.driver)
        self.log.info("Input Search Item")
        self.sei.search_input('')
        self.log.info("Click on search button")
        self.sei.search_button()
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print("Alert Text", alert_text)
            assert alert_text == "Please enter some search keyword", "Alert text mismatch"
            alert.accept()
        except NoAlertPresentException:
            pytest.fail("Alert not present when expected.")

    def test_search_invalid_product(self, setup):
        self.driver = setup
        self.log.info("Opening Browser")
        self.sip = Search(self.driver)
        self.log.info("Input Search Item")
        self.sip.search_input('xyz123')
        self.log.info("Click on search button")
        self.sip.search_button()
        assert self.driver.find_element(By.XPATH, "//div[@class='no-result']").text == ("No products were found that "
                                                                                        "matched your criteria.")

    def test_search_partial_keyword(self, setup):
        self.driver = setup
        self.log.info("Opening Browser")
        self.spk = Search(self.driver)
        self.log.info("Input Search Item")
        self.spk.search_input('lap')
        self.log.info("Click on search button")
        self.spk.search_button()
        assert "search?q=lap" in self.driver.current_url.lower()

    def test_search_special_keyword(self, setup):
        self.driver = setup
        self.log.info("Opening Browser")
        self.s_spk = Search(self.driver)
        self.log.info("Input Search Item")
        self.s_spk.search_input('@#$%^')
        self.log.info("Click on search button")
        self.s_spk.search_button()
        assert self.driver.find_element(By.XPATH, "//div[@class='no-result']").text == ("No products were found that "
                                                                                        "matched your criteria.")

    def test_search_whitespace(self, setup):
        self.driver = setup
        self.log.info("Opening Browser")
        self.sws = Search(self.driver)
        self.log.info("Input Search Item")
        self.sws.search_input('    ')
        self.log.info("Click on search button")
        self.sws.search_button()
        assert self.driver.find_element(By.XPATH, "//div[@class='no-result']").text == ("Search term minimum length is "
                                                                                        "3 characters")
