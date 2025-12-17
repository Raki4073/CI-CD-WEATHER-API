import os


class Config:
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
    WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast"
