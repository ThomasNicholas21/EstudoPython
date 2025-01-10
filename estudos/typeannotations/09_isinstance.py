# isinstance é uma built-in python que verifica tipo de variáveis

def somar(x: float, y: float | int | None = None) -> float | int:
    if isinstance(y, (float, int)):
        return x + y
    return x + x


soma = somar(1)
print(soma)
