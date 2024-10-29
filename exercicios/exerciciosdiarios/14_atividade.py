# Dia 14: Tratamento de Exceções
# Desenvolva um calculadora que peça dois números ao usuário, e faça a divisão tratando a exceção de divisão por zero.
def divisao_por_zero(self):
    ...

def verificacao_string(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)

        for arg in args:
            if isinstance(arg, (str, bool)):
                raise ValueError('Erro. Deve ser colocado um número.')
        
        return resultado
    
    return interno

class Calculadora:
    @verificacao_string
    def __init__(self, numero1: int | float, numero2: int | float) -> None:
        self.numero1 = numero1
        self.numero2 = numero2
    
    def soma(self):
        soma = f'Soma: {self.numero1} + {self.numero2} = {self.numero1 - self.numero2}'
        return soma
    
    def subtracao(self):
        subtracao = f'Subtração: {self.numero1} - {self.numero2} = {self.numero1 - self.numero2}'
        return subtracao

    def multiplicacao(self):
        multiplicacao = f'Multiplicação: {self.numero1} * {self.numero2} = {self.numero1 * self.numero2}'
        return multiplicacao
    
    def divisao(self):
        divisao = f'Divisão: {self.numero1} / {self.numero2} = {self.numero1 / self.numero2}'
        return divisao

def calculadora(digitos):
    ...

def processar_comandos(historico_calculo):
    comandos = input('Comandos: Soma, subtração, multiplicação, divisão e histórico\n-->').lower()

    match comandos:
        case 'soma':
            ...
            return True
        case 'subtração':
            ...
            return True
        case 'multiplicação':
            ...
            return True
        case 'divisão':
            ...
            return True
        case 'histórico':
            ...
        case 'sair':
            return False
        case _:
            print('Opção inválida.')
            return True

def main():
    historico_calculo = []

    while True:
        comando = processar_comandos(historico_calculo)
        if not comando:
            break
        

if __name__ == '__main__':
    main()
    teste = Calculadora('1', 2)
