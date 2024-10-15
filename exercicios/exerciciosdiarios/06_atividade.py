# Dia 6: Dicionários
# Faça um programa que gerencie o estoque de uma loja, onde o usuário pode criar um estoque, adicionar ou 
# remover itens do estoque, além de consultar a quantidade disponível de um item específico.

class Produto:
    def __init__(self, produtos: dict=None) -> None:
        self.produtos = produtos
 
    def remover_produto(self, valor):
        self.produtos.pop(valor)

    def __repr__(self) -> str:
        return f'{'\n'.join([f'Produto: {chave} - Quantidade: {valor}' for chave, valor in self.produtos.items()])}'
    
class Estoque:
    def __init__(self, nome_estoque, produtos: dict=None, lista_dict: dict=None) -> None:
        self.nome_estoque = nome_estoque
        self.produtos = produtos
        if lista_dict is not None:
            self.lista_dict = {}

    def criar_estoque(self, estoque_dict):
        estoque_dict.update({self.nome_estoque: {self.produtos}})

    def __repr__(self) -> str:
        return f'{self.nome_estoque.capitalize()}: \n{self.produtos}'

def procura_chave(chave, estoque_dict: dict) -> bool:
    if chave in estoque_dict:
        return True
    return False

def criar_estoque(estoque_dict):
    nome_estoque = input('Nome do estoque: ')
    estoque = Estoque(nome_estoque, None, estoque_dict)
    estoque.criar_estoque(estoque_dict)

def inserir_produto(estoque_dict):
    try:
        nome_produto = input('Nome do produto: ')
        quantidade_produto = int(input('Quantidade do produto: '))
        produto = Produto({nome_produto: quantidade_produto})

        nome_chave = input('Nome do estoque: ')
        if procura_chave(nome_chave, estoque_dict):
            estoque = Estoque(nome_chave, produto, estoque_dict)
            estoque_dict = estoque.criar_estoque(estoque_dict)
            print(produto)

    except ValueError:
        raise print(f'A quantidade do produto: {quantidade_produto} de ser um número - ', ValueError)

def remover_produto(estoque_dict):
    ...

def consultar_produto(estoque_dict):
    ...

def main():
    estoque_dict = {}
    
    while True:
        comandos = input('Comandos: criar estoque [ce]\nadicionar produto [ap]\n' 
        'remover produto [rp]\ndeletar estoque [de]\neditar estoque [ee]\nconsultar estoque [ce]\nsair [s]\n-->')

        if comandos == 'ce':
            criar_estoque(estoque_dict)
        elif comandos == 'ap':
            inserir_produto(estoque_dict)
        elif comandos == 'rp':
            ...
        elif comandos == 'de':
            ...
        elif comandos == 'c':
            print(estoque_dict)
        elif comandos == 's':
            break
        else:
            print('Comando invalido!')

if __name__ == "__main__":
    main() 