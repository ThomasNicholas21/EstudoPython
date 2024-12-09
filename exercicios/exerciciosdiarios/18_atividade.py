# Dia 18: Classes e Objetos
# Implemente uma classe Carro com atributos como marca, modelo e ano, e um método para ligar o carro.
from datetime import datetime

class Carro:
    def __init__(self, marca: str, modelo: str, ano: datetime) -> None:
            self.marca = marca
            self.moodelo = modelo
            self.ano = ano

class Moto:
    ...

class Aviao:
    ...

class Barco:
    ...

def ligar():
    ...

def main():
    ...

if __name__ == "__main__":
    main()