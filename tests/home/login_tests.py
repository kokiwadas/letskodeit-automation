from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest


class LoginTests(unittest.TestCase):

    def test_valid_login(self):
        base_url = 'https://learn.letskodeit.com'
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(base_url)
        driver.implicitly_wait(10)

        login_page = LoginPage(driver)
        login_page.login('koki.wadas@gmail.com', 'Sheffield1')

        confirm_button = driver.find_element(By.XPATH, "//form[@id='new_user']//input[@name='commit']")
        confirm_button.click()

        user_icon = driver.find_element(By.XPATH, f"//*[@id='navbar']//li[4]/a/img")

        if user_icon is not None:
            print('Login successful!')
        else:
            print('Login failed')


tt = LoginTests()
tt.test_valid_login()
