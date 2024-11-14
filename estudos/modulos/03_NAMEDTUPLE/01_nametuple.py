# namedtuples - tuplas imutáveis com nomes para valores
# Usamos namedtuples para criar classes de objetos que são apenas um
# agrupamento de atributos, como classes normais sem métodos, ou registros de
# bases de dados, etc.
# As namedtuples são imutáveis assim como as tuplas.
# https://docs.python.org/3/library/collections.html#collections.namedtuple
# https://docs.python.org/3/library/typing.html#typing.NamedTuple
# https://brasilescola.uol.com.br/curiosidades/baralho.htm
# Quando dados são imutáveis e não precisam de métodos
from typing import NamedTuple
from collections import namedtuple

Carta = namedtuple('Carta', ['valor', 'naipe'])
as_espadas = Carta('A', '♠')

print(as_espadas)

for valor in as_espadas:
    print(valor)

class Pessoa(NamedTuple):
    nome: str
    idade: int
    tamanho: int

pessoa = Pessoa('Fulano', 22, 145)
print(pessoa)
