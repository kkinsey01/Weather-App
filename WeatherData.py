import requests
from urllib.request import urlopen
import json
 
with open("apis/weatherAPI.txt") as f: # Get weather api 
    api_key_weather = f.readline()
    f.close()

with open("apis/ipAPI.txt") as f: # Get IP api to get physical location
    api_key_ip = f.readline()
    f.close()

# Retrieve current weather data for given location
def get_weather_data(city_zip): 
    api_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "zip": city_zip,
        "units": "imperial",
        "appid": api_key_weather
    }
    response = requests.get(api_url, params=params)
    data = response.json()
    return data

# Access physical location from which program is being ran
def get_physical_location():
    api_url = "http://api.ipstack.com/check"
    params = {
        "access_key": api_key_ip
    }
    response = requests.get(api_url, params=params)
    location = response.json()
    return location

def create_weather_report(data):
    report = "Weather Report:\n"
    city = data["name"]
    report += f"City {city}\n"
    temperature = data["main"]["temp"]
    report += f"Temperature: {temperature}°F\n"
    type = data["weather"][0]["main"]
    report += f"Weather: {type}\n"
    humidity = data["main"]["humidity"]
    report += f"Humidity: {humidity}%\n"
    wind_speed = data["wind"]["speed"]
    report += f"Wind Speed: {wind_speed} mph\n"
    return report

# Retrieve weather forecast for next 5 days
def weather_forecast(city_zip):
    api_url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "zip": city_zip,
        "units": "imperial",
        "appid": api_key_weather
    }
    response = requests.get(api_url, params=params)
    data = response.json()
    return data

#city_zip = input("Enter city zip code or to use current location enter 'n': ")
#if (city_zip == 'n'):
#    location = get_physical_location()
#    city_zip = location["zip"]

#data = get_weather_data(city_zip)
#report = create_weather_report(data)
#print(report)