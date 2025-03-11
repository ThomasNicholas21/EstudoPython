# estudo de match case com listas
def comandos(comando: str):
    match comando.split(): # tira espaços e retorna uma lista
        case ['ls', *directories]:
            for directory in directories:
                print('directory from:', directory)

        case ['ls' | 'list', path]: # | == or
            print('changing directory to', path)

        case ['cd', path]:
            print('changing directory to', path)

        case _:
            print('Unknown command')

comandos('ls /home /users /etc')
