# Gets the current temperature at given latitude and longitude
import requests
import os

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

        