import requests
import json
import logging

class Weather():

    def __init__(self) -> None:
        pass

    def get_weather_forecase_data(self, status=False):

        r = requests.get("https://pda.weather.gov.hk/locspc/data/fnd_uc.xml")
        data = json.loads(r.content)
        
        if status:
            return data, r.status_code
        else:
            return data


    def get_weather_forecase(self, day=None):

        data = self.get_weather_forecase_data()

        if day == None:
            return data.get("forecast_detail")

        else:
    
            try:
                return data.get("forecast_detail")[day]
            except IndexError:
                logging.error(f"Index outof range for forecast_detail, day={day}")
                return None

    def get_weather_forecase_general(self):

        data = self.get_weather_forecase_data()
        return data.get("general_situation")

    

        



if __name__ == "__main__":

    w = Weather()
    w.get_weather_forecase_general()

