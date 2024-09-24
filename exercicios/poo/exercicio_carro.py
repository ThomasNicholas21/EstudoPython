# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def carro(self):
        return self.nome

    @property
    def motor(self):
        return self._motor
    
    @property
    def fabricante(self):
        return self._fabricante
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

    @carro.deleter
    def carro(self):
        self.nome = 0
        self._motor = 0
        self._fabricante = 0

    @motor.deleter
    def motor(self):
        self._motor = 0
    
    @fabricante.deleter
    def fabricante(self):
        self._fabricante = 0


    def __str__(self):
        atributo = []
        if hasattr(self, 'nome'):
            atributo.append(f'Carro: {self.nome}')

        if hasattr(self, 'motor'):
            atributo.append(f'Motor: {self.motor}')

        if hasattr(self, 'fabricante'):
            atributo.append(f'Fabricante: {self.fabricante}')
        
        return f'{'|'.join(atributo)}'

        
class Motor:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return f'{self.nome}'
class Fabricante:
    def __init__(self, nome):
        self.nome = nome
    
    def __str__(self):
        return f'{self.nome}'

def cadastro_carro(lista_de_carro):
    print('Iniciando Cadastro de Carros')
    carro = input('Nome do carro: ')
    motor = input('Motor do carro: ')
    fabricante = input('Fabricante do carro: ')

    carro, motor, fabricante = Carro(carro), Motor(motor), Fabricante(fabricante)
    carro.motor, carro.fabricante = motor, fabricante

    lista_de_carro.append(carro)

def listar_carros(lista_de_carro):
    try:
        for carro in lista_de_carro:
            print(carro)
    except:
        print('Sem carros cadastrado.')

def edit_carro_cadastrado(lista_de_carro):
    for carro in lista_de_carro:
        print(carro.nome)
        print()
    
        selecao = input('Qual carro deseja editar ou deletar?\n'
                        '-->')
        
        if selecao == carro.nome:
            alteracao = input('Deseja alterar o nome, motor ou fabricante?\n'
                                'N - Nome\n'
                                'M - Motor\n'
                                'F - Fabricante\n'
                                'S - Sair\n'
                                '-->').lower()
                                
            if alteracao == 'n':
                op = input('Editar ou excluir?\n'
                           'E - Edidar\n'
                           'D - Deletar\n'
                           '--> ')
                
                if op == 'e':
                    novo_nome = input('Novo nome: ')
                    carro.nome = novo_nome

                elif op == 'd':
                    print('Deletando carro por completo (Motor e fabricante)\n')
                    del carro.nome

                else:
                    print('Comando invalido')
            
            elif alteracao == 'm':
                op = input('Editar ou excluir?\n'
                           'E - Edidar\n'
                           'D - Deletar\n'
                           '--> ')
                
                if op == 'e':
                    novo_motor = input('Novo motor: ')
                    carro.motor = novo_motor

                elif op == 'd':
                    del carro.motor

                else:
                    print('Comando invalido')

            elif alteracao == 'f':
                op = input('Editar ou excluir?\n'
                           'E - Edidar\n'
                           'D - Deletar\n'
                           '--> ')
                
                if op == 'e':
                    novo_fabricante = input('Novo fabricante: ')
                    carro.fabricante = novo_fabricante

                elif op == 'd':
                    del carro.fabricante

                else:
                    print('Comando invalido')
            
            elif alteracao == 's':
                break

            else:
                print('Comando inválido.')
        
        else:
            print('Comando inválido.')


def main():
    lista_carro_cadastrado = []

    while True:       
        op = input('Deseja cadastrar, listar, editar ou sair?\n'
                   'C - Cadastrar\n'
                   'L - Listar\n'
                   'E - Editar\n'
                   'S - Sair\n'
                   '--> ').lower()

        if op == 'c':
            cadastro_carro(lista_carro_cadastrado)
            print()
        elif op == 'l':
            listar_carros(lista_carro_cadastrado)
            print()
        elif op == 'e':
            edit_carro_cadastrado(lista_carro_cadastrado)
        elif op == 's':
            break
        else:
            print('Comando desconhecido')



main()
