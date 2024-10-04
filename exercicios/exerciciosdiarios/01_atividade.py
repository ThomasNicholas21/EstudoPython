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
    def idade_minima(self) -> bool:
        idade = ANO_ATUAL - self._ano_nascimento
        if idade == 16 or idade == 17 or idade >= 70:
            print('Voto Facultativo')
            return True
        
        elif 18 <= idade < 70:
            print('Voto Obrigatório')
            return True
        
        else:
            return False

class Pessoa(NecessarioParaVotar):
    def __init__(self, nome, cpf, ano_nascimento) -> None:
        self._nome = nome
        self._cpf = cpf
        self._ano_nascimento = ano_nascimento     

if __name__ == '__main__':
    user_test = Pessoa('Fulano', '123456789', 2000)
    user_test.idade_minima()