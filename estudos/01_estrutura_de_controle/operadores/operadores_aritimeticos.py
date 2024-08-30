# Operadores aritméticos são aqueles que realizão operação matemática
# Faz a soma
def soma(n1, n2):
    return print(n1 + n2)
# Faz a subtração
def subtracao(n1, n2):
    return print(n1 - n2)
# Faz a multiplicação
def multiplicacao(n1, n2):
    return print(n1 * n2)
# Faz a divisão
def divisao(n1, n2):
    return print(n1 / n2)
# Faz a divisão inteira, retornando um número inteiro
def divisao_inteira(n1, n2):
    return print(n1 // n2)
# Faz o resto da divisão
def modulo(n1, n2):
    return print(n1 % n2)
# Faz a exponenciação
def exponenciacao(n1, n2):
    return print(n1 ** n2)

soma(8, 2)
subtracao(8, 2)
multiplicacao(8, 2)
divisao(8, 2)
divisao_inteira(8, 2)
modulo(8, 2)
exponenciacao(8, 2)

# Regras para cálculos aritiméticos, seguindo a seguinte regra:
# 1º Parêntesis
# 2º Expoêntes
# 3º Multiplicação e divisão(esquerda para direita)
# 4º Soma e subtração(esquerda para direita)
# Exemplos de cálculos seguindo a primeira regra:

print((10+5) / (15+5))
print((55+5) * 5)
print((5**2) + (5+5))

# Segunda regra

print(10 ** 2 * 5)
print(2 ** 8 + 23)
print(2 ** 10 / 1000)

# Terceira regra

print(10 * 2 + 2)
print(10 / 2 * 5)
print(10 // 3 + 2)

# Quarta Regra

print(11 + 11)
print(22 + 54 - 2)
print(22 - 34 + 2)