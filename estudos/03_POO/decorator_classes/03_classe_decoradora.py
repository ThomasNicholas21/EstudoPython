# própria classe que decora um objeto

from typing import Any


class Multiplicador:
    def __init__(self, multiplicador) -> None:
        self.multiplicador = multiplicador
    
    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self.multiplicador
        return interna
    
class Divisor:
    def __init__(self, divisor) -> None:
        self.divisor = divisor

    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado / self.divisor
        return interna

@Divisor(5)
@Multiplicador(10)
def soma(x, y):
    return x+ y

somar = soma(2, 6)
print(somar)