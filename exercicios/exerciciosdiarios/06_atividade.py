# Dia 6: Dicionários
# Faça um programa que gerencie o estoque de uma loja, onde o usuário pode criar um estoque, adicionar ou 
# remover itens do estoque, além de consultar a quantidade disponível de um item específico.

class Estoque:
    def __init__(self, nome_estoque, produtos: dict=None, lista_dict: dict=None) -> None:
        self.nome_estoque = nome_estoque
        self.produtos = produtos
        if lista_dict is not None:
            self.lista_dict = {}

    def criar_estoque(self):
        self.lista_dict.update({self.nome_estoque: {**self.produtos}})

    def deletar_estoque(self):
        if self.produtos is None:
            del self.lista_dict
        else:
            print('Estoque possui produtos:', self.produtos, 'Estoque não deletado')
    
    def __repr__(self) -> str:
        return f'{self.__class__.__name__}:{[f'{key}: {value}' for key, value in self.lista_dict.items()]}'
    
def inserir_produto():
    ...

def remover_produto():
    ...

def consultar_produto():
    ...

def main():
    estoque_dict = {}
    nome_estoque = 'estoque_teste1'
    produtos = {'havaina_teste': 22}
    estoque1 = Estoque(nome_estoque, produtos, estoque_dict)
    estoque1.criar_estoque()
    print(estoque1)
    estoque1.deletar_estoque()
    print(estoque1)

if __name__ == "__main__":
    main() 