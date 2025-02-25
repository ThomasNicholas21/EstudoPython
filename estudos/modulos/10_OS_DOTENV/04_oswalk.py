# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
from itertools import count
import os


caminho = os.path.join('C:', '/Teste', 'estudo', 'estudos', 'modulos')
contador = count()


for root, dirs, files in os.walk(caminho):
    o_contador = next(contador)
    print(o_contador, root)

    for _dirs in dirs:
        print(o_contador, _dirs)

    for file in files:
        caminho_arquivo = os.path.join(root, file)
        print(o_contador, caminho_arquivo)
        #  Possível deletar todos os arquivos usando os.unlink(caminho_arquivo)
        #  OBS: não tem lixeira
