# Dia 12: Arquivos (Leitura)
# Crie um programa que leia um arquivo de texto e conte quantas palavras há nesse arquivo.

class MyReader:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.modo = 'r'
        self._abrir_arquivo = None

    def __enter__(self):
        print('Iniciando processo de leitura.')
        self._abrir_arquivo = open(self.nome_arquivo, self.modo, encoding='utf8')
        return self._abrir_arquivo
    
    def __exit__(self, class_exception_, exception_, traceback_):
        print('Finalizando processo de leitura.')
        self._abrir_arquivo.close()

def contador_de_palavras():
    with MyReader('D:/programação/EstudoPython/exercicios/exerciciosdiarios/12_atividade.txt') as arquivo:
        contador = 1
        for lines in arquivo.readlines():
            palavras = lines.split(' ')
            for palavra in palavras:
                if not palavra == '\n':
                    print(palavra)
                    contador += 1
        return contador


def main():
    quantidade_palavras = contador_de_palavras()
    print(f'A quantidade de palvras no arquivo de texto: {quantidade_palavras}')


if __name__ == "__main__":
    main()