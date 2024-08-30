# Identação, o objetivo é manter o código fonte
# limpo, legível e manutenível.

# O interpretador python consegue determinar
# onde o bloco inicia e onde ele termina.

# Indicado deixar 4 espaços em branco por
# nivel de identação. E cada bloco adicionado
# 4 novos espaços em branco.
# Exemplo: 

def exponencia_valor(valor, n): # Inicia o bloco do metodo
    if valor >= 0: # Inicia a condificional
        return print(valor**n)
    return print('Operação não relizada')
    # finaliza a condiciononal 
# finaliza o metodo

exponencia_valor(20, 2)