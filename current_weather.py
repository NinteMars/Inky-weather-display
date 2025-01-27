# Gets the current temperature at given latitude and longitude
import requests
import os

class CurrentWeather:
    API_KEY = os.getenv('WEATHER_API')

    def __init__(self, zipcode: str):
        self._zip: str = zipcode
    
    def get_current_temp(self) -> int:
        URL: str = f'https://api.openweathermap.org/data/2.5/weather?zip={self._zip},us&units=imperial&appid={CurrentWeather.API_KEY}'

        response = requests.get(URL)

        data = response.json()

        print("------ Weather API Response ------")
        print(data)
        print("------ Weather API Response END ------")


        temperature: int = round(data['main']['temp'])

        return temperature

        