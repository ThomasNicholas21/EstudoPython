# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int
    email: str 

if __name__ == '__main__':
    pessoa1 = Pessoa('Thomas', 23, 'thomas@gmail.com')
    print(pessoa1)
    pessoa1.nome = 'Thomas Nicholas'
    print(pessoa1)
    print(pessoa1.nome)
    del pessoa1.email
    try:
        print(pessoa1)
    except AttributeError as ae:
        print('Pessoa sem email!:', ae)
        print(pessoa1.nome, pessoa1.idade)