# Estudando polimorfismo com herança

class passaro:
    def voar(self):
        print('Voando')

class Pardal(passaro):
    def voar(self):
        super().voar()

class Avestruz(passaro):
    def voar(self):
        print('Avestruz não voa')

class Aguia(passaro):
    def voar(self):
        print('Voa rápido')

class Aviao(passaro):
    def voar(self):
        print('Decolando')

def voo(objeto): # Recebe um objeto porém tem tratamentos diferentes para cada um
    objeto.voar()

passaro1 = Pardal()
passaro2 = Avestruz()
passaro3 = Aguia()
passaro4 = Aviao()

voo(passaro1)
voo(passaro2)
voo(passaro3)
voo(passaro4)
