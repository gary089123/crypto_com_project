from selenium.webdriver.common.by import By

from utils.basePage import BasePage
from libs.webs.crypto import exchangeDetailPage


class ExchangePage(BasePage):

    SEARCH_BOX = [By.CLASS_NAME, "search-input"]
    SEARCH_RESULT = [By.XPATH, "//*[contains(@class, 'global-search-wrapper')]//*[@class='group-item']"]
    

    def __init__(self, driver) -> None:
        super().__init__(driver)


    def input_search(self, input_text):

        search_text_box = self.find_element(self.SEARCH_BOX)
        search_text_box.send_keys(input_text)
        search_text_box.click()

    def click_first_search(self):

        search_result = self.find_all_element(self.SEARCH_RESULT)
        
        if len(search_result) > 0:

            search_result[0].click()

        return exchangeDetailPage.ExchangeDetailPage(self.driver)




        

        

    