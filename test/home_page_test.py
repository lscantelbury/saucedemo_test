from home_page.home_page import HomePage
from selenium.webdriver.common.by import By
from login_page.login_page import LoginPage
import unittest
from time import sleep

class HomePageTest(unittest.TestCase):
    def test_products_are_visible(self):
        home_page = HomePage()

        products = home_page.browser.find_element(By.XPATH, '//*[@id="inventory_container"]')

        self.assertTrue(products.is_displayed())

    def test_menu_toggle(self):
        home_page = HomePage()

        menu = home_page.browser.find_element(By.XPATH, '//*[@id="menu_button_container"]/div/div[2]')

        hidden = lambda : menu.get_attribute('aria-hidden') == 'true'
        
        self.assertTrue(hidden())

        home_page.click_menu_button()

        self.assertFalse(hidden())

if __name__ == '__name__':
    unittest.main()
