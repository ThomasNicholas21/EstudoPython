# Dia 7: Conjuntos
# Crie um programa que receba duas listas de números e exiba os números que estão em ambas as listas (interseção).
import random

class GeradorSet:
    def gerar_numero_aleatorios(self, start, stop, quantidade, lista: set):
        numero = [random.randint(start, stop) for number in range(quantidade)]
        lista = {*numero}
        return lista

def inserir_parametro(lista_set: GeradorSet):
    try:
        print('Iniciando definição de intervalo de números aleatórios')
        comeco = int(input('Entre: '))
        final = int(input('E: '))
        quantidade = int(input('Quantos números devem ser gerados: '))
        lista_set.gerar_numero_aleatorios(comeco, final, quantidade, lista_set)

    except ValueError as v:
        raise print(f'Deve ser inserido números inteiros, erro: {v}')

def main():
    lista_set1 = GeradorSet()
    lista_set2 = GeradorSet()

    inserir_parametro(lista_set1)
    print(lista_set1)


if __name__ == '__main__':
    main()