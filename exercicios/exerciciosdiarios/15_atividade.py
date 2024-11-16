# Dia 15: Estruturas Aninhadas
# Faça um programa que simule uma agenda telefônica, 
# onde o usuário pode cadastrar contatos (nome e número) e buscar um contato pelo nome.
from dataclasses import dataclass

@dataclass
class Contato:
    _nome: str
    _numero: str 

    @property
    def get_nome(self) -> str:
        return self._nome

    @property
    def get_numero(self) -> str:
        return self._numero

@dataclass
class Agenda_telefonica:
    lista_contatos: list[Contato]

    def find_contato(self, contato: Contato) -> bool:
        if contato in self.lista_contatos:
            return True
        return False
    
    def get_informacoes(self, contato: Contato) -> str | None:
        if self.find_contato(contato):
            return f'Nome:{contato.get_nome}, número:{contato.get_numero}'
        return 

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
    if agenda.find_contato(contato_teste1):
        print('Presente')
    contato = agenda.get_informacoes(contato_teste1)
    print(contato)