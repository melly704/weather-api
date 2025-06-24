from pydantic import BaseModel

class CurrentWeatherResponse(BaseModel):
    city: str
    temperature: float
    wind_speed: float
    weather_code: int
