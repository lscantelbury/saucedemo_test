from pages.home_page import HomePage
from selenium.webdriver.common.by import By
from resources.home_page_locators import HomePageLocators
from resources.login_page_locators import LoginPageLocators
from resources.cart_page_locators import CartPageLocators
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import unittest

class CartPageTest(unittest.TestCase):
    def setUp(self):
        self.service = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=self.service)

        self.browser.get('https://www.saucedemo.com/')

        username_textfield = self.browser.find_element(By.XPATH, LoginPageLocators.username_textfield)
        username_textfield.send_keys('standard_user')

        password_textfield = self.browser.find_element(By.XPATH, LoginPageLocators.password_textfield)
        password_textfield.send_keys('secret_sauce')

        login_button = self.browser.find_element(By.XPATH, LoginPageLocators.login_button)
        login_button.click()

        self.home_page = HomePage(browser=self.browser)

    def test_item_added_to_cart_is_correct(self):
        self.home_page.click_add_to_cart_button()

        first_inventory_item_name = self.browser.find_element(By.XPATH, HomePageLocators.first_inventory_item_name).text

        self.home_page.click_cart_button()

        item_at_cart = self.browser.find_element(By.XPATH, CartPageLocators.item_at_cart_name).text

        self.assertEqual(first_inventory_item_name, item_at_cart)


if __name__ == '__name__':
    unittest.main()
