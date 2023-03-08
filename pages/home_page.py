from page import Page
from resources.home_page_locators import HomePageLocators
from selenium.webdriver.common.by import By

class HomePage(Page):
    def __init__(self, browser):
        super().__init__(browser=browser)
        self.inventory_items =lambda : self.browser.find_element(By.XPATH, HomePageLocators.inventory_items)


    def click_menu_button(self):
        self.menu_button = self.browser.find_element(By.XPATH, HomePageLocators.menu_button)
        self.menu_button.click()
    
    def click_sort_button(self, option):
        sort_button = self.browser.find_element(By.CLASS_NAME, HomePageLocators.sort_button)
        sort_button.click()
        selected_option = self.browser.find_element(By.XPATH, HomePageLocators.selected_option(option=option))
        selected_option.click()

    def click_add_to_cart_button(self):
        add_to_cart_button = self.browser.find_element(By.XPATH, HomePageLocators.add_to_cart_button)
        add_to_cart_button.click()
    