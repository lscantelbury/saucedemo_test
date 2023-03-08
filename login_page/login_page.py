from selenium import webdriver
from page import Page

class LoginPage(Page):
    def __init__(self):
        super().__init__()
        self.browser.get('https://www.saucedemo.com/')


    def set_username(self, username):
        username_textfield = self.browser.find_element('xpath', '//*[@id="user-name"]')
        username_textfield.send_keys(username)

    def set_password(self, password):
        password_textfield = self.browser.find_element('xpath', '//*[@id="password"]')
        password_textfield.send_keys(password)

    def click_login_button(self):
        login_button = self.browser.find_element('xpath', '//*[@id="login-button"]')
        login_button.click()