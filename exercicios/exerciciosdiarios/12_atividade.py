# Dia 12: Arquivos (Leitura)
# Crie um programa que leia um arquivo de texto e conte quantas palavras há nesse arquivo.

class MyReader:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.modo = 'r'

    def __enter__(self):
        ...
    
    def __exit__(self):
        ...


def main():
    ...


if __name__ == "__main__":
    main()