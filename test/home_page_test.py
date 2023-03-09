from pages.home_page import HomePage
from selenium.webdriver.common.by import By
from resources.home_page_locators import HomePageLocators
from resources.login_page_locators import LoginPageLocators
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import unittest

class HomePageTest(unittest.TestCase):
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

    def test_products_are_visible(self):
        products = self.home_page.inventory_items()

        self.assertTrue(products.is_displayed())

    def test_menu_toggle(self):
        menu = self.home_page.browser.find_element(By.XPATH, HomePageLocators.menu)

        hidden = lambda : menu.get_attribute('aria-hidden') == 'true'
        
        self.assertTrue(hidden())

        self.home_page.click_menu_button()

        self.assertFalse(hidden())

    def test_add_to_cart(self):
        self.home_page.click_add_to_cart_button()

        amount_of_items = self.browser.find_element(By.XPATH, HomePageLocators.amount_of_items_at_cart)

        self.assertTrue(amount_of_items.is_displayed())

    def test_sort_button(self):

        self.home_page.click_sort_button(option=1)

        first_inventory_item = lambda : self.browser.find_element(By.XPATH, HomePageLocators.first_inventory_item).text

        self.assertEqual(first_inventory_item(), 'Sauce Labs Backpack')

        self.home_page.click_sort_button(option=2)

        self.assertEqual(first_inventory_item(), 'Test.allTheThings() T-Shirt (Red)')

        self.home_page.click_sort_button(option=3)

        self.assertEqual(first_inventory_item(), 'Sauce Labs Onesie')

        self.home_page.click_sort_button(option=4)

        self.assertEqual(first_inventory_item(), 'Sauce Labs Fleece Jacket')

if __name__ == '__name__':
    unittest.main()
