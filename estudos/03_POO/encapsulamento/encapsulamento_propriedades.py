class Produto:
    def __init__(self,  nome, valor_p):
        self.nome = nome
        self.valor_p = valor_p

    @property
    def valor(self):
        return self.valor_p or 0
    
    @valor.setter
    def valor(self, preco):
        self.valor_p = preco

    @valor.deleter
    def valor(self):
        self.valor_p = 0
        
    def __str__(self):
        return f'{self.nome}, valor: {self.valor_p}'
    
prod1 = Produto('Banana', 28.60)
print(prod1.valor) # Getter - Possibilita puxar a informacão do atributo
print(prod1)
prod1.valor = 30.50 # Setter - Possibilita a atribuicao de valor
print(prod1)
del prod1.valor # Deleter - Possibilita a exclusão do valor
print(prod1)

