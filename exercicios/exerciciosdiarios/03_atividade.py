# Dia 3: Estruturas de Repetição (For)
# Crie um programa que exiba a tabuada de um número informado pelo usuário.
class Tabuada:
    def __init__(self, numero: int) -> None:
        self.numero = numero
    
    def realiza_tabuada(self):
        list_tabuada = [f'{self.numero} x {item} = {self.numero*item}' for item in range(1, 11)]
        return '\n'.join(list_tabuada)

# def tabuada(numero: int):
#     texto_tabuda = ''
#     for item in range(1, 11, 1):
#         texto_tabuda += f'{numero} x {item} = {numero*item}\n'
#     return texto_tabuda

def main():
    try:
        numero = int(input('Insira o número para saber a tabuada: '))
        print(Tabuada(numero).realiza_tabuada())
    except ValueError as v:
        print('Número inváido, erro: ', v)
    finally:
        print(f'Tabuada de {numero}.')

main()