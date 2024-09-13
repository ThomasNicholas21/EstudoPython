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

    def empacotar(self, lista_pessoas_dict):
        lista_pessoas_dict.append(self.__dict__)
         
    def exportar(self, lista_de_dicionario):
        with open('D:/programação/EstudoPython/exercicios/poo/classes_objetos_json/pessoa.json', 'w') as arquivo:
            json.dump(lista_de_dicionario, arquivo, indent=2)

def cadastrar(lista_pessoas):
    deseja_cadastrar = input('Deseja cadastrar pessoa? [S]im ou [N]ão: ').lower().startswith('s')
    if deseja_cadastrar:
        try:
            nome = input('Nome: ')
            ano_nascimento = int(input('Ano de Nascimento: '))
            genero = input('Genero:')
            tamanho = int(input('Tamanho em CM: '))

            pessoa = CriaPessoa(nome=nome, ano_nascimento=ano_nascimento, genero=genero, tamanho=tamanho)
            print('Cadastro concluido.')
            pessoa.empacotar(lista_pessoas)
            return pessoa

        except ValueError:
            print(f'{ValueError}: Opa, você inseriu um valor errado.')
            return
        except Exception:
            print('Algo aconteceu 😢')
            return
    return

def main():
    lista_pessoas = []

    while True:
        opcoes = input('Comandos: Cadastrar, Exportar ou Sair\n'
                       '--> ').lower()
        if opcoes == 'cadastrar':
            pessoa = cadastrar(lista_pessoas)
        elif opcoes == 'exportar':
            print('Exportando...')
            pessoa.exportar(lista_pessoas)
            print('Exportado!!')
        elif opcoes == 'sair':
            break
        else:
            print('Opcao invalida')
    

main()            
