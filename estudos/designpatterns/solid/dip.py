"""
🔹 D - Dependency Inversion Principle (DIP)
Exercício: Criar uma classe RelatorioService que depende
de um repositório de dados. A ideia é aplicar DIP usando
uma interface de repositório, permitindo trocar facilmente
a implementação (ex: banco SQL vs arquivo JSON).
"""
from abc import ABC, abstractmethod


class RepositoryInterface(ABC):
    @abstractmethod
    def get_data(self) -> list:
        pass


class SQLRepository(RepositoryInterface):
    def get_data(self) -> list:
        print("Conectando ao banco de dados SQL...")
        return ["SQL: Produto A", "SQL: Produto B"]


class JSONRepository(RepositoryInterface):
    def get_data(self) -> list:
        print("Lendo dados do arquivo JSON...")
        return [{"JSON1": "Produto X"}, {"JSON2": "Produto Y"}]


class ReportService:
    def __init__(self, repository: RepositoryInterface):
        self.repository = repository

    def generate_report(self):
        data = self.repository.get_data()
        print("=== RELATÓRIO GERADO ===")
        for item in data:
            print(f"- {item}")


if __name__ == "__main__":
    repository1 = SQLRepository()
    repository2 = JSONRepository()

    report1 = ReportService(repository1)
    report2 = ReportService(repository2)
    report1.generate_report()
    report2.generate_report()
