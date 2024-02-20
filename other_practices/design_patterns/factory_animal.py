from abc import ABC, abstractmethod
from enum import Enum


class AnimalType(Enum):
    DOG = "Dog"
    CAT = "Cat"
    FISH = "Fish"


class Animal(ABC):
    def __init__(self, context: dict):
        self.name = context["name"]
        self.age = context["age"]

    @abstractmethod
    def get_info(self) -> str:
        pass


class Dog(Animal):
    def __init__(self, context: dict):
        super().__init__(context)

    def get_info(self) -> str:
        return f"Dog: {self.name} - {self.age}"


class Cat(Animal):
    def __init__(self, context: dict):
        super().__init__(context)

    def get_info(self) -> str:
        return f"Cat: {self.name} - {self.age}"


class Fish(Animal):
    def __init__(self, context: dict):
        super().__init__(context)

    def get_info(self) -> str:
        return f"Fish: {self.name} - {self.age}"


class AnimalFactory:
    def create_animal(self, animal_type: AnimalType, context: dict) -> Animal:
        if animal_type == AnimalType.DOG:
            return Dog(context)
        elif animal_type == AnimalType.CAT:
            return Cat(context)
        elif animal_type == AnimalType.FISH:
            return Fish(context)
        else:
            raise ValueError("Invalid animal_type")


#Testing
if __name__ == "__main__":
    animal_factory = AnimalFactory()

    dog = animal_factory.create_animal(AnimalType.DOG, {"name": "Rex", "age": 3})
    cat = animal_factory.create_animal(AnimalType.CAT, {"name": "Fluffy", "age": 2})
    fish = animal_factory.create_animal(AnimalType.FISH, {"name": "Nemo", "age": 1})

    print(dog.get_info())
    print(cat.get_info())
    print(fish.get_info())
