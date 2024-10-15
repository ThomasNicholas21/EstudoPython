# Dia 6: Dicionários
# Faça um programa que gerencie o estoque de uma loja, onde o usuário pode criar um estoque, adicionar ou 
# remover itens do estoque, além de consultar a quantidade disponível de um item específico.

class Produto:
    def __init__(self, produtos: dict=None, estoque_dict: dict=None) -> None:
        self.produtos = produtos if produtos else {}
        self.estoque_dict = estoque_dict

    def inserir_produto(self, nome_chave):
        self.estoque_dict[nome_chave].update({**self.produtos})
  
class Estoque:
    def __init__(self, nome_estoque, produtos: dict=None, lista_dict: dict=None) -> None:
        self.nome_estoque = nome_estoque
        self.produtos = produtos 
        if lista_dict is not None:
            self.lista_dict = {}

    def criar_estoque(self, estoque_dict):
        if self.produtos is None:
            estoque_dict.update({self.nome_estoque: {}})

def procura_chave(chave, estoque_dict: dict) -> bool:
    if chave in estoque_dict:
        return True
    return False

def criar_estoque(estoque_dict: dict):
    nome_estoque = input('Nome do estoque: ')
    estoque = Estoque(nome_estoque, None, estoque_dict)
    estoque.criar_estoque(estoque_dict)
    print()

def inserir_produto(estoque_dict: dict):
    try:
        nome_chave = input('Nome do estoque: ')
        if procura_chave(nome_chave, estoque_dict):
            nome_produto = input('Nome do produto: ')
            quantidade_produto = int(input('Quantidade do produto: '))
            produto = Produto({nome_produto: quantidade_produto}, estoque_dict)
            produto.inserir_produto(nome_chave)
            print()
            
        else:
            print('Estoque não encontrado')
            print()
            return

    except ValueError:
        raise print(f'A quantidade do produto: {quantidade_produto} de ser um número - ', ValueError, end='\n')
        

def remover_produto(estoque_dict: dict):
    try:
        nome_chave = input('Nome do estoque: ')
        nome_produto = input('Nome do produto: ')
        if procura_chave(nome_chave, estoque_dict) and nome_produto in estoque_dict[nome_chave]:
            estoque_dict[nome_chave].pop(nome_produto)
        
        else:
            print('Estoque ou produto não existe.', end='\n')
            return 
        
    except Exception as e:
        print('Erro: ', e, end='\n')

def consultar_produto(estoque_dict: dict):
    nome_estoque = input('Digite o nome do estoque: ')
    if procura_chave(nome_estoque, estoque_dict): 
        nome_produto = input('Digite o nome do produto: ')
        if nome_produto in estoque_dict[nome_estoque]:
            print([f'Estoque: {chave} | Produto: {nome_produto} | Quantidade: {valor[nome_produto]}' for chave, valor in estoque_dict.items()], end='\n')
        else:
            print('Produto não encontrado!', end='\n')
            

def main():
    estoque_dict = {}
    
    while True:
        comandos = input('Comandos: \ncriar estoque [ce]\nadicionar produto [ap]\n' 
        'remover produto [rp]\nconsultar estoque [c]\nsair [s]\n-->')

        if comandos == 'ce':
            criar_estoque(estoque_dict)
        elif comandos == 'ap':
            inserir_produto(estoque_dict)
        elif comandos == 'rp':
            remover_produto(estoque_dict)
        elif comandos == 'c':
            consultar_produto(estoque_dict)
        elif comandos == 's':
            break
        else:
            print('Comando invalido!', end='\n')

if __name__ == "__main__":
    main()  