from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, symbol, price, change):
        pass


class Stock:
    def __init__(self, symbol, price):
        self._observers = []
        self._symbol = symbol
        self._price = price
        self._change = None

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._symbol, self._price, self._change)

    def set_price(self, new_price):
        self._change = new_price - self._price
        self._price = new_price
        self.notify_observers()


class PriceDisplay(Observer):
    def update(self, symbol, price, change):
        print(f"Price Display: {symbol} - Price: {price}, Change: {change}")


class ChangeDisplay(Observer):
    def update(self, symbol, price, change):
        print(f"Change Display: {symbol} - Change: {change}")


#Testing
if __name__ == "__main__":
    stock = Stock("APL", 150)

    display_price = PriceDisplay()
    display_change = ChangeDisplay()

    stock.attach(display_price)
    stock.attach(display_change)

    stock.set_price(175)


