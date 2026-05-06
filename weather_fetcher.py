#this is our code to fetch weather info.
import requests

def get_weather(city,api_key):
    API_KEY = api_key

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    res = requests.get(url)
    data = res.json()

    if data.get("cod") != 200:
        return None, "City not found"

    # Extract data
    weather_data = {
        "temp": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "description": data["weather"][0]["description"],
        "icon": data["weather"][0]["icon"],
        "city": data["name"],
        "country": data["sys"]["country"]
    }

    return weather_data, None
