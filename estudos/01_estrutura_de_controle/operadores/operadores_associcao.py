#  Verifica se um objeto está numa sequencia
lista_carros = ['Ferrari', 'Lamborghini', 'Fiat']
print('Fiat' in lista_carros)
print('Fiat' not in lista_carros)
print('Lamborghini' in lista_carros)

lista_carros_novo = [
    carros for carros in lista_carros
    if len(carros) == 4
]

print(*lista_carros_novo, sep='\n')