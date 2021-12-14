import time
from selenium.webdriver.common.by import By

from utils.basePage import BasePage

class ExchangeDetailPage(BasePage):

    TIME_LINE = [By.XPATH ,"//*[contains(@class, 'time-line')]/*[text()='{}']"]
    CURSOR_BUTTON = [By.XPATH, "//*[contains(@class, 'control-')]//*[contains(@class, 'buttonWrap-')]"]

    def __init__(self, driver) -> None:
        super().__init__(driver)


    def click_time_line(self, time_line):

        TIME_LINE = self.TIME_LINE.copy()
        TIME_LINE[1] = TIME_LINE[1].format(time_line)

        ele = self.find_element(TIME_LINE)
        ele.click()

    def change_cursor(self, cursor):


        eles = self.find_all_element(self.CURSOR_BUTTON)

        eles[1].click()


    
