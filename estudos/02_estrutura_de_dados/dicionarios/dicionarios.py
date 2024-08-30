
# Um dicionário é um conjunto não ordenado de chave e valor.
# A chave deve ser um valor imutável
# O valor pode ser qualquer objeto
pessoa = {"Nome": "Thomas", "Idade": 23}
# pessoa = dict(nome="Thomas", idade=23)
pessoa["Profissao"] = "Analista" # adicionando valor
print(pessoa)
print(pessoa["Nome"]) 
print(pessoa["Idade"])
print(pessoa["Profissao"])

pessoa["Profissao"] = "Desenvolvedor" # Sobrescrevendo o valor
print(pessoa)
print(pessoa["Profissao"])
print()

# Dicionários aninhados - diconário dentro de dicionário
estoques = {
    "Estoque 1": {"Produto": "Maçã", "Quantidade": 25, "Valor": 2.50},
    "Estoque 2": {"Produto": "Relogio", "Quantidade": 5, "Valor": 258.50},
    "Estoque 3":{"Produto": "Celular", "Quantidade": 3, "Valor": 2500.25, "Cor": {"Branco": 2, "Preto": 1}}
}
def print_dic(**kwargs): # desempacota chave e valor, servindo apenas em funcoes
    for chave, valor in kwargs.items(): # Como iterar sobre um dicionário
        print(chave, valor)

print_dic(**estoques)
print(estoques["Estoque 1"]["Quantidade"]) # acessa o valor em dicionários aninhados
print(estoques["Estoque 3"]["Cor"]) 
print(estoques["Estoque 3"]["Cor"]["Branco"]) 



