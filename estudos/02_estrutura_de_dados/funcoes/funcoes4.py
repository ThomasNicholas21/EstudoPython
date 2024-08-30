# Objetos de primeira classe
# atribuir funcoes a variaveis
# parrar como parametros para funcoes
# utilzar com valores em estrutura de dados
# usar como valor de retorna para uma funcao(closure)
# Closure cria uma associcao de dados com uma funcao que trabalha esses dados
# Exemplo

def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b

def multiplicacao(a, b):
    return a * b 

def reliza_operacao(a, b, funcao):
    operacao = funcao(a, b)
    return print(f'O valor da operacao é {operacao}')

reliza_operacao(10, 2, soma)
reliza_operacao(10, 2, sub)
reliza_operacao(10, 2, div)
reliza_operacao(10, 2, multiplicacao)