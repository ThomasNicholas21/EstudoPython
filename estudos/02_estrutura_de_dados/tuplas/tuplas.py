# Tuplas parecem listas, porém são imutáveis
# Como criar:

nomes = ("Thomas", "Nicholas", "Pedrosa")
tecnologia = tuple("Python")
numeros = tuple([1, 2, 3, 4])
pais = ("Argentina",)
print(nomes)
print(tecnologia)
print(numeros)
print(pais)
print()
# Como acessar indices

print(nomes[::-1])
print(tecnologia[2])
print(numeros[0])
print(pais[-1])
print()
# Tuplas aninhadas
# tuplas dentro de tuplas

matriz = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print(matriz[1][1])