# Generator functions

# toda função generator utiliza o comando yield - serve para pausar a função
def gen_lista(tamanho_lista1: int):
    for item in range(1, tamanho_lista1):
        yield item
        # print('+') yield permite que haja outras iterações após ser executado
        # return 'Teste' # Realiza a parada da iteração de uma generator function
        

# toda vez que uma função geradora atingir o comando return, o mesmo irá levantar a exceção StopIteration
# o yiel pode ser utilizar yield from - pegar informação de outros locais
def gent_lista2(tamanho_lista1: int, tamanho_lista2: int):
    yield from gen_lista(tamanho_lista1) # Chama a ultima iteração executada de outro yield
    for item in range(tamanho_lista2):
        yield item

def main():
    try:
        tamanho_lista1 = int(input('Tamanho da lista: '))
        generator1 = gen_lista(tamanho_lista1)
        for item in generator1:
            print(item)

        tamanho_lista2 = int(input('Tamanho da lista: '))
        generator2 = gent_lista2(tamanho_lista1 ,tamanho_lista2)
        for item in generator2:
            print(item)

    except Exception:
        print('Erro')

main()