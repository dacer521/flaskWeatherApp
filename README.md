**Weather App**

This is a weather app created for an assessment to showcase and practice skills in web development, Python, and Flask.

**Project Overview**

The app allows users to search for the weather in a given location by entering a zip code, country, city, county, or geographical area (e.g., New England or Europe).

**How to Run**

Clone or download the repository.

Run server.py.

Open a web browser and navigate to localhost:8000. The app is set to run on a local server.

**Functionality**

The app uses an API call based on the user’s input with error handling.

If no value is entered, it defaults to displaying the weather for Boston.

If the entered city is not found, the user is redirected to a "City Not Found" page, prompting them to re-enter a location.

For valid inputs, the app displays:

Weather status

Temperature

Feels-like temperature

A relevant status image

A "More Info" button reveals additional details, including:

Sunrise and sunset times

Longitude and latitude

Humidity

Sea level

I attempted to create a 5 day forecat, however, the API I am using only provides the 1 day forecast in the free version, so I was inhibited from adding it.

**Requirements**

Ensure you have the necessary dependencies installed to run the app. Refer to the requirements.txt file for details.

 