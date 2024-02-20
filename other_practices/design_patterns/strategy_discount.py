from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, total: float) -> float:
        pass


class NoDiscount(DiscountStrategy):
    def apply_discount(self, total: float) -> float:
        return total


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage):
        self._percentage = percentage

    def apply_discount(self, total: float) -> float:
        return total * (1 - self._percentage / 100)


class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, fixed_amount):
        self._fixed_amount = fixed_amount

    def apply_discount(self, total: float) -> float:
        return total - self._fixed_amount


class ShoppingCart:

    def __init__(self, discount_strategy: DiscountStrategy):
        self._items = {}
        self._discount_strategy = discount_strategy

    def add_item(self, item: str, price: float):
        self._items[item] = price

    def remove_item(self, item: str):
        if item in self._items:
            self._items.pop(item)

    def get_total(self) -> float:
        return sum(self._items.values())

    def get_total_after_discount(self) -> float:
        total = self.get_total()
        return self._discount_strategy.apply_discount(total)


#Testing
if __name__ == "__main__":
    cart = ShoppingCart(PercentageDiscount(10))

    cart.add_item("Item 1", 10.0)
    cart.add_item("Item 2", 20.0)
    cart.add_item("Item 3", 30.0)

    print("Total before discount:", cart.get_total())
    print("Total after discount:", cart.get_total_after_discount())
