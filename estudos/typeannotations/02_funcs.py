# type annotations para funções

# Parêmetros são tipados e a seta indica o que a função retorna
def somar(x: float, y: int) -> float:
    return x + y


soma = somar(2, 2)
print(soma)
