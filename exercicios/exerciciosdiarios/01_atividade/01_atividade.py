# Dia 1: Estruturas Condicionais
# Crie um programa que leia a idade de uma pessoa e informe se ela pode votar ou não.

# Necessário para votar no Brasil
# Idade minima: 16 e 17 e maiores de 70 anos- Voto Facultativo
# Idade minima: 18 aos 70 anos - Voto Obrigatório
# Nacionalidade: Ser Brasileiro ou naturalizado
# Titulo de Eleitor: Numero de identificação
# Documento de Identificação: Utilizar CPF ou RG 
# Capacidade Civil: direitos políticos suspensos (condenação eleitoral)
# Esse programa Verifica se a pessoa está apta a votar, não realiza consultas externas

# Programa a ser refatorado
from datetime import datetime

ANO_ATUAL = datetime.now().year

class NecessarioParaVotar:
    def idade_minima(self, ano_nascimento) -> bool:
        idade = ANO_ATUAL - ano_nascimento
        if idade == 16 or idade == 17 or idade >= 70:
            return True
        
        elif 18 <= idade < 70:
            return True
        
        return False
        
    def verifica_nacionalidade(self, cpf) -> bool:
        validacao = input('Confirme seu CPF: ')
        if validacao == cpf:
            return True
        
        return False
    
    def verifica_titulo(self):
        inscricao_titulo = input('Insira sua inscriação de titulo: ')
        if 0 < len(inscricao_titulo) <= 6:
            return True
        
        return False
     
    def capacidade_civil(self):
        verifica_capacidade_civil = input('Possui condenação eleitoral, [s]im ou [n]ão: ').lower().startswith('n')
        if verifica_capacidade_civil:
            return True
        
        return False
    
class Pessoa:
    def __init__(self, nome, cpf, ano_nascimento) -> None:
        self._nome = nome
        self._cpf = cpf
        self._ano_nascimento = ano_nascimento     
        self.necessario_para_votar = NecessarioParaVotar()

    def pode_votar(self) -> bool:
        if self.necessario_para_votar.idade_minima(self._ano_nascimento) and self.necessario_para_votar.verifica_nacionalidade(self._cpf) and self.necessario_para_votar.verifica_titulo() and self.necessario_para_votar.capacidade_civil():
            print('Está apto a votar.')

        else:
            print('Não está apto a votar.')

def main():
    nome = input('Digite seu nome: ')
    cpf = input('Digite seu CPF: ')
    ano_nascimento = int(input('Digite seu ano de nascimento: '))
    print('\nIniciando validação...')
    usuario = Pessoa(nome=nome, cpf=cpf, ano_nascimento=ano_nascimento)
    usuario.pode_votar()

main()