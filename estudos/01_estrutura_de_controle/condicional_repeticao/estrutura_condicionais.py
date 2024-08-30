# Estrutura condicional permite desvio caso as expressões
# lógicas são atendidas.
# if / if-else / elif
# if aninhado - são condicionais dentro de condicionais
# if ternário - condição em uma unica linha.
# "retorno da primeira condição" if condição else "retorno da segunda"
# Atividade para colocar em prática
# jogo de adivinha

def regra(numero_correto, valor_palpite):
    diferenca = numero_correto - valor_palpite
    if diferenca > 30:
        return print(f'O valor: {valor_palpite} está muito Longe!')
    elif 20 <= diferenca <= 30:
        return print(f'O valor: {valor_palpite} está Longe!')
    elif 10 <= diferenca < 20:
        return print(f'O valor: {valor_palpite} está Perto!')
    else:
        return print(f'O valor: {valor_palpite} está Muito Perto!')

def advinhou(numero_correto, valor_palpite):
    if numero_correto == valor_palpite:
        print(f'Vitóriaa, valor {valor_palpite} está correto!')
        return True
    return False

tentativas = 10
numero_correto = 12
while tentativas > 0:
    valor_palpite = int(input('Tente advinhar o valor:'))
    if advinhou(numero_correto, valor_palpite):
        break
    else:
        regra(numero_correto, valor_palpite)
        tentativas -= 1 
        tentativa = print('Ultima tentativa!!!\n') if tentativas == 1 else print(f'Numero de tentivas: {tentativas}\n') 