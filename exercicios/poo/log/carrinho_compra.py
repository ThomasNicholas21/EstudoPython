# criando carrinho de compra que utilizará as classes Log
from log import LogFIleMixin

class Carrinho:
    def __init__(self, produtos=[]):
        self._produtos = produtos
    
    def adicionar_produto(self):
        self._produtos.append(Produto)

    def remover_produto(self):
        self._produtos.pop()

class Produto(Carrinho, LogFIleMixin):
    def __init__(self, nome, categoria, produtos=[]):
        super().__init__(produtos)
        self.nome = nome
        self.categoria = categoria

    def adicionar_produto(self):
        super().adicionar_produto()
        print('Adicionando produto!')
        mensagem = f'Adicionando {self.__class__.__name__}: {self.nome}, {self.categoria}'
        self.log_sucesso(mensagem)

    def remover_produto(self):
        super().remover_produto()
        print('Removendo produto!')
        mensagem = f'Removendo {self.__class__.__name__}: {self.nome}, {self.categoria}'
        self.log_sucesso(mensagem)