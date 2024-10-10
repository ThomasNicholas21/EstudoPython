# Dia 5: Tuplas
# Crie um programa que armazene nomes de cidades em uma tupla e, em seguida, exiba cada cidade em uma linha diferente.

class Cidade:
    def __init__(self, nome):
        self.nome = nome
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}:{self.nome}'

class ArmazenaCidade(Cidade):
    def __init__(self, nome, lista=()):
        super().__init__(nome)
        self.lista = lista
    
    def armazena_tupla(self):
        return self.lista(self.nome, )

def main():
    lista_cidade = ()

    while True:

        opcao = input('Comando: Inserir, Listar ou Sair ==> ').lower()

        if opcao == 'inserir':
            ...
        elif opcao == 'listar':
            ...
        elif opcao == 'sair':
            break
        else:
            print('Comando Inválido.')

if __name__ == '__main__':
    # main()
    lista = ()
    print(bool(lista))