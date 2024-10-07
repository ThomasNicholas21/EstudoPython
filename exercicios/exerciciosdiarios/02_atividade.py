# Dia 2: Estruturas de Repetição (While)
# Faça um programa que peça ao usuário um número e continue pedindo até que o número seja positivo.

def verifica_positivo(num) -> bool:
    if num % 2 == 0:
        return True
    return False

def main():
    
    while True:
        try:
            numero = int(input('Insira um número: '))
            if verifica_positivo(numero):
                print('Número positivo! Encerrando programa.')
                break
            else:
                print('Número errado.')

        except Exception as e:
            print(f'Deve ser um número! Erro: {e}')

main()