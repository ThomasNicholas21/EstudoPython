# Dia 3: Estruturas de Repetição (For)
# Crie um programa que exiba a tabuada de um número informado pelo usuário.

def tabuada(numero: int):
    texto_tabuda = ''
    for item in range(1, 11, 1):
        texto_tabuda += f'{numero} x {item} = {numero*item}\n'
    return texto_tabuda

def main():
    try:
        numero = int(input('Insira o número para saber a tabuada: '))
        print(tabuada(numero))
    except ValueError as v:
        print('Número inváido, erro: ', v)
    finally:
        print(f'Tabuada de {numero}.')

main()