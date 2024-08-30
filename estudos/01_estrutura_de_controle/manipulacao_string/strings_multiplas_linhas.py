# Strings múltiplas linhas são definidads  informando:
# 3 aspas simples ou duplas
# todos os espaçoes em brnaco são incluidos na string final
valor1 = 123
valor2 = 321
print(f"""
Soma = {valor1 + valor2}
    Subtracao = {valor1 + valor2}
Divisao = {valor1 / valor2}
    Divisao inteira = {valor1 // valor2}
Resto = {valor1 % valor2}
    Multiplicaco = {valor1 * valor2}
Exponenciacao = {valor1**2, valor2**2} 
""")