# Herança Múltipla - Python Orientado a Objetos
# Quer dizer que no Python, uma classe pode estender
# várias outras classes.
# Herança simples:
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Herança múltipla e mixins
# Log -> FileLog
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Cliente(Pessoa, FileLog)
#
# A, B, C, D
# D(B, C) - C(A) - B(A) - A
#
# método -> falar
#           A
#         /   \
#        B     C
#         \   /
#           D
#
# Python 3 usa C3 superclass linearization
# para gerar o mro.
# Você não precisa estudar isso (é complexo)
# https://en.wikipedia.org/wiki/C3_linearization
#
# Para saber a ordem de chamada dos métodos
# Use o método de classe Classe.mro()
# Ou o atributo __mro__ (Dunder - Double Underscore)


class animal:
    def __init__(self, num_patas):
        self.num_patas = num_patas

    def __str__(self):
        return f'{self.__class__.__name__}: {' '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'

class mamifero(animal):
    def __init__(self, cor_pelo, **kwargs): # **kwargs - todo argumento novo na classe animal sera adicionado caso utilizar o "**kwargs"
        super().__init__(**kwargs)
        self.cor_pelo = cor_pelo

class ave(animal):
    def __init__(self, cor_bico, **kwargs):
        super().__init__(**kwargs)
        self.cor_bico = cor_bico
        
        

class Cachorro(mamifero):
    pass

class Ornitorrinco(mamifero, ave):
    pass

cachorro = Cachorro(num_patas=4, cor_pelo='Azul') # Utilizando chave e valor devido ao kwargs
print(cachorro)
ornitorrinco = Ornitorrinco(num_patas=4, cor_pelo='Preto', cor_bico='Amarelo')
print(ornitorrinco)


