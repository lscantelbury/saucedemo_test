from page import Page
from selenium.webdriver.common.by import By

class HomePage(Page):
    def __init__(self, browser):
        super().__init__(browser=browser)
        self.inventory_items =lambda : self.browser.find_element(By.XPATH, '//*[@id="inventory_container"]')


    def click_menu_button(self):
        self.menu_button = self.browser.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]')
        self.menu_button.click()
    
    def click_sort_button(self, option):
        sort_button = self.browser.find_element(By.CLASS_NAME, 'product_sort_container')
        sort_button.click()
        selected_option = self.browser.find_element(By.XPATH, f'''//*[@id="header_container"]/div[2]/div/span/select/option[{option}]''')
        selected_option.click()

    def click_add_to_cart_button(self):
        add_to_cart_button = self.browser.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
        add_to_cart_button.click()
    