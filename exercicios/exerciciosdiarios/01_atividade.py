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
ANO_ATUAL = 2024 # Refatorar posteriormente utilizando datetime
     
class NecessarioParaVotar:
    def idade_minima(self, ano_nascimento) -> bool:
        idade = ANO_ATUAL - ano_nascimento
        if idade == 16 or idade == 17 or idade >= 70:
            return True
        
        elif 18 <= idade < 70:
            return True
        
        return False
        
    def verifica_nacionalidade(self, cpf) -> bool:
        validacao = input('Informe seu CPF: ')
        if validacao == cpf:
            print('CPF confirmado, possui nacionalidade.')
            return True
        
        return False
    
    def verifica_titulo(self):
        inscricao_titulo = input('Insira sua inscriação de titulo: ')
        if 0 < len(inscricao_titulo) <= 6:
            return True
        
        return False
            
    
class Pessoa:
    def __init__(self, nome, cpf, ano_nascimento) -> None:
        self._nome = nome
        self._cpf = cpf
        self._ano_nascimento = ano_nascimento     
        self.necessario_para_votar = NecessarioParaVotar()

    def pode_votar(self):
        if self.necessario_para_votar.idade_minima(self._ano_nascimento) and self.necessario_para_votar.verifica_nacionalidade(self._cpf) and self.necessario_para_votar.verifica_titulo() :
            print(f'{self._nome} pode votar')

    def __del__(self):
        print('Dados sendo destruídos após validação!')

if __name__ == '__main__':
    user_test = Pessoa('Fulano', '123456789', 2000)
    user_test.pode_votar()
    #user_test.necessario_para_votar.idade_minima(2000)
    #user_test.necessario_para_votar.verifica_nacionalidade('123456789')
    #user_test.necessario_para_votar.verifica_titulo()
    del user_test