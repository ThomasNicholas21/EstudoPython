# Dia 15: Estruturas Aninhadas
# Faça um programa que simule uma agenda telefônica, 
# onde o usuário pode cadastrar contatos (nome e número) e buscar um contato pelo nome.
from dataclasses import dataclass

@dataclass
class Contato:
    nome: str
    numero: str 

@dataclass
class Agenda_telefonica:
    lista_contatos: list[Contato]

def cadastro_contato():
    ...

def buscar_contato():
    ...

def main():
    ...

if __name__ == '__main__':
    main()
    contato_teste1 = Contato('Fulano', '62982520334')
    lista_contatos = [contato_teste1]
    agenda = Agenda_telefonica(lista_contatos)
    print(contato_teste1, agenda)