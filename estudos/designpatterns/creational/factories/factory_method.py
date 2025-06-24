"""
Exemplo prático para entender o padrão de projeto Factory Method.

Componentes principais:
- Product
- ConcreteProduct
- ConcreteCreator
- Creator
"""
from abc import ABC, abstractmethod


# Product
class Report(ABC):
    @abstractmethod
    def generate_csv(self) -> None:
        pass


# ConcreteProducts
class ReportStock(Report):
    def generate_csv(self) -> None:
        print("Gerando relatório de Stock em CSV...")


class ReportSales(Report):
    def generate_csv(self) -> None:
        print("Gerando relatório de Sales em CSV...")


# Creator
class ReportCreator(ABC):
    @abstractmethod
    def create_report(self) -> Report:
        pass


# ConcreteCreators
class StockReportCreator(ReportCreator):
    def create_report(self) -> Report:
        return ReportStock()


class SalesReportCreator(ReportCreator):
    def create_report(self) -> Report:
        return ReportSales()


if __name__ == "__main__":
    creators = {
        "Stock": StockReportCreator(),
        "Sales": SalesReportCreator(),
    }

    reports = ["Stock", "Sales", "Sales", "Stock", "Ages"]

    for tipo in reports:
        creator = creators.get(tipo)
        if creator:
            report = creator.create_report()
            report.generate_csv()
        else:
            print(f"Tipo de relatório '{tipo}' não suportado.")
