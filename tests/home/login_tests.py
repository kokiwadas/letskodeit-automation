from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class LoginTests:

    def test_valid_login(self):
        base_url = 'https://learn.letskodeit.com'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(10)

        login_button = driver.find_element(By.XPATH, "//div[@id='navbar']//a[@href='/sign_in']")
        login_button.click()

        email_input_field = driver.find_element(By.ID, "user_email")
        user_email = 'koki.wadas@gmail.com'
        email_input_field.send_keys(user_email)

        password_input_field = driver.find_element(By.ID, 'user_password')
        user_password = 'Sheffield1'
        password_input_field.send_keys(user_password)

        confirm_button = driver.find_element(By.XPATH, "//form[@id='new_user']//input[@name='commit']")
        confirm_button.click()

        user_icon = driver.find_element(By.XPATH, f"//*[@id='navbar']//li[4]/a/img")

        if user_icon is not None:
            print('Login successful!')
        else:
            print('Login failed')


tt = LoginTests()
tt.test_valid_login()
