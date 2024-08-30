# Operadores de identidades, sendo eles operadores que comparam objetos
# para testar se ocupam a mesma posição da memória
# is - verifica se um objeto ocupa o mesmo espaço

valor1 = 1000
valor2 = 1000
valor3 = 500

print(valor1 is valor2)
print(valor1 is not valor2)
print(valor1 is valor3)
print(valor1 is not valor3)
print(valor2 is valor3)
print(valor2 is not valor3)