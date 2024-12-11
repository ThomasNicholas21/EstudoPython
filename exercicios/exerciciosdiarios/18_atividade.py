# Dia 18: Classes e Objetos
# Implemente uma classe Carro, Moto, Avião, Barco com atributos como marca, modelo e ano..
from datetime import datetime

class MyRepr:
    def __repr__(self):
        atributos = [f'{chave}: {valor}' for chave, valor in self.__dict__.items()]
        return f"{self.__class__.__name__}: {', '.join(atributos)}"

class Carro(MyRepr):
    def __init__(self, marca: str, modelo: str, ano_cadastro: datetime) -> None:
            self.marca = marca
            self.moodelo = modelo
            self.ano_cadastro = ano_cadastro

class Moto(MyRepr):
    def __init__(self, marca: str, modelo: str, ano_cadastro: datetime) -> None:
            self.marca = marca
            self.moodelo = modelo
            self.ano_cadastro = ano_cadastro

class Aviao(MyRepr):
    def __init__(self, marca: str, modelo: str, ano_cadastro: datetime) -> None:
            self.marca = marca
            self.moodelo = modelo
            self.ano_cadastro = ano_cadastro

class Barco(MyRepr):
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
    ano_cadastro = datetime.now().strftime('%d/%m/%Y')
    return marca, modelo, ano_cadastro

def cadastrar_veiculo(lista_veiculos: list):
    print('Iniciando Garagem')
    opcao = input('Entrada:\nCarro - [C]\nMoto - [M]\nAvião - [A]\nBarco - [B]\nListar - [L]\nSair - [S]\n-->').lower().strip()

    match opcao:
        case 'c':
            marca, modelo, ano_cadastro = cadastrar()
            carro = Carro(marca, modelo, ano_cadastro)
            lista_veiculos.append(carro)
            return True
        case 'm':
            marca, modelo, ano_cadastro = cadastrar()
            moto = Moto(marca, modelo, ano_cadastro)
            lista_veiculos.append(moto)
            return True
        case 'a':
            marca, modelo, ano_cadastro = cadastrar()
            aviao = Aviao(marca, modelo, ano_cadastro)
            lista_veiculos.append(aviao)
            return True
        case 'b':
            marca, modelo, ano_cadastro = cadastrar()
            barco = Barco(marca, modelo, ano_cadastro)
            lista_veiculos.append(barco)
            return True
        case 'l':
            print(*lista_veiculos, sep='\n')
            return True 
        case 's':
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