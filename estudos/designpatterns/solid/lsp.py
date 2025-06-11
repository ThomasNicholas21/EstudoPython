"""
🔹 L - Liskov Substitution Principle (LSP)
Exercício: Modelar veículos com classes Carro e Bicicleta.
A classe base Veiculo define um método abastecer(), mas isso
não faz sentido pra bicicleta. O desafio é ajustar essa
hierarquia pra respeitar LSP.
"""
from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass


class Fuelable(ABC):
    @abstractmethod
    def fill_tank(self):
        pass


class Car(Vehicle, Fuelable):
    def move(self):
        print("Carro em movimento")

    def fill_tank(self):
        print("Abastecendo o carro com gasolina")


class Bicycle(Vehicle):
    def move(self):
        print("Bicicleta em movimento")


if __name__ == "__main__":
    def test_vehicle(vehicle: Vehicle):
        vehicle.move()

    def test_fuelable(fuelable: Fuelable):
        fuelable.fill_tank()

    car = Car()
    bike = Bicycle()

    test_vehicle(car)
    test_vehicle(bike)

    test_fuelable(car)
    try:
        test_fuelable(bike)
    except AttributeError as expected:
        print(f'Erro esperado: {expected}')
