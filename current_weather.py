# Gets the current temperature at given latitude and longitude
import requests
import os
from datetime import datetime, timedelta

class CurrentWeather:
    API_KEY = os.getenv('WEATHER_API')

    def __init__(self, zipcode: str):
        self._zip: str = zipcode
        self._data = None

    def refresh(self):
        URL: str = f'https://api.openweathermap.org/data/2.5/weather?zip={self._zip},us&units=imperial&appid={CurrentWeather.API_KEY}'

        response = requests.get(URL)

        self._data = response.json()

        print("------ Weather API Response ------")
        print(self._data)
        print("------ Weather API Response END ------")

        FIVE_DAY_URL: str = f'https://api.openweathermap.org/data/2.5/forecast?zip={self._zip},us&units=imperial&appid={CurrentWeather.API_KEY}'

        response = requests.get(FIVE_DAY_URL)

        self._five_day_data = response.json()

        print("------ Five Day API Response ------")
        print(self._five_day_data)
        print("------ Five Day API Response END ------")

        tomorrow = datetime.now() + timedelta(days=1)
        tomorrow_date = tomorrow.date()
        two_days = datetime.now() + timedelta(days=2)
        two_days_date = two_days.date()
        self._tomorrow_weather: list = []
        self._two_days_weather: list = []

        for time in self._five_day_data["list"]:
            weather_time = datetime.fromtimestamp(time["dt"])
            if weather_time.date() == tomorrow_date:
                self._tomorrow_weather.append(time)
                print(f"Timestamp:\n{time}\n")
            elif weather_time.date() == two_days_date:
                self._two_days_weather.append(time)


    def get_current_temp(self) -> int:
        if (self._data is None):
            self.refresh()

        return round(self._data['main']['temp'])
    
    def get_current_condition(self) -> str:
        if (self._data is None):
            self.refresh()
        
        return self._data['weather'][0]['main']
    
    def get_min_max_temp(self) -> list[int, int]:
        '''
        Return the min and max temperature for the current day as a list:
        [min, max]
        '''
        if (self._data is None):
            self.refresh()

        min: int = round(self._data['main']['temp_min'])
        max: int = round(self._data['main']['temp_max'])

        return [min, max]
    
    def get_city_name(self) -> str:
        if (self._data is None):
            self.refresh()
        
        return self._data['name']

    def get_tomorrow_temps(self) -> tuple[int, int]:
        max_temps: list[float] = [timestamp['main']['temp_max'] for timestamp in self._tomorrow_weather]
        min_temps: list[float] = [timestamp['main']['temp_min'] for timestamp in self._tomorrow_weather]

        max_temp: int = round(max(max_temps))
        min_temp: int = round(min(min_temps))

        return (min_temp, max_temp)
