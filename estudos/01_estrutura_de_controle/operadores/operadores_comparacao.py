# Operadores utilizado para comparar valores
# == igual
# != diferente
# > e >= Maior/Maior ou igual
# < e <= Menor/Menor ou igual

# Primeiro exemplo
salario = 1000
conta = 150

if salario == 1000:
    print("Recebeu o salário completo")
else: 
    print("Não recebeu salário completo")

# Segundo exemplo
if conta != 1000:
    print("Sem dinheiro para sacar")
else: 
    print("Dinhero disponivel para sacar")

# Terceiro exemplo

if conta >= 1000:
    print("Sua conta tem mais de mil.")

if conta > 150:
    print("Conta com mais de 150")
else:
    print("Conta com 150")

# Quarto exemplo

if conta <= 150:
    print("A conta tem 150 ou menos")

if conta < 150:
    print("Menos que 150")