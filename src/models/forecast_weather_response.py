from pydantic import BaseModel
from typing import List

class ForecastWeatherResponse(BaseModel):
    city: str
    dates: List[str]
    temp_max: List[float]
    temp_min: List[float]
    precipitations: List[float]
