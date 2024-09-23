# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @property
    def fabricante(self):
        return self._fabricante
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

    def __str__(self):
        return f'Carro: {self.nome}, Motor: {self.motor.nome if self.motor.nome else 'Carro sem Motor'}, Fabricante: {self.fabricante.nome if self.fabricante.nome else 'Carro sem Fabricante'}'

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

def cadastro_carro(lista_de_carro):
    print('Iniciando Cadastro de Carros')
    carro = input('Nome do carro: ')
    motor = input('Motor do carro: ')
    fabricante = input('Fabricante do carro: ')

    carro1, motor1, fabricante1 = Carro(carro), Motor(motor), Fabricante(fabricante)
    carro1.motor, carro1.fabricante = motor1, fabricante1

    lista_de_carro.append(carro1)

def main():
    lista_carro_cadastrado = []

    while True:       
        op = input('Deseja cadastrar, listar, editar ou sair?\n'
                   'C - Cadastrar\n'
                   'L - Listar\n'
                   'S - Sair\n'
                   '--> ').lower()

        if op == 'c':
            cadastro_carro(lista_carro_cadastrado)
            print()
        elif op == 'l':
            for objeto in lista_carro_cadastrado:
                print(objeto)
        elif op == 'e':
            pass
        elif op == 's':
            break
        else:
            print('Comando desconhecido')



main()
