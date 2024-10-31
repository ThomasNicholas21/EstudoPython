from abc import ABC, abstractmethod

class Pessoa:
    ...

class Cliente(Pessoa): # Agrega classe Conta
    ...

class Transacao(ABC):
    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass

class Conta(Transacao):
    def sacar(self, valor):
        pass

    def depositar(self, valor):
        pass

class ContaCorrente(Conta):
    def sacar(self, valor):
        pass

    def depositar(self, valor):
        pass

class ContaPoupanca(Conta):
    def sacar(self, valor):
        pass

    def depositar(self, valor):
        pass

class Banco: # agrega clientes e contas
    ...