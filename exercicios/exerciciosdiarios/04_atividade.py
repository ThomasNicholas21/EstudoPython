# Dia 4: Listas
# Desenvolva um programa que receba 5 números e exiba o maior, o menor e a média desses números.

class VerificaNumeros:
    def __init__(self, lista=[]):
        self.lista = lista

    def maior(self):
        self.lista.sort()
        return self.lista[-1]

    def menor(self):
        self.lista.sort()
        return self.lista[0]
    
    def media(self):
        total = 0
        for itens in self.lista:
            total += itens
        return total / len(self.lista)

def main():
    lista = []
    contador = 0

    while contador < 5:
        try:
            numero = int(input('Digite os números: '))
            lista.append(numero)
            contador += 1
        except ValueError:
            print('Erro de valor ', ValueError)
    else:
        print('Maior número: ', VerificaNumeros(lista).maior())
        print('Menor número: ', VerificaNumeros(lista).menor())
        print('Média de valores: ', VerificaNumeros(lista).media())

main()