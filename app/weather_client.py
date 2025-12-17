import requests
from app.config import Config

def get_weather(city="Hyderabad"):
    params = {
        "latitude": 17.3850,
        "longitude": 78.4867,
        "current_weather": True
    }

    response = requests.get(Config.WEATHER_API_URL, params=params, timeout=5)
    response.raise_for_status()
    return response.json()
