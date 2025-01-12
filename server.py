from flask import Flask, render_template, request #importing Flask, render_template, and request from flask
from weather import get_current_weather
from waitress import serve
import requests

app = Flask(__name__) #creating an instance of the Flask class

# Dictionary to map weather statuses to icon URLs
weather_icons = {                                   #dictionary of weather statuses used later to get image
    "clear": "static/images/clear.jpg",
    "clouds": "static/images/cloudy.jpg",
    "rain": "static/images/rainy.jpg",
    "thunderstorm": "static/images/thunderstorm.jpg",
    "snow": "static/images/snowy.jpg",
    "mist": "static/images/drizzle.jpg",
    "fog": "static/images/fog.jpg",
    "wind": "static/images/windy.jpg",
    "sunny": "static/images/sunny.jpg",
    "tornado": "static/images/tornado.jpg",
    "smoke": "static/images/smoky.jpg",
    "haze": "static/images/smoky.jpg",
    "drizzle": "static/images/drizzle.jpg",
    "default": "static/images/failsafe.jpg"
}

@app.route('/')
@app.route('/index') #setting up index page on load
def index():
    return render_template('index.html')

@app.route('/weather')   #setting up weather page when city/location is entered

def get_weather(): #getting longitude and latitude from city name
    city = request.args.get('city')
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')

    if not city and latitude and longitude:   #getting user location
        # Use a reverse geocoding API to get the city name from latitude and longitude
        response = requests.get(f'https://api.bigdatacloud.net/data/reverse-geocode-client?latitude={latitude}&longitude={longitude}&localityLanguage=en')
        data = response.json()
        city = data.get('city')

    if not city or not city.strip():
        city = "Boston"

    weather_data = get_current_weather(city)   #getting weather data from weather.py

    if not weather_data['cod'] == 200:
        return render_template('city-not-found.html')

    weather_status = weather_data["weather"][0]["main"].lower()                #getting weather status from weather data
    icon_url = weather_icons.get(weather_status, weather_icons["default"])     #getting icon url from weather_icons dictionary

    return render_template(         #rendering weather.html with weather data
        "weather.html",
        title=weather_data['name'],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}",
        sunrise=weather_data['sys']['sunrise'],
        sunset=weather_data['sys']['sunset'],
        lon=weather_data['coord']['lon'],
        lat=weather_data['coord']['lat'],
        humidity=weather_data['main']['humidity'],
        sea_level=weather_data['main'].get('sea_level', 'N/A'),
        icon=icon_url
    )

if __name__ == "__main__":
    print("Server Started") #print statement to show server has started
    serve(app, host="0.0.0.0", port=8000) #running the server locally on port 8000