# Dia 18: Classes e Objetos
# Implemente uma classe Carro, Moto, Avião, Barco com atributos como marca, modelo e ano.
# Dia 19: Construtores e Destrutores
# Expanda o exercício anterior utilizando CSV e Json
import datetime
import csv
import json

class MyRepr:
    def __repr__(self):
        atributos = [f'{chave}: {valor}' for chave, valor in self.__dict__.items()]
        return f"{self.__class__.__name__}: {', '.join(atributos)}"

class Carro(MyRepr):
    def __init__(self, marca: str, modelo: str, ano_cadastro: datetime) -> None:
            self.marca = marca
            self.modelo = modelo
            self.ano_cadastro = ano_cadastro

class Moto(MyRepr):
    def __init__(self, marca: str, modelo: str, ano_cadastro: datetime) -> None:
            self.marca = marca
            self.modelo = modelo
            self.ano_cadastro = ano_cadastro

class Barco(MyRepr):
    def __init__(self, marca: str, modelo: str, ano_cadastro: datetime) -> None:
            self.marca = marca
            self.modelo = modelo
            self.ano_cadastro = ano_cadastro

class MyReader:
    def __init__(self, arquivo, modo):
        self.arquivo = arquivo
        self.modo = modo
        self._arquivo_abrir = None

    def __enter__(self):
        self._arquivo_abrir = open(self.arquivo, self.modo, encoding='utf-8')
        return self._arquivo_abrir

def main():
      ...

if __name__ == "__main__":
      main()        