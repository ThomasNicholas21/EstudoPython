import doc1
import doc2
import doc3

print(dir(doc1)) # mostra todos os atributos de um objeto
# Saída - ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
# DocStrings
print(doc1.__doc__) # Acessa a documentação do código definida no arquivo doc.py

print(help(doc1)) # Exibe informções detalhadas sobre um objeto, módulo, função, classe oui método, mostrando sua documentação e explicando seu uso

if 'soma' in dir(doc2):
    print(dir(doc2))
    print(doc2.__doc__)
    print(help(doc2))

if 'Calculadora' in dir(doc3): # Verifica se a classe Calculadora está implementada
    print(dir(doc3))
    print(doc3.__doc__)
    print(help(doc3)) #