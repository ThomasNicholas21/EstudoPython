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