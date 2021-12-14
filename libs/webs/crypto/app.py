from utils.webdriverManager import WebDriverManager
from libs.webs.crypto import exchangePage

class CryptoApp():

    def __init__(self,driver,  browser='chrome') -> None:
        
        self.url = 'https://crypto.com/exchange'
        self.browser = browser
        self.driver = driver
        

    def open(self):

        self.driver.get(self.url)

        return exchangePage.ExchangePage(self.driver)