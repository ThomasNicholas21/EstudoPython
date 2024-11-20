# Dia 16: Funções Lambda
# Crie uma lista de dicionários, onde cada dicionário represente 
# uma pessoa (nome e idade). Use uma função lambda para ordenar 
# essa lista pela idade.

def main():
    lista_pessoa = [
        {'Nome': 'Thomas', 'Idade': 24},
        {'Nome': 'Fulano', 'Idade': 32},
        {'Nome': 'João', 'Idade': 12},
        {'Nome': 'Nicholas', 'Idade': 5},
        {'Nome': 'Maria', 'Idade': 88}
    ]

    print(lista_pessoa[0]['Idade'])
    lista_pessoas_ordenada = sorted(lista_pessoa, key=lambda lista_pessoa: lista_pessoa['Idade'])
    print(lista_pessoas_ordenada)

if __name__ == '__main__':
    main()