# Métodos úteis para manipulação de string
# string.upper() - todos caracteres para maiúsculo
# string.lower() - todos caracteres para minúsculo
# string.title() - Primeiro caractere Maiúsculo e o restante minúsculo
# string.strip() - remove espaços
# string.lstrip() - remove o espaço a esquerda
# string.rstrip() - remove o esparaço a direita
# string.center() - 2 argumentos sendo o segundo opcional; número de caracter, e com o que vai ser preenchido
# string.split(sep, maxsplit) - o sep é o criterio de separação e maxsplit o maximo de separação (opcional) 
# 'item'.join(string) -  junta o item na string
# string.replace(old, new, count): Substitui todas as ocorrências de uma substring 
# por outra. O argumento count é opcional e define o número máximo de substituições.
# string.startswith(prefix): Verifica se a string começa com a substring especificada.
# string.endswith(suffix): Verifica se a string termina com a substring especificada.
# string.find(sub): Retorna o índice da primeira ocorrência da substring. 
# Retorna -1 se a substring não for encontrada.
# string.count(sub): Conta quantas vezes a substring aparece na string.
# string.zfill(width): Preenche a string com zeros à esquerda até atingir o comprimento especificado.
# string.isdigit(): Verifica se todos os caracteres na string são dígitos.
# string.isalpha(): Verifica se todos os caracteres na string são letras.

string = 'ThOmAsNicholas'
print(string.title())
print(string.lower())
print(string.upper())
print(string.strip())
print(string.lstrip())
print(string.rstrip())
print(string.center(10, '!'))
print('!'.join(string))
string_texto = ' Thomas joga basquete. '
print(string_texto.split(" "))
print(string.replace('Nicholas', 'Pedrosa'))
print(string.startswith('T'))
print(string.endswith('s'))
print(string.find('i'))
print(string.count('h'))
print(string.zfill(25))
print(string.isdigit())
print(string.isalpha())