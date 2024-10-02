# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# Levantando e tratando suas Exceptions (Exceções)
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)

# class MeuError(Exception):
#     ...

# class OutroError(Exception):
#     ...
# def levantar():
#     exception_ = MeuError('a', 'b', 'c')
#     raise exception_
# try:
#     levantar()
# except (MeuError, ZeroDivisionError) as error:
#     print(error.__class__.__name__)
#     print(error.args)
#     print()
#     exception_ = OutroError('Vou lançar de novo')
#     raise exception_ from error

# Utilizar duas linguas é considerado uma má prática
class MeuError(Exception): ...

class NumeroErro(Exception): ...

def levantar_erro():
    exception_ = MeuError('Erro indicado')
    exception_.add_note('Anotação sobre erro')
    exception_.add_note('Segunda anotação sobre o erro')
    return exception_

def levanta_erro_numero(numero):
    exception_ = NumeroErro('Este número não é compatível')
    exception_.add_note('Anotação sobre erro') # Serve para anotar sobre um erro específico, sendo uma ferramenta de comunicação
    exception_.add_note('Segunda anotação sobre o erro')
    if numero == 1:
        raise exception_
    

try:

    numero1 = 1
    levanta_erro_numero(numero1)

except NumeroErro as erro:
    print(erro)
    print(erro.__class__.__name__)
    print()
    exception_ = MeuError('Lançando um erro sobre o erro de número')
    exception_.add_note('Nota sobre exceção sobre uma exceção')
    exception_.__notes__ += erro.__notes__.copy() # Faz uma copia das outras notas
    raise exception_ from erro # Irá gerar uma exceção sobre uma exceção