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
# Decoradores para método
def meu_planeta(metodo):
    def interno(self, *args, **kwargs): # cria método
        resultado = metodo(self, *args, **kwargs)

        if 'Terra' in resultado:
            return 'Lar doce lar'
        elif not 'Terra' in resultado:
            return 'Isso não é a terra'
        
        return resultado
    
    return interno


@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome
    
    @meu_planeta
    def identifica_planeta(self):
        return f'Este planeta se chama {self.nome}'

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
    print()
    print(planeta1.identifica_planeta(), planeta2.identifica_planeta(), sep=' | ')

main()

# Forma elegante e clean de se aproveitar métodos para diversas classes DRY