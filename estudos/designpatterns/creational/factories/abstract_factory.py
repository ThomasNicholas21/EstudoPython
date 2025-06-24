"""
Exemplo prático para entender o padrão de projeto Factory Method.

Componentes principais:
- AbstractProduct
- ConcreteProduct
- AbstractFactory
- ConcreteFactory
- Client
"""
from abc import ABC, abstractmethod


# AbstractProduct
class Report(ABC):
    @abstractmethod
    def generate(self) -> None: pass


# ConcreteProducts
class StockReportCSV(Report):
    def generate(self) -> None:
        print("CSV: relatório de estoque")


class SalesReportCSV(Report):
    def generate(self) -> None:
        print("CSV: relatório de vendas")


class StockReportPDF(Report):
    def generate(self) -> None:
        print("PDF: relatório de estoque")


class SalesReportPDF(Report):
    def generate(self) -> None:
        print("PDF: relatório de vendas")


# AbstractFactory
class ReportFactory(ABC):
    @abstractmethod
    def create_stock_report(self) -> Report: pass

    @abstractmethod
    def create_sales_report(self) -> Report: pass


# ConcreteCreators
class CSVReportFactory(ReportFactory):
    def create_stock_report(self) -> Report:
        return StockReportCSV()

    def create_sales_report(self) -> Report:
        return SalesReportCSV()


class PDFReportFactory(ReportFactory):
    def create_stock_report(self) -> Report:
        return StockReportPDF()

    def create_sales_report(self) -> Report:
        return SalesReportPDF()


# Client
class Client:
    def __init__(self, factory: ReportFactory):
        self.factory = factory

    def generate_reports(self):
        stock_report = self.factory.create_stock_report()
        sales_report = self.factory.create_sales_report()

        stock_report.generate()
        sales_report.generate()


if __name__ == "__main__":
    factory1 = CSVReportFactory()
    factory2 = PDFReportFactory()
    client1 = Client(factory1)
    client1.generate_reports()
    print()
    client2 = Client(factory2)
    client2.generate_reports()
