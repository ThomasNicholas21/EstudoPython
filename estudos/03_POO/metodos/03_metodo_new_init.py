# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ DEVE retornar o novo objeto
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ NÃO DEVE retornar nada (None)
# object é a super classe de uma classe

class A:
    def __new__(cls, *args, **kwargs): # Faz com que receba os atributos inicializados da classe e é reponsável por criar o objeto
        instancia = super().__new__(cls) 
        return instancia

    def __init__(self, A) -> None:
        self.A = A

    def __repr__(self) -> str:
        return f'letra:{self.A}'

if __name__ == '__main__':
    a = A('A')
    print(a)