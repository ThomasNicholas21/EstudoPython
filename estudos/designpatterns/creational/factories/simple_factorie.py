"""
Para práticar e entender melhor simple factories
Atividade deve seguir o conceito por trás dos principais
componentes para se cirar uma simple factorie.
- Produto
- Produto concreto
- Fábrica Simples
"""
from abc import ABC, abstractmethod


# Produto
class Report(ABC):
    @abstractmethod
    def generate_csv() -> None: pass


# Produto Concreto
class ReportEstoque(Report):
    def generate_csv():
        pass


class ReportVendas(Report):
    def generate_csv():
        pass


# Fábrica Simples
class FactoryRelatorio:
    @staticmethod
    def get_report():
        pass


if __name__ == "__main__":
    ...
