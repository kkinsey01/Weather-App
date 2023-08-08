from WeatherData import get_weather_data

def new_location(window, zip):
    location_data = get_weather_data(zip) # get weather data via location given by zip code

    # Get city name for potential new location
    city_name = location_data["name"]

    # Get valid weather data for location
    weather_type = location_data["weather"][0]["main"]
    temperature_value = location_data["main"]["temp"]
    humidity_value = location_data["main"]["humidity"]
    wind_value = location_data["wind"]["speed"]

    # Update the interface with new location data
    window["-CITY-"].update(city_name)
    window["-TYPE-"].update(f"Weather is {weather_type}")
    window["-TEMP-"].update(f"Temperature is {temperature_value}°F")
    window["-HUMIDITY-"].update(f"Humidity: {humidity_value}%")
    window["-WIND-"].update(f"Wind Speed: {wind_value} mph")

    
