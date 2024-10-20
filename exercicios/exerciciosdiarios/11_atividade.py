# Dia 11: Manipulação de Strings
# Crie um programa que inverta uma string informada pelo usuário, sem usar funções 

class InverteString:
    def __init__(self, string: str) -> None:
        self.string = string
    
    def __repr__(self) -> str:
        return f'{self.string[::-1]}'

def main():
    string = input('Digite qualquer coisa: ')
    string_invertida = InverteString(string)
    print(f'Iniciando processo de inversão...\n{string} | {string_invertida}')

if __name__ == "__main__":
    main()