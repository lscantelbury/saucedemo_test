from pages.login_page import LoginPage
from resources.login_page_locators import LoginPageLocators
from resources.home_page_locators import HomePageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import unittest

class LoginPageTest(unittest.TestCase):
    def setUp(self):
        self.service = Service(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=self.service)
        self.login_page = LoginPage(browser=browser)

    def test_unsucessfull_login(self):
        self.login_page.set_username('standard_user')
        self.login_page.set_password('invalid_password')
        self.login_page.click_login_button()

        error_label = self.login_page.browser.find_element(By.XPATH, LoginPageLocators.error_label)

        self.assertTrue(error_label.is_displayed())

    def test_sucessfull_login(self):
        self.login_page.set_username('standard_user')
        self.login_page.set_password('secret_sauce')
        self.login_page.click_login_button()

        products_label = self.login_page.browser.find_element(By.XPATH, HomePageLocators.products_label)

        self.assertTrue(products_label.is_displayed())

if __name__ == '__name__':
    unittest.main()