from app.main import create_app

def test_weather_endpoint():
    app = create_app()
    client = app.test_client()

    response = client.get("/weather")
    assert response.status_code == 200
