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

        result = login_page.verify_login_success()
        assert result is True

        driver.quit()


tt = LoginTests()
tt.test_valid_login()
