from selenium import webdriver
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class LoginPage(SeleniumDriver):

    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "//div[@id='navbar']//a[@href='/sign_in']"
    _email_field = "user_email"
    _password_field = "user_password"
    _confirm_button = "//form[@id='new_user']//input[@name='commit']"

    # def get_login_link(self):
    #     return self.driver.find_element(By.XPATH, self._login_link)
    #
    # def get_email_field(self):
    #     return self.driver.find_element(By.ID, self._email_field)
    #
    # def get_password_field(self):
    #     return self.driver.find_element(By.ID, self._password_field)
    #
    # def get_confirm_button(self):
    #     return self.driver.find_element(By.ID, self._confirm_button)

    def click_login_link(self):
        self.element_click(self._login_link, locator_type='xpath')

    def enter_email(self, user_email):
        self.send_chars(user_email, self._email_field, locator_type='id')

    def enter_password(self, user_password):
        self.send_chars(user_password, self._password_field, locator_type='id')

    def click_confirm_button(self):
        self.element_click(self._confirm_button, locator_type='xpath')

    def login(self, user_email='', user_password=''):
        self.click_login_link()
        self.enter_email('')
        self.enter_email(user_email)
        self.enter_password(user_password)
        self.click_confirm_button()

    def verify_login_success(self):
        result = self.is_element_present("//*[@id='navbar']//li[4]/a/img", locator_type='xpath')
        return result

    def verify_login_failure(self):
        result = self.is_element_present("//body//div[contains(text(), 'Invalid email or password.')]",
                                         locator_type='xpath')
        return result
