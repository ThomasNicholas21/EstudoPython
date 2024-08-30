# todo: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
# todo: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
# todo: Retorne o plano de internet adequado:
# Solicita ao usuário que insira o consumo médio mensal de dados:
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:

def recomendar_plano(consumo_medio):
    if consumo_medio <= 10:
        return 'Plano Essencial Fibra - 50Mbps'
    elif 10 < consumo_medio <= 20:
        return 'Plano Prata Fibra - 100Mbps'
    elif consumo_medio > 20:
        return 'Plano Premium Fibra - 300Mbps'
    return 'Valor inválido.'

consumo_medio = float(input())
print(recomendar_plano(consumo_medio))