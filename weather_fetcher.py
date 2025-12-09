# weather_fetcher.py
import requests

class WeatherFetcher:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    def __init__(self, api_key):
        self.api_key = api_key

    def fetch_city(self, city):
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'
            }
            response = requests.get(self.BASE_URL, params=params)
            response.raise_for_status()
            return response.json()

        except Exception as e:
            print(f"Error fetching weather for {city}: {e}")
            return None
