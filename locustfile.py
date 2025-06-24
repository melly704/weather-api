from locust import HttpUser, task, between

class WeatherUser(HttpUser):
    wait_time = between(1, 3)  

    @task
    def get_current_weather(self):
        self.client.get("/current/Paris")

    @task
    def get_forecast(self):
        self.client.get("/forecast/Paris")

    @task
    def get_home(self):
        self.client.get("/")
