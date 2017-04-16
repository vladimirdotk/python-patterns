import pytest
from patterns.behavioral.observer.weather_data import WeatherData
from patterns.behavioral.observer.weather_publisher import WeatherStation
from patterns.behavioral.observer.temperature_display import TemperatureDisplay
from patterns.behavioral.observer.pressure_display import PressureDisplay


@pytest.fixture
def temperature():
    return 30


@pytest.fixture
def pressure():
    return 10


def test_weather_station(temperature, pressure):
    weather_station = WeatherStation()

    temperature_display = TemperatureDisplay()
    pressure_display = PressureDisplay()

    for observer in [temperature_display, pressure_display]:
        weather_station.register_observer(observer)

    weather_data = WeatherData()
    weather_data.temperature = temperature
    weather_data.pressure = pressure

    for data in (temperature, pressure):
        assert str(data) in str(weather_data)

    weather_station.weather_data = weather_data

    assert temperature_display.display() == temperature
    assert pressure_display.display() == pressure

    weather_station.remove_observer(temperature_display)
    weather_station.remove_observer(pressure_display)
