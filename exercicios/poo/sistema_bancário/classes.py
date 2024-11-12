import abc

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

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}:{' | '.join([f'{valor!r}' for valor in self.__dict__.values()])}'

class Cliente(Pessoa): # Agrega classe Conta
    def __init__(self, conta, nome: str, idade: int, cpf: str, cep: str) -> None:
        super().__init__(nome, idade, cpf, cep)
        self.conta = conta

class Conta(abc.ABC):
    def __init__(self, numero: int, saldo: float = 0, agencia='001') -> None:
        self.agencia = agencia
        self._numero = numero
        self._saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor) -> float: ...  

    def depositar(self, valor: float) -> None:
        print(f'Depositando R${valor:.2f}')
        self.saldo += valor

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}: {self.agencia!r} | {self._numero!r} | {self._saldo!r}'

class ContaCorrente(Conta):
    def __init__(self, limite_maximo, numero: int, saldo: float = 0) -> None:
        super().__init__(numero, saldo)
        self.limite_maximo = limite_maximo

    def sacar(self, valor) -> float:
        if valor > self.limite_maximo:
            print('Saque negado.')
            return 
        
        self._saldo -= valor
        print('Saque efetuado.')
        return self._saldo

class ContaPoupanca(Conta):
    def sacar(self, valor) -> float | None:
        if valor > self._saldo:
            print('Saque negado.')
            return
        
        self._saldo -= valor
        print('Saque efetuado.')
        return self._saldo


class Banco: # agrega clientes e contas
    def __init__(self, agencias: list[int], contas: list[Conta], clientes: list[Pessoa]) -> None:
        self.agencias = agencias or []
        self.contas = contas or []
        self.clientes = clientes or []

    def _checar_agencia(self, conta: Conta) -> bool:
        if conta.agencia in self.agencias:
            return True
        return False

    def _checar_conta(self, conta: Conta) -> bool:
        if conta in self.contas:
            return True
        return False

    def _checar_cliente(self, cliente: Pessoa) -> bool:
        if cliente in self.clientes:
            return True
        return False
    
    def autenticar(self, cliente: Pessoa, conta: Conta) -> bool:
        return self._checar_agencia(conta) and \
        self._checar_cliente(cliente) and self._checar_conta(conta)
    
if __name__ == '__main__':
    #conta = Conta(1, 120.50)
    cc = ContaCorrente(1000, 12, 1000)
    cp = ContaPoupanca(1, 555)
    cliente1 = Cliente(cc, 'Thomas', 22, '123456789', '123456')
    cliente2 = Cliente(cp, 'Nicholas', 21, '987456321', '123987456')
    print(cliente1)
    lista_contas = [cc, cp]
    lista_clientes = [cliente1, cliente2]
    #cp.sacar(155)
    #print(cp._saldo)
    banco = Banco('001', lista_contas, lista_clientes)
    print(banco.verificar_agencia(cp))
