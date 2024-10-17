# Dia 9: Funções Recursivas
# Crie uma função recursiva em Python que calcule o fatorial de um número dado.

def fatorial(numero):
    if numero == 1:
        return numero
    return numero * fatorial(numero - 1) 

def main():
    numero = int(input('Digite um número: '))
    valor = fatorial(numero)
    print(valor)

if __name__ == '__main__':
    main()