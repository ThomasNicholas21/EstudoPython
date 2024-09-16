class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def calcula_idade_nome(cls ,ano, mês, dia, nome): # CLS referencia a classe
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod
    def maioridade(idade):
        return 'Maior de idade' if idade >= 18 else 'Menor de idade.'
    

p1 = Pessoa.calcula_idade_nome(2000, 7, 31, 'Fulano')
p2 = Pessoa.calcula_idade_nome(2010, 7, 31, 'Ciclano')
print(p1.nome, p1.idade)
print(p2.nome, p2.idade)
print(p1.maioridade(p1.idade))
print(p2.maioridade(p2.idade))