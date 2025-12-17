import logging
import requests
from app.config import Config


logger = logging.getLogger(__name__)


def get_weather():
    logger.info("Calling weather API")

    params = {
        "latitude": 17.3850,
        "longitude": 78.4867,
        "current_weather": True
    }

    response = requests.get(Config.WEATHER_API_URL, params=params, timeout=5)
    response.raise_for_status()

    logger.info("Weather API call successful")
    return response.json()
