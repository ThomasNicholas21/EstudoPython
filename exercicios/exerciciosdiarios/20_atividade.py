# Dia 20: Herança
# Crie uma classe Veiculo e faça a classe Carro herdá-la. 
# Veiculo deve conter atributos e métodos comuns a todos os veículos.

class Veiculo:
    def __init__(
            self, 
            marca: str, 
            quantidade_rodas: int, 
            capacidade_tanque: float, 
            motor_ligado: bool = False
            ):
        self.marca = marca
        self.quantidade_rodas = quantidade_rodas
        self.capacidade_tanque = capacidade_tanque
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

    def autonomia(self, distancia_percorrida, litros_cosumido) -> float:
        consumo_medio: float = distancia_percorrida / litros_cosumido
        autonomia: float = self.capacidade_tanque * consumo_medio
        return autonomia



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
