# Exercicio - Save sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos.
# Faça em arquivos separados
import json

class CriaPessoa:
    def __init__(self, nome, ano_nascimento, genero, tamanho):
        self.nome = nome
        self.ano_nascimento = ano_nascimento
        self.genero = genero
        self.tamanho =  tamanho

    def empacotar(self, lista_de_dicionario):
        lista_de_dicionario.append(self.__dict__)
         
    def exportar(self, lista_de_dicionario):
        with open('D:/programação/EstudoPython/exercicios/poo/classes_objetos_json/pessoa.json', 'w') as arquivo:
            json.dump(lista_de_dicionario, arquivo, indent=2)

def main():
    pessoa1 = CriaPessoa('Fulano', 2001, 'Masculino', 175)
    pessoa2 = CriaPessoa('Ciclana', 1996, 'Feminino', 150)
    pessoa1.exportar()
    pessoa2.exportar()

    
main()            
