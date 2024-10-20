# Dia 12: Arquivos (Leitura)
# Crie um programa que leia um arquivo de texto e conte quantas palavras há nesse arquivo.

class MyReader:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.modo = 'r'
        self._abrir_arquivo = None

    def __enter__(self):
        self._abrir_arquivo = open(self.nome_arquivo, self.modo, encoding='utf8')
        return self._abrir_arquivo
    
    def __exit__(self):
        print('Finalizando processo de leitura.')

def contador_de_palavras():
    ...

def main():
    ...


if __name__ == "__main__":
    main()