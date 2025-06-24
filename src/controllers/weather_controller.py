from fastapi import APIRouter, HTTPException
from src.services.open_meteo_service import get_current_weather, get_weather_forecast
from src.models.current_weather_response import CurrentWeatherResponse
from src.models.forecast_weather_response import ForecastWeatherResponse

router = APIRouter()

from fastapi.responses import JSONResponse
from fastapi import status

from fastapi import HTTPException

@router.get("/current/{city}" ,responses={404: {"description": "Ville inconnue"}})
async def current_weather(city: str):
    if not city or city.lower() in ["null", "none", "undefined", "0", "false", "true", "0", "123", ""]:
        raise HTTPException(status_code=404, detail="Ville inconnue")

    result = await get_current_weather(city)
    if not result:
        raise HTTPException(status_code=404, detail="Ville inconnue")
    return result



@router.get("/forecast/{city}",responses={404: {"description": "Ville inconnue"}})
async def forecast_weather(city: str):
    if not city or city.lower() in ["null", "none", "undefined", "0", "false", "true", "0", "123", ""]:
        raise HTTPException(status_code=404, detail="Ville inconnue")

    forecast = await get_weather_forecast(city)
    if not forecast:
        raise HTTPException(status_code=404, detail="Ville inconnue")
    return forecast





