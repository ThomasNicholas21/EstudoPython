# Iterator e Iterable
# Iterable - um objeto que pode retornar um membro de cada vez
# Iterator é um objeto que pode ser iterado
iterable = ['Teste1', 'Teste2', 'Teste3']
iterator = iter(iterable) # tem __iter__ = iter() e __next__() -> passa pra proxima iteração

print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())