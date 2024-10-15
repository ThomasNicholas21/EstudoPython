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

    def criar_estoque(self):
        self.lista_dict.update({self.nome_estoque: {self.produtos}})
        return self.lista_dict

    def __repr__(self) -> str:
        return f'{self.nome_estoque.capitalize()}: \n{self.produtos}'
    
def criar_estoque():
    ...

def inserir_produto(estoque_dict):
    ...

def remover_produto():
    ...

def consultar_produto():
    ...

def main():
    estoque_dict = {}
    
    while True:
        comandos = input('Comandos: criar estoque [ce], adicionar produto [ap],' 
        'remover produto [rp], deletar estoque [de] e sair [s]\n-->')

        if comandos == 'ce':
            ...
        elif comandos == 'ap':
            ...
        elif comandos == 'rp':
            ...
        elif comandos == 'de':
            ...
        elif comandos == 's':
            ...
        else:
            print('Comando invalido!')

if __name__ == "__main__":
    main() 