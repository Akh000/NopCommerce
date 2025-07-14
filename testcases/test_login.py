from pageobject.loginPage import Login
from Utilities.logs import LogGenerator
import pytest


class Test_login:
    log = LogGenerator.loggen()

    @pytest.mark.skip
    @pytest.mark.parametrize("email,password",
                             [('akhman@gmail.com', 'Akh123'),
                              ('akhman@gmail.com', 'akh123'),
                              ('ak@gmail.com', 'Akh123'),
                              ('akhm@gmail.com', 'ak123')])
    def test_login_002(self, setup, email, password):
        self.driver = setup
        self.log.info("Opening browser with NopCommerce website")
        self.lg = Login(self.driver)
        self.log.info("Click on login tab/link")
        self.lg.click_login_link()
        self.log.info(f"Enter email {email} and password {password}")
        self.lg.enter_emil_password(email, password)
        self.log.info("Click on Login button")
        self.lg.click_on_login_button()
