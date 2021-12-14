from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging


class BasePage():
    
    def __init__(self, driver) -> None:
        self.driver = driver

    def find_element(self, locator, timeout=10):

        locator = self.setup_locator(locator)
        logging.debug(f'find element with locator: {str(locator)}')
        ele = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

        return ele

    def find_all_element(self, locator, timeout=10):

        locator = self.setup_locator(locator)
        logging.debug(f'find all element with locator: {str(locator)}')
        eles = WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

        return eles

    def setup_locator(self, locator):

        return (locator[0], locator[1])




