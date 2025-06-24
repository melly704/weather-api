from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_current_valid_city():
    response = client.get("/current/Paris")
    assert response.status_code == 200
    assert "temperature" in response.json()

def test_current_invalid_city():
    response = client.get("/current/FakeCity123")
    assert response.status_code == 404

def test_forecast_valid_city():
    response = client.get("/forecast/Lyon")
    assert response.status_code == 200
    json = response.json()
    assert "dates" in json


def test_current_city_with_accent():
    response = client.get("/current/Évry")
    assert response.status_code in [200, 404]

def test_forecast_city_empty():
    response = client.get("/forecast/")
    assert response.status_code == 404

def test_current_forecast_consistency():
    city = "Marseille"
    current = client.get(f"/current/{city}").json()
    forecast = client.get(f"/forecast/{city}").json()
    assert current["city"] == forecast["city"]
