# sys.argv - Executa arquivos com argumentos do sistema
import sys

# primeiro argumento sempre vai ser o módulo no
# qual está sendo chamado
argumentos = sys.argv
quantidade = len(argumentos)


if quantidade <= 1:
    print('Sem argumentos passados')
else:
    try:
        print(f'Passou {argumentos[1:]}')
        print(f'Passou {argumentos[1]}')
        print(f'Passou {argumentos[2]}')
    except IndexError:
        print('Sem arqgumentos')
