# Dia 14: Tratamento de Exceções
# Desenvolva um calculadora que peça dois números ao usuário, e faça a divisão tratando a exceção de divisão por zero.
from typing import Any


def divisao_por_zero(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)
        
        if args[1] == 0:
            raise ZeroDivisionError('Erro de divisão por zero')

        return resultado
    
    return interno

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
    def soma(self, numero1: int | float, numero2: int | float):
        soma = f'Soma: {numero1} + {numero2} = {numero1 - numero2}'
        return soma
    
    @verificacao_string
    def subtracao(self, numero1: int | float, numero2: int | float):
        subtracao = f'Subtração: {numero1} - {numero2} = {numero1 - numero2}'
        return subtracao

    @verificacao_string
    def multiplicacao(self, numero1: int | float, numero2: int | float):
        multiplicacao = f'Multiplicação: {numero1} * {numero2} = {numero1 * numero2}'
        return multiplicacao
    
    @divisao_por_zero
    @verificacao_string
    def divisao(self, numero1: int | float, numero2: int | float):
        divisao = f'Divisão: {numero1} / {numero2} = {numero1 / numero2}'
        return divisao

def solicitar_digito():
    numero1 = int(input('Digite o número1: '))
    numero2 = int(input('Digite o número2: '))
    return numero1, numero2

def somar(historico_calculo: list, calculadora: Calculadora):
    try:
        numero1, numero2 = solicitar_digito()
        resultado = calculadora.soma(numero1, numero2)
        print(resultado)
        historico_calculo.append(resultado)

    except ValueError as ve:
        print(f'Números devem ser números!: ', ve)

def processar_comandos(historico_calculo: list):
    calc = Calculadora()
    comandos = input('Comandos: Soma, subtração, multiplicação, divisão e histórico\n-->').lower()

    match comandos:
        case 'soma':
            somar(historico_calculo, calc)
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
            print(historico_calculo, sep='\n')
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