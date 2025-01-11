from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)

# Dictionary to map weather statuses to icon URLs
weather_icons = {
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
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/weather')
def get_weather():
    city = request.args.get('city')

    if not city or not city.strip():
        city = "Boston"

    weather_data = get_current_weather(city)

    if not weather_data['cod'] == 200:
        return render_template('city-not-found.html')

    weather_status = weather_data["weather"][0]["main"].lower()
    icon_url = weather_icons.get(weather_status, weather_icons["default"])

    return render_template(
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
    print("Server Started")
    serve(app, host="0.0.0.0", port=8000)
