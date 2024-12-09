# Dia 18: Classes e Objetos
# Implemente uma classe Carro, Moto, Avião, Barco com atributos como marca, modelo e ano..
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
    return True

def cadastrar_veiculo(lista_veiculos):
    print('Iniciando Garagem')
    opcao = input('Entrada:\nCarro - [C]\nMoto - [M]\nAvião - [A]\nBarco - [B]\n-->')

    match opcao:
        case 'c':
            ...
        case 'm':
            ...
        case 'a':
            ...
        case 'b':
            ...
        case _:
            print('Opção inválida.')

def main():
    lista_veiculos = []

if __name__ == "__main__":
    main()