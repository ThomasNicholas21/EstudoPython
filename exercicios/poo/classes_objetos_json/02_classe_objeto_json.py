# Recebe objetos
import json

ANO_ATUAL  = 2024
class Pessoa:
    def __init__(self, nome, ano_nascimento, genero, tamanho):
        self.nome = nome
        self.ano_nascimento = ano_nascimento
        self.genero = genero
        self.tamanho =  tamanho

    def inverte_nome(self):
        return self.nome[::-1]
    
    def calcula_idade(self):
        return ANO_ATUAL - self.ano_nascimento
    
    def verifica_tamanho(self):
        if self.tamanho <= 140:
            return 'pessoa com nanismo.'
        elif 140 < self.tamanho <= 150:
            return 'pessoa pequena.'
        elif 150 < self.tamanho <= 165:
            return 'pessoa média.'
        elif 165 < self.tamanho <= 180:
            return 'pessoa alta.'
        elif 180 < self.tamanho <= 230:
            return 'pessoa muito alta.'
        elif self.tamanho > 230:
            return 'pessoa com gigantismo.'

    def __str__(self):
        return f'{[f'{chave}: {valor}' for chave, valor in self.__dict__.items()]}\nSe chama {self.inverte_nome()}, possui {self.calcula_idade()}, e é uma {self.verifica_tamanho()} '
        
        

def main():
    print('Lendo dados...')
    with open('D:/programação/EstudoPython/exercicios/poo/classes_objetos_json/pessoa.json', 'r') as arquivo:
        dados = json.load(arquivo)
    print('Leitura Feita!')

    for dado in dados:
        pessoa = Pessoa(**dado)
        print(pessoa)

    print('Leituras finalizadas e aplicacoes feitas!')

main()