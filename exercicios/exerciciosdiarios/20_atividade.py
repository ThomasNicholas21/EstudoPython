# Dia 20: Herança
# Crie uma classe Veiculo e faça a classe Carro herdá-la. 
# Veiculo deve conter atributos e métodos comuns a todos os veículos.

class Veiculo:
    def __init__(
            self, marca: str, 
            quantidade_rodas: int, 
            tanque_litros: float, 
            km_rodado: float
            ):
        self.marca = marca
        self.quantidade_rodas = quantidade_rodas
        self.tanque_litros = tanque_litros
        self.km_rodado = km_rodado

    def ligar(): ...

    def desligar(): ...

    def autonomia(): ...

def main():
    ...

if __name__ == "__main__":
    main()
