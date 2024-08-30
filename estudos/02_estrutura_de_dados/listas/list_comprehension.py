# List comprehension
# Sintaxe curta para criar uma nova lista de uma lista já existente
# Exemplo

lista = [2, 3, 4, 5]
nova_lista1 = [valor for valor in lista]
print(*nova_lista1, sep='\n')
print()

nova_lista2 = [valor for valor in lista if valor % 2 == 0]
print(*nova_lista2, sep='\n')
print()

nova_lista2 = [valor * 2 for valor in lista]
print(*nova_lista2, sep='\n')
print()

nova_lista = [
    valor * 2               # Mapeamento
    for valor in lista
    if valor % 2 == 0       # Filtragem
]
print(*nova_lista, sep='\n')
# lembrando que tudo a direita da lista é filtragem, a esquerda mapeamento
# filtragem seleciona o elemento que atende uma condicao especifica - não necessáriamente terá a mesma quantidade da lista antiga
nova_lista = [
    valor for valor in lista
    if valor % 2 == 0       # Filtragem
]
# Mapeamento transforma um elemento de acordo - devendo ter a mesma quantidade do lista antiga
nova_lista = [
    valor * 2               # Mapeamento
    for valor in lista
]
print(*nova_lista, sep='\n')

# Dois FOR dentro da List Comprhension
lista_2for = []
for x in range(3):
    for y in range(3):
        lista_2for.append((x,y))

print(*lista_2for, sep='\n')

nova_lista2for = [
    (x, y)
    for x in range(3) 
    for y in range(3)
]

print(nova_lista2for , sep='\n') 