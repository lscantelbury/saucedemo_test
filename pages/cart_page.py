from page import Page
from resources.cart_page_locators import CartPageLocators
from selenium.webdriver.common.by import By

class CartPage(Page):
    def __init__(self, browser):
        super().__init__(browser)

    def click_remove_button(self):
        remove_button = self.browser.find_element(By.XPATH, CartPageLocators.remove_button)
        remove_button.click()

    def click_continue_shopping_button(self):
        continue_shopping_button = self.browser.find_element(By.XPATH, CartPageLocators.continue_shopping_button)
        continue_shopping_button.click()

    def click_checkout_button(self):
        checkout_button = self.browser.find_element(By.XPATH, CartPageLocators.checkout_button) 
        checkout_button.click()

    def set_firstname_textfield(self, first_name):
        firstname_textfield = self.browser.find_element(By.XPATH, CartPageLocators.first_name_textfield)
        firstname_textfield.send_keys(first_name)
    
    def set_last_textfield(self, last_name):
        lastname_textfield = self.browser.find_element(By.XPATH, CartPageLocators.last_name_textfield)
        lastname_textfield.send_keys(last_name)

    def set_zip_textfield(self, zip):
        zip_textfield = self.browser.find_element(By.XPATH, CartPageLocators.zip_textfield)
        zip_textfield.send_keys(zip)

    def click_continue_button(self):
        continue_button = self.browser.find_element(By.XPATH, CartPageLocators.continue_button)
        continue_button.click()

    def click_finish_button(self):
        finish_button = self.browser.find_element(By.XPATH, CartPageLocators.finish_button)
        finish_button.click()

