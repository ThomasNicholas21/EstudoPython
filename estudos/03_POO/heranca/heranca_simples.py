class veiculo:
    def __init__(self, cor, placa, num_roda):
        self.cor = cor
        self.placa = placa
        self.num_roda = num_roda

    def liga_motor(self):
        print('Ligando motor.')

    def desliga_motor(self):
        print('Desligando Motor')

    def __str__(self):
        return f'Veiculo: {self.modelo}, {self.marca}, {self.cor}, {self.placa} e numero de rodas:{self.num_roda}'

class moto(veiculo):
    def __init__(self, modelo, marca, cor, placa, num_roda):
        self.modelo = modelo
        self.marca = marca
        super().__init__(cor, placa, num_roda)

    def travar_guidao(self):
        print('Guidão Travado')

class carro(veiculo):
    def __init__(self, modelo, marca, cor, placa, num_roda):
        self.modelo = modelo
        self.marca = marca
        super().__init__(cor, placa, num_roda)

    

veiculo1 = carro('Sedan', 'BMW', 'Preto', 'AOX-3213', 4)
print(veiculo1)
veiculo1.liga_motor()
