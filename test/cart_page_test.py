import re
from pages.home_page import HomePage
from pages.cart_page import CartPage
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

    def test_checkout_with_empty_cart(self):
        self.home_page.click_cart_button()

        cart_page = CartPage(self.browser)

        cart_page.click_checkout_button()

        cart_page.set_firstname_textfield('First')
        cart_page.set_last_textfield('Last')
        cart_page.set_zip_textfield('123')

        cart_page.click_continue_button()

        cart_page.click_finish_button()

        checkout_complete_label = self.browser.find_element(By.XPATH, CartPageLocators.checkout_complete_label)

        self.assertFalse(checkout_complete_label.is_displayed())

    def test_textfield_validation(self):
        self.home_page.click_cart_button()

        cart_page = CartPage(self.browser)

        cart_page.click_checkout_button()

        error_label = lambda : self.browser.find_element(By.XPATH, CartPageLocators.error_label)

        cart_page.click_continue_button()

        self.assertTrue(error_label().is_displayed())

        cart_page.set_firstname_textfield('First')
        cart_page.set_last_textfield('Last')

        cart_page.click_continue_button()

        self.assertTrue(error_label().is_displayed())

    def test_price_is_correct(self):
        self.home_page.click_add_to_cart_button()
        self.home_page.click_cart_button()

        cart_page = CartPage(self.browser)

        cart_page.click_checkout_button()

        cart_page.set_firstname_textfield('First')
        cart_page.set_last_textfield('Last')
        cart_page.set_zip_textfield('123')

        cart_page.click_continue_button()

        item_price = self.browser.find_element(By.XPATH, CartPageLocators.item_price).text
        item_price = float(re.findall(r'\d+\.\d+', item_price)[0])

        tax_price = self.browser.find_element(By.XPATH, CartPageLocators.tax_price).text
        tax_price = float(re.findall(r'\d+\.\d+', tax_price)[0])

        total_price = self.browser.find_element(By.XPATH, CartPageLocators.total_price).text
        total_price = float(re.findall(r'\d+\.\d+', total_price)[0])

        self.assertEqual((item_price + tax_price),total_price)
        

        
if __name__ == '__name__':
    unittest.main()
