# Dia 7: Conjuntos
# Crie um programa que receba duas listas de números e exiba os números que estão em ambas as listas (interseção).
import random

class GeradorSet:
   def gerar_numero_aleatorios(self, start, stop, quantidade, lista_set):
        numero = [random.randint(start, stop) for number in range(quantidade)]
        lista_set = {*numero}
        return lista_set
        
def inserir_parametro(lista_set: set):
    try:
        print(f'Iniciando definição de intervalo de números aleatórios')
        comeco = int(input('Entre: '))
        final = int(input('E: '))
        quantidade = int(input('Quantos números devem ser gerados: '))
        if comeco <= final and quantidade > 0:
            gerador = GeradorSet()
            lista_set = gerador.gerar_numero_aleatorios(comeco, final, quantidade, lista_set)
            print('Lista criada com sucesso!')
            return lista_set
        
        else:
            print('Erro, começo deve ser menor que o final ou a quantidade deve ser maior que 0')
            return
        
    except ValueError as v:
        raise print(f'Deve ser inserido números inteiros, erro: {v}')

def main():
    lista_set1 = {}
    lista_set2 = {}

    lista_set1 = inserir_parametro(lista_set1)
    lista_set2 = inserir_parametro(lista_set2)
    if lista_set1 and lista_set2:
        print(f'Lista 1 {lista_set1} e lista 2 {lista_set2}, intersecção: {lista_set1.intersection(lista_set2)}')
    else:
        print('Ocorreu um erro.')

if __name__ == '__main__':
    main()