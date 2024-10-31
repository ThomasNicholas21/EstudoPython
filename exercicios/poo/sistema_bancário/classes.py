from abc import ABC, abstractmethod

class Pessoa:
    def __init__(self, nome, idade, cpf, cep) -> None:
        self._nome = nome
        self._idade = idade
        self._cpf = cpf
        self._cep = cep

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade
    
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def cep(self):
        return self._cep

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

if __name__ == '__main__':
    cliente1 = Pessoa('Thomas', 22, '123456789', '123456')
    print(cliente1.nome)
    print(cliente1.idade)
    print(cliente1.cpf)
    print(cliente1.cep)