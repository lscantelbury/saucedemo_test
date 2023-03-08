from pages.home_page import HomePage
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import unittest
from time import sleep

class HomePageTest(unittest.TestCase):
    def setUp(self):
        self.service = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=self.service)
        self.home_page = HomePage(browser=self.browser)

    def test_products_are_visible(self):
        products = self.home_page.inventory_items

        self.assertTrue(products.is_displayed())

    def test_menu_toggle(self):
        menu = self.home_page.browser.find_element(By.XPATH, '//*[@id="menu_button_container"]/div/div[2]')

        hidden = lambda : menu.get_attribute('aria-hidden') == 'true'
        
        self.assertTrue(hidden())

        self.home_page.click_menu_button()

        self.assertFalse(hidden())

    def test_add_to_cart(self):
        self.home_page.click_add_to_cart_button()

        amount_of_items = self.browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a/span')

        self.assertTrue(amount_of_items.is_displayed())

    def test_sort_button(self):

        self.home_page.click_sort_button(option=1)

        first_inventory_item = lambda : self.browser.find_element('xpath', '//*[@id="inventory_container"]/div/div[1]/div[2]/div[1]/a/div').text

        self.assertEqual(first_inventory_item(), 'Sauce Labs Backpack')

        self.home_page.click_sort_button(option=2)

        self.assertEqual(first_inventory_item(), 'Test.allTheThings() T-Shirt (Red)')

        self.home_page.click_sort_button(option=3)

        self.assertEqual(first_inventory_item(), 'Sauce Labs Onesie')

        self.home_page.click_sort_button(option=4)

        self.assertEqual(first_inventory_item(), 'Sauce Labs Fleece Jacket')

if __name__ == '__name__':
    unittest.main()
