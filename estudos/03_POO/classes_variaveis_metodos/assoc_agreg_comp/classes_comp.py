# Estudando composição

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.endereco = []

    def inserir_endereco(self, rua, numero, complemento):
        self.endereco.append(Endereco(rua, numero, complemento))

    def __str__(self):
        return f'Pessoa: {self.nome}, Idade: {self.idade}, Endereço: {[f'{dados}' for dados in self.endereco]}'

class Endereco:
    def __init__(self, rua, numero, complemento):
        self.rua = rua
        self.numero = numero
        self.complemento = complemento

    def __str__(self):
        return f'Rua: {self.rua}, Numero: {self.numero}, Complemento: {self.complemento}'

def cadastro_pessoa(opcao):
    if opcao:

        try:
            nome = input('Insira nome:')
            idade = int(input('Insira idade:'))
            pessoa = Pessoa(nome=nome, idade=idade)
            return pessoa
        
        except ValueError as v:
            print(f'{ValueError}: Valor {v} não compatível com idade')
        
    print('Obrigado.')
    return

def cadastro_endereco(pessoa):
    if pessoa:
        try:

            rua = input('Insira a rua:')
            numero = int(input('Insira o numero:'))
            complemento = input('Insira o complemento:')
            pessoa.inserir_endereco(rua, numero, complemento)
            return pessoa
        
        except ValueError as v:
            print(f'{ValueError}: O valor {v} não é compatível com o número da rua')
    
    return
    
def main():
    opcao = input('Inicial cadastro? [S] ou [N]').lower().startswith('s')
    pessoa = cadastro_pessoa(opcao)
    pessoa = cadastro_endereco(pessoa)

    if pessoa:
        print(pessoa)


main()