from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv() # Load environment variables from .env file 


def get_current_weather(city="Kansas City"): 
    """does API call to get weather data"""
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    weather_data = requests.get(request_url).json()

    return weather_data


if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n') #all the erst of this is for debugging purposes. doesn't impact user interaction. seperate file in case I add more in the future.

    city = input("\nPlease enter a city name: ")

    if not bool(city.strip()):
        city = "Boston"

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)