import pytest
import respx
import sys
from httpx import Response

from src.services.open_meteo_service import (
    get_coordinates,
    get_current_weather,
    get_weather_forecast,
)

@pytest.mark.asyncio
@respx.mock
async def test_get_coordinates_success():
    respx.get("https://geocoding-api.open-meteo.com/v1/search").mock(
        return_value=Response(200, json={
            "results": [{
                "latitude": 48.8566,
                "longitude": 2.3522
            }]
        })
    )

    lat, lon = await get_coordinates("Paris")
    assert lat == 48.8566
    assert lon == 2.3522

@pytest.mark.asyncio
@respx.mock
async def test_get_coordinates_failure():
    respx.get("https://geocoding-api.open-meteo.com/v1/search").mock(
        return_value=Response(200, json={"results": []})
    )

    result = await get_coordinates("FakeCity")
    assert result is None

@pytest.mark.asyncio
@respx.mock
async def test_get_current_weather_success():
    respx.get("https://geocoding-api.open-meteo.com/v1/search").mock(
        return_value=Response(200, json={
            "results": [{"latitude": 48.8566, "longitude": 2.3522}]
        })
    )
    respx.get("https://api.open-meteo.com/v1/forecast").mock(
        return_value=Response(200, json={
            "current_weather": {
                "temperature": 22.5,
                "windspeed": 10.0,
                "weathercode": 1
            }
        })
    )

    data = await get_current_weather("Paris")
    assert data["city"] == "Paris"
    assert data["temperature"] == 22.5
    assert data["wind_speed"] == 10.0
    assert data["weather_code"] == 1

@pytest.mark.asyncio
@respx.mock
async def test_get_weather_forecast_success():
    respx.get("https://geocoding-api.open-meteo.com/v1/search").mock(
        return_value=Response(200, json={
            "results": [{"latitude": 48.8566, "longitude": 2.3522}]
        })
    )
    respx.get("https://api.open-meteo.com/v1/forecast").mock(
        return_value=Response(200, json={
            "daily": {
                "time": ["2025-06-23"],
                "temperature_2m_max": [25.0],
                "temperature_2m_min": [15.0],
                "precipitation_sum": [0.0]
            }
        })
    )

    forecast = await get_weather_forecast("Paris")
    assert forecast["city"] == "Paris"
    assert forecast["dates"] == ["2025-06-23"]
    assert forecast["temp_max"] == [25.0]
    assert forecast["temp_min"] == [15.0]
    assert forecast["precipitations"] == [0.0]

