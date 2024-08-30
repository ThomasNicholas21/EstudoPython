# Uma coleção de objetos que possui elementos unicos
# Ou seja, não possui elementos repitidos. Representando
# conjuntos matematicos.
# Exemplos
#Não necessáriamente virá em ordem

print(set([1, 2, 3, 1, 1, 3]))
print(set("Thomas"))
print(set(("Thomas", "Thomas", "Python")))

# Acesso de dados, necessário converter para lista
conjunto = {1, 2, 3, 4}
conjunto = list(conjunto) # forma de converter
print(conjunto[::-1])

# Para acessar os dados iterando
for c in conjunto:
    print(c)

# função enumerate - adiciona um contador a um iteravel
for indice, c in enumerate(conjunto, start=1):
    print(indice, "-", c)


    

