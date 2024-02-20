from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, temperature, humidity, pressure) -> None:
        pass


class WeatherData:
    def __init__(self):
        self._observers = []
        self._temperature = None
        self._humidity = None
        self._pressure = None

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)

    def set_measurements(self, temperature, humidity, pressure):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify_observers()


class CurrentConditionsDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        print(f"Current Conditions: temperature = {temperature}, humidity = {humidity}, pressure = {pressure}")


class StatisticsDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        print(f"Statistics: temperature = {temperature}, humidity = {humidity}, pressure = {pressure}")


class ForecastDisplay(Observer):
    def update(self, temperature, humidity, pressure):
        print(f"Forecast: temperature = {temperature}, humidity = {humidity}, pressure = {pressure}")


#Testing
if __name__ == "__main__":
    weather_data = WeatherData()

    current_conditions = CurrentConditionsDisplay()
    statistic = StatisticsDisplay()
    forecast = ForecastDisplay()

    weather_data.attach(current_conditions)
    weather_data.attach(statistic)
    weather_data.attach(forecast)

    print("...all 3 should display:")
    weather_data.set_measurements(15.3, 75, 66)

    print("...only statistic and forecast should display:")
    weather_data.detach(current_conditions)
    weather_data.set_measurements(18.0, 62.3, 51)
