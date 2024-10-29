# Dia 14: Tratamento de Exceções
# Desenvolva um calculadora que peça dois números ao usuário, e faça a divisão tratando a exceção de divisão por zero.

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
    
def subtrair(historico_calculo: list, calculadora: Calculadora):
    try:
        numero1, numero2 = solicitar_digito()
        resultado = calculadora.subtracao(numero1, numero2)
        print(resultado)
        historico_calculo.append(resultado)

    except ValueError as ve:
        print(f'Números devem ser números!: ', ve)

def multiplicar(historico_calculo: list, calculadora: Calculadora):
    try:
        numero1, numero2 = solicitar_digito()
        resultado = calculadora.multiplicacao(numero1, numero2)
        print(resultado)
        historico_calculo.append(resultado)

    except ValueError as ve:
        print(f'Números devem ser números!: ', ve)

def processar_comandos(historico_calculo: list):
    calc = Calculadora()
    comandos = input('Comandos: Soma[sum], subtração[sub], multiplicação[mult], divisão[div], histórico[hist] e sair[s]\n-->').lower()
    
    match comandos:
        case 'sum':
            somar(historico_calculo, calc)
            return True
        case 'sub':
            subtrair(historico_calculo, calc)
            return True
        case 'mult':
            multiplicar(historico_calculo, calc)
            return True
        case 'div':
            ...
            return True
        case 'hist':
            print(historico_calculo, sep='\n')
        case 's':
            return False
        case _:
            print('Opção inválida. Tente sum, sub, mult, div ou hist para comandos válidos')
            return True

def main():
    historico_calculo = []

    while True:
        comando = processar_comandos(historico_calculo)
        if not comando:
            break
        

if __name__ == '__main__':
    main()