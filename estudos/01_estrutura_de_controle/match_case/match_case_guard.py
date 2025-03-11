# estudo de match case aplicando case guard
def comandos(comando: str):
    match comando.split():
        case ['ls' | 'list', *directories] if len(directories) > 1:
            for directory in directories:
                print('directory from:', directory)

        case ['ls' | 'list', *directories] if len(directories) <= 1:
            print('one directory from:', directories[0])

        case ['cd', path]:
            print('changing directory to', path)

        case _:
            print('Unknown command')

comandos('ls /home /users /etc')
print()
comandos('ls /home')
