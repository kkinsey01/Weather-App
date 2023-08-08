from WeatherData import *
import PySimpleGUI as sg

def main(city_zip):
    forecast_data = weather_forecast(city_zip)
    city_name = forecast_data["city"]["name"]
    layout = [[]]
    index = 0
    for i in range(0, 40, 8): # Weather API provides forecast for every 3 hours. Skip 8 indexes in data to get new day. This is for 5 day forecast
        # Get data for given day. 
        temperature_value = forecast_data["list"][i]["main"]["temp_max"]
        weather_type = forecast_data["list"][i]["weather"][0]["main"]
        date_value = forecast_data["list"][i]["dt_txt"]
        date_value = date_value[:10]
        # Set label for given day
        day_label = sg.Text(f"Date: {date_value}", enable_events=True, key="-DAY-", font=("Arial, 16"))
        weather_type = sg.Text(f"Weather is: {weather_type}", enable_events=True, key="-TYPE-", font=("Arial, 16"))
        temperature_label = sg.Text(f"Temperature is: {temperature_value}", enable_events=True, key="-TEMP-", font=("Arial, 16"))
        # Generate column for day's data
        column = [
            [day_label],
            [weather_type],
            [temperature_label]
        ]
        # Set layout to display one day per row
        if(index < 4):
            layout += [[sg.Column(column, key="-COLUMN-")], [sg.HSeparator()]]
        else:
            layout += [[sg.Column(column, key="-COLUMN-")]]
        index += 1

    window = sg.Window("5 Day Forecast", layout, size=(300, 625))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
