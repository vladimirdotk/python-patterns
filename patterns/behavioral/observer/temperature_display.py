class TemperatureDisplay:

    def __init__(self):
        self.temperature = None

    def update(self, weather_data):
        self.temperature = weather_data.temperature

    def display(self):
        return self.temperature
