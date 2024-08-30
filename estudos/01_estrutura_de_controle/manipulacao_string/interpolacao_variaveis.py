# Interpolação de Variáveis
# % - versão antiga
nome = 'thomas nicholas' # %s para strings
idade = 23 # %d para inteiros %f para float
profissao = 'AnAliSta'
linguagem = 'pYthon'
print('Me chamo %s tenho %d anos, sou %s e atualmente estudo '
      '%s.'%(nome.title(), idade, profissao.lower(), linguagem.upper()))

# format - "especifica de forma automatica"
print('Me chamo {} tenho {} anos, sou {} e atualmente estudo '
      '{}.'.format(nome.title(), idade, profissao.lower(), linguagem.upper()))
# format - "especifica de forma manual"
print('Me chamo {3} tenho {2} anos, sou {1} e atualmente estudo '
      '{0}.'.format(nome.title(), idade, profissao.lower(), linguagem.upper()))
# format - "especifica de forma logica"
print('Me chamo {name} tenho {age} anos, sou {profession} e atualmente estudo '
      '{language}.'.format(name=nome.title(), age=idade, profession=profissao.lower(), 
                            language=linguagem.upper()))
# format - "desempacotando dicionario"
pessoa = {'nome': nome.upper(), 
          'idade': idade, 
          'profissao': profissao.upper(), 
          'linguagem': linguagem.upper()
          }
print('Me chamo {nome} tenho {idade} anos, sou {profissao} e atualmente estudo '
      '{linguagem}.'.format(**pessoa))

# f strings
print(f'Me chamo {nome.title()} tenho {idade} anos, sou {profissao.lower()} e atualmente estudo '
      f'{linguagem.upper()}.')
valor = 2.15213
print(f'O valor é: {valor:.2f}')
