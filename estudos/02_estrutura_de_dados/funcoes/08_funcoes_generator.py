# Iterator e Iterable
# Iterable - um objeto que pode retornar um membro de cada vez
# Iterator é um objeto que pode ser iterado
iterable = ['Teste1', 'Teste2', 'Teste3']
iterator = iter(iterable) # tem __iter__ = iter() e __next__() -> passa pra proxima iteração

print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())

# generator expression - função que sabe pausar, ou seja espera pedir um valor
generator = (numero for numero in range(1000))
print(generator.__next__()) # Retorna valor apenas quando realiza a chamada, poupando mémoria.
print(generator.__next__())
print(generator.__next__())
# A lista pode acessar indice por indice por ja estar na mémoria, ao contrário do generator