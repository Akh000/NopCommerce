import pytest

from pageobject.registerPage import Register
from Utilities.logs import LogGenerator
from Utilities import XLUtils
import os


class Test_Register:
    log = LogGenerator.loggen()
    file = os.path.abspath("testdata/NopCommerce_Registration.xlsx")
    expected_result = []
    actual_result = []

    @pytest.mark.skip
    def test_register_01(self, setup):
        self.log.info("Opening Browser with NopCommerce")
        self.driver = setup
        self.reg = Register(self.driver)
        self.log.info("Click on Register tab/link")
        self.reg.click_Register_link()
        self.log.info("Getting Data from Excel sheet ")
        no_of_rows = XLUtils.RowCount(self.file, 'Sheet1')
        for row in range(2, no_of_rows + 1):
            gender = XLUtils.ReadData(self.file, 'Sheet1', row, 1)
            first_name = XLUtils.ReadData(self.file, 'Sheet1', row, 2)
            last_name = XLUtils.ReadData(self.file, 'Sheet1', row, 3)
            email = XLUtils.ReadData(self.file, 'Sheet1', row, 4)
            company_name = XLUtils.ReadData(self.file, 'Sheet1', row, 5)
            password = XLUtils.ReadData(self.file, 'Sheet1', row, 6)
            confirm_password = XLUtils.ReadData(self.file, 'Sheet1', row, 7)
            expectedResult = XLUtils.ReadData(self.file, 'Sheet1', row, 8)
            self.expected_result.append(expectedResult)
            self.log.info("Click on Gender")
            self.reg.select_gender(gender)
            self.log.info(f"Enter personal Info {first_name}, {last_name}, {email}, {company_name}")
            self.reg.enter_personal_info(first_name, last_name, email, company_name)
            # self.reg.tick_on_newsletter()
            self.log.info("Enter password and confirm Password")
            self.reg.enter_password_confirm_password(password, confirm_password)
            self.log.info("Enter Register Button")
            success_msg = self.reg.click_on_register_button()
            if success_msg == 'Your registration completed':
                XLUtils.WriteData(self.file, 'Sheet1', row, 9, 'Pass')
                self.actual_result.append('Pass')
                self.reg.click_on_logout_link()
                self.log.info("Click on Register tab/link")
            else:
                self.driver.save_screenshot(os.path.abspath(f"Screenshots/fail_{first_name+last_name}.png"))
                XLUtils.WriteData(self.file, 'Sheet1', row, 9, 'Fail')
                self.actual_result.append('Fail')
        if self.expected_result == self.actual_result:
            assert True
        else:
            assert False