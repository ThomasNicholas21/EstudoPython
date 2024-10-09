# Utilizando função decoradora para criar um context manager
from contextlib import contextmanager # Chamando função decoradora para criar um context manager
import json

@contextmanager
def my_open_cliente(caminho_arquivo, modo):
    try: # utiliza para tratar excções
        print('Abrindo Arquivo.')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo # yield transforma a função em um generetor - pausa a função toda vez que é chamada 
    except Exception as e: # Trata os erros
        print('Erro: ', e)
    finally:
        print('Fechando arquivo')
        arquivo.close()

def cadastro_cliente(dicionario_cliente: dict):
    print('Iniciando cadastro de cliente.')
    nome = input('Nome: ')
    data_nascimento = input('Data de nascimento: ')
    cpf = input('CPF: ')
    dicionario_cliente.update({'Cliente': {'Nome': nome, 'Nascimento': data_nascimento, 'CPF': cpf}})
    return dicionario_cliente

def main():
    dicionario_cliente = {}
    cadastro_cliente(dicionario_cliente)
    with my_open_cliente('D:/programação/EstudoPython/estudos/03_POO/context_manager/03/arquivo.json', 'w') as arquivo:
        if dicionario_cliente:
            json.dump(dicionario_cliente, arquivo)

main()