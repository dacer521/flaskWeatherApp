from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve

app = Flask(__name__) #This is the Flask app object 


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html') #view function


@app.route('/weather') #route decerator. How I run python code in response to a URL
def get_weather():
    """Get weather data for a specific city"""
    city = request.args.get('city')

    # Check for empty strings or string with only spaces

    if not bool(city.strip()): #default value just in case the user doesn't enter a city
        city = "Boston"

    weather_data = get_current_weather(city)   #runs function from weather.py

    # City is not found by API
    if not weather_data['cod'] == 200:
        return render_template('city-not-found.html')  #error handling

    return render_template(        #changing the html file based on the API JSON data.
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}",
        sunrise=weather_data['sys']['sunrise'],
        sunset=weather_data['sys']['sunset'],
        lon=weather_data['coord']['lon'],
        lat=weather_data['coord']['lat'],
        humidity=weather_data['main']['humidity'],
        sea_level=weather_data['main'].get('sea_level', 'N/A')
    )


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000) #starts the local server. To view put in browser 'localhost:8000'