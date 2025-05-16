# aqui será feito um validador de cnpj
# o cnpj é composto por 14 digitos, sendo os 2 últimos digitos os verificadores
# primneira etapa:
# Pegar os 12 primeiro digitos e multiplicar por 5,4,3,2,9,8,7,6,5,4,3,2
# depois pegar o resultado e fazer uma soma e dividir por 11
# regra:
# se o resto da divisao for menor que 2, primeiro digito sera 0, se maior que 2, o primeiro digito sera (11 - resto da divisão)

# segunda etapa:
# pegar os 12 primeiros digitos e multiplicar por 6,5,4,3,2,9,8,7,6,5,4,3,2
# depois de pegar o resultado e fazer uma soma e dividir por 11
# regra:
# se o resto da divisao for menor que 2, segundo digito sera 0, se maior que 2, segundo digito sera (11 - quociente da divisão inteiro)
import re

def clean_cnpj(cnpj: str) -> str:
    return re.sub(r'\D', '', cnpj)

def calculate_digit(cnpj, weights):
    total = sum(int(d) * w for d, w in zip(cnpj, weights))
    rest = total % 11
    return 0 if rest < 2 else 11 - rest

def is_sequential(cnpj: str) -> bool:
    return cnpj == cnpj[0] * len(cnpj)

def verifier(cnpj: str):
    cnpj = clean_cnpj(cnpj)

    if len(cnpj) != 14:
        return {'erro': 'CNPJ deve conter 14 dígitos numéricos'}

    if is_sequential(cnpj):
        return {'erro': 'CNPJ com dígitos repetidos não são válidos'}

    cnpj_base = cnpj[:12]
    digit1 = calculate_digit(cnpj_base, [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2])
    digit2 = calculate_digit(cnpj_base + str(digit1), [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2])

    if cnpj[-2:] == f"{digit1}{digit2}":
        return {'valido': True, 'cnpj': cnpj}
    else:
        return {'erro': 'CNPJ informado é inválido!', 'cnpj': cnpj}
    

print(verifier('18426795000160'))

