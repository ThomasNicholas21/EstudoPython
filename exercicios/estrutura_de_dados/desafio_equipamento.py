# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:
# TODO: Crie um loop para solicita os itens ao usuário:
# TODO: Solicite o item e armazena na variável "item":
# TODO: Adicione o item à lista "itens":
# Exibe a lista de itens
itens = []
equipamentos_inseridos = 0
while equipamentos_inseridos < 3:
    equipamento = input()
    itens.append(equipamento)
    equipamentos_inseridos += 1 
else:
    print("Lista de Equipamentos:")  
    for item in itens:
        # Loop que percorre cada item na lista "itens"
        print(f"- {item}")