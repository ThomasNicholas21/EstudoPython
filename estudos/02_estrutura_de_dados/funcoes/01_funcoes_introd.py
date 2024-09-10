# Função é um bloco de código reutilizavel que realiza tarefas especificas
# tornando o código mais legivel e modular, possibilitando o reaproveitamento
# do código.
# Caso uma função não tenha um valor especifico para retornar, ele irá retornar None
#Exemplos de funções:

def menu():
    menu = """
1 - Saudar 
2 - Saudar com nome
3 - Adeus
4 - Adeus sem nome
5 - Sair
Opção:"""
    return(menu)

def saudar():
    print("Olá!")

def saudar_com_nome(nome="Desconhecido"): # Caso não insira nada aparecerá a variavel declarada
    return print(f"Olá {nome}") # Serve para retornar o valor chamado

def adeus():
    print("Adeus")

def adeus_com_nome(nome="Desconhecido"):
    return print(f"Adeus {nome}")

saudar_com_nome()

while True:
    opc = input(menu())

    if opc == "1":
        saudar()
    elif opc == "2":
        nome_saudar = input("Insira seu nome:")
        saudar_com_nome(nome_saudar)
    elif opc == "3":
        adeus()
    elif opc == "4":
        nome_adeus = input("Insira seu nome:")
        adeus_com_nome(nome_adeus)
    elif opc == "5":
        break
    else:
        print("Opção invalida")