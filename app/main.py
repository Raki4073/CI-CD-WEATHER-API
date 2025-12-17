import logging
from flask import Flask
from app.routes import weather_bp


def create_app():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    app = Flask(__name__)
    app.register_blueprint(weather_bp)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
