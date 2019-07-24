from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    _login_link = "//div[@id='navbar']//a[@href='/sign_in']"
    _email_field = "user_email"
    _password_field = "user_password"
    _confirm_button = "//form[@id='new_user']//input[@name='commit']"

    def get_login_link(self):
        return self.driver.find_element(By.XPATH, self._login_link)

    def get_email_field(self):
        return self.driver.find_element(By.ID, self._email_field)

    def get_password_field(self):
        return self.driver.find_element(By.ID, self._password_field)

    def get_confirm_button(self):
        return self.driver.find_element(By.ID, self._confirm_button)

    def click_login_link(self):
        self.get_login_link().click()

    def enter_email(self, user_email):
        self.get_email_field().send_keys(user_email)

    def enter_password(self, user_password):
        self.get_password_field().send_keys(user_password)

    def click_confirm_button(self):
        self.get_confirm_button().click()

    def login(self, user_email, user_password):
        self.click_login_link()
        self.enter_email(user_email)
        self.enter_password(user_password)
        self.click_confirm_button()

