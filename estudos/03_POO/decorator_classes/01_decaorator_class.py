# Estudando decorator com classes
# Estudo de decoradores em classes

# Adciona método rapr para classes 
# Definindo o que poderia ser um Mixin
def adiciona_repr(cls): # Recebe classe
    def meu_repr(self):
        classe_nome = self.__class__.__name__
        classe_atributo = self.__dict__
        classe_repr = f'{classe_nome} - {classe_atributo}'
        return classe_repr
    
    cls.__repr__ = meu_repr     # Atribui um método para classe
    return cls

@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

@adiciona_repr
class Galaxia:
    def __init__(self, nome):
        self.nome = nome

def main():
    time1 = Time('Fluminese')
    time2 = Time('São Paulo')
    planeta1 = Planeta('Terra')
    planeta2 = Planeta('Jupiter')
    galaxia1 = Galaxia('Via Lactea')
    galaxia2 = Galaxia('Andrômeda')

    print(time1, time2, sep=' | ')
    print(planeta1, planeta2, sep=' | ')
    print(galaxia1, galaxia2, sep=' | ')

main()

# Forma elegante e clean de se aproveitar métodos para diversas classes DRY