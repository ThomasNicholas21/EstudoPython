# csv.writer e csv.DictWriter para escrever em CSV
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / '02_csv_arquivo2.csv'

lista_dicionarios = [
    {'Nome': 'Thomas', 'Idade': 24, 'Profissão': 'Engenheiro de Software'},
    {'Nome': 'Pedro', 'Idade': 32, 'Profissão': 'Barbeiro'},
    {'Nome': 'Lucas', 'Idade': 25, 'Profissão': 'Bombeiro'},
    {'Nome': 'Lourdes', 'Idade': 85, 'Profissão': 'Engenheira de computação'}
]

with open(CAMINHO_CSV, 'w', encoding='utf-8') as arquivo:
    nome_colunas = lista_dicionarios[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas
    )
    escritor.writeheader()
    for cliente in lista_dicionarios:
        print(cliente)
        escritor.writerow(cliente)