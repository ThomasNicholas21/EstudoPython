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
            self.modelo = modelo
            self.ano_cadastro = ano_cadastro

class Moto(MyRepr):
    def __init__(self, marca: str, modelo: str, ano_cadastro: datetime) -> None:
            self.marca = marca
            self.modelo = modelo
            self.ano_cadastro = ano_cadastro

class Aviao(MyRepr):
    def __init__(self, marca: str, modelo: str, ano_cadastro: datetime) -> None:
            self.marca = marca
            self.modelo = modelo
            self.ano_cadastro = ano_cadastro

class Barco(MyRepr):
    def __init__(self, marca: str, modelo: str, ano_cadastro: datetime) -> None:
            self.marca = marca
            self.modelo = modelo
            self.ano_cadastro = ano_cadastro

def ligar(classe):
    print(f'O {classe.__class__.__name__} da marca {classe.marca} está ligando.')

def cadastrar():
    marca = input('Marca:')
    modelo = input('Modelo:')
    ano_cadastro = datetime.now().strftime('%d/%m/%Y')
    return marca, modelo, ano_cadastro

def cadastrar_veiculo(lista_veiculos: list):
    opcao = input('Entrada:\nCarro - [C]\nMoto - [M]\nAvião - [A]\nBarco - [B]\n'
                  'Listar - [L]\nLigar Veículo - [LV]\nSair - [S]\n-->').lower().strip()

    match opcao:
        case 'c':
            marca, modelo, ano_cadastro = cadastrar()
            carro = Carro(marca, modelo, ano_cadastro)
            lista_veiculos.append(carro)
            print()
            return True
        case 'm':
            marca, modelo, ano_cadastro = cadastrar()
            moto = Moto(marca, modelo, ano_cadastro)
            lista_veiculos.append(moto)
            print()
            return True
        case 'a':
            marca, modelo, ano_cadastro = cadastrar()
            aviao = Aviao(marca, modelo, ano_cadastro)
            lista_veiculos.append(aviao)
            print()
            return True
        case 'b':
            marca, modelo, ano_cadastro = cadastrar()
            barco = Barco(marca, modelo, ano_cadastro)
            lista_veiculos.append(barco)
            print()
            return True
        case 'l':
            print(*lista_veiculos, sep='\n', end='\n')
            return True 
        case 'lv':
            for ordem, veiculo in enumerate(lista_veiculos):
                print(f'{ordem}', veiculo)

            try:    
                selecionar_veiculo = int(input('Selecione qual veiculo deseja ligar pela enumeração: '))
                if selecionar_veiculo + 1 > len(lista_veiculos):
                    print('Número inválido! Finalizando')
                else:
                    vaiculo = lista_veiculos[selecionar_veiculo]
                    ligar(veiculo)

            except ValueError:
                print('Deve ser selecionado número inteiro! Finalizando ...')

            return True
        case 's':
            return False
        case _:
            print('Opção inválida.')
            return True

def main():
    lista_veiculos = []

    while True:
        cadastrar = cadastrar_veiculo(lista_veiculos)
        if not cadastrar:
            print('Encerrando.')
            break
        
if __name__ == "__main__":
    main()