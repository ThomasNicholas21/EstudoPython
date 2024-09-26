# Entendendo Herança

class Pai:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def metodo_falar(self):
        print(f'{self.nome} {self.sobrenome} falando.')

    def __str__(self):
        return f'{self.sobrenome}'

class Filho(Pai):
    def __init__(self, nome, pai):
        super().__init__(nome, pai)
        
    def metodo_falar(self):
        print(f'{self.nome} {self.sobrenome} falando.')
    
    def __str__(self):
        return f'{self.sobrenome}'

class Neto(Filho):
    def __init__(self, nome, pai):
        super().__init__(nome, pai)
        
    def metodo_falar(self):
        print(f'{self.nome} {self.sobrenome} falando.')

    def __str__(self):
        return f'{self.sobrenome}'

pai = Pai('Jão', 'Silva')
filho = Filho('Rodoberto', pai)
neto = Neto('Josley', filho)

print(pai.metodo_falar(), filho.metodo_falar(), neto.metodo_falar())