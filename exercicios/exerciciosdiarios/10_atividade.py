# Dia 10: List Comprehension
# Escreva um programa que receba uma lista de números e retorne uma nova lista com o quadrado de cada número, usando list comprehension.
import random
import math
   
def quadrado_da_lista(comeco: int, final: int, quantidade_elementos: int):   
    lista = [random.randint(comeco, final) for number in range(quantidade_elementos)]
    lista_quadrada = [ numero ** 2 for numero in lista ]
    return lista_quadrada

def main():
    try:
        comeco = int(input('Digite o comeco: '))
        final = int(input('Digite o final: '))
        quantidade_elementos = int(input('Quantidade: '))

        if comeco <= final and quantidade_elementos > 0:
            print('Iniciando geração de lista e elevando ao quadrado...')
            lista_quadrada = quadrado_da_lista(comeco, final, quantidade_elementos)
            print(f'Processo finalizado...\nSua lista elevada ao quadrado: {lista_quadrada}\nSua lista era: {[int(math.sqrt(numero)) for numero in lista_quadrada]}')

    except ValueError as v:
        print(f'Valor deve ser um número inteiro.\nERRO: {v}')

if __name__ == '__main__':
    main()