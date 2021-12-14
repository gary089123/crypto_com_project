import pytest

import logging
from utils.baseTest import BaseApiTest
from libs.apis.weather import Weather



class TestWeatherApi(BaseApiTest):

    @pytest.mark.order(1)
    def test_forecase_api_status(self):

        w = Weather()
        data, status = w.get_weather_forecase_data(status=True)

        assert status == 200


    @pytest.mark.order(2)
    def test_forecase_general_situation(self):
        w = Weather()

        general_situation = w.get_weather_forecase_general()
        logging.info(str(general_situation))

        assert general_situation is not None

    @pytest.mark.order(3)
    def test_forecase_day_three(self):

        w = Weather()
        forecase = w.get_weather_forecase(3)

        logging.info(str(forecase))
        logging.info("humidity : {} - {}".format(forecase.get("min_rh"), forecase.get("max_rh")))

        assert forecase.get("min_rh") is not None 
        assert forecase.get("max_rh") is not None



        

