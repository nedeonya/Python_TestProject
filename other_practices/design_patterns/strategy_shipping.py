from abc import ABC, abstractmethod
from enum import Enum


class ShippingStrategy(ABC):
    @abstractmethod
    def calculate_shipping_cost(self, weight):
        pass


class FedEx(ShippingStrategy):
    def calculate_shipping_cost(self, weight):
        return weight * 2.5


class UPS(ShippingStrategy):
    def calculate_shipping_cost(self, weight):
        return weight * 3


class DHL(ShippingStrategy):
    def calculate_shipping_cost(self, weight):
        return weight * 4


class Amazon(ShippingStrategy):
    def calculate_shipping_cost(self, weight):
        return weight * 3.25


class ShippingProcess:
    def __init__(self, shipping_provider: ShippingStrategy):
        self.provider = shipping_provider

    def calculate_shipping_cost(self, weight):
        return self.provider.calculate_shipping_cost(weight)


class CarrierEnum(Enum):
    FEDEX = 1
    UPS = 2
    DHL = 3


#Testing
print("Select a provider for shipping:")
print("1. FedEx")
print("2. UPS")
print("3. DHL")
print("4. Amazon")

choice = int(input("Enter the number corresponding to your choice: "))
weight = float(input("Enter the weight of the package (in pounds): "))

if choice == 1:
    provider = FedEx()
elif choice == 2:
    provider = UPS()
elif choice == 3:
    provider = DHL()
elif choice == 4:
    provider = Amazon()
else:
    print("Invalid choice!")
    exit(1)

shipping_process = ShippingProcess(provider)
shipping_cost = shipping_process.calculate_shipping_cost(weight)
print(f"The shipping cost for {type(provider).__name__} is ${shipping_cost:.2f}")
