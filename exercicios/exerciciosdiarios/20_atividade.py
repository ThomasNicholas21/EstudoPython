# Dia 20: Herança
# Crie uma classe Veiculo e faça a classe Carro herdá-la. 
# Veiculo deve conter atributos e métodos comuns a todos os veículos.

class Veiculo:
    def __init__(
            self, marca: str, 
            quantidade_rodas: int, 
            tanque_litros: float, 
            km_rodado: float,
            motor_ligado: bool = False
            ):
        self.marca = marca
        self.quantidade_rodas = quantidade_rodas
        self.tanque_litros = tanque_litros
        self.km_rodado = km_rodado
        self.motor_ligado = motor_ligado
        
    def ligar(self) -> bool:
        if self.motor_ligado is True:
            print('Carro já está ligado.')

        self.motor_ligado = True
        return True

    def desligar(self) -> bool:
        if self.motor_ligado is False:
            print('Motor já está desligado')

        self.motor_ligado = False 
        return False

    def autonomia(self): ...

def cadastro(): ...

def excluir(): ...

def main():
    lista_veiculos = []

    while True:
        opcao = input('comandos: cadastrar [c], excluir [e] e sair [s]\n-->')

        match opcao:
            case 'c': ...
            case 'e': ...
            case 's':
                break
            case _:
                print('Comando desconhecido.')

if __name__ == "__main__":
    #main()
    carro_teste = Veiculo('teste', 4, 40, 1000)
    carro_teste.desligar()
    carro_teste.ligar()
    carro_teste.ligar()
