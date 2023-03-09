from selenium.webdriver.chrome.options import Options

class Page:
    def __init__(self, browser):
        self.options = Options()
        self.options.add_experimental_option('detach', True)
        self.browser = browser
