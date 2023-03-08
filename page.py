from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class Page:
    def __init__(self):
        self.options = Options()
        self.options.add_experimental_option('detach', True)
        self.service = Service(ChromeDriverManager().install())
        self.browser = webdriver.Chrome(service=self.service)
