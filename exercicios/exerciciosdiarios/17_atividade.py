# Dia 17: Decoradores
# Crie um decorador que calcule o tempo de execução de uma função.

#https://docs.python.org/pt-br/3.14/library/time.html
#https://docs.python.org/pt-br/3.10/library/timeit.html

from random import randint
import time

def calcula_tempo_execucao(func):
    func.flag_execucao = False

    def interna(*args, **kwargs):

        if not func.flag_execucao:
            func.flag_execucao = True
            inicio = time.time()
            resultado = func(*args, **kwargs)
            fim = time.time()
            tempo = fim - inicio
            print(f'Fução {func.__name__} demorou {tempo} para ser executada')
            func.flag_execucao = False

            return resultado
        
        else:
            return func(*args, **kwargs)
        
    return interna


@calcula_tempo_execucao
def quick_sort(lista, inicio, fim):
    if inicio > fim:
        return
    anterior = inicio
    posterior = fim
    pivo = lista[inicio]

    while anterior < posterior:
        while anterior < posterior and lista[posterior] > pivo:
            posterior = posterior - 1

        if anterior < posterior:
            lista[anterior] = lista[posterior]
            anterior = anterior + 1

        while anterior < posterior and lista[anterior] <= pivo:
            anterior = anterior + 1

        if anterior < posterior:
            lista[posterior] = lista[anterior]
            posterior = posterior - 1

        lista[anterior] = pivo

    quick_sort(lista, inicio, anterior - 1)
    quick_sort(lista, anterior + 1, fim)

@calcula_tempo_execucao
def gerador_lista(tamanho_lista: int) -> list:
    lista_aleatorio = [randint(1, 9) for numero in range(0, tamanho_lista)]
    return lista_aleatorio
    
def main():
    lista = []
    print('Iniciando programa gerador de lista aleatória ...')

    try:
        tamanho_lista = int(input('Insira o tamanho da lista: '))
        lista = gerador_lista(tamanho_lista)

    except ValueError as ve:
        print('Insira um número inteiro! Erro:', ve)

    if lista:
        print('lista gerada!')
        print(lista)
        # implementa quick sort
        print('Ordenando lista ...')

        tamanho_lista = len(lista)
        quick_sort(lista, 0, tamanho_lista - 1)
        print(lista)

if __name__ == '__main__':
    main()
    # lista = [randint(1, 9) for numero in range(0, 100)]
    # print(lista)