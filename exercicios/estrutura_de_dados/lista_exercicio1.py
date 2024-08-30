# Exercicio de lista, utilizando funcao e dicionario
# Escreva uma função em Python que receba uma lista como entrada e retorne um dicionário onde as
# chaves são os elementos da lista e os valores são a contagem de cada elemento na lista.

def recebe_lista(args):
    dic = {}
    for arg in args:
        dic.setdefault(arg, args.count(arg))
    return print(dic)

lista = [1, 1, 'Thomas', 'Thomas', 4 ]
recebe_lista(lista)