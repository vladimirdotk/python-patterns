class PressureDisplay:

    def __init__(self):
        self.pressure = None

    def update(self, weather_data):
        self.pressure = weather_data.pressure

    def display(self):
        return self.pressure
