# problema dos parâmetros mutáveis em python

def adicionar_pessoas(nome, lista=[]): # ao ser criado em, o python utilizará apenas esse objeto mutável para inserir valores
    lista.append(nome)
    return lista

cliente1 = adicionar_pessoas('Thomas')
adicionar_pessoas('Nicholas')
print(cliente1)

cliente2 = adicionar_pessoas('Fulano')
adicionar_pessoas('Ciclano')
print(cliente2)

# Ideal, não utilizar objeto mutável