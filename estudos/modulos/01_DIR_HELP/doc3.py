# entendendo como realizar documentação de uma classe

# estudo sobre DocStrings
""" Documentando classe calculadora

Esse código irá possuir a classe calculadora e método de soma
"""
class Calculadora:
    def soma(self, x: int | float, y: int | float) -> int | float: # Type anotation
        """
        Está função realiza soma dos parâmetros

        :param x:Número 1
        :type x: int or float
        :param y:Número 2
        :type y: int or float

        return: A soma entre x e y
        :rtype: int or float

        """
        # Tipo de anotação parecida com TypeAnotation
        return f'{x + y}'
    
    def erro(self):# para fazer levantamento de erro, é interessante apontar o erro ao invés de utilizar TypeAnotation
        """ Método retorna erro
        :raises ValueError: Método não for definido
        :raises NotImplementedErros: Se método não for implementado
        """
        raise ValueError('Teste')


# Aparecem como dados
if __name__ == "__main__":
    variavel1 = 10
    variavel2 = 15

    resultado = Calculadora()
    print(resultado.soma(variavel1, variavel2))