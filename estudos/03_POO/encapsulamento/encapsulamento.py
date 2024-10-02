class conta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self._saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo = self._saldo + valor
            return print('Deposito Aprovado')
        return print('Deposito Reprovado')

    def sacar(self, valor):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
            return print('Saque Aprovado')
        return print('Saque  Reprovado')
    
    def __str__(self) -> str: # Será um método com má pratica pois foi definido que _saldo é um atributo privado
        return f'{self.__class__.__name__}:\n{'\n'.join([f'{chave}:{valor}' for chave, valor in self.__dict__.items()])}'
    
conta1 = conta('Thomas', 1200)
# print(conta1._saldo) # Má prática pois foi definido que o dado está protegido
conta1.depositar(1000)
# conta1.depositar(-1)
conta1.sacar(3000)
conta1.sacar(2199)
print(conta1)