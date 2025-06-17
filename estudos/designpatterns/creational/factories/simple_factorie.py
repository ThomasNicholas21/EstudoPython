"""
Exemplo prático para entender o padrão de projeto Simple Factory.

Componentes principais:
- Produto (interface base)
- Produto concreto (implementações específicas)
- Fábrica Simples (classe responsável por criar os objetos)
"""

from abc import ABC, abstractmethod


# Produto
class Report(ABC):
    @abstractmethod
    def generate_csv(self) -> None:
        pass


# Produto Concreto
class ReportStock(Report):
    def generate_csv(self) -> None:
        print("Gerando relatório de Stock em CSV...")


class ReportSales(Report):
    def generate_csv(self) -> None:
        print("Gerando relatório de Sales em CSV...")


# Fábrica Simples
class FactoryRelatorio:
    @staticmethod
    def get_report(tipo: str) -> Report:
        if tipo == "Stock":
            return ReportStock()
        elif tipo == "Sales":
            return ReportSales()
        else:
            raise ValueError(f"Tipo de relatório '{tipo}' não suportado.")


if __name__ == "__main__":
    reports = ["Stock", "Sales", "Sales", "Stock", "Ages"]

    for report in reports:
        relatorio = FactoryRelatorio.get_report(report)
        relatorio.generate_csv()
