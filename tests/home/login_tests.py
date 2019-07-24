from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
import unittest
import pytest


class LoginTests(unittest.TestCase):

    base_url = 'https://learn.letskodeit.com'
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    login_page = LoginPage(driver)

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.driver.get(self.base_url)
        self.login_page.login('wrong@email.com', 'wrongpassword')
        result = self.login_page.verify_login_failure()
        assert result is True

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.login_page.login('koki.wadas@gmail.com', 'Sheffield1')
        result = self.login_page.verify_login_success()
        assert result is True
        self.driver.quit()

