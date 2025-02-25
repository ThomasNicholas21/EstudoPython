# os.listdir navega em caminhos 
# C: \\Teste\\estudo\\arquivo # windows
import os


caminho = os.path.join('C:', '\Teste', 'estudo', 'estudos', 'modulos')

for pasta in os.listdir(caminho):  # vai listar arquivos no diretório
    pasta_caminho = os.path.join(caminho, pasta)
    for item in os.listdir(pasta_caminho):
        print(item)
