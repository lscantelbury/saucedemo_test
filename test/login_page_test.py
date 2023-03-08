from login_page.login_page import LoginPage
import unittest

class LoginPageTest(unittest.TestCase):
    def test_unsucessfull_login(self):
        login_page = LoginPage()
        login_page.set_username('standard_user')
        login_page.set_password('invalid_password')
        login_page.click_login_button()

        error_text = login_page.browser.find_element('xpath', '//*[@id="login_button_container"]/div/form/div[3]/h3')

        self.assertTrue(error_text.is_displayed())

    def test_sucessfull_login(self):
        login_page = LoginPage()
        login_page.set_username('standard_user')
        login_page.set_password('secret_sauce')
        login_page.click_login_button()

        products_label = login_page.browser.find_element('xpath', '//*[@id="header_container"]/div[2]/span')

        self.assertTrue(products_label.is_displayed())

if __name__ == '__name__':
    unittest.main()