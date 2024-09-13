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
        if self.tamanho < 140:
            print('Tamanho para pessoas comm nanismo.')
        elif self.tamanho > 140:
            print('Pessoa pequena.')
        elif 150 < self.tamanho <= 165:
            print('Pessoa média.')
        elif 165 < self.tamanho <= 180:
            print('Pessoa alta.')
        else:
            print('Pessoa muito alta.')
        
