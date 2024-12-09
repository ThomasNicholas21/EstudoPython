# Dia 18: Classes e Objetos
# Implemente uma classe Carro com atributos como marca, modelo e ano, e um método para ligar o carro.
from datetime import datetime

class Carro:
    def __init__(self, marca: str, modelo: str, ano: datetime) -> None:
            self.marca = marca
            self.moodelo = modelo
            self.ano = ano

class Moto:
    def __init__(self, marca: str, modelo: str, ano: datetime) -> None:
            self.marca = marca
            self.moodelo = modelo
            self.ano = ano

class Aviao:
    def __init__(self, marca: str, modelo: str, ano: datetime) -> None:
            self.marca = marca
            self.moodelo = modelo
            self.ano = ano

class Barco:
    def __init__(self, marca: str, modelo: str, ano: datetime) -> None:
            self.marca = marca
            self.moodelo = modelo
            self.ano = ano

def ligar(classe):
    print(f'O {classe.__class__.__name__} da marca {classe.marca} está ligando.')

def main():
    carro = Carro('Chevrolet', 'Sedan', datetime(1998, 2, 1))
    ligar(carro)

if __name__ == "__main__":
    main()