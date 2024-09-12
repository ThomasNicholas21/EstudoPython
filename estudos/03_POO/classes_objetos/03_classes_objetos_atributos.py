# Estudando atributos de classe

class Pessoa:
    ano = 2024 # Atributo de classe

    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self.ano_nascimento = ano_nascimento

    def get_idade(self):
        return Pessoa.ano - self.ano_nascimento
    
    def e_mariodidade(self):
        if self.get_idade() > 18:
            return 'Mairoidade'
        return 'Menoridade'
    
    def __str__(self):
        return f'{self.nome} tem {self.get_idade()} e está na {self.e_mariodidade()}'
    
def main():
    print(Pessoa.ano)
    pessoa1 = Pessoa('Matheus', 2000)
    print(pessoa1.get_idade())
    print(pessoa1.e_mariodidade())
    print(pessoa1)

main()

    

