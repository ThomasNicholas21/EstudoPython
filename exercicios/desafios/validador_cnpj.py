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


def verifier(cnpj) -> bool:
    cnpj_first = first_digit(cnpj)
    cnpj_second = second_digit(cnpj_first)
    
    cnpj_validate = get_last_digits(cnpj)
    cnpj_int = [int(integer) for integer in cnpj_validate]

    if cnpj_second[12:14] == cnpj_int:
        return True

    return False



def get_last_digits(cnpj):
    if ('-' and '.' and '/') in cnpj:
        cnpj_formated = cnpj.replace('-', '').replace('.', '').replace('/', '')
        cnpj_no_verifier_digits = ' '.join(cnpj_formated[12:14])
        cnpj_split = cnpj_no_verifier_digits.split(' ')
        
        return cnpj_split

 
def remove_last_digits(cnpj: str) -> list[str]:
    if not cnpj.isdigit():
        cnpj = ' '.join(re.sub(r'\D', '', cnpj[0:12]))
        cnpj_split = cnpj.split(' ')
        return cnpj_split


def first_digit(cnpj: str):
    cnpj_formated = format(cnpj)
    list_verified = []

    for iterator, value in enumerate(cnpj_formated):
        variable = first_rule_multiplier(iterator, int(value))
        list_verified.append(variable)
    
    list_sum = sum(list_verified)
    rest = list_sum % 11

    if rest < 2:
        last_digit = 0
    else:
        last_digit = 11 - rest

    cnpj_formated.append(last_digit)
    
    return cnpj_formated


def second_digit(cnpj: str):
    list_verified = []

    for iterator, value in enumerate(cnpj):
        variable = second_rule_multiplier(iterator, int(value))
        list_verified.append(variable)
    
    list_sum = sum(list_verified)
    rest = list_sum % 11

    if rest < 2:
        last_digit = 0
    else:
        last_digit = 11 - rest

    list_verified.append(last_digit)

    return list_verified


def first_rule_multiplier(iterator, value):
    list_verifier = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    for verifier_iterator, verifier in enumerate(list_verifier):
        if verifier_iterator == iterator:
            variable = verifier * value
            return variable


def second_rule_multiplier(iterator, value):
    list_verifier = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    for verifier_iterator ,verifier in enumerate(list_verifier):
        if verifier_iterator == iterator:
            variable = verifier * value
            return variable


print(verifier('16.840.122/0001-15'))
