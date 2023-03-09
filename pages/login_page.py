from selenium import webdriver
from resources.login_page_locators import LoginPageLocators
from selenium.webdriver.common.by import By
from pages.page import Page

class LoginPage(Page):
    def __init__(self, browser):
        super().__init__(browser=browser)
        self.browser.get('https://www.saucedemo.com/')


    def set_username(self, username):
        username_textfield = self.browser.find_element(By.XPATH, LoginPageLocators.username_textfield)
        username_textfield.send_keys(username)

    def set_password(self, password):
        password_textfield = self.browser.find_element(By.XPATH,LoginPageLocators.password_textfield)
        password_textfield.send_keys(password)

    def click_login_button(self):
        login_button = self.browser.find_element(By.XPATH, LoginPageLocators.login_button)
        login_button.click()