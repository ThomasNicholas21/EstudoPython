from abc import ABC, abstractmethod

class ControleRemoto(ABC): # Definindo estrutura das subclasses
    @abstractmethod # torna obrigatório o uso dos métodos
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def __init__(self, marca_p):
        self.marca_p = marca_p

    def ligar(self):
        print(f'Ligando TV {self.marca_p}')
    
    def desligar(self):
        print(f'Desligando TV {self.marca_p}')

    @property
    def marca(self):
        return self.marca_p or 'Desconhecido'
    
class ControleDVD(ControleRemoto):
    def __init__(self, marca_p):
        self.marca_p = marca_p

    def ligar(self):
        print('Ligando DVD')
    
    def desligar(self):
        print('Desligando DVD')

    @property
    def marca(self):
        return self.marca_p or 'Desconhecido'

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print('Ligando Ar-Condicionado')
    
    # def desligar(self):
    #     print('Desligando Ar-Condicionado')

    # @property
    # def marca(self):
    #     return self.marca_p or 'Desconhecido'

controle1 = ControleTV('LG')
controle1.ligar()
controle1.desligar()

controle2 = ControleDVD('Phillips')
controle2.ligar()
controle2.desligar()

try:
    controle3 = ControleArCondicionado()
    controle3.ligar()
    controle3.desligar()
except TypeError:
    print('Método obrigatório ausente.')
