# Dia 5: Tuplas
# Crie um programa que armazene nomes de cidades em uma tupla e, em seguida, exiba cada cidade em uma linha diferente.

class Cidade:
    def __init__(self, nome):
        self.nome = nome
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}:{self.nome}'

class ArmazenaCidade:
    def __init__(self, nome, lista: tuple=None) -> None:
        if lista is None:
            self.lista = ()
        self.lista = lista
        self.cidade = Cidade(nome)
    
    def armazena_tupla(self):
        nova_tupla = self.lista + (self.cidade, )
        return nova_tupla

def inserir_cidade(lista: tuple, nome_cidade: str) -> tuple:
    armazena_cidade = ArmazenaCidade(nome_cidade, lista)
    return armazena_cidade.armazena_tupla()

def processar_comandos(lista_cidade: tuple):
    opcao = input('Comando: Inserir, Listar ou Sair \n--> ').lower()

    if opcao == 'inserir':
            nome_cidade = input('Insira o nome da cidade: ') # boa prática
            lista_cidade = inserir_cidade(lista_cidade, nome_cidade)
    elif opcao == 'listar':
        print(*lista_cidade, sep='\n')
    elif opcao == 'sair':
        return False, lista_cidade
    else:
        print('Comando Inválido.')
    
    return True, lista_cidade

def main():
    lista_cidade = ()

    while True:

        continuar, lista_cidade = processar_comandos(lista_cidade)
        if not continuar:
            break

    print('Cidades cadastradas:', *lista_cidade, sep='\n')


if __name__ == '__main__':
    main()
