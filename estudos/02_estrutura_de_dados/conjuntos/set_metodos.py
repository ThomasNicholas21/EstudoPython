# Metodos de conjunto em python
# union - faz a união de todo o conjunto

conjunto_a = {2, 5, 6}
conjunto_b = {2, 3, 1}
print(conjunto_a.union(conjunto_b))

# intersection - pega a intersecção de um conjunto com relação a outro
print(conjunto_a.intersection(conjunto_b))

# difference - pega a diferença de um conjunto a outro, ou seja, mostra o valor unico
print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

# symmetric_difference - pega tudo que está fora da intersecção
print(conjunto_a.symmetric_difference(conjunto_b))
print(conjunto_b.symmetric_difference(conjunto_a))

# issubset - retorna um valor bool, e indica se todos os elementos de um conjunto pertencem a outro
c_1 = {1, 2, 3}
c_2 = {6, 5, 4, 3, 2, 1}

print(c_1.issubset(c_2)) # todos os valores de c_1 pertencem a c_2
print(c_2.issubset(c_1)) # Nem todos os valores de c_2 pertencem a c_1

# issuperset - ao contrário de issubset
print(c_1.issuperset(c_2))
print(c_2.issuperset(c_1)) 

#isdisjoint - retorna um valor bool e sinaliza se os valores de um conjunto estão em outro
conj_1 = {1, 2, 3} 
conj_2 = {4, 5, 6}

print(conj_1.isdisjoint(conj_2))
print(conj_2.isdisjoint(conj_1)) 

# add - adiciona um valor caso ele não exista
conj_1.add(4)
conj_1.add(5)
conj_1.add(6)
print(conj_1)

# clear - limpa o set
conj_1.clear()
print(conj_1)

# copy - realiza uma copia rasa do set
conj_1 = conj_2.copy()
print(conj_1)

# discard - descarta um valor presente na lista
conj_1.discard(4)
print(conj_1)

# pop - tira o valor do set o primeiro valor
conj_1.pop()
print(conj_1)

# remove - mesa função do discard, mas da erro quando o elemnto não existe
conj_1.remove(6)
try:
    conj_1.remove(45)
except KeyError as K:
    print(f'O valor {K} ocasiona KeyError por não existir no conjunto')
print(conj_1)

# len - tira o tamanho do conjunto
print(len(conj_1))

# in - verifica se um numero está no conjunto
conj_3 = {1, 2, 3, 4, 5, 6}
print(12 in conj_3)
print(6 in conj_3)
