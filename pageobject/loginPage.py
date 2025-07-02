from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Login:
    login_tab_link_text = (By.LINK_TEXT, "Log in")
    enter_email_id = (By.ID, "Email")
    enter_password_id = (By.ID, "Password")
    click_password_eye_xpath = (By.XPATH, "//div[@class='login-password']/span")
    click_on_remember_me_id = (By.ID, "RememberMe")
    click_on_forgot_password_link_text = (By.LINK_TEXT, "Forgot password?")
    click_on_login_button_xpath = (By.XPATH, "button-1 login-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_login_link(self):
        self.driver.find_element(*Login.login_tab_link_text).click()

    def enter_emil_password(self, email, pwd):
        self.driver.find_element(*Login.enter_password_id).send_keys(email)
        self.driver.find_element(*Login.enter_password_id).send_keys(pwd)

    def click_on_password_eye(self):
        self.driver.find_element(*Login.click_password_eye_xpath).click()

    def click_on_remember_me(self):
        self.driver.find_element(*Login.click_on_remember_me_id).click()

    def click_on_forget_password(self):
        self.driver.find_element(*Login.click_on_forgot_password_link_text).click()

    def click_on_login_button(self):
        self.driver.find_element(*Login.click_on_login_button_xpath).click()
