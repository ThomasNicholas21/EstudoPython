from log import LogFIleMixin, LogPrintMixin
from carrinho_compra import Carrinho, Produto

prod1 = Produto('Caneta', 'Material')
carrinho = Carrinho()

prod1.adicionar_produto()
prod1.remover_produto()