# Metodos usados para classe lista
# Conceito de pilha - primeiro a entrar e ultimo a sair
# Metodo append, adiciona objetos ao final da lista
lista = []
lista.append("Thomas")
lista.append([10, 20, 30])
lista.append(("Thomas", "Nicholas"))

# Metodo clear - limpa a lista
lista.clear()
print(*lista, sep='\n')

# Metodo copy - faz uma copia rasa (shallow copy)
lista1 = [1, 2, 3] 
lista2  = lista1.copy()      
lista2[0] = 5

print(lista1)
print(lista2)

# Metodo count - quantas vezes o objeto aparece dentro da lista
nomes = ["Thomas", "Thomas", "Alberto", 1, 1, 2]
print(nomes.count("Thomas"))
print(nomes.count("Alberto"))
print(nomes.count(1))

# Metodo exetend - adiciona outros valores de uma lista ao final da lista que chamou o metodo
sequencia1 = [1, 2, 3, 4, 5]
sequencia2 = [6, 7, 8, 9, 10]
sequencia1.extend(sequencia2)
print(sequencia1)

# Metodo index - mostra a posicao de um elemento dentro da lsita (sempre retornado a primeira ocorrencia)
print(sequencia1.index(6))

# Metodo pop - tira o ultimo elemento selencionado (podendo passar o index)
sequencia1.pop(2)
sequencia1.pop()
print(sequencia1)

# Metodo remove - passa o objeto para remover (precisa de um argumento)
sequencia1.remove(8)
print(sequencia1)

# Metodo reverse - inverte a ordem da lista
sequencia1.reverse()
print(sequencia1)

# Metodo sort - metodo de ordenacao de lista (por padrao na ordem crescente)
animais = ['Gato', 'Cachorro', 'Arraia', 'Passaro', 'Morcego']
animais.sort()
print(animais)
animais.sort(reverse=True)
print(animais)
animais.sort(key=lambda x: len(x))
print(animais)

# Metodo len - tamanho da lista (pode ser usado em listas)
print(len(animais))

# Sorted funcao bult-in - retorna uma nova lista (por padrão é crescente) 
# ideal quando se quer preservar a lista original
ordenacao = sorted(animais, key=len, reverse=True)
print(ordenacao) # nova lista "ordenacao"
print(sorted(animais, key=len, reverse=True)) # preserva a lista original