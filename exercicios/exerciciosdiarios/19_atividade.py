# Dia 18: Classes e Objetos
# Implemente uma classe Carro, Moto, Avião, Barco com atributos como marca, modelo e ano.
# Dia 19: Construtores e Destrutores
# Expanda o exercício anterior utilizando CSV e Json
import datetime
import csv
import json
from pathlib import Path
from typing import TypedDict

# Nome do arquivo de importação deve ser = 19_arquivo_(modo).modo
PATH_IMPORT_CSV = Path(__file__).parent / '19_arquivo_csv.csv'
PATH_IMPORT_JSON = Path(__file__).parent / '19_arquivo_json.json'
PATH_EXPORT_CSV = Path(__file__).parent / '19_exportado.csv'
PATH_EXPORT_JSON = Path(__file__).parent / '19_exportado.json'

class MyRepr:
    def __repr__(self):
        atributos = [f'{chave}: {valor}' for chave, valor in self.__dict__.items()]
        return f"{self.__class__.__name__} - {', '.join(atributos)}"

class Carro(MyRepr):
    def __init__(self, marca: str, modelo: str, ano: datetime) -> None:
            self.marca = marca
            self.modelo = modelo
            self.ano = ano

class Moto(MyRepr):
    def __init__(self, marca: str, modelo: str, ano: datetime) -> None:
            self.marca = marca
            self.modelo = modelo
            self.ano = ano

class Barco(MyRepr):
    def __init__(self, marca: str, modelo: str, ano: datetime) -> None:
            self.marca = marca
            self.modelo = modelo
            self.ano = ano

class MyFileReader:
    def __init__(self, arquivo, modo):
        self.arquivo = arquivo
        self.modo = modo
        self._arquivo_abrir = None

    def __enter__(self):
        self._arquivo_abrir = open(self.arquivo, self.modo, encoding='utf-8')
        return self._arquivo_abrir
    
    def __exit__(self, class_exception_, exception_, traceback_):
        self._arquivo_abrir.close()

class FormatJson(TypedDict):
    Class: str
    marca: str
    modelo: str
    ano: int

def cadastrar():
    marca = input('Marca:')
    modelo = input('Modelo:')
    ano = int(input('Ano:'))
    return marca, modelo, ano

def cadastro_veiculos(lista_veiculos: list):
    opcao = input('Entrada:\nCarro - [C]\nMoto - [M]\nBarco [B]\nSair - [S]\n-->').lower().strip()

    match opcao:
        case 'c':
            marca, modelo, ano = cadastrar()
            carro = Carro(marca, modelo, ano)
            lista_veiculos.append(carro)
            print()
            return True
        case 'm':
            marca, modelo, ano = cadastrar()
            moto = Moto(marca, modelo, ano)
            lista_veiculos.append(moto)
            print()
            return True
        case 'b':
            marca, modelo, ano = cadastrar()
            barco = Barco(marca, modelo, ano)
            lista_veiculos.append(barco)
            print()
            return True
        case 'l':
            print(*lista_veiculos, sep='\n', end='\n')
            return True 
        case 's':
            return False
        case _:
            print('Opção inválida.')
            return True

def importa_veiculos(lista_veiculos: list): 
    modo = input('Importar em JSON [json] ou CSV [csv]: ')

    if modo == 'json':
        with MyFileReader(PATH_IMPORT_JSON, 'r') as arquivo:
            arquivo_json: FormatJson = json.load(arquivo)
            classes = {'carro': Carro, 'moto': Moto, 'barco': Barco}
            for dado in arquivo_json:
                objeto = dado['Class'].lower().strip()
                classe_objeto = classes.get(objeto)
                if classe_objeto:
                    lista_veiculos.append(classe_objeto(marca=dado['marca'], modelo=dado['modelo'], ano=dado['ano']))

    elif modo == 'csv':
        with MyFileReader(PATH_IMPORT_CSV, 'r') as arquivo:
            leitor = csv.DictReader(arquivo)
            for dado in leitor:
                objeto = dado['Class'].lower().strip()
                classes = {'carro': Carro, 'moto': Moto, 'barco': Barco}
                objeto_classe = classes.get(objeto)
                if objeto_classe:
                    lista_veiculos.append(objeto_classe(marca=dado['marca'], modelo=dado['modelo'], ano=dado['ano']))
                else:
                    print(f'Dado {dado["Class"]} inválido.')
    
    else:
        print('Modo não identificado.')
     
def exporta_veiculos(lista_veiculos: list):
    modo = input('Importar em JSON [json] ou CSV [csv]: ')

    if modo == 'json':
        with MyFileReader(PATH_EXPORT_JSON, 'w') as arquivo:
            lista_json = []
            for item in lista_veiculos:
                lista_json.append(item.__dict__)
            json.dump(lista_json, arquivo, indent=3)

    elif modo == 'csv':
        with MyFileReader(PATH_EXPORT_CSV, 'w') as arquivo:
            coluna = ['Class', 'marca', 'modelo', 'ano']
            linha = []
            escritor = csv.writer(arquivo)
            for item in lista_veiculos:
                linha.append(item.__dict__)
                
            escritor.writerow(coluna)
            for item1 in linha:
                escritor.writerow(item1.values())


    
    else:
        print('Modo não identificado.')

def menu_opcoes(lista_veiculos: list) -> bool: 
    opcoes = input('Comandos: cadastrar veiculo [cv], importar veiculo [ic],'
                   'exportar veiculo [ev], listar [l] e sair [s]\n-->').lower()

    match opcoes:
        case 'cv':
            cadastro_veiculos(lista_veiculos)
            return True
        case 'ic':
            importa_veiculos(lista_veiculos)
            return True
        case 'ev':
            exporta_veiculos(lista_veiculos)
            return True
        case 'l':
            print(*lista_veiculos, sep='\n')
            return True
        case 's':
            print('Sair.')
            return False
        case _:
            print('Comando Invalido.')
            return True
        
def main():
    lista_veiculos = []

    while True:
        menu = menu_opcoes(lista_veiculos)
        if not menu:
            break

if __name__ == "__main__":
    main()