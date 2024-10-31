from abc import ABC, abstractmethod

class Pessoa:
    def __init__(self, nome: str, idade: int, cpf: str, cep: str) -> None:
        self._nome = nome
        self._idade = idade
        self._cpf = cpf
        self._cep = cep

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def idade(self):
        return self._idade
    
    @property
    def cpf(self) -> str:
        return self._cpf
    
    @property
    def cep(self) -> str:
        return self._cep

class Cliente(Pessoa): # Agrega classe Conta
    def __init__(self, conta, nome: str, idade: int, cpf: str, cep: str) -> None:
        super().__init__(nome, idade, cpf, cep)
        self.conta = conta

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
    cliente2 = Pessoa('Nicholas', 21, '987456321', '123987456')
    print(cliente2.nome)
    print(cliente2.idade)
    print(cliente2.cpf)
    print(cliente2.cep)