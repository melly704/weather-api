from fastapi import FastAPI
from src.controllers.weather_controller import router as weather_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API météo opérationnelle"}

app.include_router(weather_router)
