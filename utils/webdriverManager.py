import logging
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as Cs
from selenium.webdriver.firefox.service import Service as Fs

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class WebDriverManager():

    def __init__(self, browser='chrome') -> None:
        self.browser = browser

    def get_driver(self, browser='chrome'):

        driver = None

        if self.browser == 'chrome':
            service = Cs(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service)
        elif self.browser == 'firebox':
            service = Fs(GeckoDriverManager().install())
            driver = webdriver.Firefox(service=service)
        else:
            logging.error("Unknown driver !")

        return driver
