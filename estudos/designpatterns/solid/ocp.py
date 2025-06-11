"""
🔹 O - Open/Closed Principle (OCP)
Exercício: Criar um sistema de cálculo de frete. Inicialmente só tem um tipo de
frete, mas a tarefa é adicionar mais tipos sem modificar a classe principal.
Você vai usar uma interface/abstração.
"""
from abc import ABC, abstractmethod


class ShippingStrategy(ABC):
    @abstractmethod
    def calculate(self, weight: float) -> float:
        pass


class StandardShipping(ShippingStrategy):
    def calculate(self, weight: float) -> float:
        return 10 + (weight * 1.2)


class ExpressShipping(ShippingStrategy):
    def calculate(self, weight: float) -> float:
        return 20 + (weight * 2.0)


class FreeShipping(ShippingStrategy):
    def calculate(self, weight: float) -> float:
        return 0.0


class ShippingCalculator:
    def __init__(self, strategy: ShippingStrategy):
        self.strategy = strategy

    def calculate_shipping(self, weight: float) -> float:
        return self.strategy.calculate(weight)


if __name__ == "__main__":
    weight = 5.0

    standard = ShippingCalculator(StandardShipping())
    express = ShippingCalculator(ExpressShipping())
    free = ShippingCalculator(FreeShipping())

    print("Frete padrão:", standard.calculate_shipping(weight))
    print("Frete expresso:", express.calculate_shipping(weight))
    print("Frete gratuito:", free.calculate_shipping(weight))
