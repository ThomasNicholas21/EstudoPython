# estudo sobre DocStrings
""" Começo do código -> indica o título

Esse código irá possuir funções de soma
"""

def soma(x: int | float, y: int | float) -> int | float: # Type anotation
    """
    Está função realiza soma dos parâmetros

    :param x:Número 1
    :type x: int or float
    :param y:Número 2
    :type y: int or float

    return: A soma entre x e y
    :rtype: int or float

    """# Tipo de anotação parecida com TypeAnotation
    return x + y

# Aparecem como dados
if __name__ == "__main__":
    variavel1 = 10
    variavel2 = 15

    resultado = soma(variavel1, variavel2)
    print(resultado)