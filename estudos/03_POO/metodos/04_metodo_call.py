# m[etodo __call__
# callable é algo que pode ser executado com parênteses.
# em classes normais, __call__ faz a instância de uma classes callable

from typing import Any


class LigarParaAlguem:
    def __init__(self, numero) -> None:
        self.numero = numero

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print(f'Ligando para o número {self.numero}')

ligacao1 = LigarParaAlguem(62992540634)
ligacao1() # método call permite que seja executada