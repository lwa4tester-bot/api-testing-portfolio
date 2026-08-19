"""
This script fetches and displays current weather data for a user-specified city using the Open-Meteo APIs.
It first converts the city name into geographical coordinates, then requests weather details like temperature,
wind speed, and a weather condition code.
Finally, it displays the weather information in the selected unit (Celsius or Fahrenheit) and translates
the numeric weather code into a readable description.
"""
import requests
import sys


# WMO Weather interpretation codes (WW) in a dict
weather_codes = {
    '0': 'Clear sky',
    '1': 'Mainly clear',
    '2': 'Partly cloudy',
    '3': 'Overcast',
    '45': 'Fog',
    '48': 'Depositing rime fog',
    '51': 'Light drizzle',
    '53': 'Moderate drizzle',
    '55': 'Dense drizzle',
    '56': 'Light freezing drizzle',
    '57': 'Dense freezing drizzle',
    '61': 'Slight rain',
    '63': 'Moderate rain',
    '65': 'Heavy rain',
    '66': 'Light freezing rain',
    '67': 'Heavy freezing rain',
    '71': 'Slight snow fall',
    '73': 'Moderate snow fall',
    '75': 'Heavy snow fall',
    '77': 'Snow grains',
    '80': 'Slight rain showers',
    '81': 'Moderate rain showers',
    '82': 'Violent rain showers',
    '85': 'Slight snow showers',
    '86': 'Heavy snow showers',
    '95': 'Thunderstorm: slight or moderate',
    '96': 'Thunderstorm with slight hail',
    '99': 'Thunderstorm with heavy hail',
}

city_name =  input("City name: ")
temperature_unit = input("Temperature unit: Choose between C(celsius) or F(fahrenheit): ")
temperature_unit = 'celsius' if temperature_unit.upper() == 'C' else 'fahrenheit'

api_endpoint_geocoding = "https://geocoding-api.open-meteo.com/v1/search?"
api_endpoint_meteo = "https://api.open-meteo.com/v1/forecast?"

try:
    params = {
        'name': city_name,
        'count': 1,
        'language': 'en',
        'format': 'json'
    }
    response = requests.get(f"{api_endpoint_geocoding}", params=params)
    response.raise_for_status()

except requests.exceptions.ConnectionError:
    print("Connection error!")
    sys.exit()

except requests.exceptions.RequestException:
    print("Unknown issue")
    sys.exit()

geocoding_resonse = response.json()

# Check if the 'results' key is missing or holds an empty list
if 'results' not in geocoding_resonse or geocoding_resonse['results'] == []:
    print("Unknown city name!")
    sys.exit()


lat = geocoding_resonse['results'][0]['latitude']
lon = geocoding_resonse['results'][0]['longitude']
country = geocoding_resonse['results'][0]['country']

try:
    params = {
        'latitude': lat,
        'longitude': lon,
        'current': ['temperature_2m', 'wind_speed_10m', 'weather_code'],
        'temperature_unit': temperature_unit
    }
    response = requests.get(f"{api_endpoint_meteo}", params=params)
    response.raise_for_status()
except requests.exceptions.ConnectionError:
    print("connection error!")
    sys.exit()

except requests.exceptions.RequestException:
    print("Unknown issue")
    sys.exit()

meteo_response = response.json()

current_temp = meteo_response['current']['temperature_2m']
wind_speed = meteo_response['current']['wind_speed_10m']
weather_code = meteo_response['current']['weather_code']

print(f"City={city_name}, Country={country}, temperature={current_temp} {'°C' if temperature_unit == 'celsius' else 'F'}, windspeed={wind_speed}km/h")

try:
    print(f"Weather code: {weather_code} means {weather_codes[str(weather_code)]}")
except KeyError:
    print("Unknown weather code!")
