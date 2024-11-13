#@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False,
#           match_args=True, kw_only=False, slots=False, weakref_slot=False)

# init (padrão True): Cria automaticamente o método __init__, para 
# inicializar atributos da classe com base nos argumentos passados 
# na criação do objeto.

# repr (padrão True): Gera automaticamente um método __repr__, que retorna 
# uma representação legível da instância, útil para debugging e exibição em 
# texto.

# eq (padrão True): Cria automaticamente um método __eq__, 
# permitindo comparar duas instâncias da classe para verificar se 
# são iguais (baseado nos valores dos atributos).

# order (padrão False): Gera métodos de comparação (__lt__, __le__, __gt__, __ge__) 
# para ordenar instâncias. Só funciona se eq=True. Útil se você precisar 
# comparar ou ordenar objetos de maneira ordenada.

# unsafe_hash (padrão False): Permite criar um __hash__ para a instância 
# (para ser usada em estruturas de dados como conjuntos e dicionários). 
#  com cuidado, pois pode gerar valores inconsistentes se os dados mudarem.

# frozen (padrão False): Torna a instância imutável, evitando a modificação 
# de seus atributos após a criação do objeto. Quando True, o __hash__ é gerado 
# automaticamente, tornando-o seguro para usar em coleções.

# match_args (padrão True): Disponibiliza os atributos da instância para 
# serem usados em match (como se fosse um pattern matching), possibilitando 
#  comparação estruturada de objetos.

# kw_only (padrão False): Faz com que todos os parâmetros do __init__ sejam 
#  (keyword-only). Assim, ao criar o objeto, todos os argumentos devem ser 
# passados com o nome.

# slots (padrão False): Usa __slots__ para a criação dos atributos, o que 
# reduz o uso de memória e melhora a velocidade de acesso aos atributos.

# weakref_slot (padrão False): Cria um espaço reservado para uma referência 
# fraca (weakref) na instância, o que permite gerenciar ciclos de referência, 
# útil em cenários de coleta de lixo e gerenciamento de memória.

from dataclasses import dataclass

@dataclass(repr=False) # desativa repr, funcionando para outros métodos
class Pessoa:
    nome: str
    sobrenome: str

    def __post_init__(self): # sempre iniciado após o init 
        return f'{self.nome} {self.sobrenome}'
    
    def __repr__(self) -> str:
        atributos = f'{self.nome}, {self.sobrenome}'
        return f'{self.__class__.__name__}({atributos})'
    
if __name__ == "__main__":
    pessoa1 = Pessoa('thomas', 'Teste')
    print(pessoa1)