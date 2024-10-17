# Dia 8: Funções
# Desenvolva uma função que receba um número e retorne se ele é primo ou não.

class Primo:
    def verificar_numero_primo(self, valor) -> bool:
        multiplo = 0
        for numero in range(2, valor):
            if valor % numero == 0:
                multiplo += 1
            if multiplo == 0:
                return True
            return False

def processa_valor(valor):
    print('Iniciando processo de verificação')
    verificador = Primo()
    if verificador.verificar_numero_primo(valor):
        print(f'Número {valor} é primo.')
    else:
        print(f'Número {valor} não é primo.')
        
def main():
    try:
        valor = int(input('Insira um valor: '))
        processa_valor(valor)
    except ValueError as v:
        print(f'ValueError, não foi colocado um número inteiro: {v}')

if __name__ == '__main__':
    main()