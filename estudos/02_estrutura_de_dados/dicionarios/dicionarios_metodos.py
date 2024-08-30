# Metodos utilizados na classe dic
def print_dic(**kwargs): # desempacota chave e valor, servindo apenas em funcoes
    for chave, valor in kwargs.items(): # Como iterar sobre um dicionário
        print(chave, valor)

estoques = {
    "Estoque 1": {"Produto": "Maçã", "Quantidade": 25, "Valor": 2.50},
    "Estoque 2": {"Produto": "Relogio", "Quantidade": 5, "Valor": 258.50},
    "Estoque 3":{"Produto": "Celular", "Quantidade": 3, "Valor": 2500.25, "Cor": {"Branco": 2, "Preto": 1}}
}

# clear - limpa o dicionario
print_dic(**estoques)
estoque_copia = estoques.copy()
estoques.clear()
print_dic(**estoques)
print()

# copy - faz uma copia raza do dicionario
# estoque_copia = estoques.copy()
estoque_copia2 = estoque_copia.copy()
print_dic(**estoque_copia)
print()

# fromkeys - cria um novo dicionario sequencia de chave com o mesmo valor
estoque_novo = dict().fromkeys(["Vermelho", "Azul"], 0)
print(estoque_novo)
print()

# get - acessa um valor dentro de um dicionário
print(estoque_copia.get("Estoque 1"))
estoque5 = estoque_copia.get("Chave", "N")
print(estoque5) # Retorna none quando nao esxistir
print()

# Items - retorna a chave o valor
print(list(estoque_copia.items()))
print()

# keys - retorna apenas a chave
print(list(estoque_copia.keys()))
print()

# values - retorna o valor
print(list(estoque_copia.values()))
print()

# pop - remove uma chave
estoque_copia.pop("Estoque 3")
print(estoque_copia.pop("Estoque 5", "Esse estoque não existe")) # Quando não encontra retorna valor, quando encontra remove sem retornar a mensagem
print_dic(**estoque_copia)
print()

# popitem - remove o item na sequencia
estoque_copia.popitem()
estoque_copia.popitem()
try:
    estoque_copia.popitem() # retorn key
except KeyError as KeyError:
    print(f"Não é possível retirar valor de um dic vazio. Erro: {KeyError}")
print(estoque_copia)
print()

# setdefault - adicona um valor, caso exista ele não substitui
estoque_copia2.setdefault("Estoque 2", {"Produto": "Tenis", "Quantidade": 1, "Valor": 550})
estoque_copia2.setdefault("Estoque 4", {"Produto": "Tenis", "Quantidade": 1, "Valor": 550})
print_dic(**estoque_copia2)
print()

# update - atualiza o dicionario ou adiciona caso não exista
estoque_copia2.update({"Estoque 1": {"Produto": "Maçã", "Quantidade": 25, "Valor": 3.50}}) # atualiza os valores da chave
print_dic(**estoque_copia2)
print()
estoque_copia2.update({"Estoque 5": {"Produto": "Copo", "Quantidade": 155, "Valor": 5}})
print_dic(**estoque_copia2)
print()

# in - verifica valor exxistente
print("Estoque 1" in estoque_copia2)
print("Estoque 6" in estoque_copia2)
print("Produto" in estoque_copia2["Estoque 1"])
print("Branco" in estoque_copia2["Estoque 3"]["Cor"])
print()

# del - remove valor
del estoque_copia2["Estoque 5"]
del estoque_copia2["Estoque 4"]
print_dic(**estoque_copia2)
print()
try:
    del estoque_copia2
    print_dic(**estoque_copia2)
except NameError as NameError:
    print(f"Como o dicionário foi excluido, não será possível encontra-lo. Erro: {KeyError}")