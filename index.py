import tkinter as tk
from tkinter import ttk
import requests
from geopy.geocoders import Nominatim

def get_weather():
    city = city_entry.get()
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(city)

    if location:
        latitude = location.latitude
        longitude = location.longitude
        url = f'http://api.weatherapi.com/v1/current.json?key=9f06dd24443a40a9b5293651240802&q={latitude},{longitude}'
        try:
            response = requests.get(url)
            response.raise_for_status()
            weather_data = response.json()

            if 'error' not in weather_data:
                weather_info['text'] = f"Weather: {weather_data['current']['condition']['text']}\nTemperature: {weather_data['current']['temp_c']}°C"
            else:
                weather_info['text'] = 'Failed to fetch weather data. Please try again.'
        except requests.exceptions.RequestException as e:
            weather_info['text'] = f'Error: {e}'
    else:
        weather_info['text'] = 'Location not found.'

# Create tkinter window
window = tk.Tk()
window.title("Weather Forecast")

# Set a different theme - 'clam'
style = ttk.Style(window)
style.theme_use('vista')

# Custom colors
background_color = '#f0f0f0'
foreground_color = '#333333'
button_color = '#4CAF50'

# Set custom colors for the theme
style.configure('TLabel', background=background_color, foreground=foreground_color, font=("Helvetica", 14))
style.configure('TButton', background=button_color, foreground=foreground_color, font=("Helvetica", 14))

# Create widgets
city_label = ttk.Label(window, text="Enter city:")
city_entry = ttk.Entry(window, font=("Helvetica", 14))
get_weather_button = ttk.Button(window, text="Get Weather", command=get_weather)
weather_info = ttk.Label(window, text="")

# Place widgets in the window
city_label.grid(row=0, column=0, padx=10, pady=10)
city_entry.grid(row=0, column=1, padx=10, pady=10)
get_weather_button.grid(row=1, columnspan=2, padx=10, pady=10)
weather_info.grid(row=2, columnspan=2, padx=10, pady=10)

# Set focus to the city entry field
city_entry.focus()

label1 = ttk.Label(text="Created by: Shivam Gohil")
label1.grid(row=4, columnspan=5, padx=10, pady=50)

# Run the tkinter event loop
window.mainloop()
