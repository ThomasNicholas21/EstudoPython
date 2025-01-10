# optional type é tornar uma variável opcional tipando e atribuindo valor.

def somar(x: float, y: float | int = 1) -> float | int:
    return x + y


soma = somar(1)
print(soma)
