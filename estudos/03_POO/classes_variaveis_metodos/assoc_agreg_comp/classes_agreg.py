# Entendendo agragação

class Carrinho:
    def __init__(self):
        self._produtos = []

    def inserir_produto(self, *produtos):
        self._produtos += produtos

    def total(self):
        return sum(self._produtos)
    
    def lista_produtos(self):
        for produto in self._produtos:
            print(f'{produto.nome}, R${produto.preco}')

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


def main():
    carrinho_compras = Carrinho()
    produtos_cadastrados = [
        {
            'nome': 'teclado',
            'preco': 120
        },
        {
            'nome': 'mouse',
            'preco': 90
        },
        {
            'nome': 'Monitor',
            'preco': 500
        }
    ]
    
    for produto in produtos_cadastrados:
        print(f'{produto['nome']}: R${produto['preco']:.2f}')
    
    while True:
        opcoes = input('Selecione um produto: ')

        for produto in produtos_cadastrados:
            if opcoes == produto['nome']:
                produto_interesse = Produto(**produto)
                carrinho_compras.inserir_produto(produto_interesse)
                print('Produto Adicionado')
            

        carrinho_compras.lista_produtos()

        sair = input('Deseja sair? Digite sair. \n-->').lower().startswith('s')
        if sair:
            break
        else:
            continue

main()