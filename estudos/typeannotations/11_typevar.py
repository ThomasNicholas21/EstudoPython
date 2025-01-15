from typing import TypeVar


T = TypeVar('T')  # tipo dinamico


def get_item(lista: list[T], index: int) -> T:
    return lista[index]


lista_inteiro = get_item([1, 2, 3], 1)  # retorna inteiro
lista_strings = get_item(['a', 'b', 'c'], 1)  # retorna string
