import httpx
from urllib.parse import quote

async def get_coordinates(city: str):
    encoded_city = quote(city)
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={encoded_city}&count=1&language=fr&format=json"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            return None
        data = response.json()
        results = data.get("results")
        if not results:
            return None  
        return results[0]["latitude"], results[0]["longitude"]
    
async def get_weather_forecast(city: str):
    coordinates = await get_coordinates(city)
    if not coordinates:
        return None

    lat, lon = coordinates
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        f"&daily=temperature_2m_max,temperature_2m_min,precipitation_sum"
        f"&timezone=Europe/Paris"
    )

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            return None
        data = response.json()

    return {
        "city": city,
        "dates": data["daily"]["time"],
        "temp_max": data["daily"]["temperature_2m_max"],
        "temp_min": data["daily"]["temperature_2m_min"],
        "precipitations": data["daily"]["precipitation_sum"]
    }


async def get_current_weather(city: str):
    coordinates = await get_coordinates(city)
    if not coordinates:
        return None

    lat, lon = coordinates
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            return None
        data = response.json()

    return {
        "city": city,
        "temperature": data["current_weather"]["temperature"],
        "wind_speed": data["current_weather"]["windspeed"],
        "weather_code": data["current_weather"]["weathercode"]
    }
