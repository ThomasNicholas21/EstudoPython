# Dia 18: Classes e Objetos
# Implemente uma classe Carro, Moto, Avião, Barco com atributos como marca, modelo e ano..
from datetime import datetime

class Carro:
    def __init__(self, marca: str, modelo: str, ano_cadastro: datetime) -> None:
            self.marca = marca
            self.moodelo = modelo
            self.ano_cadastro = ano_cadastro

class Moto:
    def __init__(self, marca: str, modelo: str, ano_cadastro: datetime) -> None:
            self.marca = marca
            self.moodelo = modelo
            self.ano_cadastro = ano_cadastro

class Aviao:
    def __init__(self, marca: str, modelo: str, ano_cadastro: datetime) -> None:
            self.marca = marca
            self.moodelo = modelo
            self.ano_cadastro = ano_cadastro

class Barco:
    def __init__(self, marca: str, modelo: str, ano_cadastro: datetime) -> None:
            self.marca = marca
            self.moodelo = modelo
            self.ano_cadastro = ano_cadastro

def ligar(classe):
    print(f'O {classe.__class__.__name__} da marca {classe.marca} está ligando.')
    return True

def cadastrar():
    marca = input('Marca:')
    modelo = input('Modelo:')
    ano_cadastro = datetime.now()
    return marca, modelo, ano_cadastro

def cadastrar_veiculo(lista_veiculos):
    print('Iniciando Garagem')
    opcao = input('Entrada:\nCarro - [C]\nMoto - [M]\nAvião - [A]\nBarco - [B]\nSair - [S]\n-->').lower().strip()

    match opcao:
        case 'c':
            ...
            return True
        case 'm':
            ...
            return True
        case 'a':
            ...
            return True
        case 'b':
            ...
            return True
        case 's':
            ...
            return False
        case _:
            print('Opção inválida.')

def main():
    lista_veiculos = []

    while True:
        cadastrar = cadastrar_veiculo(lista_veiculos)
        if not cadastrar:
            print('Encerrando.')
            break
        
if __name__ == "__main__":
    main()