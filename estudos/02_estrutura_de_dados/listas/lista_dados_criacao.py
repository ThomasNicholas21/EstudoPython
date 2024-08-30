# Listas armazeam de forma sequencial qualquer objeto.input
# Objetos mutáveis 
# Fatimatento lista[inicio:final:passo]
# Exemplos de criação de lista:
       #     0          1         2
frutas = ['Abacaxi', 'Mamão', 'Banana']
print(frutas[0:2])
frutas = []

# Bult-in (list) que cria lista caso esteja vazio, ou itera sobre o objeto inserido(Deve ser iteravel)
letras = list('Thomas') 
print(letras)
numeros = list(range(20))
print(numeros[::-1])
pessoa = ['Thomas', 23, True]
print(pessoa)

# Exemplos de listas com matriz
matriz = [ 
    [1, '2', 3],
    [4, '5', 6],
    [7, 'a', 8]
]
# matriz[linha][coluna]
print(matriz[1][1])
print(matriz[2][1])