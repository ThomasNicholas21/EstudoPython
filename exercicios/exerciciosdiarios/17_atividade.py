# Dia 17: Decoradores
# Crie um decorador que calcule o tempo de execução de uma função.

#https://docs.python.org/pt-br/3.14/library/time.html
#https://docs.python.org/pt-br/3.10/library/timeit.html

from random import randint

def calcula_tempo_execucao():
    ...

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

def gerador_lista(tamanho_lista: int) -> list:
    lista_aleatorio = [randint(1, 9) for numero in range(0, tamanho_lista)]
    return lista_aleatorio
    
def main():
    ...

if __name__ == '__main__':
    main()
    lista = [randint(1, 9) for numero in range(0, 100)]
    print(lista)