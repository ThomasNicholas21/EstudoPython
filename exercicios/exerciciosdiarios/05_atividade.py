# Dia 5: Tuplas
# Crie um programa que armazene nomes de cidades em uma tupla e, em seguida, exiba cada cidade em uma linha diferente.

class Cidade:
    def __init__(self, nome):
        self.nome = nome
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}:{self.nome}'

class ArmazenaCidade:
    def __init__(self, nome, lista=()):
        self.lista = lista
        self.cidade = Cidade(nome)
    
    def armazena_tupla(self):
        nova_tupla = self.lista + (self.cidade, )
        return nova_tupla

def inserir_cidade(lista):
    nome_cidade = input('Insira o nome da cidade: ')
    armazena_cidade = ArmazenaCidade(nome_cidade, lista)
    print(nome_cidade)
    return armazena_cidade.armazena_tupla()

def main():
    lista_cidade = ()

    while True:

        opcao = input('Comando: Inserir, Listar ou Sair ==> ').lower()

        if opcao == 'inserir':
            lista_cidade = inserir_cidade(lista_cidade)
        elif opcao == 'listar':
            print(lista_cidade)
        elif opcao == 'sair':
            break
        else:
            print('Comando Inválido.')

if __name__ == '__main__':
    main()
