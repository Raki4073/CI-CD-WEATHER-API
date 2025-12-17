from flask import Blueprint, jsonify
from app.weather_client import get_weather


weather_bp = Blueprint("weather", __name__)


@weather_bp.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Weather API", "status": "ok"})


@weather_bp.route("/weather", methods=["GET"])
def weather():
    data = get_weather()
    return jsonify(data)
