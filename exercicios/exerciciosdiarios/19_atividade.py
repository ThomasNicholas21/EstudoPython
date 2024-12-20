# Dia 18: Classes e Objetos
# Implemente uma classe Carro, Moto, Avião, Barco com atributos como marca, modelo e ano.
# Dia 19: Construtores e Destrutores
# Expanda o exercício anterior utilizando CSV e Json
import datetime
import csv
import json
from pathlib import Path

PATH_CSV = Path(__file__).parent / '19_arquivo_csv.csv'
PATH_JSON = Path(__file__).parent / '19_arquivo_json.json'

class MyRepr:
    def __repr__(self):
        atributos = [f'{chave}: {valor}' for chave, valor in self.__dict__.items()]
        return f"{self.__class__.__name__}: {', '.join(atributos)}"

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

class MyReaderCSV:
    def __init__(self, arquivo, modo):
        self.arquivo = arquivo
        self.modo = modo
        self._arquivo_abrir = None

    def __enter__(self):
        self._arquivo_abrir = open(self.arquivo, self.modo, encoding='utf-8')
        return self._arquivo_abrir
    
    def __exit__(self, class_exception_, exception_, traceback_):
        self._arquivo_abrir.close()

class MyReaderJSON:
    def __init__(self, arquivo, modo):
        self.arquivo = arquivo
        self.modo = modo
        self._arquivo_abrir = None

    def __enter__(self):
        self._arquivo_abrir = open(self.arquivo, self.modo, encoding='utf-8')
        return self._arquivo_abrir
    
    def __exit__(self, class_exception_, exception_, traceback_):
        self._arquivo_abrir.close()

def main():
      ...

if __name__ == "__main__":
      main()        