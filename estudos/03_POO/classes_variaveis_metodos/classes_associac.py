# Entendendo associação

class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta

    
class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'O escritor está utilizando a seguinte ferramaenta: {self.nome}'


escritor1 = Escritor('Fulano')
ferramenta1 = FerramentaDeEscrever('Teclado')
escritor1.ferramenta = ferramenta1            # Utilizando associação "fraca" para relacionar duas classes instanciadas 

print(escritor1.ferramenta.escrever())
print(ferramenta1.escrever())
