
import dotenv
import requests
import json
import os
from dotenv import dotenv_values
from location import Location

# Load environment from the repo .env (if present) and prefer system env vars
dotenv.load_dotenv(dotenv_path="common_agent/.env")

# Read API key from environment first, then fall back to parsing the .env file
API_KEY = os.getenv("OPENWEATHER_API_KEY")
print(API_KEY)
BASE_URL = "http://api.openweathermap.org/data/3.0/weather?"

def get_weather(city):
    location = Location(city)
    location.get_location_based_on_city()
    # Construct the complete URL
    complete_url = f"https://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid={API_KEY}&units=metric"
    print(complete_url)

    # Send a request to the API
    response = requests.get(complete_url)

    # Convert the response to JSON (Python dictionary)
    data = response.json()
    #print to debug
    print(data["weather"])

    # Check for successful response
    if data["cod"] == 200:
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        humidity = main["humidity"]
        description = weather["description"]

        # Print the weather information
        print(f"City: {location.city_name}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")
    else:
        print(f"City '{location.city_name}' Not Found or Invalid API Key.")

class WeatherTool(Location):
    def __init__(self, city):
        super().__init__(city)
        self.BASE_URL = os.getenv("WEATHER_API_URL")
        self.API_KEY = os.getenv("OPENWEATHER_API_KEY")

    def get_current_weather(self, unit):
        """Get the current weather for the specified city.

        Args:
            unit (str, optional): The unit of measurement for temperature. Defaults to "metric".
            there are some units: ["default/None", "metric", "imperial"].
            with default unit is Kelvin, metric is Celsius, imperial is Fahrenheit.

        Returns:
            dict: A dictionary containing the weather information, or None if not found.
        """
        location = Location(self.city_name)
        location.get_location_based_on_city()
        # Construct the complete URL
        if unit == "" or unit is None or unit == "default":
            #with default unit (Kelvin)
            complete_url = f"{self.BASE_URL}?lat={location.latitude}&lon={location.longitude}&appid={self.API_KEY}"
        else:
            #with specified unit
            #metric(Celsius) or imperial(Fahrenheit)
            complete_url = f"{self.BASE_URL}?lat={location.latitude}&lon={location.longitude}&appid={self.API_KEY}&units={unit}"
        print(complete_url)

        # Send a request to the API
        response = requests.get(complete_url)

        # Convert the response to JSON (Python dictionary)
        data = response.json()
        #print to debug
        print(data["weather"])

        # Check for successful response
        if data["cod"] == 200:
            main = data["main"]
            weather = data["weather"][0]
            temperature = main["temp"]
            humidity = main["humidity"]
            description = weather["description"]

            # Return the weather information
            return {
                "city": location.city_name,
                "temperature": temperature,
                "humidity": humidity,
                "description": description
            }
        else:
            return None
        
# Example usage
if __name__ == "__main__":
    city = "London"
    weather_tool = WeatherTool(city)
    weather_info = weather_tool.get_current_weather(unit="metric")
    if weather_info:
        print(f"City: {weather_info['city']}")
        print(f"Temperature: {weather_info['temperature']}°C")
        print(f"Humidity: {weather_info['humidity']}%")
        print(f"Description: {weather_info['description']}")
    else:
        print(f"City '{city}' Not Found or Invalid API Key.")