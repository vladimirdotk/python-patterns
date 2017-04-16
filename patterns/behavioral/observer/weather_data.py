class WeatherData:

    def __init__(self):
        self._temperature = None
        self._pressure = None

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        self._temperature = temperature

    @property
    def pressure(self):
        return self._pressure

    @pressure.setter
    def pressure(self, pressure):
        self._pressure = pressure

    def __str__(self):
        return 'Temperature is {}. Pressure is {}.'.format(
            self.temperature, self.pressure
        )
