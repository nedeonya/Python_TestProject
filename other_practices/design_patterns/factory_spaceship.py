from abc import ABC, abstractmethod
from enum import Enum


class SpaceShipEnum(Enum):
    MILLENNIUM_FALCON = "MillenniumFalcon"
    INFINITY = "Infinity"
    ENTERPRISE = "Enterprise"
    SERENITY = "Serenity"


class SpaceShip(ABC):
    def __init__(self, position, size, display_name, speed):
        self.position = position
        self.size = size
        self.display_name = display_name
        self.speed = speed

    @abstractmethod
    def get_info(self):
        pass



class MillenniumFalcon(SpaceShip):
    def get_info(self):
        return f"MillenniumFalcon: position = {self.position}, size = {self.size}, display name = {self.display_name}, speed = {self.speed}"


class Infinity(SpaceShip):
    def get_info(self):
        return f"Infinity: position = {self.position}, size = {self.size}, display name = {self.display_name}, speed = {self.speed}"


class Enterprise(SpaceShip):
    def get_info(self):
        return f"Enterprise: position = {self.position}, size = {self.size}, display name = {self.display_name}, speed = {self.speed}"


class Serenity(SpaceShip):
    def get_info(self):
        return f"Serenity: position = {self.position}, size = {self.size}, display name = {self.display_name}, speed = {self.speed}"


class SpaceShipFactory():
    def create_ship(self, ship_type: SpaceShipEnum, position, size, display_name, speed) -> SpaceShip:
        if ship_type == SpaceShipEnum.MILLENNIUM_FALCON:
            return MillenniumFalcon(position, size, display_name, speed)
        elif ship_type == SpaceShipEnum.INFINITY:
            return Infinity(position, size, display_name, speed)
        elif ship_type == SpaceShipEnum.ENTERPRISE:
            return Enterprise(position, size, display_name, speed)
        elif ship_type == SpaceShipEnum.SERENITY:
            return Serenity(position, size, display_name, speed)
        else:
            raise ValueError("unexpected ship_type")


#Testing
if __name__ == "__main__":
    factory = SpaceShipFactory()

    ship1 = factory.create_ship(SpaceShipEnum.MILLENNIUM_FALCON, (10,20), 30, "falcone", 55)
    ship2 = factory.create_ship(SpaceShipEnum.INFINITY, (30, 45), 15, "infinity", 100)
    ship3 = factory.create_ship(SpaceShipEnum.ENTERPRISE, (55, 100), 100, "enterprise", 1500)
    ship4 = factory.create_ship(SpaceShipEnum.SERENITY, (5, 25), 5, "serenity", 1000)

    print(ship1.get_info())
    print(ship2.get_info())
    print(ship3.get_info())
    print(ship4.get_info())