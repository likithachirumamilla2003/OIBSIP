!pip install requests

import requests

# Function to get weather data
def get_weather_data(city, api_key):
    try:
        response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&appid={api_key}")
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Function to display weather information
def display_weather_info(city, data):
    if data:
        weather = data['weather'][0]['main']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        print(f"Weather in {city}: {weather}")
        print(f"Temperature: {temp}°F (Feels like {feels_like}°F)")
        print(f"Humidity: {humidity}%")
    else:
        print(f"Could not retrieve weather data for {city}")

# Main function
def main():
    api_key = '381e092f35ff597ebc9457bc86c28b9b'
    city = input("Enter city: ")
    weather_data = get_weather_data(city, api_key)
    display_weather_info(city, weather_data)

if __name__ == "__main__":
    main()
