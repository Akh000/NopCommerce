import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Register:
    register_link_text = (By.LINK_TEXT, "Register")
    register_page_title_xpath = (By.XPATH, "//div[@class= 'page-title']")
    select_male_id = (By.ID, "gender-male")
    select_female_id = (By.ID, "gender-female")
    enter_first_name_id = (By.ID, "FirstName")
    enter_last_name_id = (By.ID, "LastName")
    enter_email_id = (By.ID, "Email")
    enter_company_name_id = (By.ID, "Company")
    tick_on_newsletter_id = (By.ID, "Newsletter")
    enter_password_id = (By.ID, "Password")
    enter_confirm_password_id = (By.ID, "ConfirmPassword")
    click_on_register_button_xpath = (By.XPATH, "//button[@name='register-button']")
    text_msg_registration_complete_xpath = (By.XPATH, "//div[@class='result']")
    logout_link_text = (By.LINK_TEXT, "Log out")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_Register_link(self):
        self.driver.find_element(*Register.register_link_text).click()
        # time.sleep(2)
        # self.wait.until(EC.visibility_of_element_located(*Register.register_page_title_xpath))

    def select_gender(self, gender):
        if gender == 'Null':
            pass
        else:
            if gender == 'm' or gender == 'M':
                self.driver.find_element(*Register.select_male_id).click()
            elif gender == 'f' or gender == 'F':
                self.driver.find_element(*Register.select_female_id).click()
            else:
                print('Gender Not Selected')

    def enter_personal_info(self, first_name, last_name, email, company_name):
        if first_name == 'Null':
            pass
        else:
            self.driver.find_element(*Register.enter_first_name_id).send_keys(first_name)
        if last_name == 'Null':
            pass
        else:
            self.driver.find_element(*Register.enter_last_name_id).send_keys(last_name)

        if email == 'Null':
            pass
        else:
            self.driver.find_element(*Register.enter_email_id).send_keys(email)
        if company_name == 'Null':
            pass
        else:
            self.driver.find_element(*Register.enter_company_name_id).send_keys(company_name)

    def tick_on_newsletter(self):
        self.driver.find_element(*Register.tick_on_newsletter_id).click()

    def enter_password_confirm_password(self, pwd, cnp):
        if pwd == 'Null':
            pass
        else:
            self.driver.find_element(*Register.enter_password_id).send_keys(pwd)
        if cnp == 'Null':
            pass
        else:
            self.driver.find_element(*Register.enter_confirm_password_id).send_keys(cnp)

    def click_on_register_button(self):
        self.driver.find_element(*Register.click_on_register_button_xpath).click()
        time.sleep(5)
        # self.wait.until(EC.element_located_to_be_selected(*Register.text_msg_registration_complete_xpath))
        try:
            msg = self.driver.find_element(*Register.text_msg_registration_complete_xpath).text
            return msg
        except:
            return False

    def click_on_logout_link(self):
        self.driver.find_element(*Register.logout_link_text).click()