import streamlit as st
import requests

# URL de ton backend FastAPI
API_URL = "http://localhost:8000"  # à adapter si ton API tourne ailleurs

st.title("📡 Météo en Direct et Prévisions")

city = st.text_input("Entrez une ville :", "Paris")

if st.button("Obtenir la météo actuelle"):
    response = requests.get(f"{API_URL}/current/{city}")
    if response.status_code == 200:
        data = response.json()
        st.success(f"Météo actuelle à {data['city']}")
        st.metric("Température", f"{data['temperature']}°C")
        st.metric("Vent", f"{data['wind_speed']} km/h")
        st.metric("Code météo", data['weather_code'])
    else:
        st.error("Ville non trouvée ou erreur serveur.")

if st.button("Obtenir les prévisions à 7 jours"):
    response = requests.get(f"{API_URL}/forecast/{city}")
    if response.status_code == 200:
        data = response.json()
        st.success(f"Prévisions pour {data['city']}")
        for date, tmin, tmax, rain in zip(data["dates"], data["temp_min"], data["temp_max"], data["precipitations"]):
            st.write(f"📅 {date} - 🌡️ {tmin}°C / {tmax}°C - 🌧️ {rain} mm")
    else:
        st.error("Impossible de récupérer les prévisions.")
