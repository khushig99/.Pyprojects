
#import the "requests" module, which allows sending HTTP requests.
import requests

# Taking'api_key' as a variable and assigning it OpenWeatherMap API key.
api_key = '30d4741c779ba94c470ca1f63045390a'

# Taking user input for the City name
user_input = input("Enter city: ")

# Using'requests.get()' method to send a GET request to the OpenWeatherMap API.

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

#if the response from the API has a 'cod' (status code) equal to '404',
# which indicates that the city was not found.
if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    # Extract weather information from the API response and store it in variables.
    #'weather_data.json()' returns a Python dictionary parsed from the JSON response.
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    # Display the weather and temperature information for the entered city.
    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}ºF")
