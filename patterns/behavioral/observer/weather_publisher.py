class WeatherStation:

    def __init__(self):
        self._weather_data = None
        self.observers = []

    @property
    def weather_data(self):
        return self._weather_data

    @weather_data.setter
    def weather_data(self, weather_data):
        self._weather_data = weather_data
        self._measurement_change()

    def _measurement_change(self):
        self._notify_observers()

    def _notify_observers(self):
        for observer in self.observers:
            observer.update(self.weather_data)

    def register_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)
