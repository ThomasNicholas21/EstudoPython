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
    def __init__(self, agencia: str, numero: int, saldo: float = 0) -> None:
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
    def __init__(self, limite_maximo, agencia: str, numero: int, saldo: float = 0) -> None:
        super().__init__(agencia, numero, saldo)
        self.limite_maxim = limite_maximo

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
    def __init__(self, agencias: list[str], contas: list[Conta], clientes: list[Pessoa]) -> None:
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
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}:{'\n'.join([f'{value}' for value in self.__dict__.values()])}'
    
if __name__ == '__main__':
    #conta = Conta(1, 120.50)
    cc = ContaCorrente(1000, '001', 12, 1000)
    cp = ContaPoupanca('003', 1, 555)
    cliente1 = Cliente(cc, 'Thomas', 22, '123456789', '123456')
    cliente2 = Cliente(cp, 'Nicholas', 21, '987456321', '123987456')
    print(cliente1)
    lista_contas = [cc, cp]
    lista_clientes = [cliente1, cliente2]
    lista_agencias = ['001', '002']
    #cp.sacar(155)
    #print(cp._saldo)
    banco = Banco(lista_agencias, lista_contas, lista_clientes)
    print('Conta Auntenticada' if banco.autenticar(cliente1, cc) else 'Conta não autenticada')
    print('Conta Auntenticada' if banco.autenticar(cliente2, cp) else 'Conta não autenticada')
