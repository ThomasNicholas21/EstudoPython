# Aplicação de estudos em python

class A:
    def identidificador(self):
        print('A')

class B(A):
    def identidificador(self):
        print('B') 

class C(A):
    def identidificador(self):
        print('C')

class D(B, C):
    def identidificador(self):
        print('D')

b = B()
c = C()
d = D()

# Mostra a chamada de cada objeto instanciado no programa
print(A.__mro__)
print(B.mro())
print(C.mro())
print(D.mro())