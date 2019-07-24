from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login(self, user_email, user_password):
        login_button = self.driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        login_button.click()

        email_input_field = self.driver.find_element(By.ID, "user_email")
        email_input_field.send_keys(user_email)

        password_input_field = self.driver.find_element(By.ID, 'user_password')
        password_input_field.send_keys(user_password)
