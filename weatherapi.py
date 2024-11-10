import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': '1bd69368dec3abaf2095f6b7eb91decc',
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    return response.json()

def display_weather(weather_data):
    if weather_data['cod'] == 200:
        main = weather_data['main']
        weather = weather_data['weather'][0]
        wind = weather_data['wind']

        print(f"City: {weather_data['name']}")
        print(f"Temperature: {main['temp']}°C")
        print(f"Weather: {weather['description']}")
        print(f"Humidity: {main['humidity']}%")
        print(f"Wind Speed: {wind['speed']} m/s")
    else:
        print("City not found.")

def main():
    api_key = "1bd69368dec3abaf2095f6b7eb91decc"
    city_name = input("Enter city name: ")
    weather_data = get_weather(city_name, api_key)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
