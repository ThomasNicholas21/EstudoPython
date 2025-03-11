# estudo de match case aplicando case guard
# pré requisito
from dataclasses import dataclass

@dataclass
class Comando:
    command: str
    directories: list[str]


def comandos(comando: Comando):
    match comando:
        case Comando(command='ls'): # Utilizando um atributo da classe para dar match
            for directory in comando['directories']:
                print('directory from:', directory)

        case Comando(command='cd', directories=[_, *_]): # Utilizando um atributo da classe para dar match
            for directory in comando['directories']:
                print('directory from:', directory)


comando1 = Comando(command='ls', directories=['/home'])
comando2 = Comando(command='cd', directories=['/user', '/home'])

comandos(comando1)
print()
comandos(comando2)
