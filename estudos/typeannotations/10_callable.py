# criando callable para tipagem de funções
from collections.abc import Callable 
# módulo que disponibiliza classe para criar um callable

# Recebe dois inteiros e retorna um inteiro
SomaInteiros = Callable[[int, int], int]


def executa(func: SomaInteiros, a: int, b: int) -> int:
    return func(a, b)


def soma(a: int, b: int) -> int:
    return a + b


executa(soma, 2, 5)
