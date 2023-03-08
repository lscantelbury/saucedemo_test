from login_page.login_page import LoginPage
from selenium import webdriver
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

        error_text = self.login_page.browser.find_element('xpath', '//*[@id="login_button_container"]/div/form/div[3]/h3')

        self.assertTrue(error_text.is_displayed())

    def test_sucessfull_login(self):
        self.login_page.set_username('standard_user')
        self.login_page.set_password('secret_sauce')
        self.login_page.click_login_button()

        products_label = self.login_page.browser.find_element('xpath', '//*[@id="header_container"]/div[2]/span')

        self.assertTrue(products_label.is_displayed())

if __name__ == '__name__':
    unittest.main()