# estudo de match case com dicionários
def comandos(comando: dict):
    match comando:
        case {'command': 'ls', 'directories': [_, *_]}: # _ : indica apenas um diretorio, *_: indica vários diretórios
            for directory in comando['directories']:
                print('directory from:', directory)

        case _:
            print('Unknown command')

comandos({'command': 'ls', 'directories': ['/user', '/home', '/files']})
print()
