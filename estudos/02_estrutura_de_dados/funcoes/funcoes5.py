# Escopo local e escobo global
# Escopo global - má prática
# Variaveis globais sao acessiveis de qualquer luigugar, incluindo dentro das funcoes
# uma funcao so consegue modificar uma variavel global declarando ela
# Exemplo:
x = 10

def altera_x():
    global x
    x += 1
    print(x)

altera_x()

# Escopo local
# escopo que se refere dentro de um metodo, quando finalizado elas sao destruidas

def retorna_y():
    y = 10 # escopo local
    return print(y)

retorna_y()


# escopo encaixado (nested scope)
# escopos aninhados dentro de outras funcoes, a funcao interna acessa os dados da funcao exerterna
# exemplo contador

def contador():
    contador = 0
    def incrementa_contador():
        nonlocal contador # nested scope - funcao interna tem acesso aos dados da funcao exerterna
        contador += 1
        return contador
    return incrementa_contador

conta = contador()
for i in range(10):
    print(conta())

