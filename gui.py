import PySimpleGUI as sg
from WeatherData import get_physical_location, get_weather_data
from gui_functions import new_location
from forecastGUI import main

# list of image file names (not currently in use)
images = ["clear-night.png", "humidity-icon-vector-22865309.jpg", "partly-cloudy.png", "rain.png", "snow.jpg", "sun.jpg", "wind-speed.png", "cloudy.png", "thermometer.png"]

# label asking user for location, selected by radio buttons
location_label = sg.Text("Location?", key="-LOCATION-", font=("Arial", 18))

# create radio buttons
rb1 = sg.Radio("Enter Location", "type", enable_events=True, key="-ENTER-", font=("Arial", 18))
rb2 = sg.Radio("Use My Location", "type", enable_events=True, key="-PHYSICAL-", font=("Arial", 18), default="True")

# input zip code, label and input field
enter_location_label = sg.Text("Enter location by zip: ", enable_events=True, key="-PROMPT-", font=("Arial", 18), visible=False)
enter_location_text = sg.Input("", enable_events=True, key="-INPUT-", font=("Arial", 18), size = (20, 18), visible=False)

# create 3 buttons, an OK (confirmation of input), an exit, and a forecast button to display 5 day forecast
ok_button = sg.Button("Ok", key="-OK-", size=(8, 1), font=("Arial", 14))
exit_button = sg.Button("Exit", key="-EXIT-", size=(8, 1), font=("Arial", 14))
forecast_button = sg.Button("5 Day Forecast", key="-FORECAST-", size=(12, 2), font=("Arial, 14"))

# get physical location from where program is being ran. Using the IP api
location = get_physical_location()
city_zip = location["zip"]

# get json file of weather data for physical location from Weather API. Use this to get all the data about the weather for location
weather_data = get_weather_data(city_zip)

city_name = weather_data["name"]
city_label = sg.Text(city_name, enable_events=True, key="-CITY-", font=("Arial", 18))

# get weather group paramater (rain, clouds, clear sky)
weather_type = weather_data["weather"][0]["main"]
weather_type_label = sg.Text(f"{weather_type}", enable_events=True, key="-TYPE-", font=("Arial", 18))

# get and display temperature
temperature_value = weather_data["main"]["temp"]
temperature_label = sg.Text(f"Temperature is {temperature_value}", key="-TEMP-", font=("Arial", 18))

# get and display humidity
humidity_value = weather_data["main"]["humidity"]
humidity_label = sg.Text(f"Humidity: {humidity_value}", enable_events=True, key="-HUMIDITY-", font=("Arial", 16))

# get and display wind speed
wind_value = weather_data["wind"]["speed"]
wind_label = sg.Text(f"Wind Speed: {wind_value}", enable_events=True, key="-WIND-", font=("Arial", 16))

# label to give basic instruction for user
instructional_label = sg.Text("Double click OK to change location after selecting/inputting. Hit Exit to exit", enable_events=False, key="-INSTRUCT-", font=("Arial, 12"))

# Split the interface into two columns. One for location input, one for weather data
data_column = [
    [
        location_label,
    ],
    [
        rb1, rb2
    ],
    [
        enter_location_label
    ],
    [
        enter_location_text
    ],
    [
        ok_button
    ]
]
weather_column = [
    [
        city_label
    ],
    [
        weather_type_label
    ],
    [
        temperature_label
    ],
    [
        humidity_label
    ],
    [
        wind_label
    ],
    [
        exit_button
    ]
]
# generate interface layout
layout = [
    [
        sg.pin(sg.Column(data_column, key="-COLUMN-")),
        sg.VSeparator(),
        sg.pin(sg.Column(weather_column, key="-COLUMN2-")),
    ],
    [
        instructional_label
    ],
    [
        forecast_button
    ]
]

window = sg.Window("Weather App", layout, size=(875, 400))

while True:
    event, values = window.read()
    if event == "-EXIT-" or event == sg.WIN_CLOSED:
        break
    # Make input field display to screen
    if event == "-ENTER-":
        window['-PROMPT-'].update(visible=True)
        window['-INPUT-'].update(visible=True)
    # Remove input field from screen if valid
    elif event == "-PHYSICAL-":
        window["-PROMPT-"].update(visible=False)
        window["-INPUT-"].update(visible=False)
        new_location(window, city_zip) # Set weather data to physical location (again if nessacary)
        window.visibility_changed()
    # Confirm input data, set new weather data
    elif event == "-OK-":
        zip_code = values["-INPUT-"]
        new_location(window, zip_code)
    # Generate the 5 day forecast for given location
    if event == "-FORECAST-" and values["-INPUT-"] == "":
        main(city_zip)
    elif event == "-FORECAST-":
        zip_code = values["-INPUT-"]
        main(zip_code)
    print(event, values)

window.close()