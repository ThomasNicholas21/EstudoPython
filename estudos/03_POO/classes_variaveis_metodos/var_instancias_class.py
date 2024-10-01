# Estudo sobre variaveis de instância e métodos

class Estudante: 
    escola = 'Uni' # Atributo que todo objeto instanciado terá compartilhado

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula  # Atributo no qual mudará de objeto para objeto

    def __str__(self):
        return f'{self.escola}: {self.nome} e {self.matricula}'
    
aluno1 = Estudante('Fulano', 2120644)
aluno2 = Estudante('Ciclano', 2130699)

print(aluno1)
print(aluno2)

Estudante.escola = 'Udemy'

print(aluno1)
print(aluno2)