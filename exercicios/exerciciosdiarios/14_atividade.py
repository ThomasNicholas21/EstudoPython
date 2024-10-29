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

def calculadora(historico_calculo, operacao):
    try:
        numero1 = int(input('Digite o número1: '))
        numero2 = int(input('Digite o número2: '))

    except:
        ...

def processar_comandos(historico_calculo, calculadora):
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
    calc = Calculadora()

    while True:
        comando = processar_comandos(historico_calculo, calc)
        if not comando:
            break
        

if __name__ == '__main__':
    main()