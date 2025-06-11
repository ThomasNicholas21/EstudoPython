"""
🔹 I - Interface Segregation Principle (ISP)
Exercício: Criar interfaces para diferentes tipos de
funcionários (Desenvolvedor, Designer, Gerente), garantindo
que cada um implemente somente o que precisa — sem métodos inúteis.
"""
from abc import ABC, abstractmethod


class TaskFinisher(ABC):
    @abstractmethod
    def finish_tasks(self):
        pass


class ComponentFinisher(ABC):
    @abstractmethod
    def finish_components(self):
        pass


class TaskManager(ABC):
    @abstractmethod
    def manage_tasks(self):
        pass


class ComponentManager(ABC):
    @abstractmethod
    def manage_components(self):
        pass


class Developer(TaskFinisher):
    def finish_tasks(self):
        print("Dev finalizou uma tarefa.")


class Designer(ComponentFinisher):
    def finish_components(self):
        print("Designer finalizou um componente visual.")


class Manager(TaskManager, ComponentManager):
    def manage_tasks(self):
        print("Gerente está organizando tarefas.")

    def manage_components(self):
        print("Gerente está revisando componentes.")


if __name__ == "__main__":
    dev = Developer()
    designer = Designer()
    manager = Manager()

    dev.finish_tasks()
    designer.finish_components()
    manager.manage_tasks()
    manager.manage_components()
