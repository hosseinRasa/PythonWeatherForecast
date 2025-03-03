import requests
import os
from dotenv import load_dotenv
from pprint import pprint
load_dotenv()
API_KEY = os.getenv('API_KEY')
class Weather():
    def __init__(self, city):
        self.__city = city
        
        
    def get_weather(self):
        weather_result = requests.get(F'https://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={self.__city}').json()
        return weather_result

if __name__ == '__main__':
    Today = Weather('tehran')
    pprint(Today.get_weather())


