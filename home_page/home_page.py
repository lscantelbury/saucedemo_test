from page import Page

class HomePage(Page):
    def __init__(self):
        super().__init__()
        self.browser.get('https://www.saucedemo.com/')

        username_textfield = self.browser.find_element('xpath', '//*[@id="user-name"]')
        username_textfield.send_keys('standard_user')

        password_textfield = self.browser.find_element('xpath', '//*[@id="password"]')
        password_textfield.send_keys('secret_sauce')

        login_button = self.browser.find_element('xpath', '//*[@id="login-button"]')
        login_button.click()


    def click_menu_button(self):
        menu_button = self.browser.find_element('xpath', '//*[@id="react-burger-menu-btn"]')
        menu_button.click()
    
    def click_shopping_cart_button(self):
        shopping_cart_button = self.browser.find_element('xpath', '//*[@id="shopping_cart_container"]/a')
        shopping_cart_button.click()

    def click_sort_button(self):
        sort_button = self.browser.find_element('xpath', '//*[@id="header_container"]/div[2]/div/span/select')
        sort_button.click()

    def click_all_items_menu_option(self):
        all_items_menu_option = self.browser.find_element('xpath', '//*[@id="inventory_sidebar_link"]')
        all_items_menu_option.click()

    def click_about_menu_option(self):
        about_menu_option = self.browser.find_element('xpath', '//*[@id="about_sidebar_link"]')
        about_menu_option.clickO()

    def click_logout_menu_option(self):
        logout_menu_option = self.browser.find_element('xpath', '//*[@id="logout_sidebar_link"]')
        logout_menu_option.click()

    def click_reset_app_state_menu_option(self):
        reset_app_state_option = self.browser.find_element('xpath', '//*[@id="reset_sidebar_link"]')
        reset_app_state_option.click()
    