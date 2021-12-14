import pytest
import time
import logging

from utils.baseTest import BaseWebTest
from libs.webs.crypto.app import CryptoApp
from libs.webs.crypto.exchangePage import ExchangePage
from libs.webs.crypto.exchangeDetailPage import ExchangeDetailPage


class TestCryptoCom(BaseWebTest):

    @pytest.mark.order(1)
    def test_search_and_go_to_cro_page(self):

        app = CryptoApp(self.driver)
        exchange_page = app.open()

        exchange_page.input_search('CRO/USDT')
        exhange_detail_page = exchange_page.click_first_search()
        time.sleep(2)


    @pytest.mark.order(2)
    def test_detail_page_change_1m_timeline(self):

        exhange_detail_page = ExchangeDetailPage(self.driver)
        exhange_detail_page.click_time_line("1m")
        time.sleep(2)

    @pytest.mark.order(3)
    def test_detail_page_change_5m_timeline(self):

        exhange_detail_page = ExchangeDetailPage(self.driver)
        exhange_detail_page.click_time_line("5m")
        time.sleep(2)
    
    @pytest.mark.order(4)
    def test_detail_page_change_30m_timeline(self):

        exhange_detail_page = ExchangeDetailPage(self.driver)
        exhange_detail_page.click_time_line("30m")
        time.sleep(2)

