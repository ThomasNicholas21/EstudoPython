# CSV (Comma Separated Values - Valores separados por vírgulas)
# É um formato de arquivo que armazena dados em forma de tabela, onde cada
# linha representa uma linha da tabela e as colunas são separadas por vírgulas.
# Ele é amplamente utilizado para transferir dados entre sistemas de diferentes
# plataformas, como por exemplo, para importar ou exportar dados para uma
# planilha (Google Sheets, Excel, LibreOffice Calc) ou para uma base de dados.
# Um arquivo CSV geralmente tem a extensão ".csv" e pode ser aberto em um
# editor de texto ou em uma planilha eletrônica.
# Um exemplo de um arquivo CSV pode ser:
# Nome,Idade,Endereço
# Luiz Otávio,32,"Av Brasil, 21, Centro"
# João da Silva,55,"Rua 22, 44, Nova Era"
# A primeira linha do arquivo define os nomes das colunas da, enquanto as
# linhas seguintes contêm os valores das linhas, separados por vírgulas.
# Regras simples do CSV
# 1 - Separe os valores das colunas com um delimitador único (,)
# 2 - Cada registro deve estar em uma linha
# 3 - Não deixar linhas ou espaços sobrando
# 4 - Use o caractere de escape (") quando o delimitador aparecer no valor.

# csv.reader e csv.DictReader 
# respectivamente lê  arquiv em formato de lista e lê em formato de dicionário
import csv
from pathlib import Path


ROOT_FILE = Path(__file__).parent / '01_csv_arquivo1.csv'

with open(ROOT_FILE, 'r') as arquivo:
    leitor1 = csv.reader(arquivo)

    for dados1 in leitor1:
        print(dados1)


with open(ROOT_FILE, 'r') as arquivo:
    leitor2 = csv.DictReader(arquivo)

    for dados2 in leitor2:
        print(dados2)