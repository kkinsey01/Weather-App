import PySimpleGUI as sg
from WeatherData import get_physical_location, get_weather_data

images = ["clear-night.png", "humidity-icon-vector-22865309.jpg", "partly-cloudy.png", "rain.png", "snow.jpg", "sun.jpg", "wind-speed.png", "cloudy.png", "thermometer.png"]

location = get_physical_location()
city_zip = location["zip"]
weather_data = get_weather_data(city_zip)

city_label = sg.Text(weather_data["name"], enable_events=True, key="-CITY-", font=("Arial", 18))

temperature_image = sg.Image(images[8], size=(20, 20))
temperature_label = sg.Text(weather_data["main"]["temp"])

humidity_image = sg.Image(images[1], size=(20, 20))
humidity_value = weather_data["main"]["humidity"]
humidity_label = sg.Text(f"Humidity: {humidity_value}", enable_events=True, key="-HUMIDITY-", font=("Arial", 16))

wind_image = sg.Image(images[6], size=(20, 20))
wind_value = weather_data["wind"]["speed"]
wind_label = sg.Text(f"Wind Speed: {wind_value}", enable_events=True, key="-WIND", font=("Arial", 16))

weather_column = [
    [
        city_label
    ],
    [
        temperature_image, temperature_label
    ],
    [
        humidity_image, humidity_label
    ],
    [
        wind_image, wind_label
    ]
]
layout = [[weather_column]]

window = sg.Window("Test", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

window.close()